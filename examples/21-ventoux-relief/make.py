#!/usr/bin/env python3
"""Mont Ventoux relief: outside data in, 3DCraft steps out (AGENTS.md section 3, Python).

  make.py fetch   downloads the public data (SRTM elevation, IGN BD TOPO road and summit tower) and
                  writes the small extract under data/ that the model needs, with data/SOURCES.md.
                  The raw downloads are cached in data/raw/ (not committed).
  make.py         runs offline from data/ and writes build.json, deterministically.

Python only converts the data: it projects longitude and latitude to Lambert-93, resamples the
elevation model to the model's grid and writes numbers into steps. Everything that is geometry is a
3DCraft command in build.json: the scales, the terrain surface, the solid, the pins' placement on it,
the tower, the contour layers and every measure.
"""

import datetime
import gzip
import heapq
import json
import math
import struct
import sys
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
RAW = DATA / "raw"

SKADI_URL = "https://s3.amazonaws.com/elevation-tiles-prod/skadi/N44/N44E005.hgt.gz"
WFS_URL = "https://data.geopf.fr/wfs/ows"

# The model's grid: nodes every 350 m in Lambert-93, 37 x 29 nodes (12.6 x 9.8 km), placed so that the
# node (18, 21) falls on the elevation model's highest cell, the summit of Mont Ventoux.
GRID_SPACING = 350.0
GRID_COLUMNS, GRID_ROWS = 37, 29
SUMMIT_NODE = (18, 21)
SMOOTHING = GRID_SPACING / 4  # a Gaussian's sigma, against aliasing: the nodes are 12 cells apart
CLIMB_LENGTH = 15700.0  # the race's figure for the climb (letourfemmes.fr), measured back from the top
FOREST_EDGE_FROM_TOP = 6200.0  # Chalet Reynard, "-6.2 km", where the road quits the forest (stage report)


# --------------------------------------------------------------------------------------------------
# Lambert-93 (EPSG:2154): Lambert conformal conic on GRS80, standard parallels 44 N and 49 N, origin
# 46.5 N 3 E, false easting 700 000 m, northing 6 600 000 m (IGN, NTG 71; Snyder, Map Projections,
# USGS Professional Paper 1395, p. 107-109).

_A = 6378137.0
_F = 1 / 298.257222101
_E = math.sqrt(2 * _F - _F * _F)
_PHI1, _PHI2, _PHI0, _LAM0 = map(math.radians, (44.0, 49.0, 46.5, 3.0))
_FE, _FN = 700000.0, 6600000.0


def _m(p):
    return math.cos(p) / math.sqrt(1 - (_E * math.sin(p)) ** 2)


def _t(p):
    return math.tan(math.pi / 4 - p / 2) / ((1 - _E * math.sin(p)) / (1 + _E * math.sin(p))) ** (_E / 2)


_N = (math.log(_m(_PHI1)) - math.log(_m(_PHI2))) / (math.log(_t(_PHI1)) - math.log(_t(_PHI2)))
_FF = _m(_PHI1) / (_N * _t(_PHI1) ** _N)
_RHO0 = _A * _FF * _t(_PHI0) ** _N


def lambert93(lon, lat):
    rho = _A * _FF * _t(math.radians(lat)) ** _N
    theta = _N * (math.radians(lon) - _LAM0)
    return _FE + rho * math.sin(theta), _FN + _RHO0 - rho * math.cos(theta)


def lonlat(x, y):
    dx, dy = x - _FE, _RHO0 - (y - _FN)
    rho = math.copysign(math.hypot(dx, dy), _N)
    t = (rho / (_A * _FF)) ** (1 / _N)
    lon = math.atan2(dx, dy) / _N + _LAM0
    phi = math.pi / 2 - 2 * math.atan(t)
    for _ in range(12):
        phi = math.pi / 2 - 2 * math.atan(t * ((1 - _E * math.sin(phi)) / (1 + _E * math.sin(phi))) ** (_E / 2))
    return math.degrees(lon), math.degrees(phi)


# --------------------------------------------------------------------------------------------------
# fetch

def download(url, target):
    if target.is_file():
        return target.read_bytes()
    print(f"downloading {url}", file=sys.stderr)
    request = urllib.request.Request(url, headers={"User-Agent": "3dcraft-examples ventoux-relief"})
    with urllib.request.urlopen(request, timeout=120) as response:
        body = response.read()
    target.write_bytes(body)
    return body


def wfs(type_name, cql, target):
    query = urllib.parse.urlencode({
        "SERVICE": "WFS", "VERSION": "2.0.0", "REQUEST": "GetFeature", "TYPENAMES": type_name,
        "OUTPUTFORMAT": "application/json", "SRSNAME": "EPSG:2154", "COUNT": "2000", "CQL_FILTER": cql})
    return json.loads(download(f"{WFS_URL}?{query}", target))


class Srtm:
    """A 1 x 1 degree SRTMGL1 tile (3601 x 3601 big-endian int16, rows from the north)."""

    def __init__(self, raw, south, west):
        self.data, self.south, self.west = raw, south, west
        self.n = int(math.isqrt(len(raw) // 2))

    def cell(self, row, col):
        offset = 2 * (row * self.n + col)
        return struct.unpack(">h", self.data[offset:offset + 2])[0]

    def at(self, lon, lat):
        """Bilinear between the four cells around the point."""
        r = (self.south + 1 - lat) * (self.n - 1)
        c = (lon - self.west) * (self.n - 1)
        r0, c0 = int(r), int(c)
        fr, fc = r - r0, c - c0
        return ((1 - fr) * ((1 - fc) * self.cell(r0, c0) + fc * self.cell(r0, c0 + 1))
                + fr * ((1 - fc) * self.cell(r0 + 1, c0) + fc * self.cell(r0 + 1, c0 + 1)))

    def smoothed(self, e, n, sigma, step=30.0):
        """The tile, smoothed by a Gaussian of sigma (m), at the Lambert-93 point (e, n): bilinear samples
        every step metres out to 2.5 sigma, weighted."""
        reach = int(math.ceil(2.5 * sigma / step))
        total = weight = 0.0
        for a in range(-reach, reach + 1):
            for b in range(-reach, reach + 1):
                w = math.exp(-((a * step) ** 2 + (b * step) ** 2) / (2 * sigma * sigma))
                total += w * self.at(*lonlat(e + a * step, n + b * step))
                weight += w
        return total / weight

    def highest(self, lon0, lat0, lon1, lat1):
        best = None
        for row in range(int((self.south + 1 - lat1) * (self.n - 1)), int((self.south + 1 - lat0) * (self.n - 1)) + 1):
            for col in range(int((lon0 - self.west) * (self.n - 1)), int((lon1 - self.west) * (self.n - 1)) + 1):
                h = self.cell(row, col)
                if best is None or h > best[0]:
                    best = (h, row, col)
        h, row, col = best
        return h, self.west + col / (self.n - 1), self.south + 1 - row / (self.n - 1)


def chain_road(sections, start, end):
    """The shortest way along the road's sections from the node nearest start to the node nearest end."""
    def key(p):
        return (round(p[0], 2), round(p[1], 2))
    graph = {}
    for index, section in enumerate(sections):
        points = section["geometry"]["coordinates"]
        length = sum(math.dist(p[:2], q[:2]) for p, q in zip(points, points[1:]))
        a, b = key(points[0]), key(points[-1])
        graph.setdefault(a, []).append((b, index, length))
        graph.setdefault(b, []).append((a, index, length))
    nodes = sorted(graph)
    first = min(nodes, key=lambda k: math.dist(k, start))
    last = min(nodes, key=lambda k: math.dist(k, end))
    distance, previous, queue = {first: 0.0}, {}, [(0.0, first)]
    while queue:
        d, node = heapq.heappop(queue)
        if d > distance[node]:
            continue
        for other, index, length in graph[node]:
            if d + length < distance.get(other, math.inf):
                distance[other] = d + length
                previous[other] = (node, index)
                heapq.heappush(queue, (d + length, other))
    pieces, used, node = [], [], last
    while node != first:
        before, index = previous[node]
        points = sections[index]["geometry"]["coordinates"]
        if key(points[0]) != before:
            points = points[::-1]
        pieces.append(points)
        used.append(sections[index]["properties"])
        node = before
    pieces.reverse()
    line = list(pieces[0])
    for piece in pieces[1:]:
        line += piece[1:]
    return line, used


def fetch():
    RAW.mkdir(parents=True, exist_ok=True)
    today = datetime.date.today().isoformat()

    # Elevation: the SRTM tile, its highest cell near the summit, and the grid aligned on it.
    srtm = Srtm(gzip.decompress(download(SKADI_URL, RAW / "N44E005.hgt.gz")), 44, 5)
    summit_h, summit_lon, summit_lat = srtm.highest(5.25, 44.15, 5.31, 44.19)
    se, sn = lambert93(summit_lon, summit_lat)
    e0 = se - SUMMIT_NODE[0] * GRID_SPACING
    n0 = sn - SUMMIT_NODE[1] * GRID_SPACING
    grid = [[srtm.smoothed(e0 + i * GRID_SPACING, n0 + j * GRID_SPACING, SMOOTHING) for j in range(GRID_ROWS)]
            for i in range(GRID_COLUMNS)]
    # Peak preservation: the summit node keeps the tile's highest cell, which smoothing would lower by
    # some 36 m (the summit cone is narrower than the grid).
    smoothed_summit = grid[SUMMIT_NODE[0]][SUMMIT_NODE[1]]
    grid[SUMMIT_NODE[0]][SUMMIT_NODE[1]] = summit_h

    # The road: the D974 from Bedoin to the summit, IGN BD TOPO, in Lambert-93 with its altitudes.
    road = wfs("BDTOPO_V3:troncon_de_route",
               "cpx_numero='D974' AND BBOX(geometrie,44.08,5.10,44.25,5.40)", RAW / "d974.json")
    bedoin = lambert93(5.1797, 44.1246)
    line, used = chain_road(road["features"], bedoin, (se, sn))
    road_dates = sorted((u["date_modification"] or "")[:10] for u in used)
    road_precision = sorted({u["precision_altimetrique"] for u in used})
    top = max(range(len(line)), key=lambda k: line[k][2])
    line = line[:top + 1]  # Bedoin to the road's highest point, at the summit
    along = [0.0]
    for p, q in zip(line, line[1:]):
        along.append(along[-1] + math.dist(p, q))  # length along the road, with its rise (3D)
    start = along[-1] - CLIMB_LENGTH
    k = next(i for i in range(len(along)) if along[i] >= start)
    t = (start - along[k - 1]) / (along[k] - along[k - 1])
    first = [line[k - 1][d] + t * (line[k][d] - line[k - 1][d]) for d in range(3)]
    climb = [first] + line[k:]

    # The summit tower: the tallest "Tour, donjon" building of BD TOPO near the summit, and its antenna.
    near = "BBOX(geometrie,44.172,5.274,44.176,5.282)"
    buildings = wfs("BDTOPO_V3:batiment", f"nature='Tour, donjon' AND {near}", RAW / "towers.json")
    tower = max(buildings["features"], key=lambda f: f["properties"]["hauteur"] or 0)
    ring = tower["geometry"]["coordinates"][0][0]
    area = 0.5 * abs(sum(ring[i][0] * ring[i + 1][1] - ring[i + 1][0] * ring[i][1] for i in range(len(ring) - 1)))
    cx = sum(p[0] for p in ring[:-1]) / (len(ring) - 1)
    cy = sum(p[1] for p in ring[:-1]) / (len(ring) - 1)
    masts = wfs("BDTOPO_V3:construction_ponctuelle", f"nature='Antenne' AND {near}", RAW / "antennas.json")
    mast = max(masts["features"], key=lambda f: f["properties"]["hauteur"] or 0)
    tp = tower["properties"]

    DATA.mkdir(exist_ok=True)
    with open(DATA / "elevation.csv", "w") as out:
        out.write("# Mont Ventoux elevation grid for ventoux-relief, written by make.py fetch on "
                  f"{today}.\n")
        out.write("# Source: Mapzen terrain tiles, skadi N44E005 (SRTMGL1, 1 arc-second), heights in m above "
                  "the EGM96 geoid.\n")
        out.write("# Nodes: Lambert-93 (EPSG:2154), every 350 m; one line per column, west to east; its values "
                  "south to north.\n")
        out.write(f"# Each node is the tile smoothed by a Gaussian of sigma {SMOOTHING:g} m (against aliasing), except "
                  f"node (18, 21) on the tile's highest cell: {summit_h} m (smoothed {smoothed_summit:.0f} m).\n")
        out.write(f"# spacing_m,{GRID_SPACING:.0f}\n# columns,{GRID_COLUMNS}\n# rows,{GRID_ROWS}\n")
        out.write(f"# origin_e,{e0:.2f}\n# origin_n,{n0:.2f}\n")
        out.write(f"# summit_node,{SUMMIT_NODE[0]},{SUMMIT_NODE[1]}\n# summit_m,{summit_h}\n")
        for column in grid:
            out.write(",".join(f"{h:.0f}" for h in column) + "\n")
    with open(DATA / "route.csv", "w") as out:
        out.write("# The climb of Mont Ventoux from Bedoin (D974), the last 15.7 km to the road's highest point, "
                  f"written by make.py fetch on {today}.\n")
        out.write("# Source: IGN BD TOPO, troncon_de_route cpx_numero D974, Lambert-93 (EPSG:2154), altitudes "
                  "in m (NGF-IGN69).\n")
        out.write("# e,n,altitude\n")
        for p in climb:
            out.write(f"{p[0]:.2f},{p[1]:.2f},{p[2]:.1f}\n")
    def at_distance(s):
        """The climb's point s metres along it (with its rise), interpolated between IGN's points."""
        for k in range(1, len(climb)):
            if along_climb[k] >= s:
                t = (s - along_climb[k - 1]) / (along_climb[k] - along_climb[k - 1])
                return [climb[k - 1][d] + t * (climb[k][d] - climb[k - 1][d]) for d in range(3)]
        return climb[-1]
    along_climb = [0.0]
    for p, q in zip(climb, climb[1:]):
        along_climb.append(along_climb[-1] + math.dist(p, q))
    edge = at_distance(along_climb[-1] - FOREST_EDGE_FROM_TOP)
    with open(DATA / "kilometres.csv", "w") as out:
        out.write("# The climb's kilometres, measured along route.csv with its rise from the climb's start, written by "
                  f"make.py fetch on {today}.\n")
        out.write("# Points interpolated between IGN BD TOPO's points (Lambert-93, altitudes in m NGF-IGN69).\n")
        out.write(f"# forest_edge,{edge[0]:.2f},{edge[1]:.2f},{edge[2]:.1f}  (Chalet Reynard, 6.2 km before the top)\n")
        out.write("# km,e,n,altitude\n")
        for km in range(int(along_climb[-1] // 1000) + 1):
            p = at_distance(km * 1000.0)
            out.write(f"{km},{p[0]:.2f},{p[1]:.2f},{p[2]:.1f}\n")
    with open(DATA / "tower.csv", "w") as out:
        out.write("# The summit tower of Mont Ventoux and its antenna, written by make.py fetch on "
                  f"{today}.\n")
        out.write("# Source: IGN BD TOPO, batiment (nature 'Tour, donjon') and construction_ponctuelle "
                  "(nature 'Antenne'), Lambert-93.\n")
        out.write("# key,value\n")
        out.write(f"centre_e,{cx:.2f}\ncentre_n,{cy:.2f}\nfootprint_m2,{area:.1f}\n")
        out.write(f"ground_m,{tp['altitude_minimale_sol']}\nheight_m,{tp['hauteur']}\n")
        out.write(f"mast_top_m,{mast['geometry']['coordinates'][2]}\n")
    sources = SOURCES.format(
        today=today, skadi=SKADI_URL, road_dates=f"{road_dates[0]} and {road_dates[-1]}",
        road_count=len(used), road_precision=" or ".join(f"{v:g} m" for v in road_precision), tower_id=tp["cleabs"], tower_date=(tp["date_modification"] or "")[:10],
        mast_id=mast["properties"]["cleabs"])
    (DATA / "SOURCES.md").write_text(sources)
    print(f"summit cell {summit_h} m at {summit_lon:.6f} E {summit_lat:.6f} N; climb {len(climb)} points, "
          f"{first[2]:.1f} m to {climb[-1][2]:.1f} m; tower {tp['hauteur']} m", file=sys.stderr)


SOURCES = """# Sources of the data in this folder

Written by `make.py fetch` on {today}. `make.py` builds `build.json` from these files alone.

## elevation.csv: the terrain

- **Data:** the Mapzen terrain tile `skadi/N44/N44E005.hgt.gz` ({skadi}), 1 arc-second (about 30 m),
  in the SRTMGL1 format: heights in metres above the EGM96 geoid. Hosted on the AWS Open Data registry
  ("Terrain Tiles").
- **Licence:** SRTM is in the public domain. The tiles' maker asks for this attribution
  (github.com/tilezen/joerd, docs/attribution.md, "Required attribution when using Mapzen's hosted
  service"):

  > Mapzen; ArcticDEM terrain data DEM(s) were created from DigitalGlobe, Inc., imagery and funded under
  > National Science Foundation awards 1043681, 1559691, and 1542736; Australia terrain data © Commonwealth
  > of Australia (Geoscience Australia) 2017; Austria terrain data © offene Daten Österreichs – Digitales
  > Geländemodell (DGM) Österreich; Canada terrain data contains information licensed under the Open
  > Government Licence – Canada; Europe terrain data produced using Copernicus data and information funded
  > by the European Union - EU-DEM layers; Global ETOPO1 terrain data U.S. National Oceanic and
  > Atmospheric Administration; Mexico terrain data source: INEGI, Continental relief, 2016; New Zealand
  > terrain data Copyright 2011 Crown copyright (c) Land Information New Zealand and the New Zealand
  > Government (All rights reserved); Norway terrain data © Kartverket; United Kingdom terrain data ©
  > Environment Agency copyright and/or database right 2015. All rights reserved; United States 3DEP
  > (formerly NED) and global GMTED2010 and SRTM terrain data courtesy of the U.S. Geological Survey.

  For this tile: SRTM data courtesy of the U.S. Geological Survey.
- **What was done:** the tile was resampled at 37 x 29 nodes 350 m apart in Lambert-93 (EPSG:2154), the
  grid placed so that one node falls on the tile's highest cell, the summit (1910 m). Each node is the
  tile smoothed by a Gaussian of sigma 87.5 m (a quarter of the node spacing; bilinear samples every
  30 m out to 2.5 sigma), so that ravines narrower than the grid do not alias into bumps. The summit node
  alone keeps the tile's highest cell (peak preservation), since smoothing would lower the narrow summit
  cone by some 36 m. Heights rounded to whole metres.
- **Accuracy:** SRTM's absolute height error is 6.2 m over Eurasia at 90 % (Rodríguez, Morris and Belz,
  "A Global Assessment of the SRTM Performance", Photogrammetric Engineering & Remote Sensing 72(3),
  2006, pp. 249-260); the mission asked for 16 m.

## route.csv: the climb

- **Data:** IGN BD TOPO, layer `troncon_de_route`: of the sections numbered D974 near Mont Ventoux, the
  {road_count} from Bédoin to the summit, through the Géoplateforme WFS (https://data.geopf.fr/wfs/ows,
  type `BDTOPO_V3:troncon_de_route`), in Lambert-93 with IGN's altitudes (NGF-IGN69, stated to
  {road_precision}). Sections last updated between {road_dates}.
- **Licence:** Licence Ouverte / Open Licence 2.0 (Etalab): free reuse with attribution. Attribution:
  "IGN – BD TOPO®, Géoplateforme, extracted {today}".
- **What was done:** the sections were chained from Bédoin to the road's highest point at the summit
  (21.5 km), and the last 15.7 km of it (measured along the road with its rise) kept, the length the race
  gives for the climb. The points are IGN's own, unchanged.

## kilometres.csv: the climb's kilometres and the forest's edge

- **Data:** points of route.csv, interpolated: one every 1000 m along the road (with its rise) from the
  climb's start, km 0 to km 15; and, in the header, the point 6.2 km before the top, Chalet Reynard,
  "which marks the moment on which the Mont Ventoux road quits the forest and enters a moon-like, fully
  exposed landscape" (the race's stage report, below).
- **Licence:** as route.csv.

## tower.csv: the summit tower

- **Data:** IGN BD TOPO, layer `batiment`, the building `{tower_id}` (nature "Tour, donjon", last updated
  {tower_date}): its footprint's centre and area, its ground altitude and height; and layer
  `construction_ponctuelle`, the antenna `{mast_id}` on it: the altitude of its top.
- **Licence:** as above, Licence Ouverte 2.0, "IGN – BD TOPO®, Géoplateforme, extracted {today}".

## The race

Tour de France Femmes avec Zwift 2026, stage 7, La Voulte-sur-Rhône to Mont Ventoux, 7 August 2026, with
the climb from Bédoin: "Mont Ventoux (15.7km at 8.8%)", Marion Rousse's stage commentary,
https://www.letourfemmes.fr/en/news/2026/stage-7/commentary-from-marion-rousse-22/1296943, and the stage
report, https://www.letourfemmes.fr/en/news/2026/stage-7/kasia-the-real-giant-of-provence/1301373
(both read 2026-11-07).
"""


# --------------------------------------------------------------------------------------------------
# build

def read_csv(name):
    meta, rows = {}, []
    for line in (DATA / name).read_text().splitlines():
        if line.startswith("#"):
            parts = line[1:].strip().split(",")
            if len(parts) >= 2 and parts[0].replace("_", "").isalnum() and " " not in parts[0]:
                meta[parts[0]] = parts[1:]
            continue
        if line.strip():
            rows.append(line.split(","))
    return meta, rows


def metres(v):
    """A length in metres as 3DCraft reads it, to a tenth of a metre."""
    text = f"{v:.1f}".rstrip("0").rstrip(".")
    return f"{text} m"


def build():
    meta, columns = read_csv("elevation.csv")
    grid = [[int(v) for v in column] for column in columns]
    e0, n0 = float(meta["origin_e"][0]), float(meta["origin_n"][0])
    spacing = float(meta["spacing_m"][0])
    ni, nj = len(grid), len(grid[0])
    summit_i, summit_j = (int(v) for v in meta["summit_node"])
    summit_m = int(meta["summit_m"][0])
    km_meta, km_rows = read_csv("kilometres.csv")
    marks = [[float(v) for v in row[1:]] for row in km_rows]  # km 0, 1, ... 15: e, n, altitude
    forest_edge = float(km_meta["forest_edge"][2].split()[0])
    tower = {row[0]: float(row[1]) for row in read_csv("tower.csv")[1]}

    # Statistics of the data that the checks compare the model with.
    weights = lambda n: [0.5 if k in (0, n - 1) else 1.0 for k in range(n)]
    wi, wj = weights(ni), weights(nj)
    mean_h = sum(wi[i] * wj[j] * grid[i][j] for i in range(ni) for j in range(nj)) / ((ni - 1) * (nj - 1))
    lowest = min(min(column) for column in grid)

    def plan(e, n):
        """A point of the map in the model's plan: metres from the grid's origin, at the map's scale."""
        return [f"{metres(e - e0)} / map_scale", f"{metres(n - n0)} / map_scale"]

    S = []
    ids = {}

    def add(step):
        S.append(step)

    def feature(step):
        """A step that adds a feature (an extrusion with cut adds two); returns the feature's id."""
        S.append(step)
        feature.count += 2 if any(k in step[1] for k in ("cut", "join", "intersect")) and step[0] == "feature.extrude" else 1
        name = step[1].get("name")
        ids[name] = f"F{feature.count}"
        return ids[name]
    feature.count = 0

    relief = "product == 1"
    layers = "product == 2"

    # ---- variables
    add(["document.setTolerance", {"linear": 0.001}])
    add(["variable.set", {"name": "vertical_exaggeration", "expr": "2.1"}])
    add(["variable.set", {"name": "contour_interval", "expr": "100 m"}])
    add(["variable.set", {"name": "product", "expr": "1"}])
    add(["variable.publish", {"name": "vertical_exaggeration", "label": "Vertical exaggeration", "description": "How many times taller than the map's scale the printed relief's heights are drawn (the laser-cut layers take theirs from the sheet thickness)", "group": "Relief", "order": 1, "kind": "number", "min": "1", "max": "3", "step": "0.1"}])
    add(["variable.publish", {"name": "contour_interval", "label": "Contour interval", "description": "Height between the laser-cut contour layers, one 3 mm sheet each, counted from sea level", "group": "Relief", "order": 2, "kind": "number", "min": "100 m", "max": "200 m", "step": "50 m", "unit": "m"}])
    add(["variable.publish", {"name": "product", "label": "Product", "description": "A relief 3D-printed in two colours with brass kilometre pins, or a stack of laser-cut contour layers", "group": "Relief", "order": 3, "kind": "choice", "choices": ["Printed relief", "Laser-cut layers"]}])
    add(["variable.set", {"name": "map_scale", "expr": "70000"}])
    add(["variable.set", {"name": "sheet_thickness", "expr": "3 mm"}])
    add(["variable.set", {"name": "vertical_scale", "expr": "if(product == 2, sheet_thickness / contour_interval, vertical_exaggeration / map_scale)"}])
    add(["variable.set", {"name": "node_pitch", "expr": f"{metres(spacing)} / map_scale"}])
    add(["variable.set", {"name": "relief_width", "expr": f"{ni - 1} * node_pitch"}])
    add(["variable.set", {"name": "relief_depth", "expr": f"{nj - 1} * node_pitch"}])
    add(["variable.set", {"name": "summit_elevation", "expr": f"{summit_m} m"}])
    add(["variable.set", {"name": "blank_height", "expr": "summit_elevation * vertical_scale + 10 mm"}])
    add(["variable.set", {"name": "forest_edge_elevation", "expr": metres(forest_edge)}])
    add(["variable.set", {"name": "data_mean_elevation", "expr": metres(mean_h)}])
    add(["variable.set", {"name": "climb_start_altitude", "expr": metres(marks[0][2])}])
    add(["variable.set", {"name": "srtm_accuracy", "expr": "16 m"}])
    add(["variable.set", {"name": "pin_diameter", "expr": "1.5 mm"}])
    add(["variable.set", {"name": "start_pin_diameter", "expr": "2.5 mm"}])
    add(["variable.set", {"name": "pin_hole_clearance", "expr": "0.1 mm"}])
    add(["variable.set", {"name": "pin_protrusion", "expr": "2 mm"}])
    add(["variable.set", {"name": "hole_floor", "expr": "3 mm"}])
    add(["variable.set", {"name": "landmark_scale", "expr": "10"}])
    add(["variable.set", {"name": "tower_height", "expr": metres(tower["height_m"])}])
    add(["variable.set", {"name": "tower_diameter", "expr": f"sqrt({tower['footprint_m2']:.1f} * 4 / pi) * 1 m"}])
    add(["variable.set", {"name": "tower_ground", "expr": metres(tower["ground_m"])}])
    add(["variable.set", {"name": "mast_top", "expr": metres(tower["mast_top_m"])}])
    add(["variable.set", {"name": "mast_diameter", "expr": "0.6 mm"}])
    add(["variable.set", {"name": "tower_roof", "expr": "tower_ground * vertical_scale + landmark_scale * tower_height / map_scale"}])
    add(["variable.set", {"name": "mast_length", "expr": "landmark_scale * (mast_top - tower_ground - tower_height) / map_scale"}])
    add(["variable.set", {"name": "base_border", "expr": "15 mm"}])
    add(["variable.set", {"name": "base_thickness", "expr": "22 mm"}])
    add(["variable.set", {"name": "base_corner_radius", "expr": "8 mm"}])
    add(["variable.set", {"name": "base_round_over", "expr": "3 mm"}])
    add(["variable.set", {"name": "bottom_edge_break", "expr": "1 mm"}])
    add(["variable.set", {"name": "stack_base_level", "expr": f"floor({lowest} m / contour_interval) * contour_interval"}])
    add(["variable.set", {"name": "contour_layer_count", "expr": "floor((summit_elevation - stack_base_level) / contour_interval) + 1"}])

    # ---- the terrain: one live spline per column of the grid, closed down to sea level, lofted
    names = []
    for i in range(ni):
        name = f"Terrain column {i + 1}"
        names.append(name)
        z = lambda j: f"{grid[i][j]} m * vertical_scale"
        feature(["sketch.create", {"name": name, "plane": "yz", "offset": f"{i} * node_pitch"}])
        add(["sketch.polyline", {"sketch": name, "points": [["0 mm", z(0)], ["0 mm", "0 mm"], ["relief_depth", "0 mm"], ["relief_depth", z(nj - 1)]]}])
        add(["sketch.spline", {"sketch": name, "live": True, "through": ["e1"] + [[f"{j} * node_pitch", z(j)] for j in range(1, nj - 1)] + ["e4"]}])
    terrain = feature(["feature.loft", {"sections": names, "name": "Terrain"}])

    # ---- the climb: brass pins at km 0 to 15 in blind holes, standing on the holes' floors
    feature(["sketch.create", {"name": "Kilometre marks", "plane": "xy", "offset": "hole_floor"}])
    for k, p in enumerate(marks):
        add(["sketch.circle", {"sketch": "Kilometre marks", "center": plan(*p[:2]), "radius": "start_pin_diameter / 2" if k == 0 else "pin_diameter / 2"}])
    feature(["feature.extrude", {"sketch": "Kilometre marks", "distance": "blank_height", "name": "Pin blanks", "when": relief}])
    feature(["feature.transform", {"source": "Terrain", "translate": [0, 0, "pin_protrusion"], "keep": True, "name": "Terrain at the pins' tops", "when": relief}])
    feature(["feature.boolean", {"op": "intersect", "target": "Pin blanks", "tool": "Terrain at the pins' tops", "name": "Kilometre pins", "when": relief}])
    feature(["feature.offsetProfile", {"sketch": "Kilometre marks", "distance": "pin_hole_clearance", "name": "Hole outlines"}])

    # ---- the printed relief in two colours: forest up to Chalet Reynard, bare limestone above
    feature(["feature.block", {"size": ["relief_width + 2 mm", "relief_depth + 2 mm", "forest_edge_elevation * vertical_scale + 1 mm"], "position": ["-1 mm", "-1 mm", "-1 mm"], "name": "Forest blank", "when": relief}])
    feature(["feature.block", {"size": ["relief_width + 2 mm", "relief_depth + 2 mm", "blank_height - forest_edge_elevation * vertical_scale"], "position": ["-1 mm", "-1 mm", "forest_edge_elevation * vertical_scale"], "name": "Summit blank", "when": relief}])
    feature(["feature.extrude", {"sketch": "Hole outlines", "distance": "blank_height", "cut": "Forest blank", "name": "Forest blank drilled", "when": relief}])
    feature(["feature.extrude", {"sketch": "Hole outlines", "distance": "blank_height", "cut": "Summit blank", "name": "Summit blank drilled", "when": relief}])
    feature(["feature.boolean", {"op": "intersect", "target": "Forest blank drilled", "tool": "Terrain", "keepTool": True, "name": "Forest drilled", "when": relief}])
    feature(["feature.boolean", {"op": "intersect", "target": "Summit blank drilled", "tool": "Terrain", "keepTool": True, "name": "Bald summit", "when": relief}])
    # the faces from the terrain (the boolean's tool) are named copy(1)/...
    side = lambda e: f"{ids['Forest drilled']}:copy(1)/{terrain}:side(" + ",".join([e] * ni) + ")"
    caps = [f"{ids['Forest drilled']}:copy(1)/{terrain}:{cap}(e5,e6,e7,e{nj + 6})" for cap in ("startCap", "endCap")]
    feature(["feature.chamfer", {"edges": [[side("e6"), side("e5")], [side("e6"), side("e7")]] + [[side("e6"), c] for c in caps], "distance": "bottom_edge_break", "name": "Forested slopes", "when": relief}])

    # ---- the summit tower, a landmark at ten times the map's scale, its foot fitted to the terrain
    tx, ty = plan(tower["centre_e"], tower["centre_n"])
    feature(["sketch.create", {"name": "Tower section", "plane": "zx", "offset": ty}])
    foot = "tower_ground * vertical_scale - 3 mm"
    radius = f"{tx} + landmark_scale * tower_diameter / map_scale / 2"
    pts = [[foot, tx], [foot, radius], ["tower_roof", radius], ["tower_roof", f"{tx} + mast_diameter / 2"]]
    bands = 5
    for b in range(1, bands + 1):
        pts.append([f"tower_roof + {b} * mast_length / {bands}", f"{tx} + mast_diameter / 2"])
    pts.append(["tower_roof + mast_length", tx])
    add(["sketch.polyline", {"sketch": "Tower section", "closed": True, "points": pts}])
    tower_blank = feature(["feature.revolve", {"sketch": "Tower section", "axis": f"e{2 * len(pts)}", "name": "Tower blank"}])
    feature(["feature.boolean", {"op": "subtract", "target": "Tower blank", "tool": "Terrain", "keepTool": True, "name": "Summit tower"}])
    # the polyline's lines are e(n+1) .. e(2n); the mast's are e(n+4) .. e(n+8): every other band red
    n = len(pts)
    red_bands = [f"{ids['Summit tower']}:copy(0)/{tower_blank}:side(e{n + 4 + b})" for b in range(0, bands, 2)]

    # ---- the contour layers (the laser-cut product): slabs of the terrain, alternately white and grey.
    # Layer 1 runs from sea level: its outline, at the stack's base level, is the whole map.
    feature(["feature.block", {"size": ["relief_width + 2 mm", "relief_depth + 2 mm", "(stack_base_level + contour_interval) * vertical_scale + 1 mm"], "position": ["-1 mm", "-1 mm", "-1 mm"], "name": "Layer 1 slab", "when": layers}])
    for k in (2, 3):
        feature(["feature.block", {"size": ["relief_width + 2 mm", "relief_depth + 2 mm", "sheet_thickness"], "position": ["-1 mm", "-1 mm", f"(stack_base_level + {k - 1} * contour_interval) * vertical_scale"], "name": f"Layer {k} slab", "when": f"{layers} && {k} <= contour_layer_count"}])
    max_layers = int((summit_m - (lowest // 100) * 100) // 100) + 1  # at the smallest interval, 100 m
    for k in range(4, max_layers + 1):
        source = 3 if k % 2 else 2
        feature(["feature.transform", {"source": f"Layer {source} slab", "translate": [0, 0, f"{k - source} * sheet_thickness"], "keep": True, "name": f"Layer {k} slab", "when": f"{layers} && {k} <= contour_layer_count"}])
    for k in range(1, max_layers + 1):
        when = layers if k == 1 else f"{layers} && {k} <= contour_layer_count"
        feature(["feature.boolean", {"op": "intersect", "target": f"Layer {k} slab", "tool": "Terrain", "keepTool": True, "name": f"Contour layer {k}", "when": when}])

    # ---- the walnut base
    base = feature(["feature.block", {"size": ["relief_width + 2 * base_border", "relief_depth + 2 * base_border", "base_thickness"], "position": ["-base_border", "-base_border", "-base_thickness"], "name": "Base blank"}])
    f = lambda k: f"{base}:face({k})"
    feature(["feature.fillet", {"edges": [[f(2), f(4)], [f(2), f(5)], [f(3), f(4)], [f(3), f(5)]], "radius": "base_corner_radius", "name": "Base corners"}])
    feature(["feature.fillet", {"edges": [[f(1), f(2)]], "chain": True, "radius": "base_round_over", "name": "Base round-over"}])
    feature(["feature.chamfer", {"edges": [[f(0), f(2)]], "chain": True, "distance": "bottom_edge_break", "name": "Walnut base"}])

    # ---- probes of the terrain at the summit node and at the start of the climb, for the checks
    feature(["feature.cylinder", {"radius": "0.05 mm", "height": "blank_height", "position": [f"{summit_i} * node_pitch", f"{summit_j} * node_pitch", "-1 mm"], "name": "Summit probe blank"}])
    feature(["feature.boolean", {"op": "intersect", "target": "Summit probe blank", "tool": "Terrain", "keepTool": True, "name": "Summit probe"}])
    feature(["feature.cylinder", {"radius": "0.05 mm", "height": "blank_height", "position": plan(*marks[0][:2]) + ["-1 mm"], "name": "Start probe blank"}])
    feature(["feature.boolean", {"op": "intersect", "target": "Start probe blank", "tool": "Terrain", "keepTool": True, "name": "Start probe"}])
    add(["feature.visible", {"feature": ["Terrain", "Summit probe", "Start probe"], "visible": False}])

    # ---- materials: filaments as measured by filamentcolors.xyz (Bambu Lab PLA Matte), matte dielectrics
    def look(body, color, roughness, subsurface=0.0):
        add(["body.appearance", {"body": body, "color": color, "metallic": 0, "roughness": roughness, "anisotropy": 0, "clearcoat": 0, "clearcoatRoughness": 0, "transmission": 0, "subsurface": subsurface, "subsurfaceColor": color, "pattern": None}])
    look("Forested slopes", "#656a4d", 0.8)
    add(["body.material", {"body": "Forested slopes", "name": "PLA Matte, Dark Green", "density": 1310}])
    look("Bald summit", "#d4d1c3", 0.8)
    add(["body.material", {"body": "Bald summit", "name": "PLA Matte, Bone White", "density": 1310}])
    add(["material.preset", {"body": "Kilometre pins", "preset": "steel", "color": "#c8a24a", "metallic": 1, "roughness": 0.3}])
    add(["body.material", {"body": "Kilometre pins", "name": "Brass CW508L", "density": 8470}])
    look("Summit tower", "#f2f2ef", 0.5)
    add(["face.appearance", {"body": "Summit tower", "faces": red_bands, "color": "#c21d24", "metallic": 0, "roughness": 0.5}])
    add(["body.material", {"body": "Summit tower", "name": "Resin, painted", "density": 1150}])
    for k, color in ((1, "#efefeb"), (2, "#cfcfca"), (3, "#efefeb")):
        look(f"Layer {k} slab", color, 0.45, 0.15)
        add(["body.material", {"body": f"Layer {k} slab", "name": "Cast acrylic, white" if color == "#efefeb" else "Cast acrylic, pale grey", "density": 1190}])
    add(["material.preset", {"body": "Walnut base", "preset": "walnut", "pattern": {"scale": 5}}])

    # ---- outputs and checks
    add(["assert.add", {"name": "Terrain volume from the data's mean height", "measure": "volume", "of": "Terrain", "eq": "relief_width * relief_depth * data_mean_elevation * vertical_scale", "tol": "0.001 * relief_width * relief_depth * data_mean_elevation * vertical_scale"}])
    add(["assert.add", {"name": "Summit at the data's height", "measure": "boxMax", "of": "Summit probe", "axis": "z", "min": "(summit_elevation - 2 m) * vertical_scale", "max": "(summit_elevation + 2 m) * vertical_scale"}])
    add(["assert.add", {"name": "Start of the climb at the road's height", "measure": "boxMax", "of": "Start probe", "axis": "z", "min": "(climb_start_altitude - srtm_accuracy) * vertical_scale", "max": "(climb_start_altitude + srtm_accuracy) * vertical_scale"}])
    add(["assert.add", {"name": "Sixteen kilometre pins", "measure": "count", "of": {"kind": "face", "where": {"in": "Kilometre pins", "surface": "cylinder"}}, "eq": "16", "when": relief}])
    above_edge = sum(1 for p in marks if p[2] > forest_edge)  # the pins whose holes go on through the summit's colour
    add(["assert.add", {"name": "A hole for every pin, through both colours", "measure": "count", "of": {"kind": "face", "where": [{"any": [{"in": "Forested slopes"}, {"in": "Bald summit"}]}, {"hole": True}]}, "eq": f"16 + {above_edge}", "when": relief}])
    add(["assert.add", {"name": "One layer per contour", "measure": "count", "of": {"kind": "body", "where": {"name": "Contour layer*"}}, "eq": "contour_layer_count", "when": layers}])
    add(["document.info", {"title": "Mont Ventoux relief", "description": "Mont Ventoux and the climb from Bédoin of the Tour de France Femmes 2026, stage 7, at 1:70 000: a relief 3D-printed in two colours, forest and bare limestone, with brass kilometre pins and the summit tower on a walnut base, or a stack of laser-cut contour layers. Elevation from SRTM, the road and the tower from IGN BD TOPO.", "author": "3DCraft examples", "licence": "MIT", "tags": ["topography", "relief", "map", "Mont Ventoux", "cycling", "art"]}])
    add(["document.check", {}])

    json.dump(S, open(HERE / "build.json", "w"), indent=0)
    return ids


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "fetch":
        fetch()
    elif len(sys.argv) == 1:
        build()
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()

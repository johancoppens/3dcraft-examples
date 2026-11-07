# Sources of the data in this folder

Written by `make.py fetch` on 2026-11-07. `make.py` builds `build.json` from these files alone.

## elevation.csv: the terrain

- **Data:** the Mapzen terrain tile `skadi/N44/N44E005.hgt.gz` (https://s3.amazonaws.com/elevation-tiles-prod/skadi/N44/N44E005.hgt.gz), 1 arc-second (about 30 m),
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
  101 from Bédoin to the summit, through the Géoplateforme WFS (https://data.geopf.fr/wfs/ows,
  type `BDTOPO_V3:troncon_de_route`), in Lambert-93 with IGN's altitudes (NGF-IGN69, stated to
  1.5 m). Sections last updated between 2024-10-02 and 2026-09-18.
- **Licence:** Licence Ouverte / Open Licence 2.0 (Etalab): free reuse with attribution. Attribution:
  "IGN – BD TOPO®, Géoplateforme, extracted 2026-11-07".
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

- **Data:** IGN BD TOPO, layer `batiment`, the building `BATIMENT0000000296827878` (nature "Tour, donjon", last updated
  2019-03-11): its footprint's centre and area, its ground altitude and height; and layer
  `construction_ponctuelle`, the antenna `CONSPONC0000000336577403` on it: the altitude of its top.
- **Licence:** as above, Licence Ouverte 2.0, "IGN – BD TOPO®, Géoplateforme, extracted 2026-11-07".

## The race

Tour de France Femmes avec Zwift 2026, stage 7, La Voulte-sur-Rhône to Mont Ventoux, 7 August 2026, with
the climb from Bédoin: "Mont Ventoux (15.7km at 8.8%)", Marion Rousse's stage commentary,
https://www.letourfemmes.fr/en/news/2026/stage-7/commentary-from-marion-rousse-22/1296943, and the stage
report, https://www.letourfemmes.fr/en/news/2026/stage-7/kasia-the-real-giant-of-provence/1301373
(both read 2026-11-07).

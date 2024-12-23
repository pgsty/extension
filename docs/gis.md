# GIS


> GIS: GeoSpatial Data Types, Operators, and Indexes, Hexagonal Indexing, OGR Data FDW, GeoIP & MobilityDB, etc...
## Extensions


There are 19 available extensions in this category:

[`postgis`](/postgis) [`postgis_topology`](/postgis_topology) [`postgis_raster`](/postgis_raster) [`postgis_sfcgal`](/postgis_sfcgal) [`postgis_tiger_geocoder`](/postgis_tiger_geocoder) [`address_standardizer`](/address_standardizer) [`address_standardizer_data_us`](/address_standardizer_data_us) [`pgrouting`](/pgrouting) [`pointcloud`](/pointcloud) [`pointcloud_postgis`](/pointcloud_postgis) [`h3`](/h3) [`h3_postgis`](/h3_postgis) [`q3c`](/q3c) [`ogr_fdw`](/ogr_fdw) [`geoip`](/geoip) [`pg_polyline`](/pg_polyline) [`pg_geohash`](/pg_geohash) [`mobilitydb`](/mobilitydb) [`earthdistance`](/earthdistance)


| ID | Extension | Version | Package | License | RPM | DEB | Website | `Bin` | `LOAD` | `DYLIB` | `DDL` | Description |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:-------:|:-----:|:------:|:-------:|:-----:|-------------|
| 1100 | [postgis](/postgis) | 3.5.0 | [postgis](/postgis) | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://git.osgeo.org/gitea/postgis/postgis) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | PostGIS geometry and geography spatial types and functions |
| 1101 | [postgis_topology](/postgis_topology) | 3.5.0 | [postgis](/postgis_topology) | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://git.osgeo.org/gitea/postgis/postgis) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | PostGIS topology spatial types and functions |
| 1102 | [postgis_raster](/postgis_raster) | 3.5.0 | [postgis](/postgis_raster) | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://git.osgeo.org/gitea/postgis/postgis) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | PostGIS raster types and functions |
| 1103 | [postgis_sfcgal](/postgis_sfcgal) | 3.5.0 | [postgis](/postgis_sfcgal) | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://git.osgeo.org/gitea/postgis/postgis) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | PostGIS SFCGAL functions |
| 1104 | [postgis_tiger_geocoder](/postgis_tiger_geocoder) | 3.5.0 | [postgis](/postgis_tiger_geocoder) | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://git.osgeo.org/gitea/postgis/postgis) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | PostGIS tiger geocoder and reverse geocoder |
| 1105 | [address_standardizer](/address_standardizer) | 3.5.0 | [postgis](/address_standardizer) | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://git.osgeo.org/gitea/postgis/postgis) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Used to parse an address into constituent elements. Generally used to support geocoding address normalization step. |
| 1106 | [address_standardizer_data_us](/address_standardizer_data_us) | 3.5.0 | [postgis](/address_standardizer_data_us) | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://git.osgeo.org/gitea/postgis/postgis) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Address Standardizer US dataset example |
| 1110 | [pgrouting](/pgrouting) | 3.7.0 | [pgrouting](/pgrouting) | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/pgRouting/pgrouting) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | pgRouting Extension |
| 1120 | [pointcloud](/pointcloud) | 1.2.5 | [pointcloud](/pointcloud) | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/pgpointcloud/pointcloud) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | data type for lidar point clouds |
| 1121 | [pointcloud_postgis](/pointcloud_postgis) | 1.2.5 | [pointcloud](/pointcloud_postgis) | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/pgpointcloud/pointcloud) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | integration for pointcloud LIDAR data and PostGIS geometry data |
| 1130 | [h3](/h3) | 4.1.3 | [pg_h3](/h3) | **<span class="tccyan">Apache-2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/zachasme/h3-pg) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | H3 bindings for PostgreSQL |
| 1131 | [h3_postgis](/h3_postgis) | 4.1.3 | [pg_h3](/h3_postgis) | **<span class="tccyan">Apache-2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/zachasme/h3-pg) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | H3 PostGIS integration |
| 1140 | [q3c](/q3c) | 2.0.1 | [q3c](/q3c) | **<span class="tcwarn">GPLv2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/segasai/q3c) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | q3c sky indexing plugin |
| 1150 | [ogr_fdw](/ogr_fdw) | 1.1 | [ogr_fdw](/ogr_fdw) | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/pramsey/pgsql-ogr-fdw) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | foreign-data wrapper for GIS data access |
| 1155 | [geoip](/geoip) | 0.3.0 | [geoip](/geoip) | **<span class="tcblue">BSD-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/tvondra/geoip) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | IP-based geolocation query |
| 1160 | [pg_polyline](/pg_polyline) | 0.0.1 | [pg_polyline](/pg_polyline) | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/yihong0618/pg_polyline) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Fast Google Encoded Polyline encoding & decoding for postgres |
| 1170 | [pg_geohash](/pg_geohash) | 1.0 | [pg_geohash](/pg_geohash) | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/jistok/pg_geohash) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Handle geohash based functionality for spatial coordinates |
| 1180 | [mobilitydb](/mobilitydb) | 1.1.1 | [mobilitydb](/mobilitydb) | **<span class="tcwarn">GPLv3</span>** |  | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/MobilityDB/MobilityDB) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | MobilityDB geospatial trajectory data management & analysis platform |
| 1190 | [earthdistance](/earthdistance) | 1.1 | [earthdistance](/earthdistance) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | **<span class="tcblue">CONTRIB</span>** | [LINK](https://www.postgresql.org/docs/current/earthdistance.html) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | calculate great-circle distances on the surface of the Earth |



### RHEL 8 Compatible (el8)

```yaml
pg17: postgis pgrouting pointcloud q3c geoip pg_polyline pg_geohash #pg_h3 #ogr_fdw #mobilitydb
pg16: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash #mobilitydb
pg15: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash #mobilitydb
pg14: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash #mobilitydb
pg13: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash #mobilitydb
```


### RHEL 9 Compatible (el9)

```yaml
pg17: postgis pgrouting pointcloud q3c geoip pg_polyline pg_geohash #pg_h3 #ogr_fdw #mobilitydb
pg16: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash #mobilitydb
pg15: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash #mobilitydb
pg14: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash #mobilitydb
pg13: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash #mobilitydb
```


### Debian 12 bookworm Compatible (d12)

```yaml
pg17: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash mobilitydb
pg16: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash mobilitydb
pg15: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash mobilitydb
pg14: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash mobilitydb
pg13: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash mobilitydb
```


### Ubuntu 24.04 jammy Compatible (u22)

```yaml
pg17: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash mobilitydb
pg16: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash mobilitydb
pg15: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash mobilitydb
pg14: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash mobilitydb
pg13: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash mobilitydb
```


### Ubuntu 24.04 noble Compatible (u24)

```yaml
pg17: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash mobilitydb
pg16: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash mobilitydb
pg15: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash mobilitydb
pg14: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash mobilitydb
pg13: postgis pgrouting pointcloud pg_h3 q3c ogr_fdw geoip pg_polyline pg_geohash mobilitydb
```



--------

## RPM Packages


| Package | Version | License | RPM | RPM Package | 17 | 16 | 15 | 14 | 13 | Description |
|---------|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|-------------|
| [postgis](/postgis) | 3.5.0 | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | `postgis35_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | PostGIS geometry and geography spatial types and functions |
| [pgrouting](/pgrouting) | 3.7.0 | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | `pgrouting_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | pgRouting Extension |
| [pointcloud](/pointcloud) | 1.2.5 | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | `pointcloud_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | data type for lidar point clouds |
| [pg_h3](/h3) | 4.1.3 | **<span class="tccyan">Apache-2</span>** | **<span class="tccyan">PGDG</span>** | `h3-pg_$v*` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | H3 bindings for PostgreSQL |
| [q3c](/q3c) | 2.0.1 | **<span class="tcwarn">GPLv2</span>** | **<span class="tcwarn">PIGSTY</span>** | `q3c_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | q3c sky indexing plugin |
| [ogr_fdw](/ogr_fdw) | 1.1 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `ogr_fdw_$v*` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | foreign-data wrapper for GIS data access |
| [geoip](/geoip) | 0.3.0 | **<span class="tcblue">BSD-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `geoip_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | IP-based geolocation query |
| [pg_polyline](/pg_polyline) | 0.0.1 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_polyline_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Fast Google Encoded Polyline encoding & decoding for postgres |
| [pg_geohash](/pg_geohash) | 1.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_geohash_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Handle geohash based functionality for spatial coordinates |
| [earthdistance](/earthdistance) | 1.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql$v-contrib` | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | calculate great-circle distances on the surface of the Earth |



### RHEL 8 Compatible (el8)

```yaml
pg17: postgis35_17* pgrouting_17* pointcloud_17* q3c_17* geoip_17* pg_polyline_17 pg_geohash_17* #h3-pg_17* #ogr_fdw_17*
pg16: postgis35_16* pgrouting_16* pointcloud_16* h3-pg_16* q3c_16* ogr_fdw_16* geoip_16* pg_polyline_16 pg_geohash_16*
pg15: postgis35_15* pgrouting_15* pointcloud_15* h3-pg_15* q3c_15* ogr_fdw_15* geoip_15* pg_polyline_15 pg_geohash_15*
pg14: postgis35_14* pgrouting_14* pointcloud_14* h3-pg_14* q3c_14* ogr_fdw_14* geoip_14* pg_polyline_14 pg_geohash_14*
pg13: postgis35_13* pgrouting_13* pointcloud_13* h3-pg_13* q3c_13* ogr_fdw_13* geoip_13* pg_polyline_13 pg_geohash_13*
```


### RHEL 9 Compatible (el9)

```yaml
pg17: postgis35_17* pgrouting_17* pointcloud_17* q3c_17* geoip_17* pg_polyline_17 pg_geohash_17* #h3-pg_17* #ogr_fdw_17*
pg16: postgis35_16* pgrouting_16* pointcloud_16* h3-pg_16* q3c_16* ogr_fdw_16* geoip_16* pg_polyline_16 pg_geohash_16*
pg15: postgis35_15* pgrouting_15* pointcloud_15* h3-pg_15* q3c_15* ogr_fdw_15* geoip_15* pg_polyline_15 pg_geohash_15*
pg14: postgis35_14* pgrouting_14* pointcloud_14* h3-pg_14* q3c_14* ogr_fdw_14* geoip_14* pg_polyline_14 pg_geohash_14*
pg13: postgis35_13* pgrouting_13* pointcloud_13* h3-pg_13* q3c_13* ogr_fdw_13* geoip_13* pg_polyline_13 pg_geohash_13*
```



--------

## DEB Packages


| Package | Version | License | DEB | DEB Package | 17 | 16 | 15 | 14 | 13 | Description |
|---------|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|-------------|
| [postgis](/postgis) | 3.5.0 | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-postgis-3`<br>`postgresql-$v-postgis-3-scripts` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | PostGIS geometry and geography spatial types and functions |
| [pgrouting](/pgrouting) | 3.7.0 | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pgrouting`<br>`postgresql-$v-pgrouting-scripts` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | pgRouting Extension |
| [pointcloud](/pointcloud) | 1.2.5 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pointcloud` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | data type for lidar point clouds |
| [pg_h3](/h3) | 4.1.4 | **<span class="tccyan">Apache-2</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-h3` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | H3 bindings for PostgreSQL |
| [q3c](/q3c) | 2.0.1 | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-q3c` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | q3c sky indexing plugin |
| [ogr_fdw](/ogr_fdw) | 1.1 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-ogr-fdw` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | foreign-data wrapper for GIS data access |
| [geoip](/geoip) | 0.3.0 | **<span class="tcblue">BSD-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-geoip` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | IP-based geolocation query |
| [pg_polyline](/pg_polyline) | 0.0.1 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-polyline` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Fast Google Encoded Polyline encoding & decoding for postgres |
| [pg_geohash](/pg_geohash) | 1.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-geohash` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Handle geohash based functionality for spatial coordinates |
| [mobilitydb](/mobilitydb) | 1.2.0 | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-mobilitydb` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | MobilityDB geospatial trajectory data management & analysis platform |
| [earthdistance](/earthdistance) | 1.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql-$v` | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | calculate great-circle distances on the surface of the Earth |



### Debian 12 bookworm Compatible (d12)

```yaml
pg17: postgresql-17-postgis-3 postgresql-17-postgis-3-scripts postgresql-17-pgrouting postgresql-17-pgrouting-scripts postgresql-17-pointcloud postgresql-17-h3 postgresql-17-q3c postgresql-17-ogr-fdw postgresql-17-geoip postgresql-17-pg-polyline postgresql-17-pg-geohash postgresql-17-mobilitydb
pg16: postgresql-16-postgis-3 postgresql-16-postgis-3-scripts postgresql-16-pgrouting postgresql-16-pgrouting-scripts postgresql-16-pointcloud postgresql-16-h3 postgresql-16-q3c postgresql-16-ogr-fdw postgresql-16-geoip postgresql-16-pg-polyline postgresql-16-pg-geohash postgresql-16-mobilitydb
pg15: postgresql-15-postgis-3 postgresql-15-postgis-3-scripts postgresql-15-pgrouting postgresql-15-pgrouting-scripts postgresql-15-pointcloud postgresql-15-h3 postgresql-15-q3c postgresql-15-ogr-fdw postgresql-15-geoip postgresql-15-pg-polyline postgresql-15-pg-geohash postgresql-15-mobilitydb
pg14: postgresql-14-postgis-3 postgresql-14-postgis-3-scripts postgresql-14-pgrouting postgresql-14-pgrouting-scripts postgresql-14-pointcloud postgresql-14-h3 postgresql-14-q3c postgresql-14-ogr-fdw postgresql-14-geoip postgresql-14-pg-polyline postgresql-14-pg-geohash postgresql-14-mobilitydb
pg13: postgresql-13-postgis-3 postgresql-13-postgis-3-scripts postgresql-13-pgrouting postgresql-13-pgrouting-scripts postgresql-13-pointcloud postgresql-13-h3 postgresql-13-q3c postgresql-13-ogr-fdw postgresql-13-geoip postgresql-13-pg-polyline postgresql-13-pg-geohash postgresql-13-mobilitydb
```


### Ubuntu 24.04 jammy Compatible (u22)

```yaml
pg17: postgresql-17-postgis-3 postgresql-17-postgis-3-scripts postgresql-17-pgrouting postgresql-17-pgrouting-scripts postgresql-17-pointcloud postgresql-17-h3 postgresql-17-q3c postgresql-17-ogr-fdw postgresql-17-geoip postgresql-17-pg-polyline postgresql-17-pg-geohash postgresql-17-mobilitydb
pg16: postgresql-16-postgis-3 postgresql-16-postgis-3-scripts postgresql-16-pgrouting postgresql-16-pgrouting-scripts postgresql-16-pointcloud postgresql-16-h3 postgresql-16-q3c postgresql-16-ogr-fdw postgresql-16-geoip postgresql-16-pg-polyline postgresql-16-pg-geohash postgresql-16-mobilitydb
pg15: postgresql-15-postgis-3 postgresql-15-postgis-3-scripts postgresql-15-pgrouting postgresql-15-pgrouting-scripts postgresql-15-pointcloud postgresql-15-h3 postgresql-15-q3c postgresql-15-ogr-fdw postgresql-15-geoip postgresql-15-pg-polyline postgresql-15-pg-geohash postgresql-15-mobilitydb
pg14: postgresql-14-postgis-3 postgresql-14-postgis-3-scripts postgresql-14-pgrouting postgresql-14-pgrouting-scripts postgresql-14-pointcloud postgresql-14-h3 postgresql-14-q3c postgresql-14-ogr-fdw postgresql-14-geoip postgresql-14-pg-polyline postgresql-14-pg-geohash postgresql-14-mobilitydb
pg13: postgresql-13-postgis-3 postgresql-13-postgis-3-scripts postgresql-13-pgrouting postgresql-13-pgrouting-scripts postgresql-13-pointcloud postgresql-13-h3 postgresql-13-q3c postgresql-13-ogr-fdw postgresql-13-geoip postgresql-13-pg-polyline postgresql-13-pg-geohash postgresql-13-mobilitydb
```


### Ubuntu 24.04 noble Compatible (u24)

```yaml
pg17: postgresql-17-postgis-3 postgresql-17-postgis-3-scripts postgresql-17-pgrouting postgresql-17-pgrouting-scripts postgresql-17-pointcloud postgresql-17-h3 postgresql-17-q3c postgresql-17-ogr-fdw postgresql-17-geoip postgresql-17-pg-polyline postgresql-17-pg-geohash postgresql-17-mobilitydb
pg16: postgresql-16-postgis-3 postgresql-16-postgis-3-scripts postgresql-16-pgrouting postgresql-16-pgrouting-scripts postgresql-16-pointcloud postgresql-16-h3 postgresql-16-q3c postgresql-16-ogr-fdw postgresql-16-geoip postgresql-16-pg-polyline postgresql-16-pg-geohash postgresql-16-mobilitydb
pg15: postgresql-15-postgis-3 postgresql-15-postgis-3-scripts postgresql-15-pgrouting postgresql-15-pgrouting-scripts postgresql-15-pointcloud postgresql-15-h3 postgresql-15-q3c postgresql-15-ogr-fdw postgresql-15-geoip postgresql-15-pg-polyline postgresql-15-pg-geohash postgresql-15-mobilitydb
pg14: postgresql-14-postgis-3 postgresql-14-postgis-3-scripts postgresql-14-pgrouting postgresql-14-pgrouting-scripts postgresql-14-pointcloud postgresql-14-h3 postgresql-14-q3c postgresql-14-ogr-fdw postgresql-14-geoip postgresql-14-pg-polyline postgresql-14-pg-geohash postgresql-14-mobilitydb
pg13: postgresql-13-postgis-3 postgresql-13-postgis-3-scripts postgresql-13-pgrouting postgresql-13-pgrouting-scripts postgresql-13-pointcloud postgresql-13-h3 postgresql-13-q3c postgresql-13-ogr-fdw postgresql-13-geoip postgresql-13-pg-polyline postgresql-13-pg-geohash postgresql-13-mobilitydb
```



--------

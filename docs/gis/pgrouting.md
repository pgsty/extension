# pgrouting


> [pgrouting](/https://github.com/pgRouting/pgrouting): pgRouting Extension


-------

## Extension


| ID | Extension | Version | License | RPM | DEB | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` | Requires |
|:--:|-----------|:-------:|:-------:|:---:|:---:|:------:|:-------:|:-----:|:-------:|:-------:|----------|
| 1110 | [pgrouting](https://github.com/pgRouting/pgrouting) | 3.6.0 | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | [`postgis`](/gis/postgis) |


> **Comment**: miss deb


```sql
CREATE EXTENSION pgroutingCASCADE;
```


-----------


## Packages


| OS | Version | License | RPM | RPM Package | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 3.6.0 | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | `pgrouting_$v*` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |
| [DEB](/deb) | 3.6.2 | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pgrouting*` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |



Install `pgrouting` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pgrouting_17*;
dnf install pgrouting_16*;
dnf install pgrouting_15*;
dnf install pgrouting_14*;
dnf install pgrouting_13*;
dnf install pgrouting_12*;
```


Install `pgrouting` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pgrouting*;
apt install postgresql-16-pgrouting*;
apt install postgresql-15-pgrouting*;
apt install postgresql-14-pgrouting*;
apt install postgresql-13-pgrouting*;
apt install postgresql-12-pgrouting*;
```


-----------


## Category: GIS


| ID | Extension | Version | Package | License | RPM | DEB | lang | Tags | Schemas | Requires | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:----:|------|---------|----------|:------:|:-------:|:-----:|:-------:|:-------:|
| 1100 | [postgis](/gis/postgis) | 3.5.0 | [postgis](/gis/postgis) | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1101 | [postgis_topology](/gis/postgis_topology) | 3.5.0 | [postgis](/gis/postgis_topology) | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  | `topology` | [`postgis`](/gis/postgis) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1102 | [postgis_raster](/gis/postgis_raster) | 3.5.0 | [postgis](/gis/postgis_raster) | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  | [`postgis`](/gis/postgis) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1103 | [postgis_sfcgal](/gis/postgis_sfcgal) | 3.5.0 | [postgis](/gis/postgis_sfcgal) | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  | [`postgis`](/gis/postgis) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1104 | [postgis_tiger_geocoder](/gis/postgis_tiger_geocoder) | 3.5.0 | [postgis](/gis/postgis_tiger_geocoder) | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  | `tiger` | [`postgis`](/gis/postgis), [`fuzzystrmatch`](/fts/fuzzystrmatch) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |
| 1105 | [address_standardizer](/gis/address_standardizer) | 3.5.0 | [postgis](/gis/address_standardizer) | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1106 | [address_standardizer_data_us](/gis/address_standardizer_data_us) | 3.5.0 | [postgis](/gis/address_standardizer_data_us) | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1110 | [pgrouting](/gis/pgrouting) | 3.6.0 | [pgrouting](/gis/pgrouting) | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  | [`postgis`](/gis/postgis) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1120 | [pointcloud](/gis/pointcloud) | 1.2.5 | [pointcloud](/gis/pointcloud) | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1121 | [pointcloud_postgis](/gis/pointcloud_postgis) | 1.2.5 | [pointcloud](/gis/pointcloud_postgis) | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  | [`postgis`](/gis/postgis), [`pointcloud`](/gis/pointcloud) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |
| 1130 | [h3](/gis/h3) | 4.1.3 | [pg_h3](/gis/h3) | **<span class="tccyan">Apache-2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1131 | [h3_postgis](/gis/h3_postgis) | 4.1.3 | [pg_h3](/gis/h3_postgis) | **<span class="tccyan">Apache-2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  | [`h3`](/gis/h3), [`postgis`](/gis/postgis), [`postgis_raster`](/gis/postgis_raster) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1140 | [q3c](/gis/q3c) | 2.0.1 | [q3c](/gis/q3c) | **<span class="tcwarn">GPLv2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1150 | [ogr_fdw](/gis/ogr_fdw) | 1.1 | [ogr_fdw](/gis/ogr_fdw) | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1155 | [geoip](/gis/geoip) | 0.3.0 | [geoip](/gis/geoip) | **<span class="tcblue">BSD-2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** |  |  | `geoip` | [`ip4r`](/type/ip4r) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1160 | [pg_polyline](/gis/pg_polyline) | 0.0.0 | [pg_polyline](/gis/pg_polyline) | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | Rust | `pgrx` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |
| 1170 | [pg_geohash](/gis/pg_geohash) | 1.0 | [pg_geohash](/gis/pg_geohash) | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | C | `nil-lic` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1180 | [mobilitydb](/gis/mobilitydb) | 1.1.1 | [mobilitydb](/gis/mobilitydb) | **<span class="tcwarn">GPLv3</span>** |  | **<span class="tccyan">PGDG</span>** |  |  |  | [`postgis`](/gis/postgis) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1190 | [earthdistance](/gis/earthdistance) | 1.1 | [earthdistance](/gis/earthdistance) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | **<span class="tcblue">CONTRIB</span>** | C |  |  | [`cube`](/type/cube) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |




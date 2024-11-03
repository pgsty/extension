# mobilitydb


> [mobilitydb](https://github.com/MobilityDB/MobilityDB): MobilityDB geospatial trajectory data management & analysis platform
>
> https://github.com/MobilityDB/MobilityDB





[GIS](/gis) extensions: [`postgis`](/postgis), [`postgis_topology`](/postgis_topology), [`postgis_raster`](/postgis_raster), [`postgis_sfcgal`](/postgis_sfcgal), [`postgis_tiger_geocoder`](/postgis_tiger_geocoder), [`address_standardizer`](/address_standardizer), [`address_standardizer_data_us`](/address_standardizer_data_us), [`pgrouting`](/pgrouting), [`pointcloud`](/pointcloud), [`pointcloud_postgis`](/pointcloud_postgis), [`h3`](/h3), [`h3_postgis`](/h3_postgis), [`q3c`](/q3c), [`ogr_fdw`](/ogr_fdw), [`geoip`](/geoip), [`pg_polyline`](/pg_polyline), [`pg_geohash`](/pg_geohash), [`mobilitydb`](/mobilitydb), [`earthdistance`](/earthdistance)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [mobilitydb](https://github.com/MobilityDB/MobilityDB) | 1.1.1 | **<span class="tcwarn">GPLv3</span>** |  | **<span class="tccyan">PGDG</span>** |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Package | Tags | Schemas | Requires | Required by |
|---------|------|---------|----------|-------------|
| [mobilitydb](/mobilitydb) |  |  | [`postgis`](postgis) |  |





```sql
CREATE EXTENSION mobilitydb CASCADE;
```
> **Comment**: need another schema
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [DEB](/deb) | 1.1.1 | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-mobilitydb` |  |  |  |  |  |  |  |



Install `mobilitydb` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["mobilitydb"]}'
```


Install `mobilitydb` [DEB](/deb) from the  **APT** repo:

```bash
apt install postgresql-$v-mobilitydb;
```








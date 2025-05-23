# pg_polyline


> [pg_polyline](https://github.com/yihong0618/pg_polyline): Fast Google Encoded Polyline encoding & decoding for postgres
>
> https://github.com/yihong0618/pg_polyline





[GIS](/gis) extensions: [`postgis`](/postgis), [`postgis_topology`](/postgis_topology), [`postgis_raster`](/postgis_raster), [`postgis_sfcgal`](/postgis_sfcgal), [`postgis_tiger_geocoder`](/postgis_tiger_geocoder), [`address_standardizer`](/address_standardizer), [`address_standardizer_data_us`](/address_standardizer_data_us), [`pgrouting`](/pgrouting), [`pointcloud`](/pointcloud), [`pointcloud_postgis`](/pointcloud_postgis), [`h3`](/h3), [`h3_postgis`](/h3_postgis), [`q3c`](/q3c), [`ogr_fdw`](/ogr_fdw), [`geoip`](/geoip), [`pg_polyline`](/pg_polyline), [`pg_geohash`](/pg_geohash), [`mobilitydb`](/mobilitydb), [`tzf`](/tzf), [`earthdistance`](/earthdistance)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_polyline](https://github.com/yihong0618/pg_polyline) | 0.0.1 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_polyline](/pg_polyline) | `pgrx` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_polyline;
```
> **Comment**: pgrx=0.12.7
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.0.1 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_polyline_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 0.0.1 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-polyline` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pg_polyline` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_polyline
```


Install `pg_polyline` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_polyline"]}'
```


Install `pg_polyline` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_polyline_17;
dnf install pg_polyline_16;
dnf install pg_polyline_15;
dnf install pg_polyline_14;
dnf install pg_polyline_13;
```


Install `pg_polyline` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-polyline;
apt install postgresql-16-pg-polyline;
apt install postgresql-15-pg-polyline;
apt install postgresql-14-pg-polyline;
apt install postgresql-13-pg-polyline;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_polyline_17` | `pg_polyline_16` | `pg_polyline_15` | `pg_polyline_14` | `pg_polyline_13` |
| `el9` | `pg_polyline_17` | `pg_polyline_16` | `pg_polyline_15` | `pg_polyline_14` | `pg_polyline_13` |
| `d12` | `postgresql-17-pg-polyline` | `postgresql-16-pg-polyline` | `postgresql-15-pg-polyline` | `postgresql-14-pg-polyline` | `postgresql-13-pg-polyline` |
| `u22` | `postgresql-17-pg-polyline` | `postgresql-16-pg-polyline` | `postgresql-15-pg-polyline` | `postgresql-14-pg-polyline` | `postgresql-13-pg-polyline` |
| `u24` | `postgresql-17-pg-polyline` | `postgresql-16-pg-polyline` | `postgresql-15-pg-polyline` | `postgresql-14-pg-polyline` | `postgresql-13-pg-polyline` |






# pgrouting


> [pgrouting](https://github.com/pgRouting/pgrouting): pgRouting Extension
>
> https://github.com/pgRouting/pgrouting





[GIS](/gis) extensions: [`postgis`](/postgis), [`postgis_topology`](/postgis_topology), [`postgis_raster`](/postgis_raster), [`postgis_sfcgal`](/postgis_sfcgal), [`postgis_tiger_geocoder`](/postgis_tiger_geocoder), [`address_standardizer`](/address_standardizer), [`address_standardizer_data_us`](/address_standardizer_data_us), [`pgrouting`](/pgrouting), [`pointcloud`](/pointcloud), [`pointcloud_postgis`](/pointcloud_postgis), [`h3`](/h3), [`h3_postgis`](/h3_postgis), [`q3c`](/q3c), [`ogr_fdw`](/ogr_fdw), [`geoip`](/geoip), [`pg_polyline`](/pg_polyline), [`pg_geohash`](/pg_geohash), [`mobilitydb`](/mobilitydb), [`earthdistance`](/earthdistance)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgrouting](https://github.com/pgRouting/pgrouting) | 3.7.0 | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgrouting](/pgrouting) |  |  | [`postgis`](postgis) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pgrouting CASCADE;
```
> **Comment**: pg17 on deb not ready
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 3.7.0 | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | `pgrouting_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 3.7.0 | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pgrouting postgresql-$v-pgrouting-scripts` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pgrouting` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgrouting"]}'
```


Install `pgrouting` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install pgrouting_17*;
yum install pgrouting_16*;
yum install pgrouting_15*;
yum install pgrouting_14*;
yum install pgrouting_13*;
yum install pgrouting_12*;
```


Install `pgrouting` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pgrouting postgresql-17-pgrouting-scripts;
apt install postgresql-16-pgrouting postgresql-16-pgrouting-scripts;
apt install postgresql-15-pgrouting postgresql-15-pgrouting-scripts;
apt install postgresql-14-pgrouting postgresql-14-pgrouting-scripts;
apt install postgresql-13-pgrouting postgresql-13-pgrouting-scripts;
apt install postgresql-12-pgrouting postgresql-12-pgrouting-scripts;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgrouting_17*` | `pgrouting_16*` | `pgrouting_15*` | `pgrouting_14*` | `pgrouting_13*` | `pgrouting_12*` |
| `el9` | `pgrouting_17*` | `pgrouting_16*` | `pgrouting_15*` | `pgrouting_14*` | `pgrouting_13*` | `pgrouting_12*` |
| `d12` | `postgresql-17-pgrouting`<br>`postgresql-17-pgrouting-scripts` | `postgresql-16-pgrouting`<br>`postgresql-16-pgrouting-scripts` | `postgresql-15-pgrouting`<br>`postgresql-15-pgrouting-scripts` | `postgresql-14-pgrouting`<br>`postgresql-14-pgrouting-scripts` | `postgresql-13-pgrouting`<br>`postgresql-13-pgrouting-scripts` | `postgresql-12-pgrouting`<br>`postgresql-12-pgrouting-scripts` |
| `u22` | `postgresql-17-pgrouting`<br>`postgresql-17-pgrouting-scripts` | `postgresql-16-pgrouting`<br>`postgresql-16-pgrouting-scripts` | `postgresql-15-pgrouting`<br>`postgresql-15-pgrouting-scripts` | `postgresql-14-pgrouting`<br>`postgresql-14-pgrouting-scripts` | `postgresql-13-pgrouting`<br>`postgresql-13-pgrouting-scripts` | `postgresql-12-pgrouting`<br>`postgresql-12-pgrouting-scripts` |
| `u24` | `postgresql-17-pgrouting`<br>`postgresql-17-pgrouting-scripts` | `postgresql-16-pgrouting`<br>`postgresql-16-pgrouting-scripts` | `postgresql-15-pgrouting`<br>`postgresql-15-pgrouting-scripts` | `postgresql-14-pgrouting`<br>`postgresql-14-pgrouting-scripts` | `postgresql-13-pgrouting`<br>`postgresql-13-pgrouting-scripts` | `postgresql-12-pgrouting`<br>`postgresql-12-pgrouting-scripts` |






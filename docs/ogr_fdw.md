# ogr_fdw


> [ogr_fdw](https://github.com/pramsey/pgsql-ogr-fdw): foreign-data wrapper for GIS data access
>
> https://github.com/pramsey/pgsql-ogr-fdw





[GIS](/gis) extensions: [`postgis`](/postgis), [`postgis_topology`](/postgis_topology), [`postgis_raster`](/postgis_raster), [`postgis_sfcgal`](/postgis_sfcgal), [`postgis_tiger_geocoder`](/postgis_tiger_geocoder), [`address_standardizer`](/address_standardizer), [`address_standardizer_data_us`](/address_standardizer_data_us), [`pgrouting`](/pgrouting), [`pointcloud`](/pointcloud), [`pointcloud_postgis`](/pointcloud_postgis), [`h3`](/h3), [`h3_postgis`](/h3_postgis), [`q3c`](/q3c), [`ogr_fdw`](/ogr_fdw), [`geoip`](/geoip), [`pg_polyline`](/pg_polyline), [`pg_geohash`](/pg_geohash), [`mobilitydb`](/mobilitydb), [`earthdistance`](/earthdistance)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [ogr_fdw](https://github.com/pramsey/pgsql-ogr-fdw) | 1.1.5 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [ogr_fdw](/ogr_fdw) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION ogr_fdw;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.1.5 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `ogr_fdw_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 1.1 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-ogr-fdw` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `ogr_fdw` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add ogr_fdw
```


Install `ogr_fdw` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["ogr_fdw"]}'
```


Install `ogr_fdw` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install ogr_fdw_17*;
dnf install ogr_fdw_16*;
dnf install ogr_fdw_15*;
dnf install ogr_fdw_14*;
dnf install ogr_fdw_13*;
```


Install `ogr_fdw` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-ogr-fdw;
apt install postgresql-16-ogr-fdw;
apt install postgresql-15-ogr-fdw;
apt install postgresql-14-ogr-fdw;
apt install postgresql-13-ogr-fdw;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `ogr_fdw_17*` | `ogr_fdw_16*` | `ogr_fdw_15*` | `ogr_fdw_14*` | `ogr_fdw_13*` |
| `el9` | `ogr_fdw_17*` | `ogr_fdw_16*` | `ogr_fdw_15*` | `ogr_fdw_14*` | `ogr_fdw_13*` |
| `d12` | `postgresql-17-ogr-fdw` | `postgresql-16-ogr-fdw` | `postgresql-15-ogr-fdw` | `postgresql-14-ogr-fdw` | `postgresql-13-ogr-fdw` |
| `u22` | `postgresql-17-ogr-fdw` | `postgresql-16-ogr-fdw` | `postgresql-15-ogr-fdw` | `postgresql-14-ogr-fdw` | `postgresql-13-ogr-fdw` |
| `u24` | `postgresql-17-ogr-fdw` | `postgresql-16-ogr-fdw` | `postgresql-15-ogr-fdw` | `postgresql-14-ogr-fdw` | `postgresql-13-ogr-fdw` |






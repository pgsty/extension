# q3c


> [q3c](https://github.com/segasai/q3c): q3c sky indexing plugin
>
> https://github.com/segasai/q3c





[GIS](/gis) extensions: [`postgis`](/postgis), [`postgis_topology`](/postgis_topology), [`postgis_raster`](/postgis_raster), [`postgis_sfcgal`](/postgis_sfcgal), [`postgis_tiger_geocoder`](/postgis_tiger_geocoder), [`address_standardizer`](/address_standardizer), [`address_standardizer_data_us`](/address_standardizer_data_us), [`pgrouting`](/pgrouting), [`pointcloud`](/pointcloud), [`pointcloud_postgis`](/pointcloud_postgis), [`h3`](/h3), [`h3_postgis`](/h3_postgis), [`q3c`](/q3c), [`ogr_fdw`](/ogr_fdw), [`geoip`](/geoip), [`pg_polyline`](/pg_polyline), [`pg_geohash`](/pg_geohash), [`mobilitydb`](/mobilitydb), [`tzf`](/tzf), [`earthdistance`](/earthdistance)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [q3c](https://github.com/segasai/q3c) | 2.0.1 | **<span class="tcwarn">GPLv2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [q3c](/q3c) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION q3c;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 2.0.1 | **<span class="tcwarn">GPLv2</span>** | **<span class="tcwarn">PIGSTY</span>** | `q3c_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 2.0.1 | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-q3c` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `q3c` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add q3c
```


Install `q3c` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["q3c"]}'
```


Install `q3c` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install q3c_17*;
dnf install q3c_16*;
dnf install q3c_15*;
dnf install q3c_14*;
dnf install q3c_13*;
```


Install `q3c` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-q3c;
apt install postgresql-16-q3c;
apt install postgresql-15-q3c;
apt install postgresql-14-q3c;
apt install postgresql-13-q3c;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `q3c_17*` | `q3c_16*` | `q3c_15*` | `q3c_14*` | `q3c_13*` |
| `el9` | `q3c_17*` | `q3c_16*` | `q3c_15*` | `q3c_14*` | `q3c_13*` |
| `d12` | `postgresql-17-q3c` | `postgresql-16-q3c` | `postgresql-15-q3c` | `postgresql-14-q3c` | `postgresql-13-q3c` |
| `u22` | `postgresql-17-q3c` | `postgresql-16-q3c` | `postgresql-15-q3c` | `postgresql-14-q3c` | `postgresql-13-q3c` |
| `u24` | `postgresql-17-q3c` | `postgresql-16-q3c` | `postgresql-15-q3c` | `postgresql-14-q3c` | `postgresql-13-q3c` |






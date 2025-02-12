# postgis_topology


> [postgis](https://git.osgeo.org/gitea/postgis/postgis): PostGIS topology spatial types and functions
>
> https://git.osgeo.org/gitea/postgis/postgis





[GIS](/gis) extensions: [`postgis`](/postgis), [`postgis_topology`](/postgis_topology), [`postgis_raster`](/postgis_raster), [`postgis_sfcgal`](/postgis_sfcgal), [`postgis_tiger_geocoder`](/postgis_tiger_geocoder), [`address_standardizer`](/address_standardizer), [`address_standardizer_data_us`](/address_standardizer_data_us), [`pgrouting`](/pgrouting), [`pointcloud`](/pointcloud), [`pointcloud_postgis`](/pointcloud_postgis), [`h3`](/h3), [`h3_postgis`](/h3_postgis), [`q3c`](/q3c), [`ogr_fdw`](/ogr_fdw), [`geoip`](/geoip), [`pg_polyline`](/pg_polyline), [`pg_geohash`](/pg_geohash), [`mobilitydb`](/mobilitydb), [`earthdistance`](/earthdistance)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [postgis_topology](https://git.osgeo.org/gitea/postgis/postgis) | 3.5.2 | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [postgis](/postgis_topology) |  | `topology` | [`postgis`](postgis) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION postgis_topology CASCADE;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| Distro-postgis | 3.5.2 | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | `postgis35_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| Distro-postgis | 3.5.2 | **<span class="tcwarn">GPLv2</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-postgis-3 postgresql-$v-postgis-3-scripts` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `postgis_topology` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add postgis_topology
```


Install `postgis` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["postgis"]}'
```


Install `postgis` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install postgis35_17*;
dnf install postgis35_16*;
dnf install postgis35_15*;
dnf install postgis35_14*;
dnf install postgis35_13*;
```


Install `postgis` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-postgis-3 postgresql-17-postgis-3-scripts;
apt install postgresql-16-postgis-3 postgresql-16-postgis-3-scripts;
apt install postgresql-15-postgis-3 postgresql-15-postgis-3-scripts;
apt install postgresql-14-postgis-3 postgresql-14-postgis-3-scripts;
apt install postgresql-13-postgis-3 postgresql-13-postgis-3-scripts;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `postgis35_17*` | `postgis35_16*` | `postgis35_15*` | `postgis35_14*` | `postgis35_13*` |
| `el9` | `postgis35_17*` | `postgis35_16*` | `postgis35_15*` | `postgis35_14*` | `postgis35_13*` |
| `d12` | `postgresql-17-postgis-3`<br>`postgresql-17-postgis-3-scripts` | `postgresql-16-postgis-3`<br>`postgresql-16-postgis-3-scripts` | `postgresql-15-postgis-3`<br>`postgresql-15-postgis-3-scripts` | `postgresql-14-postgis-3`<br>`postgresql-14-postgis-3-scripts` | `postgresql-13-postgis-3`<br>`postgresql-13-postgis-3-scripts` |
| `u22` | `postgresql-17-postgis-3`<br>`postgresql-17-postgis-3-scripts` | `postgresql-16-postgis-3`<br>`postgresql-16-postgis-3-scripts` | `postgresql-15-postgis-3`<br>`postgresql-15-postgis-3-scripts` | `postgresql-14-postgis-3`<br>`postgresql-14-postgis-3-scripts` | `postgresql-13-postgis-3`<br>`postgresql-13-postgis-3-scripts` |
| `u24` | `postgresql-17-postgis-3`<br>`postgresql-17-postgis-3-scripts` | `postgresql-16-postgis-3`<br>`postgresql-16-postgis-3-scripts` | `postgresql-15-postgis-3`<br>`postgresql-15-postgis-3-scripts` | `postgresql-14-postgis-3`<br>`postgresql-14-postgis-3-scripts` | `postgresql-13-postgis-3`<br>`postgresql-13-postgis-3-scripts` |






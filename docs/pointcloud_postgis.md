# pointcloud_postgis


> [pointcloud](https://github.com/pgpointcloud/pointcloud): integration for pointcloud LIDAR data and PostGIS geometry data
>
> https://github.com/pgpointcloud/pointcloud





[GIS](/gis) extensions: [`postgis`](/postgis), [`postgis_topology`](/postgis_topology), [`postgis_raster`](/postgis_raster), [`postgis_sfcgal`](/postgis_sfcgal), [`postgis_tiger_geocoder`](/postgis_tiger_geocoder), [`address_standardizer`](/address_standardizer), [`address_standardizer_data_us`](/address_standardizer_data_us), [`pgrouting`](/pgrouting), [`pointcloud`](/pointcloud), [`pointcloud_postgis`](/pointcloud_postgis), [`h3`](/h3), [`h3_postgis`](/h3_postgis), [`q3c`](/q3c), [`ogr_fdw`](/ogr_fdw), [`geoip`](/geoip), [`pg_polyline`](/pg_polyline), [`pg_geohash`](/pg_geohash), [`mobilitydb`](/mobilitydb), [`tzf`](/tzf), [`earthdistance`](/earthdistance)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pointcloud_postgis](https://github.com/pgpointcloud/pointcloud) | 1.2.5 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pointcloud](/pointcloud_postgis) |  |  | [`postgis`](postgis), [`pointcloud`](pointcloud) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pointcloud_postgis CASCADE;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| Distro-pointcloud | 1.2.5 | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | `pointcloud_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| Distro-pointcloud | 1.2.5 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pointcloud` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pointcloud_postgis` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pointcloud_postgis
```


Install `pointcloud` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pointcloud"]}'
```


Install `pointcloud` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pointcloud_17*;
dnf install pointcloud_16*;
dnf install pointcloud_15*;
dnf install pointcloud_14*;
dnf install pointcloud_13*;
```


Install `pointcloud` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pointcloud;
apt install postgresql-16-pointcloud;
apt install postgresql-15-pointcloud;
apt install postgresql-14-pointcloud;
apt install postgresql-13-pointcloud;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pointcloud_17*` | `pointcloud_16*` | `pointcloud_15*` | `pointcloud_14*` | `pointcloud_13*` |
| `el9` | `pointcloud_17*` | `pointcloud_16*` | `pointcloud_15*` | `pointcloud_14*` | `pointcloud_13*` |
| `d12` | `postgresql-17-pointcloud` | `postgresql-16-pointcloud` | `postgresql-15-pointcloud` | `postgresql-14-pointcloud` | `postgresql-13-pointcloud` |
| `u22` | `postgresql-17-pointcloud` | `postgresql-16-pointcloud` | `postgresql-15-pointcloud` | `postgresql-14-pointcloud` | `postgresql-13-pointcloud` |
| `u24` | `postgresql-17-pointcloud` | `postgresql-16-pointcloud` | `postgresql-15-pointcloud` | `postgresql-14-pointcloud` | `postgresql-13-pointcloud` |






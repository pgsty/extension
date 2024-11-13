# geoip


> [geoip](https://github.com/tvondra/geoip): IP-based geolocation query
>
> https://github.com/tvondra/geoip





[GIS](/gis) extensions: [`postgis`](/postgis), [`postgis_topology`](/postgis_topology), [`postgis_raster`](/postgis_raster), [`postgis_sfcgal`](/postgis_sfcgal), [`postgis_tiger_geocoder`](/postgis_tiger_geocoder), [`address_standardizer`](/address_standardizer), [`address_standardizer_data_us`](/address_standardizer_data_us), [`pgrouting`](/pgrouting), [`pointcloud`](/pointcloud), [`pointcloud_postgis`](/pointcloud_postgis), [`h3`](/h3), [`h3_postgis`](/h3_postgis), [`q3c`](/q3c), [`ogr_fdw`](/ogr_fdw), [`geoip`](/geoip), [`pg_polyline`](/pg_polyline), [`pg_geohash`](/pg_geohash), [`mobilitydb`](/mobilitydb), [`earthdistance`](/earthdistance)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [geoip](https://github.com/tvondra/geoip) | 0.3.0 | **<span class="tcblue">BSD-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [geoip](/geoip) | `pgdg-flaw` | `geoip` | [`ip4r`](ip4r) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION geoip CASCADE;
```
> **Comment**: no pg17 on el9, no pg13 on el8
-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `geoip_17*` | `geoip_16*` | `geoip_15*` | `geoip_14*` | `geoip_13*` | `geoip_12*` |
| `el9` | `geoip_17*` | `geoip_16*` | `geoip_15*` | `geoip_14*` | `geoip_13*` | `geoip_12*` |
| `d12` | `postgresql-17-geoip` | `postgresql-16-geoip` | `postgresql-15-geoip` | `postgresql-14-geoip` | `postgresql-13-geoip` | `postgresql-12-geoip` |
| `u22` | `postgresql-17-geoip` | `postgresql-16-geoip` | `postgresql-15-geoip` | `postgresql-14-geoip` | `postgresql-13-geoip` | `postgresql-12-geoip` |
| `u24` | `postgresql-17-geoip` | `postgresql-16-geoip` | `postgresql-15-geoip` | `postgresql-14-geoip` | `postgresql-13-geoip` | `postgresql-12-geoip` |



Install `geoip` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["geoip"]}'
```


Install `geoip` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install geoip_17*;
yum install geoip_16*;
yum install geoip_15*;
yum install geoip_14*;
yum install geoip_13*;
yum install geoip_12*;
```


Install `geoip` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-geoip;
apt install postgresql-16-geoip;
apt install postgresql-15-geoip;
apt install postgresql-14-geoip;
apt install postgresql-13-geoip;
apt install postgresql-12-geoip;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `geoip_17*` | `geoip_16*` | `geoip_15*` | `geoip_14*` | `geoip_13*` | `geoip_12*` |
| `el9` | `geoip_17*` | `geoip_16*` | `geoip_15*` | `geoip_14*` | `geoip_13*` | `geoip_12*` |
| `d12` | `postgresql-17-geoip` | `postgresql-16-geoip` | `postgresql-15-geoip` | `postgresql-14-geoip` | `postgresql-13-geoip` | `postgresql-12-geoip` |
| `u22` | `postgresql-17-geoip` | `postgresql-16-geoip` | `postgresql-15-geoip` | `postgresql-14-geoip` | `postgresql-13-geoip` | `postgresql-12-geoip` |
| `u24` | `postgresql-17-geoip` | `postgresql-16-geoip` | `postgresql-15-geoip` | `postgresql-14-geoip` | `postgresql-13-geoip` | `postgresql-12-geoip` |






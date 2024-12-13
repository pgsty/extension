# citus


> [citus](https://github.com/citusdata/citus): Distributed PostgreSQL as an extension
>
> https://github.com/citusdata/citus





[OLAP](/olap) extensions: [`citus`](/citus), [`citus_columnar`](/citus_columnar), [`columnar`](/columnar), [`pg_analytics`](/pg_analytics), [`pg_duckdb`](/pg_duckdb), [`duckdb_fdw`](/duckdb_fdw), [`pg_parquet`](/pg_parquet), [`pg_fkpart`](/pg_fkpart), [`pg_partman`](/pg_partman), [`plproxy`](/plproxy), [`pg_strom`](/pg_strom), [`tablefunc`](/tablefunc)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [citus](https://github.com/citusdata/citus) | 12.1-1 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcgreen">CITUS</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [citus](/citus) |  | `pg_catalog` |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> |
| `u24` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> |



```bash
shared_preload_libraries = 'citus'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION citus;
```
> **Comment**: conflict with hydra, no pg17, no noble, no arm64, pg12=10.2, pg13=11.3
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 12.1-1 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tccyan">PGDG</span>** | `citus_$v*` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 12.1-1 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcgreen">CITUS</span>** | `postgresql-$v-citus-12.1` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `citus` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["citus"]}'     # common case
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["citus11"]}'   # pg13 @ deb
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["citus10"]}'   # pg12 @ deb
```


Install `citus` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install citus_17*;
yum install citus_16*;
yum install citus_15*;
yum install citus_14*;
yum install citus_13*;
yum install citus_12*;
```


Install `citus` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-citus-12.1;
apt install postgresql-16-citus-12.1;
apt install postgresql-15-citus-12.1;
apt install postgresql-14-citus-12.1;
apt install postgresql-13-citus-11.3;
apt install postgresql-12-citus-10.2;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `citus_17*` | `citus_16*` | `citus_15*` | `citus_14*` | `citus_13*` | `citus_12*` |
| `el9` | `citus_17*` | `citus_16*` | `citus_15*` | `citus_14*` | `citus_13*` | `citus_12*` |
| `d12` | `postgresql-17-citus-12.1` | `postgresql-16-citus-12.1` | `postgresql-15-citus-12.1` | `postgresql-14-citus-12.1` | `postgresql-13-citus-11.3` | `postgresql-12-citus-10.2` |
| `u22` | `postgresql-17-citus-12.1` | `postgresql-16-citus-12.1` | `postgresql-15-citus-12.1` | `postgresql-14-citus-12.1` | `postgresql-13-citus-11.3` | `postgresql-12-citus-10.2` |
| `u24` | `postgresql-17-citus-12.1` | `postgresql-16-citus-12.1` | `postgresql-15-citus-12.1` | `postgresql-14-citus-12.1` | `postgresql-13-citus-11.3` | `postgresql-12-citus-10.2` |






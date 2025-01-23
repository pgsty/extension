# citus


> [citus](https://github.com/citusdata/citus): Distributed PostgreSQL as an extension
>
> https://github.com/citusdata/citus





[OLAP](/olap) extensions: [`citus`](/citus), [`citus_columnar`](/citus_columnar), [`columnar`](/columnar), [`pg_analytics`](/pg_analytics), [`pg_duckdb`](/pg_duckdb), [`pg_mooncake`](/pg_mooncake), [`duckdb_fdw`](/duckdb_fdw), [`pg_parquet`](/pg_parquet), [`pg_fkpart`](/pg_fkpart), [`pg_partman`](/pg_partman), [`plproxy`](/plproxy), [`pg_strom`](/pg_strom), [`tablefunc`](/tablefunc)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [citus](https://github.com/citusdata/citus) | 13.0.0 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [citus](/citus) |  | `pg_catalog` |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |



```bash
shared_preload_libraries = 'citus'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION citus;
```
> **Comment**: conflict with hydra
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 13.0.0 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `citus_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  |
| [DEB](/deb) | 13.0.0 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-citus` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  |



Install `citus` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add citus
```


Install `citus` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["citus"]}'
```


Install `citus` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install citus_17*;
dnf install citus_16*;
dnf install citus_15*;
dnf install citus_14*;
```


Install `citus` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-citus;
apt install postgresql-16-citus;
apt install postgresql-15-citus;
apt install postgresql-14-citus;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `citus_17*` | `citus_16*` | `citus_15*` | `citus_14*` | <span class="tcred">✘</span> |
| `el9` | `citus_17*` | `citus_16*` | `citus_15*` | `citus_14*` | <span class="tcred">✘</span> |
| `d12` | `postgresql-17-citus` | `postgresql-16-citus` | `postgresql-15-citus` | `postgresql-14-citus` | <span class="tcred">✘</span> |
| `u22` | `postgresql-17-citus` | `postgresql-16-citus` | `postgresql-15-citus` | `postgresql-14-citus` | <span class="tcred">✘</span> |
| `u24` | `postgresql-17-citus` | `postgresql-16-citus` | `postgresql-15-citus` | `postgresql-14-citus` | <span class="tcred">✘</span> |






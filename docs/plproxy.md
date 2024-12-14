# plproxy


> [plproxy](https://github.com/plproxy/plproxy): Database partitioning implemented as procedural language
>
> https://github.com/plproxy/plproxy





[OLAP](/olap) extensions: [`citus`](/citus), [`citus_columnar`](/citus_columnar), [`columnar`](/columnar), [`pg_analytics`](/pg_analytics), [`pg_duckdb`](/pg_duckdb), [`duckdb_fdw`](/duckdb_fdw), [`pg_parquet`](/pg_parquet), [`pg_fkpart`](/pg_fkpart), [`pg_partman`](/pg_partman), [`plproxy`](/plproxy), [`pg_strom`](/pg_strom), [`tablefunc`](/tablefunc)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [plproxy](https://github.com/plproxy/plproxy) | 2.11.0 | **<span class="tcblue">BSD-0</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [plproxy](/plproxy) | `pgdg-flaw` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION plproxy;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 2.11.0 | **<span class="tcblue">BSD-0</span>** | **<span class="tcwarn">PIGSTY</span>** | `plproxy_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 2.11.0 | **<span class="tcblue">BSD-0</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-plproxy` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `plproxy` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["plproxy"]}'
```


Install `plproxy` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install plproxy_17*;
dnf install plproxy_16*;
dnf install plproxy_15*;
dnf install plproxy_14*;
dnf install plproxy_13*;
dnf install plproxy_12*;
```


Install `plproxy` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-plproxy;
apt install postgresql-16-plproxy;
apt install postgresql-15-plproxy;
apt install postgresql-14-plproxy;
apt install postgresql-13-plproxy;
apt install postgresql-12-plproxy;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `plproxy_17*` | `plproxy_16*` | `plproxy_15*` | `plproxy_14*` | `plproxy_13*` | `plproxy_12*` |
| `el9` | `plproxy_17*` | `plproxy_16*` | `plproxy_15*` | `plproxy_14*` | `plproxy_13*` | `plproxy_12*` |
| `d12` | `postgresql-17-plproxy` | `postgresql-16-plproxy` | `postgresql-15-plproxy` | `postgresql-14-plproxy` | `postgresql-13-plproxy` | `postgresql-12-plproxy` |
| `u22` | `postgresql-17-plproxy` | `postgresql-16-plproxy` | `postgresql-15-plproxy` | `postgresql-14-plproxy` | `postgresql-13-plproxy` | `postgresql-12-plproxy` |
| `u24` | `postgresql-17-plproxy` | `postgresql-16-plproxy` | `postgresql-15-plproxy` | `postgresql-14-plproxy` | `postgresql-13-plproxy` | `postgresql-12-plproxy` |






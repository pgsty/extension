# pg_fkpart


> [pg_fkpart](https://github.com/lemoineat/pg_fkpart): Table partitioning by foreign key utility
>
> https://github.com/lemoineat/pg_fkpart





[OLAP](/olap) extensions: [`citus`](/citus), [`citus_columnar`](/citus_columnar), [`columnar`](/columnar), [`pg_analytics`](/pg_analytics), [`pg_duckdb`](/pg_duckdb), [`pg_mooncake`](/pg_mooncake), [`duckdb_fdw`](/duckdb_fdw), [`pg_parquet`](/pg_parquet), [`pg_fkpart`](/pg_fkpart), [`pg_partman`](/pg_partman), [`plproxy`](/plproxy), [`pg_strom`](/pg_strom), [`tablefunc`](/tablefunc)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_fkpart](https://github.com/lemoineat/pg_fkpart) | 1.7 | **<span class="tcwarn">GPLv2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_fkpart](/pg_fkpart) | `pgdg-flaw` | `pgfkpart` |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_fkpart;
```
> **Comment**: no pg13,12 on el8 pgdg repo
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.7 | **<span class="tcwarn">GPLv2</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_fkpart_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.7 | **<span class="tcwarn">GPLv2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-fkpart` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pg_fkpart` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_fkpart
```


Install `pg_fkpart` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_fkpart"]}'
```


Install `pg_fkpart` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_fkpart_17;
dnf install pg_fkpart_16;
dnf install pg_fkpart_15;
dnf install pg_fkpart_14;
dnf install pg_fkpart_13;
```


Install `pg_fkpart` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-fkpart;
apt install postgresql-16-pg-fkpart;
apt install postgresql-15-pg-fkpart;
apt install postgresql-14-pg-fkpart;
apt install postgresql-13-pg-fkpart;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_fkpart_17` | `pg_fkpart_16` | `pg_fkpart_15` | `pg_fkpart_14` | `pg_fkpart_13` |
| `el9` | `pg_fkpart_17` | `pg_fkpart_16` | `pg_fkpart_15` | `pg_fkpart_14` | `pg_fkpart_13` |
| `d12` | `postgresql-17-pg-fkpart` | `postgresql-16-pg-fkpart` | `postgresql-15-pg-fkpart` | `postgresql-14-pg-fkpart` | `postgresql-13-pg-fkpart` |
| `u22` | `postgresql-17-pg-fkpart` | `postgresql-16-pg-fkpart` | `postgresql-15-pg-fkpart` | `postgresql-14-pg-fkpart` | `postgresql-13-pg-fkpart` |
| `u24` | `postgresql-17-pg-fkpart` | `postgresql-16-pg-fkpart` | `postgresql-15-pg-fkpart` | `postgresql-14-pg-fkpart` | `postgresql-13-pg-fkpart` |






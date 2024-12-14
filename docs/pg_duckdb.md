# pg_duckdb


> [pg_duckdb](https://github.com/duckdb/pg_duckdb): DuckDB Embedded in Postgres
>
> https://github.com/duckdb/pg_duckdb





[OLAP](/olap) extensions: [`citus`](/citus), [`citus_columnar`](/citus_columnar), [`columnar`](/columnar), [`pg_analytics`](/pg_analytics), [`pg_duckdb`](/pg_duckdb), [`duckdb_fdw`](/duckdb_fdw), [`pg_parquet`](/pg_parquet), [`pg_fkpart`](/pg_fkpart), [`pg_partman`](/pg_partman), [`plproxy`](/plproxy), [`pg_strom`](/pg_strom), [`tablefunc`](/tablefunc)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_duckdb](https://github.com/duckdb/pg_duckdb) | 0.2.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C++` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_duckdb](/pg_duckdb) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |



```bash
shared_preload_libraries = 'pg_duckdb'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION pg_duckdb;
```
> **Comment**: conflict on libduckdb with duckdb_fdw
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.2.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_duckdb_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  |  |
| [DEB](/deb) | 0.2.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-duckdb` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  |  |



Install `pg_duckdb` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_duckdb"]}'
```


Install `pg_duckdb` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_duckdb_17*;
dnf install pg_duckdb_16*;
dnf install pg_duckdb_15*;
dnf install pg_duckdb_14*;
```


Install `pg_duckdb` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-duckdb;
apt install postgresql-16-pg-duckdb;
apt install postgresql-15-pg-duckdb;
apt install postgresql-14-pg-duckdb;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_duckdb_17*` | `pg_duckdb_16*` | `pg_duckdb_15*` | `pg_duckdb_14*` | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `el9` | `pg_duckdb_17*` | `pg_duckdb_16*` | `pg_duckdb_15*` | `pg_duckdb_14*` | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `d12` | `postgresql-17-pg-duckdb` | `postgresql-16-pg-duckdb` | `postgresql-15-pg-duckdb` | `postgresql-14-pg-duckdb` | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `u22` | `postgresql-17-pg-duckdb` | `postgresql-16-pg-duckdb` | `postgresql-15-pg-duckdb` | `postgresql-14-pg-duckdb` | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `u24` | `postgresql-17-pg-duckdb` | `postgresql-16-pg-duckdb` | `postgresql-15-pg-duckdb` | `postgresql-14-pg-duckdb` | <span class="tcred">✘</span> | <span class="tcred">✘</span> |





--------

## Usage

Add `pg_duckdb` to `shared_preload_libraries` via `patronictl`

```bash
pg edit-config --force -p shared_preload_libraries='pg_duckdb, pg_stat_statements, auto_explain'
pg restart --force pg-meta
```

### Create Extension

```sql
CREATE EXTENSION pg_duckdb;
```

Generate some data

```bash
pgbench -is100
```


```bash
\timing on

SELECT count(*) FROM pgbench_accounts;
-- 3268.023ms

# use the duckdb execution engine
SET duckdb.force_execution = true;


postgres@el8:5432/postgres=# explain SELECT count(*) FROM pgbench_accounts;
                                   QUERY PLAN
---------------------------------------------------------------------------------
Custom Scan (DuckDBScan)  (cost=0.00..0.00 rows=0 width=0)
DuckDB Execution Plan:

┌───────────────────────────┐
│    UNGROUPED_AGGREGATE    │
│    ────────────────────   │
│        Aggregates:        │
│        count_star()       │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│     POSTGRES_SEQ_SCAN     │
│    ────────────────────   │
│         Function:         │
│     POSTGRES_SEQ_SCAN     │
│                           │
│       ~10000000 Rows      │
└───────────────────────────┘


JIT:
Functions: 1
Options: Inlining false, Optimization false, Expressions true, Deforming true
(22 rows)


postgres@el8:5432/postgres=# SELECT count(*) FROM pgbench_accounts;
count
----------
10000000
(1 row)

Time: 696.801 ms
```

According some user feedbacks, the duckdb engine can achieve 100x - 1000x speed up on certain queries.


Check more details @ https://github.com/duckdb/pg_duckdb

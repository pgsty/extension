# pg_analytics


> [pg_analytics](https://github.com/paradedb/pg_analytics): Postgres for analytics, powered by DuckDB
>
> https://github.com/paradedb/pg_analytics





[OLAP](/olap) extensions: [`citus`](/citus), [`citus_columnar`](/citus_columnar), [`columnar`](/columnar), [`pg_analytics`](/pg_analytics), [`pg_duckdb`](/pg_duckdb), [`duckdb_fdw`](/duckdb_fdw), [`pg_parquet`](/pg_parquet), [`pg_fkpart`](/pg_fkpart), [`pg_partman`](/pg_partman), [`plproxy`](/plproxy), [`pg_strom`](/pg_strom), [`tablefunc`](/tablefunc)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_analytics](https://github.com/paradedb/pg_analytics) | 0.2.3 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_analytics](/pg_analytics) | `pgrx` | `paradedb` |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_analytics;
```
> **Comment**: pg13=0.2.1, pgrx 0.12.7
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.2.3 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_analytics_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  |
| [DEB](/deb) | 0.2.3 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-analytics` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  |



Install `pg_analytics` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_analytics"]}'
```


Install `pg_analytics` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install pg_analytics_17;
yum install pg_analytics_16;
yum install pg_analytics_15;
yum install pg_analytics_14;
yum install pg_analytics_13;
yum install pg_analytics_12;
```


Install `pg_analytics` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-analytics;
apt install postgresql-16-pg-analytics;
apt install postgresql-15-pg-analytics;
apt install postgresql-14-pg-analytics;
apt install postgresql-13-pg-analytics;
apt install postgresql-12-pg-analytics;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_analytics_17` | `pg_analytics_16` | `pg_analytics_15` | `pg_analytics_14` | `pg_analytics_13` | `pg_analytics_12` |
| `el9` | `pg_analytics_17` | `pg_analytics_16` | `pg_analytics_15` | `pg_analytics_14` | `pg_analytics_13` | `pg_analytics_12` |
| `d12` | `postgresql-17-pg-analytics` | `postgresql-16-pg-analytics` | `postgresql-15-pg-analytics` | `postgresql-14-pg-analytics` | `postgresql-13-pg-analytics` | `postgresql-12-pg-analytics` |
| `u22` | `postgresql-17-pg-analytics` | `postgresql-16-pg-analytics` | `postgresql-15-pg-analytics` | `postgresql-14-pg-analytics` | `postgresql-13-pg-analytics` | `postgresql-12-pg-analytics` |
| `u24` | `postgresql-17-pg-analytics` | `postgresql-16-pg-analytics` | `postgresql-15-pg-analytics` | `postgresql-14-pg-analytics` | `postgresql-13-pg-analytics` | `postgresql-12-pg-analytics` |






--------

## Usage

https://github.com/paradedb/pg_analytics

Example, read parquet file from S3:

```bash
CREATE EXTENSION pg_lakehouse;
CREATE FOREIGN DATA WRAPPER parquet_wrapper HANDLER parquet_fdw_handler VALIDATOR parquet_fdw_validator;

-- Provide S3 credentials
CREATE SERVER parquet_server FOREIGN DATA WRAPPER parquet_wrapper;

-- Create foreign table with auto schema creation
CREATE FOREIGN TABLE trips ()
SERVER parquet_server
OPTIONS (files 's3://paradedb-benchmarks/yellow_tripdata_2024-01.parquet');

-- Success! Now you can query the remote Parquet file like a regular Postgres table
SELECT COUNT(*) FROM trips;
  count
---------
 2964624
(1 row)
```

This fdw is read-only for now.



----

## Iceberg Support

```sql
CREATE EXTENSION pg_lakehouse;

CREATE FOREIGN DATA WRAPPER iceberg_wrapper
    HANDLER iceberg_fdw_handler
    VALIDATOR iceberg_fdw_validator;

CREATE SERVER iceberg_server
    FOREIGN DATA WRAPPER iceberg_wrapper;

-- Replace the dummy schema with the actual schema
CREATE FOREIGN TABLE iceberg_table (x INT)
    SERVER iceberg_server
    OPTIONS (files 's3://bucket/iceberg_folder');

-- Success! You can now query the Iceberg table
SELECT COUNT(*) FROM iceberg_table;
```



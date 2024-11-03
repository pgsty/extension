---
title: pg_lakehouse
weight: 180
description: PG Lakehouse 允许用户通过 FDW 读写本地与S3上的 Parquet、Iceberg 数据文件
icon: fas fa-boxes-stacked
module: [PGSQL]
tags: [Extension]
---


--------

## Metadata

- **Available PG & OS**: EL 8/9: PG15, PG16
- **Extension Package Name**: `pg_lakehouse_$v`
- **In `shared_preload_libraries`**: **yes**
- **Need `CREATE EXTENSION`**: **yes*

- [pg_lakehouse: A DuckDB Alternative in Postgres](https://blog.paradedb.com/pages/introducing_lakehouse)
- [Putting DuckDB in Postgres to Query Iceberg](https://blog.paradedb.com/pages/iceberg_lakehouse)


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


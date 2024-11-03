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
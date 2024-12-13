

--------

## Usage

> THIS EXTENSION IS CONFLICT WITH pg_duckdb & duckdb_fdw, if it is under maintained, we may remove this extension in the future


Beware that this package is conflict with the official `pg_duckdb` extension due to use the same `libduckdb.so` under same path.

And this function will block the `duckdb_fdw` functioning.


```bash
-- Create a columnstore table in PostgreSQL
CREATE TABLE user_activity (....) USING columnstore;

-- Insert data into a columnstore table
INSERT INTO user_activity VALUES ....;

-- Query a columnstore table in PostgreSQL
SELECT * FROM user_activity LIMIT 5;
```


--------

## Example

**Use mooncake with S3**:

```sql
SELECT mooncake.create_secret('<name>', 'S3', '<key_id>', '<secret>', '{"REGION": "<s3-region>"}');

SET mooncake.default_bucket = 's3://<bucket>';

SET mooncake.enable_local_cache = false; -- (if you are using Neon)
```

**Use mooncake with local columnstore**:

```sql
CREATE TABLE user_activity(
  user_id BIGINT,
  activity_type TEXT,
  activity_timestamp TIMESTAMP,
  duration INT
) USING columnstore;

INSERT INTO user_activity VALUES
  (1, 'login', '2024-01-01 08:00:00', 120),
  (2, 'page_view', '2024-01-01 08:05:00', 30),
  (3, 'logout', '2024-01-01 08:30:00', 60),
  (4, 'error', '2024-01-01 08:13:00', 60);

SELECT * FROM user_activity;
```

**Run analytic queries**

```sql
SELECT
    user_id,
    activity_type,
    SUM(duration) AS total_duration,
    COUNT(*) AS activity_count
FROM
    user_activity
GROUP BY
    user_id, activity_type
ORDER BY
    user_id, activity_type;
```

The explain result could be:

```
postgres@u22:5432/postgres=# explain SELECT
    user_id,
    activity_type,
    SUM(duration) AS total_duration,
    COUNT(*) AS activity_count
FROM
    user_activity
GROUP BY
    user_id, activity_type
ORDER BY
    user_id, activity_type;
                         QUERY PLAN
------------------------------------------------------------
 Custom Scan (DuckDBScan)  (cost=0.00..0.00 rows=0 width=0)
   DuckDB Execution Plan:

 ┌───────────────────────────┐
 │         PROJECTION        │
 │    ────────────────────   │
 │__internal_decompress_integ│
 │     ral_bigint(#0, 1)     │
 │             #1            │
 │             #2            │
 │             #3            │
 │                           │
 │          ~2 Rows          │
 └─────────────┬─────────────┘
 ┌─────────────┴─────────────┐
 │          ORDER_BY         │
 │    ────────────────────   │
 │ user_activity.user_id ASC │
 │       user_activity       │
 │     .activity_type ASC    │
 └─────────────┬─────────────┘
 ┌─────────────┴─────────────┐
 │         PROJECTION        │
 │    ────────────────────   │
 │__internal_compress_integra│
 │     l_utinyint(#0, 1)     │
 │             #1            │
 │             #2            │
 │             #3            │
 │                           │
 │          ~2 Rows          │
 └─────────────┬─────────────┘
 ┌─────────────┴─────────────┐
 │         PROJECTION        │
 │    ────────────────────   │
 │__internal_decompress_integ│
 │     ral_bigint(#0, 1)     │
 │             #1            │
 │             #2            │
 │             #3            │
 │                           │
 │          ~2 Rows          │
 └─────────────┬─────────────┘
 ┌─────────────┴─────────────┐
 │       HASH_GROUP_BY       │
 │    ────────────────────   │
 │          Groups:          │
 │             #0            │
 │             #1            │
 │                           │
 │        Aggregates:        │
 │          sum(#2)          │
 │        count_star()       │
 │                           │
 │          ~2 Rows          │
 └─────────────┬─────────────┘
 ┌─────────────┴─────────────┐
 │         PROJECTION        │
 │    ────────────────────   │
 │          user_id          │
 │       activity_type       │
 │          duration         │
 │                           │
 │          ~4 Rows          │
 └─────────────┬─────────────┘
 ┌─────────────┴─────────────┐
 │         PROJECTION        │
 │    ────────────────────   │
 │__internal_compress_integra│
 │     l_utinyint(#0, 1)     │
 │             #1            │
 │             #2            │
 │                           │
 │          ~4 Rows          │
 └─────────────┬─────────────┘
 ┌─────────────┴─────────────┐
 │     COLUMNSTORE_SCAN      │
 │    ────────────────────   │
 │         Function:         │
 │      COLUMNSTORE_SCAN     │
 │                           │
 │        Projections:       │
 │          user_id          │
 │       activity_type       │
 │          duration         │
 │                           │
 │          ~4 Rows          │
 └───────────────────────────┘


(90 rows)

```
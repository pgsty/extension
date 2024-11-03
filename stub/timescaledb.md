
--------

## Usage

Create a table and turn it into hypertable

```sql
DROP TABLE IF EXISTS ts_test;
CREATE TABLE ts_test
(
    id BIGINT PRIMARY KEY,
    ts TIMESTAMPTZ NOT NULL,
    v  INTEGER -- payload
);
SELECT create_hypertable('ts_test', by_range('id'));

INSERT INTO ts_test 
    SELECT i, now() + (i || ' seconds')::INTERVAL, i % 100 
    FROM generate_series(1, 1000000) i;


ALTER TABLE ts_test SET (timescaledb.compress_chunk_time_interval = '24 hours');
```

Continuous Agg Example:

```sql

CREATE MATERIALIZED VIEW continuous_aggregate_daily( timec, minl, sumt, sumh )
WITH (timescaledb.continuous) AS
  SELECT count(*) FROM ts_test;


SELECT add_job('SELECT 1','1h', initial_start => '2024-07-09 18:52:00+00'::timestamptz);
```
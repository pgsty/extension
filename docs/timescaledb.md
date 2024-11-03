# timescaledb


> [timescaledb](https://github.com/timescale/timescaledb): Enables scalable inserts and complex queries for time-series data
>
> https://github.com/timescale/timescaledb





[TIME](/time) extensions: [`timescaledb`](/timescaledb), [`timescaledb_toolkit`](/timescaledb_toolkit), [`timeseries`](/timeseries), [`periods`](/periods), [`temporal_tables`](/temporal_tables), [`emaj`](/emaj), [`table_version`](/table_version), [`pg_cron`](/pg_cron), [`pg_later`](/pg_later), [`pg_background`](/pg_background)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [timescaledb](https://github.com/timescale/timescaledb) | 2.17.0 | **<span class="tcwarn">Timescale</span>** | **<span class="tcwarn">TIMESCALE</span>** | **<span class="tcwarn">TIMESCALE</span>** | `C` |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Package | Tags | Schemas | Requires | Required by |
|---------|------|---------|----------|-------------|
| [timescaledb](/timescaledb) |  |  |  |  |



```bash
shared_preload_libraries = 'timescaledb'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION timescaledb;
```
> **Comment**: pg12=2.11.2, pg13=2.15.3
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 2.17.1 | **<span class="tcwarn">Timescale</span>** | **<span class="tcwarn">TIMESCALE</span>** | `timescaledb-2-postgresql-$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 2.17.1 | **<span class="tcwarn">Timescale</span>** | **<span class="tcwarn">TIMESCALE</span>** | `timescaledb-2-postgresql-$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `timescaledb` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["timescaledb"]}'
```


Install `timescaledb` [RPM](/rpm) from the **<span class="tcwarn">TIMESCALE</span>** **YUM** repo:

```bash
dnf install timescaledb-2-postgresql-17*;
dnf install timescaledb-2-postgresql-16*;
dnf install timescaledb-2-postgresql-15*;
dnf install timescaledb-2-postgresql-14*;
dnf install timescaledb-2-postgresql-13*;
dnf install timescaledb-2-postgresql-12*;
```


Install `timescaledb` [DEB](/deb) from the **<span class="tcwarn">TIMESCALE</span>** **APT** repo:

```bash
apt install timescaledb-2-postgresql-17;
apt install timescaledb-2-postgresql-16;
apt install timescaledb-2-postgresql-15;
apt install timescaledb-2-postgresql-14;
apt install timescaledb-2-postgresql-13;
apt install timescaledb-2-postgresql-12;
```






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


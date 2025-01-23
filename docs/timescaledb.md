# timescaledb


> [timescaledb](https://github.com/timescale/timescaledb): Enables scalable inserts and complex queries for time-series data
>
> https://github.com/timescale/timescaledb





[TIME](/time) extensions: [`timescaledb`](/timescaledb), [`timescaledb_toolkit`](/timescaledb_toolkit), [`timeseries`](/timeseries), [`periods`](/periods), [`temporal_tables`](/temporal_tables), [`emaj`](/emaj), [`table_version`](/table_version), [`pg_cron`](/pg_cron), [`pg_task`](/pg_task), [`pg_later`](/pg_later), [`pg_background`](/pg_background)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [timescaledb](https://github.com/timescale/timescaledb) | 2.17.2 | PIGSTY | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [timescaledb](/timescaledb) |  | `timescaledb_information`, `timescaledb_experimental` |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |



```bash
shared_preload_libraries = 'timescaledb'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION timescaledb;
```
> **Comment**: degrade to oss ver on el.aarch64
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 2.17.2 | PIGSTY | **<span class="tcwarn">PIGSTY</span>** | `timescaledb-tsl_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  |
| [DEB](/deb) | 2.17.2 | PIGSTY | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-timescaledb-tsl` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  |



Install `timescaledb` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add timescaledb
```


Install `timescaledb` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["timescaledb"]}'
```


Install `timescaledb` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install timescaledb-tsl_17*;
dnf install timescaledb-tsl_16*;
dnf install timescaledb-tsl_15*;
dnf install timescaledb-tsl_14*;
```


Install `timescaledb` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-timescaledb-tsl;
apt install postgresql-16-timescaledb-tsl;
apt install postgresql-15-timescaledb-tsl;
apt install postgresql-14-timescaledb-tsl;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `timescaledb-tsl_17*` | `timescaledb-tsl_16*` | `timescaledb-tsl_15*` | `timescaledb-tsl_14*` | <span class="tcred">✘</span> |
| `el9` | `timescaledb-tsl_17*` | `timescaledb-tsl_16*` | `timescaledb-tsl_15*` | `timescaledb-tsl_14*` | <span class="tcred">✘</span> |
| `d12` | `postgresql-17-timescaledb-tsl` | `postgresql-16-timescaledb-tsl` | `postgresql-15-timescaledb-tsl` | `postgresql-14-timescaledb-tsl` | <span class="tcred">✘</span> |
| `u22` | `postgresql-17-timescaledb-tsl` | `postgresql-16-timescaledb-tsl` | `postgresql-15-timescaledb-tsl` | `postgresql-14-timescaledb-tsl` | <span class="tcred">✘</span> |
| `u24` | `postgresql-17-timescaledb-tsl` | `postgresql-16-timescaledb-tsl` | `postgresql-15-timescaledb-tsl` | `postgresql-14-timescaledb-tsl` | <span class="tcred">✘</span> |





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

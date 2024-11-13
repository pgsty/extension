# timescaledb_toolkit


> [timescaledb_toolkit](https://github.com/timescale/timescaledb-toolkit): Library of analytical hyperfunctions, time-series pipelining, and other SQL utilities
>
> https://github.com/timescale/timescaledb-toolkit





[TIME](/time) extensions: [`timescaledb`](/timescaledb), [`timescaledb_toolkit`](/timescaledb_toolkit), [`timeseries`](/timeseries), [`periods`](/periods), [`temporal_tables`](/temporal_tables), [`emaj`](/emaj), [`table_version`](/table_version), [`pg_cron`](/pg_cron), [`pg_later`](/pg_later), [`pg_background`](/pg_background)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [timescaledb_toolkit](https://github.com/timescale/timescaledb-toolkit) | 1.18.0 | **<span class="tcwarn">Timescale</span>** | **<span class="tcwarn">TIMESCALE</span>** | **<span class="tcwarn">TIMESCALE</span>** | `Rust` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [timescaledb_toolkit](/timescaledb_toolkit) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |





```sql
CREATE EXTENSION timescaledb_toolkit;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `timescaledb-toolkit-postgresql-17` | `timescaledb-toolkit-postgresql-16` | `timescaledb-toolkit-postgresql-15` | `timescaledb-toolkit-postgresql-14` | `timescaledb-toolkit-postgresql-13` | `timescaledb-toolkit-postgresql-12` |
| `el9` | `timescaledb-toolkit-postgresql-17` | `timescaledb-toolkit-postgresql-16` | `timescaledb-toolkit-postgresql-15` | `timescaledb-toolkit-postgresql-14` | `timescaledb-toolkit-postgresql-13` | `timescaledb-toolkit-postgresql-12` |
| `d12` | `timescaledb-toolkit-postgresql-17` | `timescaledb-toolkit-postgresql-16` | `timescaledb-toolkit-postgresql-15` | `timescaledb-toolkit-postgresql-14` | `timescaledb-toolkit-postgresql-13` | `timescaledb-toolkit-postgresql-12` |
| `u22` | `timescaledb-toolkit-postgresql-17` | `timescaledb-toolkit-postgresql-16` | `timescaledb-toolkit-postgresql-15` | `timescaledb-toolkit-postgresql-14` | `timescaledb-toolkit-postgresql-13` | `timescaledb-toolkit-postgresql-12` |
| `u24` | `timescaledb-toolkit-postgresql-17` | `timescaledb-toolkit-postgresql-16` | `timescaledb-toolkit-postgresql-15` | `timescaledb-toolkit-postgresql-14` | `timescaledb-toolkit-postgresql-13` | `timescaledb-toolkit-postgresql-12` |



Install `timescaledb_toolkit` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["timescaledb_toolkit"]}'
```


Install `timescaledb_toolkit` [RPM](/rpm) from the **<span class="tcwarn">TIMESCALE</span>** **YUM** repo:

```bash
yum install timescaledb-toolkit-postgresql-17;
yum install timescaledb-toolkit-postgresql-16;
yum install timescaledb-toolkit-postgresql-15;
yum install timescaledb-toolkit-postgresql-14;
yum install timescaledb-toolkit-postgresql-13;
yum install timescaledb-toolkit-postgresql-12;
```


Install `timescaledb_toolkit` [DEB](/deb) from the **<span class="tcwarn">TIMESCALE</span>** **APT** repo:

```bash
apt install timescaledb-toolkit-postgresql-17;
apt install timescaledb-toolkit-postgresql-16;
apt install timescaledb-toolkit-postgresql-15;
apt install timescaledb-toolkit-postgresql-14;
apt install timescaledb-toolkit-postgresql-13;
apt install timescaledb-toolkit-postgresql-12;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `timescaledb-toolkit-postgresql-17` | `timescaledb-toolkit-postgresql-16` | `timescaledb-toolkit-postgresql-15` | `timescaledb-toolkit-postgresql-14` | `timescaledb-toolkit-postgresql-13` | `timescaledb-toolkit-postgresql-12` |
| `el9` | `timescaledb-toolkit-postgresql-17` | `timescaledb-toolkit-postgresql-16` | `timescaledb-toolkit-postgresql-15` | `timescaledb-toolkit-postgresql-14` | `timescaledb-toolkit-postgresql-13` | `timescaledb-toolkit-postgresql-12` |
| `d12` | `timescaledb-toolkit-postgresql-17` | `timescaledb-toolkit-postgresql-16` | `timescaledb-toolkit-postgresql-15` | `timescaledb-toolkit-postgresql-14` | `timescaledb-toolkit-postgresql-13` | `timescaledb-toolkit-postgresql-12` |
| `u22` | `timescaledb-toolkit-postgresql-17` | `timescaledb-toolkit-postgresql-16` | `timescaledb-toolkit-postgresql-15` | `timescaledb-toolkit-postgresql-14` | `timescaledb-toolkit-postgresql-13` | `timescaledb-toolkit-postgresql-12` |
| `u24` | `timescaledb-toolkit-postgresql-17` | `timescaledb-toolkit-postgresql-16` | `timescaledb-toolkit-postgresql-15` | `timescaledb-toolkit-postgresql-14` | `timescaledb-toolkit-postgresql-13` | `timescaledb-toolkit-postgresql-12` |





--------

## Usage

This extension provide experimental features for timescaledb, check the [docs](https://github.com/timescale/timescaledb-toolkit/tree/main/docs) for details.

## Features

The following links lead to pages for the different features in the TimescaleDB Toolkit repository.

- [ASAP Smoothing](asap.md) [<sup><mark>experimental</mark></sup>](/docs/README.md#tag-notes) - A data smoothing algorithm designed to generate human readable graphs which maintain any erratic data behavior while smoothing away the cyclic noise.
- [Hyperloglog](hyperloglog.md) [<sup><mark>experimental</mark></sup>](/docs/README.md#tag-notes) – An approximate `COUNT DISTINCT` based on hashing that provides reasonable accuracy in constant space. ([Methods](hyperloglog.md#hyperloglog_api))
- [LTTB](lttb.md) [<sup><mark>experimental</mark></sup>](/docs/README.md#tag-notes) – A downsample method that preserves visual similarity. ([Methods](lttb.md#api))

- [Percentile Approximation](percentile_approximation.md) - A simple percentile approximation interface [([Methods](percentile_approximation.md#api))], wraps and simplifies the lower level algorithms:
    - [T-Digest](tdigest.md) – A quantile estimate sketch optimized to provide more accurate estimates near the tails (i.e. 0.001 or 0.995) than conventional approaches. ([Methods](tdigest#tdigest_api))
    - [UddSketch](uddsketch.md) – A quantile estimate sketch which provides a guaranteed maximum relative error. ([Methods](uddsketch.md#uddsketch_api))

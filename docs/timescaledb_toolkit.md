# timescaledb_toolkit


> [timescaledb_toolkit](https://github.com/timescale/timescaledb-toolkit): Library of analytical hyperfunctions, time-series pipelining, and other SQL utilities
>
> https://github.com/timescale/timescaledb-toolkit





[TIME](/time) extensions: [`timescaledb`](/timescaledb), [`timescaledb_toolkit`](/timescaledb_toolkit), [`timeseries`](/timeseries), [`periods`](/periods), [`temporal_tables`](/temporal_tables), [`emaj`](/emaj), [`table_version`](/table_version), [`pg_cron`](/pg_cron), [`pg_task`](/pg_task), [`pg_later`](/pg_later), [`pg_background`](/pg_background)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [timescaledb_toolkit](https://github.com/timescale/timescaledb-toolkit) | 1.19.0 | **<span class="tcwarn">Timescale</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [timescaledb_toolkit](/timescaledb_toolkit) | `pgrx` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |





```sql
CREATE EXTENSION timescaledb_toolkit;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.19.0 | **<span class="tcwarn">Timescale</span>** | **<span class="tcwarn">PIGSTY</span>** | `timescaledb-toolkit_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  |
| [DEB](/deb) | 1.19.0 | **<span class="tcwarn">Timescale</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-timescaledb-toolkit` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  |



Install `timescaledb_toolkit` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add timescaledb_toolkit
```


Install `timescaledb_toolkit` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["timescaledb_toolkit"]}'
```


Install `timescaledb_toolkit` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install timescaledb-toolkit_17;
dnf install timescaledb-toolkit_16;
dnf install timescaledb-toolkit_15;
dnf install timescaledb-toolkit_14;
```


Install `timescaledb_toolkit` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-timescaledb-toolkit;
apt install postgresql-16-timescaledb-toolkit;
apt install postgresql-15-timescaledb-toolkit;
apt install postgresql-14-timescaledb-toolkit;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `timescaledb-toolkit_17` | `timescaledb-toolkit_16` | `timescaledb-toolkit_15` | `timescaledb-toolkit_14` | <span class="tcred">✘</span> |
| `el9` | `timescaledb-toolkit_17` | `timescaledb-toolkit_16` | `timescaledb-toolkit_15` | `timescaledb-toolkit_14` | <span class="tcred">✘</span> |
| `d12` | `postgresql-17-timescaledb-toolkit` | `postgresql-16-timescaledb-toolkit` | `postgresql-15-timescaledb-toolkit` | `postgresql-14-timescaledb-toolkit` | <span class="tcred">✘</span> |
| `u22` | `postgresql-17-timescaledb-toolkit` | `postgresql-16-timescaledb-toolkit` | `postgresql-15-timescaledb-toolkit` | `postgresql-14-timescaledb-toolkit` | <span class="tcred">✘</span> |
| `u24` | `postgresql-17-timescaledb-toolkit` | `postgresql-16-timescaledb-toolkit` | `postgresql-15-timescaledb-toolkit` | `postgresql-14-timescaledb-toolkit` | <span class="tcred">✘</span> |





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

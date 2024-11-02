# timescaledb


> [timescaledb](https://github.com/timescale/timescaledb): Enables scalable inserts and complex queries for time-series data
>
> https://github.com/timescale/timescaledb


-------


## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [timescaledb](https://github.com/timescale/timescaledb) | 2.17.0 | **<span class="tcwarn">Timescale</span>** | **<span class="tcwarn">TIMESCALE</span>** | **<span class="tcwarn">TIMESCALE</span>** | `C` |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Package | Tags | Schemas | Requires | Required by | Comment | Description |
|---------|------|---------|----------|-------------|:-------:|-------------|
| [timescaledb](/timescaledb) |  |  |  |  | pg12=2.11.2, pg13=2.15.3 | Enables scalable inserts and complex queries for time-series data |



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


-----------


## Category: TIME


| ID | Extension | Version | Package | License | RPM | DEB | PL | Tags | Schemas | Requires | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:--:|------|---------|----------|:------:|:-------:|:-----:|:-------:|:-------:|
| 1000 | [timescaledb](/timescaledb) | 2.17.0 | [timescaledb](/timescaledb) | **<span class="tcwarn">Timescale</span>** | **<span class="tcwarn">TIMESCALE</span>** | **<span class="tcwarn">TIMESCALE</span>** | `C` |  |  |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1010 | [timescaledb_toolkit](/timescaledb_toolkit) | 1.18.0 | [timescaledb_toolkit](/timescaledb_toolkit) | **<span class="tcwarn">Timescale</span>** | **<span class="tcwarn">TIMESCALE</span>** | **<span class="tcwarn">TIMESCALE</span>** | `Rust` |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |
| 1020 | [timeseries](/timeseries) | 0.1.6 | [pg_timeseries](/timeseries) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` |  |  | [`columnar`](columnar), [`pg_cron`](pg_cron), [`pg_ivm`](pg_ivm), [`pg_partman`](pg_partman) |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1030 | [periods](/periods) | 1.2 | [periods](/periods) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |  |  | [`btree_gist`](btree_gist) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1040 | [temporal_tables](/temporal_tables) | 1.2.2 | [temporal_tables](/temporal_tables) | **<span class="tcblue">BSD-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1050 | [emaj](/emaj) | 4.5.0 | [emaj](/emaj) | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** |  |  | `emaj` | [`dblink`](dblink), [`btree_gist`](btree_gist) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1060 | [table_version](/table_version) | 1.10.3 | [table_version](/table_version) | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** |  |  | `table_version` | [`plpgsql`](plpgsql) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1070 | [pg_cron](/pg_cron) | 1.6 | [pg_cron](/pg_cron) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  | `pg_catalog` |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1080 | [pg_later](/pg_later) | 0.2.0 | [pg_later](/pg_later) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` | `pgrx` | `pglater` | [`pgmq`](pgmq) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1090 | [pg_background](/pg_background) | 1.3 | [pg_background](/pg_background) | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |




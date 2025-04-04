# TIME


> TIME: TimescaleDB, Versioning & Temporal Table, Crontab, Async & Background Job Scheduler, ...
## Extensions


There are 11 available extensions in this category:

[`timescaledb`](/timescaledb) [`timescaledb_toolkit`](/timescaledb_toolkit) [`timeseries`](/timeseries) [`periods`](/periods) [`temporal_tables`](/temporal_tables) [`emaj`](/emaj) [`table_version`](/table_version) [`pg_cron`](/pg_cron) [`pg_task`](/pg_task) [`pg_later`](/pg_later) [`pg_background`](/pg_background)


| ID | Extension | Version | Package | License | RPM | DEB | Website | `Bin` | `LOAD` | `DYLIB` | `DDL` | Description |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:-------:|:-----:|:------:|:-------:|:-----:|-------------|
| 1000 | [timescaledb](/timescaledb) | 2.19.1 | [timescaledb](/timescaledb) | **<span class="tcwarn">Timescale</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/timescale/timescaledb) |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Enables scalable inserts and complex queries for time-series data |
| 1010 | [timescaledb_toolkit](/timescaledb_toolkit) | 1.19.0 | [timescaledb_toolkit](/timescaledb_toolkit) | **<span class="tcwarn">Timescale</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/timescale/timescaledb-toolkit) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Library of analytical hyperfunctions, time-series pipelining, and other SQL utilities |
| 1020 | [timeseries](/timeseries) | 0.1.6 | [pg_timeseries](/timeseries) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/tembo-io/pg_timeseries) |  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | Convenience API for Tembo time series stack |
| 1030 | [periods](/periods) | 1.2.3 | [periods](/periods) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/xocolatl/periods) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Provide Standard SQL functionality for PERIODs and SYSTEM VERSIONING |
| 1040 | [temporal_tables](/temporal_tables) | 1.2.2 | [temporal_tables](/temporal_tables) | **<span class="tcblue">BSD-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://pgxn.org/dist/temporal_tables/) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | temporal tables |
| 1050 | [emaj](/emaj) | 4.6.0 | [emaj](/emaj) | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/dalibo/emaj) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Enables fine-grained write logging and time travel on subsets of the database. |
| 1060 | [table_version](/table_version) | 1.11.1 | [table_version](/table_version) | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/linz/postgresql-tableversion) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | PostgreSQL table versioning extension |
| 1070 | [pg_cron](/pg_cron) | 1.6.5 | [pg_cron](/pg_cron) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/citusdata/pg_cron) |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Job scheduler for PostgreSQL |
| 1080 | [pg_task](/pg_task) | 2.1.7 | [pg_task](/pg_task) | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/RekGRpth/pg_task) |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | execute any sql command at any specific time at background |
| 1090 | [pg_later](/pg_later) | 0.3.0 | [pg_later](/pg_later) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/tembo-io/pg_later) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | pg_later: Run queries now and get results later |
| 1100 | [pg_background](/pg_background) | 1.3 | [pg_background](/pg_background) | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/vibhorkum/pg_background) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Run SQL queries in the background |



### RHEL 8 Compatible (el8)

```yaml
pg17: timescaledb timescaledb_toolkit pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background
pg16: timescaledb timescaledb_toolkit pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background
pg15: timescaledb timescaledb_toolkit pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background
pg14: timescaledb timescaledb_toolkit pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background
pg13: pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background #timescaledb #timescaledb_toolkit
```


### RHEL 9 Compatible (el9)

```yaml
pg17: timescaledb timescaledb_toolkit pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background
pg16: timescaledb timescaledb_toolkit pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background
pg15: timescaledb timescaledb_toolkit pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background
pg14: timescaledb timescaledb_toolkit pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background
pg13: pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background #timescaledb #timescaledb_toolkit
```


### Debian 12 bookworm Compatible (d12)

```yaml
pg17: timescaledb timescaledb_toolkit pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background
pg16: timescaledb timescaledb_toolkit pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background
pg15: timescaledb timescaledb_toolkit pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background
pg14: timescaledb timescaledb_toolkit pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background
pg13: pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background #timescaledb #timescaledb_toolkit
```


### Ubuntu 24.04 jammy Compatible (u22)

```yaml
pg17: timescaledb timescaledb_toolkit pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background
pg16: timescaledb timescaledb_toolkit pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background
pg15: timescaledb timescaledb_toolkit pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background
pg14: timescaledb timescaledb_toolkit pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background
pg13: pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background #timescaledb #timescaledb_toolkit
```


### Ubuntu 24.04 noble Compatible (u24)

```yaml
pg17: timescaledb timescaledb_toolkit pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background
pg16: timescaledb timescaledb_toolkit pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background
pg15: timescaledb timescaledb_toolkit pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background
pg14: timescaledb timescaledb_toolkit pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background
pg13: pg_timeseries periods temporal_tables emaj table_version pg_cron pg_task pg_later pg_background #timescaledb #timescaledb_toolkit
```



--------

## RPM Packages


| Package | Version | License | RPM | RPM Package | 17 | 16 | 15 | 14 | 13 | Description |
|---------|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|-------------|
| [timescaledb](/timescaledb) | 2.19.0 | **<span class="tcwarn">Timescale</span>** | **<span class="tcwarn">PIGSTY</span>** | `timescaledb-tsl_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | Enables scalable inserts and complex queries for time-series data |
| [timescaledb_toolkit](/timescaledb_toolkit) | 1.19.0 | **<span class="tcwarn">Timescale</span>** | **<span class="tcwarn">PIGSTY</span>** | `timescaledb-toolkit_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | Library of analytical hyperfunctions, time-series pipelining, and other SQL utilities |
| [pg_timeseries](/timeseries) | 0.1.6 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_timeseries_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Convenience API for Tembo time series stack |
| [periods](/periods) | 1.2.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `periods_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Provide Standard SQL functionality for PERIODs and SYSTEM VERSIONING |
| [temporal_tables](/temporal_tables) | 1.2.2 | **<span class="tcblue">BSD-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `temporal_tables_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | temporal tables |
| [emaj](/emaj) | 4.5.0 | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | `e-maj_$v` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Enables fine-grained write logging and time travel on subsets of the database. |
| [table_version](/table_version) | 1.11.1 | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | `table_version_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | PostgreSQL table versioning extension |
| [pg_cron](/pg_cron) | 1.6 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pg_cron_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Job scheduler for PostgreSQL |
| [pg_task](/pg_task) | 1.0.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `pg_task_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | execute any sql command at any specific time at background |
| [pg_later](/pg_later) | 0.3.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_later_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | pg_later: Run queries now and get results later |
| [pg_background](/pg_background) | 1.3 | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | `pg_background_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Run SQL queries in the background |



### RHEL 8 Compatible (el8)

```yaml
pg17: timescaledb-tsl_17* timescaledb-toolkit_17 pg_timeseries_17 periods_17* temporal_tables_17* e-maj_17 table_version_17 pg_cron_17* pg_task_17* pg_later_17 pg_background_17*
pg16: timescaledb-tsl_16* timescaledb-toolkit_16 pg_timeseries_16 periods_16* temporal_tables_16* e-maj_16 table_version_16 pg_cron_16* pg_task_16* pg_later_16 pg_background_16*
pg15: timescaledb-tsl_15* timescaledb-toolkit_15 pg_timeseries_15 periods_15* temporal_tables_15* e-maj_15 table_version_15 pg_cron_15* pg_task_15* pg_later_15 pg_background_15*
pg14: timescaledb-tsl_14* timescaledb-toolkit_14 pg_timeseries_14 periods_14* temporal_tables_14* e-maj_14 table_version_14 pg_cron_14* pg_task_14* pg_later_14 pg_background_14*
pg13: pg_timeseries_13 periods_13* temporal_tables_13* e-maj_13 table_version_13 pg_cron_13* pg_task_13* pg_later_13 pg_background_13* #timescaledb-tsl_13* #timescaledb-toolkit_13
```


### RHEL 9 Compatible (el9)

```yaml
pg17: timescaledb-tsl_17* timescaledb-toolkit_17 pg_timeseries_17 periods_17* temporal_tables_17* e-maj_17 table_version_17 pg_cron_17* pg_task_17* pg_later_17 pg_background_17*
pg16: timescaledb-tsl_16* timescaledb-toolkit_16 pg_timeseries_16 periods_16* temporal_tables_16* e-maj_16 table_version_16 pg_cron_16* pg_task_16* pg_later_16 pg_background_16*
pg15: timescaledb-tsl_15* timescaledb-toolkit_15 pg_timeseries_15 periods_15* temporal_tables_15* e-maj_15 table_version_15 pg_cron_15* pg_task_15* pg_later_15 pg_background_15*
pg14: timescaledb-tsl_14* timescaledb-toolkit_14 pg_timeseries_14 periods_14* temporal_tables_14* e-maj_14 table_version_14 pg_cron_14* pg_task_14* pg_later_14 pg_background_14*
pg13: pg_timeseries_13 periods_13* temporal_tables_13* e-maj_13 table_version_13 pg_cron_13* pg_task_13* pg_later_13 pg_background_13* #timescaledb-tsl_13* #timescaledb-toolkit_13
```



--------

## DEB Packages


| Package | Version | License | DEB | DEB Package | 17 | 16 | 15 | 14 | 13 | Description |
|---------|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|-------------|
| [timescaledb](/timescaledb) | 2.19.0 | **<span class="tcwarn">Timescale</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-timescaledb-tsl` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | Enables scalable inserts and complex queries for time-series data |
| [timescaledb_toolkit](/timescaledb_toolkit) | 1.19.0 | **<span class="tcwarn">Timescale</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-timescaledb-toolkit` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | Library of analytical hyperfunctions, time-series pipelining, and other SQL utilities |
| [pg_timeseries](/timeseries) | 0.1.6 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-timeseries` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Convenience API for Tembo time series stack |
| [periods](/periods) | 1.2.3 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-periods` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Provide Standard SQL functionality for PERIODs and SYSTEM VERSIONING |
| [temporal_tables](/temporal_tables) | 1.2.2 | **<span class="tcblue">BSD-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-temporal-tables` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | temporal tables |
| [emaj](/emaj) | 4.4.0 | **<span class="tcwarn">GPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-emaj` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Enables fine-grained write logging and time travel on subsets of the database. |
| [table_version](/table_version) | 1.11.0 | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-table-version` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | PostgreSQL table versioning extension |
| [pg_cron](/pg_cron) | 1.6 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-cron` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Job scheduler for PostgreSQL |
| [pg_task](/pg_task) | 1.0.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-task` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | execute any sql command at any specific time at background |
| [pg_later](/pg_later) | 0.3.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-later` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | pg_later: Run queries now and get results later |
| [pg_background](/pg_background) | 1.3 | **<span class="tcwarn">GPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-background` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Run SQL queries in the background |



### Debian 12 bookworm Compatible (d12)

```yaml
pg17: postgresql-17-timescaledb-tsl postgresql-17-timescaledb-toolkit postgresql-17-pg-timeseries postgresql-17-periods postgresql-17-temporal-tables postgresql-17-emaj postgresql-17-table-version postgresql-17-cron postgresql-17-pg-task postgresql-17-pg-later postgresql-17-pg-background
pg16: postgresql-16-timescaledb-tsl postgresql-16-timescaledb-toolkit postgresql-16-pg-timeseries postgresql-16-periods postgresql-16-temporal-tables postgresql-16-emaj postgresql-16-table-version postgresql-16-cron postgresql-16-pg-task postgresql-16-pg-later postgresql-16-pg-background
pg15: postgresql-15-timescaledb-tsl postgresql-15-timescaledb-toolkit postgresql-15-pg-timeseries postgresql-15-periods postgresql-15-temporal-tables postgresql-15-emaj postgresql-15-table-version postgresql-15-cron postgresql-15-pg-task postgresql-15-pg-later postgresql-15-pg-background
pg14: postgresql-14-timescaledb-tsl postgresql-14-timescaledb-toolkit postgresql-14-pg-timeseries postgresql-14-periods postgresql-14-temporal-tables postgresql-14-emaj postgresql-14-table-version postgresql-14-cron postgresql-14-pg-task postgresql-14-pg-later postgresql-14-pg-background
pg13: postgresql-13-pg-timeseries postgresql-13-periods postgresql-13-temporal-tables postgresql-13-emaj postgresql-13-table-version postgresql-13-cron postgresql-13-pg-task postgresql-13-pg-later postgresql-13-pg-background #postgresql-13-timescaledb-tsl #postgresql-13-timescaledb-toolkit
```


### Ubuntu 24.04 jammy Compatible (u22)

```yaml
pg17: postgresql-17-timescaledb-tsl postgresql-17-timescaledb-toolkit postgresql-17-pg-timeseries postgresql-17-periods postgresql-17-temporal-tables postgresql-17-emaj postgresql-17-table-version postgresql-17-cron postgresql-17-pg-task postgresql-17-pg-later postgresql-17-pg-background
pg16: postgresql-16-timescaledb-tsl postgresql-16-timescaledb-toolkit postgresql-16-pg-timeseries postgresql-16-periods postgresql-16-temporal-tables postgresql-16-emaj postgresql-16-table-version postgresql-16-cron postgresql-16-pg-task postgresql-16-pg-later postgresql-16-pg-background
pg15: postgresql-15-timescaledb-tsl postgresql-15-timescaledb-toolkit postgresql-15-pg-timeseries postgresql-15-periods postgresql-15-temporal-tables postgresql-15-emaj postgresql-15-table-version postgresql-15-cron postgresql-15-pg-task postgresql-15-pg-later postgresql-15-pg-background
pg14: postgresql-14-timescaledb-tsl postgresql-14-timescaledb-toolkit postgresql-14-pg-timeseries postgresql-14-periods postgresql-14-temporal-tables postgresql-14-emaj postgresql-14-table-version postgresql-14-cron postgresql-14-pg-task postgresql-14-pg-later postgresql-14-pg-background
pg13: postgresql-13-pg-timeseries postgresql-13-periods postgresql-13-temporal-tables postgresql-13-emaj postgresql-13-table-version postgresql-13-cron postgresql-13-pg-task postgresql-13-pg-later postgresql-13-pg-background #postgresql-13-timescaledb-tsl #postgresql-13-timescaledb-toolkit
```


### Ubuntu 24.04 noble Compatible (u24)

```yaml
pg17: postgresql-17-timescaledb-tsl postgresql-17-timescaledb-toolkit postgresql-17-pg-timeseries postgresql-17-periods postgresql-17-temporal-tables postgresql-17-emaj postgresql-17-table-version postgresql-17-cron postgresql-17-pg-task postgresql-17-pg-later postgresql-17-pg-background
pg16: postgresql-16-timescaledb-tsl postgresql-16-timescaledb-toolkit postgresql-16-pg-timeseries postgresql-16-periods postgresql-16-temporal-tables postgresql-16-emaj postgresql-16-table-version postgresql-16-cron postgresql-16-pg-task postgresql-16-pg-later postgresql-16-pg-background
pg15: postgresql-15-timescaledb-tsl postgresql-15-timescaledb-toolkit postgresql-15-pg-timeseries postgresql-15-periods postgresql-15-temporal-tables postgresql-15-emaj postgresql-15-table-version postgresql-15-cron postgresql-15-pg-task postgresql-15-pg-later postgresql-15-pg-background
pg14: postgresql-14-timescaledb-tsl postgresql-14-timescaledb-toolkit postgresql-14-pg-timeseries postgresql-14-periods postgresql-14-temporal-tables postgresql-14-emaj postgresql-14-table-version postgresql-14-cron postgresql-14-pg-task postgresql-14-pg-later postgresql-14-pg-background
pg13: postgresql-13-pg-timeseries postgresql-13-periods postgresql-13-temporal-tables postgresql-13-emaj postgresql-13-table-version postgresql-13-cron postgresql-13-pg-task postgresql-13-pg-later postgresql-13-pg-background #postgresql-13-timescaledb-tsl #postgresql-13-timescaledb-toolkit
```



--------

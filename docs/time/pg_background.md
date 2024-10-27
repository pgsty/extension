# pg_background


> [pg_background](/https://github.com/vibhorkum/pg_background): Run SQL queries in the background


-------

## Extension


| ID | Extension | Version | License | RPM | DEB | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` | Requires |
|:--:|-----------|:-------:|:-------:|:---:|:---:|:------:|:-------:|:-----:|:-------:|:-------:|----------|
| 1080 | [pg_background](https://github.com/vibhorkum/pg_background) | 1.0 | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |  |





```sql
CREATE EXTENSION pg_background;
```


-----------


## Packages


| OS | Version | License | RPM | RPM Package | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0 | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | `pg_background_$v*` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |
| [DEB](/deb) | 1.2 | **<span class="tcwarn">GPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-background` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |



Install `pg_background` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pg_background_17*;
dnf install pg_background_16*;
dnf install pg_background_15*;
dnf install pg_background_14*;
dnf install pg_background_13*;
dnf install pg_background_12*;
```


Install `pg_background` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pg-background;
apt install postgresql-16-pg-background;
apt install postgresql-15-pg-background;
apt install postgresql-14-pg-background;
apt install postgresql-13-pg-background;
apt install postgresql-12-pg-background;
```


-----------


## Category: TIME


| ID | Extension | Version | Package | License | RPM | DEB | lang | Tags | Schemas | Requires | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:----:|------|---------|----------|:------:|:-------:|:-----:|:-------:|:-------:|
| 1000 | [timescaledb](/time/timescaledb) | 2.17.0 | [timescaledb](/time/timescaledb) | **<span class="tcwarn">Timescale</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | C |  |  |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1010 | [timeseries](/time/timeseries) | 0.1.6 | [pg_timeseries](/time/timeseries) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | SQL |  |  | [`columnar`](/olap/columnar), [`pg_cron`](/time/pg_cron), [`pg_ivm`](/feat/pg_ivm), [`pg_partman`](/olap/pg_partman) |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1020 | [periods](/time/periods) | 1.2 | [periods](/time/periods) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | C |  |  | [`btree_gist`](/func/btree_gist) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1030 | [temporal_tables](/time/temporal_tables) | 1.2.2 | [temporal_tables](/time/temporal_tables) | **<span class="tcblue">BSD-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1040 | [emaj](/time/emaj) | 4.5.0 | [emaj](/time/emaj) | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** |  |  | `emaj` | [`dblink`](/fdw/dblink), [`btree_gist`](/func/btree_gist) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1050 | [table_version](/time/table_version) | 1.10.3 | [table_version](/time/table_version) | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** |  |  | `table_version` | [`plpgsql`](/lang/plpgsql) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1060 | [pg_cron](/time/pg_cron) | 1.6 | [pg_cron](/time/pg_cron) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  | `pg_catalog` |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1070 | [pg_later](/time/pg_later) | 0.1.1 | [pg_later](/time/pg_later) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | Rust | `pgrx` | `pglater` | [`pgmq`](/feat/pgmq) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1080 | [pg_background](/time/pg_background) | 1.0 | [pg_background](/time/pg_background) | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1090 | [pg_timetable](/time/pg_timetable) | 5.9.0 | [pg_timetable](/time/pg_timetable) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | Go | `bin` |  |  |  | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |




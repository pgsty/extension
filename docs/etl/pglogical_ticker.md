# pglogical


> [pglogical](/https://github.com/2ndQuadrant/pglogical): Have an accurate view on pglogical replication delay


-------

## Extension


| ID | Extension | Version | License | RPM | DEB | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` | Requires |
|:--:|-----------|:-------:|:-------:|:---:|:---:|:------:|:-------:|:-----:|:-------:|:-------:|----------|
| 9502 | [pglogical_ticker](https://github.com/2ndQuadrant/pglogical) | 1.4 | **<span class="tcblue">PostgreSQL</span>** |  | **<span class="tccyan">PGDG</span>** |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> | [`pglogical`](/etl/pglogical) |





```sql
CREATE EXTENSION pglogical_tickerCASCADE;
```


-----------


## Packages


| OS | Version | License | RPM | RPM Package | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| Distro-pglogical | 2.4.4 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pglogical_$v*` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |
| Distro-pglogical | 2.4.5 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pglogical*` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |



Install `pglogical` [DEB](/deb) from the  **APT** repo:

```bash
apt install postgresql-17-pglogical*;
apt install postgresql-16-pglogical*;
apt install postgresql-15-pglogical*;
apt install postgresql-14-pglogical*;
apt install postgresql-13-pglogical*;
apt install postgresql-12-pglogical*;
```


-----------


## Category: ETL


| ID | Extension | Version | Package | License | RPM | DEB | lang | Tags | Schemas | Requires | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:----:|------|---------|----------|:------:|:-------:|:-----:|:-------:|:-------:|
| 9500 | [pglogical](/etl/pglogical) | 2.4.4 | [pglogical](/etl/pglogical) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  | `pglogical` |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 9501 | [pglogical_origin](/etl/pglogical_origin) | 1.0.0 | [pglogical](/etl/pglogical_origin) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  | `pglogical_origin` |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 9502 | [pglogical_ticker](/etl/pglogical_ticker) | 1.4 | [pglogical](/etl/pglogical_ticker) | **<span class="tcblue">PostgreSQL</span>** |  | **<span class="tccyan">PGDG</span>** |  |  | `pglogical_ticker` | [`pglogical`](/etl/pglogical) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 9510 | [pgl_ddl_deploy](/etl/pgl_ddl_deploy) | 2.2 | [pgl_ddl_deploy](/etl/pgl_ddl_deploy) | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  | `pgl_ddl_deploy` | [`pglogical`](/etl/pglogical) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 9520 | [pg_failover_slots](/etl/pg_failover_slots) | 1.0.1 | [pg_failover_slots](/etl/pg_failover_slots) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | C | `nil-lic` |  |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |
| 9610 | [wal2json](/etl/wal2json) | 2.5.3 | [wal2json](/etl/wal2json) | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | C |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9620 | [wal2mongo](/etl/wal2mongo) | 1.0.7 | [wal2mongo](/etl/wal2mongo) | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | C |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9630 | [decoderbufs](/etl/decoderbufs) | 0.1.0 | [decoderbufs](/etl/decoderbufs) | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | C |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9640 | [decoder_raw](/etl/decoder_raw) | 1.0 | [decoder_raw](/etl/decoder_raw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | C |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  | <span class="tcwarn">✘</span> |
| 9690 | [test_decoding](/etl/test_decoding) | - | [test_decoding](/etl/test_decoding) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | **<span class="tcblue">CONTRIB</span>** | C |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9700 | [mimeo](/etl/mimeo) | 1.5.1 | [mimeo](/etl/mimeo) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** | SQL |  |  | [`dblink`](/fdw/dblink) |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 9710 | [repmgr](/etl/repmgr) | 5.4 | [repmgr](/etl/repmgr) | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  | `not-used` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 9800 | [pgcopydb](/etl/pgcopydb) | 0.15 | [pgcopydb](/etl/pgcopydb) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** | C |  |  |  |  | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9810 | [pgloader](/etl/pgloader) | 3.6.10 | [pgloader](/etl/pgloader) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | Lisp |  |  |  |  | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9820 | [pg_fact_loader](/etl/pg_fact_loader) | 2.0 | [pg_fact_loader](/etl/pg_fact_loader) | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  | `fact_loader` |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 9830 | [pg_bulkload](/etl/pg_bulkload) | 3.1.21 | [pg_bulkload](/etl/pg_bulkload) | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 9840 | [pg_comparator](/etl/pg_comparator) | 2.2.5 | [pg_comparator](/etl/pg_comparator) | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | PGDG | C | `bin`, `archived` |  |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9850 | [pgimportdoc](/etl/pgimportdoc) | 0.1.4 | [pgimportdoc](/etl/pgimportdoc) | **<span class="tcblue">BSD-2</span>** | **<span class="tccyan">PGDG</span>** | PGDG | C |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9860 | [pgexportdoc](/etl/pgexportdoc) | 0.1.4 | [pgexportdoc](/etl/pgexportdoc) | **<span class="tcblue">BSD-2</span>** | **<span class="tccyan">PGDG</span>** | PGDG | C |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |




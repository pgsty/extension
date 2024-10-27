# mimeo


> [mimeo](/https://github.com/omniti-labs/mimeo): Extension for specialized, per-table replication between PostgreSQL instances


-------

## Extension


| ID | Extension | Version | License | RPM | DEB | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` | Requires |
|:--:|-----------|:-------:|:-------:|:---:|:---:|:------:|:-------:|:-----:|:-------:|:-------:|----------|
| 9700 | [mimeo](https://github.com/omniti-labs/mimeo) | 1.5.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> | [`dblink`](dblink) |


> **Comment**: name conflict with pg_partman


```sql
CREATE EXTENSION mimeoCASCADE;
```


-----------


## Packages


| OS | Version | License | RPM | RPM Package | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.5.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `mimeo_$v` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |
| [DEB](/deb) | 1.5.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-mimeo` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |



Install `mimeo` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install mimeo_17;
dnf install mimeo_16;
dnf install mimeo_15;
dnf install mimeo_14;
dnf install mimeo_13;
dnf install mimeo_12;
```


Install `mimeo` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-mimeo;
apt install postgresql-16-mimeo;
apt install postgresql-15-mimeo;
apt install postgresql-14-mimeo;
apt install postgresql-13-mimeo;
apt install postgresql-12-mimeo;
```


-----------


## Category: ETL


| ID | Extension | Version | Package | License | RPM | DEB | lang | Tags | Schemas | Requires | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:----:|------|---------|----------|:------:|:-------:|:-----:|:-------:|:-------:|
| 9500 | [pglogical](/pglogical) | 2.4.4 | [pglogical](/pglogical) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  | `pglogical` |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 9501 | [pglogical_origin](/pglogical_origin) | 1.0.0 | [pglogical](/pglogical_origin) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  | `pglogical_origin` |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 9502 | [pglogical_ticker](/pglogical_ticker) | 1.4 | [pglogical](/pglogical_ticker) | **<span class="tcblue">PostgreSQL</span>** |  | **<span class="tccyan">PGDG</span>** |  |  | `pglogical_ticker` | [`pglogical`](pglogical) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 9510 | [pgl_ddl_deploy](/pgl_ddl_deploy) | 2.2 | [pgl_ddl_deploy](/pgl_ddl_deploy) | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  | `pgl_ddl_deploy` | [`pglogical`](pglogical) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 9520 | [pg_failover_slots](/pg_failover_slots) | 1.0.1 | [pg_failover_slots](/pg_failover_slots) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | C | `nil-lic` |  |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |
| 9610 | [wal2json](/wal2json) | 2.5.3 | [wal2json](/wal2json) | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | C |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9620 | [wal2mongo](/wal2mongo) | 1.0.7 | [wal2mongo](/wal2mongo) | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | C |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9630 | [decoderbufs](/decoderbufs) | 0.1.0 | [decoderbufs](/decoderbufs) | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | C |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9640 | [decoder_raw](/decoder_raw) | 1.0 | [decoder_raw](/decoder_raw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | C |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  | <span class="tcwarn">✘</span> |
| 9690 | [test_decoding](/test_decoding) | - | [test_decoding](/test_decoding) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | **<span class="tcblue">CONTRIB</span>** | C |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9700 | [mimeo](/mimeo) | 1.5.1 | [mimeo](/mimeo) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** | SQL |  |  | [`dblink`](dblink) |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 9710 | [repmgr](/repmgr) | 5.4 | [repmgr](/repmgr) | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  | `not-used` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 9800 | [pgcopydb](/pgcopydb) | 0.15 | [pgcopydb](/pgcopydb) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** | C |  |  |  |  | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9810 | [pgloader](/pgloader) | 3.6.10 | [pgloader](/pgloader) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | Lisp |  |  |  |  | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9820 | [pg_fact_loader](/pg_fact_loader) | 2.0 | [pg_fact_loader](/pg_fact_loader) | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  | `fact_loader` |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 9830 | [pg_bulkload](/pg_bulkload) | 3.1.21 | [pg_bulkload](/pg_bulkload) | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 9840 | [pg_comparator](/pg_comparator) | 2.2.5 | [pg_comparator](/pg_comparator) | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | PGDG | C | `bin`, `archived` |  |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9850 | [pgimportdoc](/pgimportdoc) | 0.1.4 | [pgimportdoc](/pgimportdoc) | **<span class="tcblue">BSD-2</span>** | **<span class="tccyan">PGDG</span>** | PGDG | C |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9860 | [pgexportdoc](/pgexportdoc) | 0.1.4 | [pgexportdoc](/pgexportdoc) | **<span class="tcblue">BSD-2</span>** | **<span class="tccyan">PGDG</span>** | PGDG | C |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |




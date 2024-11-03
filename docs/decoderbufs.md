# decoderbufs


> [decoderbufs](https://github.com/debezium/postgres-decoderbufs): Logical decoding plugin that delivers WAL stream changes using a Protocol Buffer format
>
> https://github.com/debezium/postgres-decoderbufs


-------


## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [decoderbufs](https://github.com/debezium/postgres-decoderbufs) | 0.1.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |



| Package | Tags | Schemas | Requires | Required by | Comment | Description |
|---------|------|---------|----------|-------------|:-------:|-------------|
| [decoderbufs](/decoderbufs) |  |  |  |  |  | Logical decoding plugin that delivers WAL stream changes using a Protocol Buffer format |





-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.1.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `postgres-decoderbufs_$v*` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 0.1.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-decoderbufs` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `decoderbufs` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["decoderbufs"]}'
```


Install `decoderbufs` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install postgres-decoderbufs_16*;
dnf install postgres-decoderbufs_15*;
dnf install postgres-decoderbufs_14*;
dnf install postgres-decoderbufs_13*;
dnf install postgres-decoderbufs_12*;
```


Install `decoderbufs` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-16-decoderbufs;
apt install postgresql-15-decoderbufs;
apt install postgresql-14-decoderbufs;
apt install postgresql-13-decoderbufs;
apt install postgresql-12-decoderbufs;
```


-----------


## Category: ETL


| ID | Extension | Version | Package | License | RPM | DEB | PL | Tags | Schemas | Requires | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:--:|------|---------|----------|:------:|:-------:|:-----:|:-------:|:-------:|
| 9500 | [pglogical](/pglogical) | 2.4.4 | [pglogical](/pglogical) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  | `pglogical` |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 9501 | [pglogical_origin](/pglogical_origin) | 1.0.0 | [pglogical](/pglogical_origin) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  | `pglogical_origin` |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 9510 | [pglogical_ticker](/pglogical_ticker) | 1.4 | [pglogical_ticker](/pglogical_ticker) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** | `C` |  | `pglogical_ticker` | [`pglogical`](pglogical) | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 9520 | [pgl_ddl_deploy](/pgl_ddl_deploy) | 2.2 | [pgl_ddl_deploy](/pgl_ddl_deploy) | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  | `pgl_ddl_deploy` | [`pglogical`](pglogical) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 9530 | [pg_failover_slots](/pg_failover_slots) | 1.0.1 | [pg_failover_slots](/pg_failover_slots) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` | `nil-lic` |  |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |
| 9630 | [wal2json](/wal2json) | 2.5.3 | [wal2json](/wal2json) | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9640 | [wal2mongo](/wal2mongo) | 1.0.7 | [wal2mongo](/wal2mongo) | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9650 | [decoderbufs](/decoderbufs) | 0.1.0 | [decoderbufs](/decoderbufs) | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9660 | [decoder_raw](/decoder_raw) | 1.0 | [decoder_raw](/decoder_raw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  | <span class="tcwarn">✘</span> |
| 9690 | [test_decoding](/test_decoding) | - | [test_decoding](/test_decoding) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | **<span class="tcblue">CONTRIB</span>** | `C` |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9700 | [mimeo](/mimeo) | 1.5.1 | [mimeo](/mimeo) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** | `SQL` |  |  | [`dblink`](dblink) |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 9710 | [repmgr](/repmgr) | 5.4 | [repmgr](/repmgr) | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  | `not-used` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 9820 | [pg_fact_loader](/pg_fact_loader) | 2.0 | [pg_fact_loader](/pg_fact_loader) | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  | `fact_loader` |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 9830 | [pg_bulkload](/pg_bulkload) | 3.1.21 | [pg_bulkload](/pg_bulkload) | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |




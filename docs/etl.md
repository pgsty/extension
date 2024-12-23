# ETL


> ETL: Logical Replication, Decoding, CDC in protobuf/JSON/Mongo format, Copy & Load & Compare Postgres Databases,...
## Extensions


There are 15 available extensions in this category:

[`pglogical`](/pglogical) [`pglogical_origin`](/pglogical_origin) [`pglogical_ticker`](/pglogical_ticker) [`pgl_ddl_deploy`](/pgl_ddl_deploy) [`pg_failover_slots`](/pg_failover_slots) [`wal2json`](/wal2json) [`wal2mongo`](/wal2mongo) [`decoderbufs`](/decoderbufs) [`decoder_raw`](/decoder_raw) [`pgoutput`](/pgoutput) [`test_decoding`](/test_decoding) [`mimeo`](/mimeo) [`repmgr`](/repmgr) [`pg_fact_loader`](/pg_fact_loader) [`pg_bulkload`](/pg_bulkload)


| ID | Extension | Version | Package | License | RPM | DEB | Website | `Bin` | `LOAD` | `DYLIB` | `DDL` | Description |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:-------:|:-----:|:------:|:-------:|:-----:|-------------|
| 9500 | [pglogical](/pglogical) | 2.4.5 | [pglogical](/pglogical) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/2ndQuadrant/pglogical) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | PostgreSQL Logical Replication |
| 9501 | [pglogical_origin](/pglogical_origin) | 1.0.0 | [pglogical](/pglogical_origin) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/2ndQuadrant/pglogical) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Dummy extension for compatibility when upgrading from Postgres 9.4 |
| 9510 | [pglogical_ticker](/pglogical_ticker) | 1.4 | [pglogical_ticker](/pglogical_ticker) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/enova/pglogical_ticker) |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Have an accurate view on pglogical replication delay |
| 9520 | [pgl_ddl_deploy](/pgl_ddl_deploy) | 2.2 | [pgl_ddl_deploy](/pgl_ddl_deploy) | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/enova/pgl_ddl_deploy) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | automated ddl deployment using pglogical |
| 9530 | [pg_failover_slots](/pg_failover_slots) | 1.0.1 | [pg_failover_slots](/pg_failover_slots) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/EnterpriseDB/pg_failover_slots) |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | PG Failover Slots extension |
| 9630 | [wal2json](/wal2json) | 2.5.3 | [wal2json](/wal2json) | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/eulerto/wal2json) |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | Changing data capture in JSON format |
| 9640 | [wal2mongo](/wal2mongo) | 1.0.7 | [wal2mongo](/wal2mongo) | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/HighgoSoftware/wal2mongo) |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | PostgreSQL logical decoding output plugin for MongoDB |
| 9650 | [decoderbufs](/decoderbufs) | 0.1.0 | [decoderbufs](/decoderbufs) | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/debezium/postgres-decoderbufs) |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | Logical decoding plugin that delivers WAL stream changes using a Protocol Buffer format |
| 9660 | [decoder_raw](/decoder_raw) | 1.0 | [decoder_raw](/decoder_raw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/michaelpq/pg_plugins/blob/main/decoder_raw/) |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | Output plugin for logical replication in Raw SQL format |
| 9680 | [pgoutput](/pgoutput) | - | [pgoutput](/pgoutput) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | **<span class="tcblue">CONTRIB</span>** | [LINK](https://www.postgresql.org/docs/current/protocol-logical-replication.html) |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | Logical Replication output plugin |
| 9690 | [test_decoding](/test_decoding) | - | [test_decoding](/test_decoding) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | **<span class="tcblue">CONTRIB</span>** | [LINK](https://www.postgresql.org/docs/current/test-decoding.html) |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | SQL-based test/example module for WAL logical decoding |
| 9700 | [mimeo](/mimeo) | 1.5.1 | [mimeo](/mimeo) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/omniti-labs/mimeo) |  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | Extension for specialized, per-table replication between PostgreSQL instances |
| 9710 | [repmgr](/repmgr) | 5.4 | [repmgr](/repmgr) | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/EnterpriseDB/repmgr) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Replication manager for PostgreSQL |
| 9820 | [pg_fact_loader](/pg_fact_loader) | 2.0 | [pg_fact_loader](/pg_fact_loader) | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/enova/pg_fact_loader) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | build fact tables with Postgres |
| 9830 | [pg_bulkload](/pg_bulkload) | 3.1.21 | [pg_bulkload](/pg_bulkload) | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/ossc-db/pg_bulkload) | **<span class="tcwarn">✔</span>** |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | pg_bulkload is a high speed data loading utility for PostgreSQL |



### RHEL 8 Compatible (el8)

```yaml
pg17: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json decoderbufs decoder_raw mimeo pg_fact_loader #wal2mongo #repmgr #pg_bulkload
pg16: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json wal2mongo decoderbufs decoder_raw mimeo pg_fact_loader pg_bulkload #repmgr
pg15: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json wal2mongo decoderbufs decoder_raw mimeo pg_fact_loader pg_bulkload #repmgr
pg14: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json wal2mongo decoderbufs decoder_raw mimeo pg_fact_loader pg_bulkload #repmgr
pg13: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json wal2mongo decoderbufs decoder_raw mimeo pg_fact_loader pg_bulkload #repmgr
```


### RHEL 9 Compatible (el9)

```yaml
pg17: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json decoderbufs decoder_raw mimeo pg_fact_loader #wal2mongo #repmgr #pg_bulkload
pg16: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json wal2mongo decoderbufs decoder_raw mimeo pg_fact_loader pg_bulkload #repmgr
pg15: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json wal2mongo decoderbufs decoder_raw mimeo pg_fact_loader pg_bulkload #repmgr
pg14: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json wal2mongo decoderbufs decoder_raw mimeo pg_fact_loader pg_bulkload #repmgr
pg13: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json wal2mongo decoderbufs decoder_raw mimeo pg_fact_loader pg_bulkload #repmgr
```


### Debian 12 bookworm Compatible (d12)

```yaml
pg17: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json decoderbufs decoder_raw mimeo pg_fact_loader #wal2mongo #repmgr #pg_bulkload
pg16: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json wal2mongo decoderbufs decoder_raw mimeo pg_fact_loader pg_bulkload #repmgr
pg15: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json wal2mongo decoderbufs decoder_raw mimeo pg_fact_loader pg_bulkload #repmgr
pg14: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json wal2mongo decoderbufs decoder_raw mimeo pg_fact_loader pg_bulkload #repmgr
pg13: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json wal2mongo decoderbufs decoder_raw mimeo pg_fact_loader pg_bulkload #repmgr
```


### Ubuntu 24.04 jammy Compatible (u22)

```yaml
pg17: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json decoderbufs decoder_raw mimeo pg_fact_loader #wal2mongo #repmgr #pg_bulkload
pg16: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json wal2mongo decoderbufs decoder_raw mimeo pg_fact_loader pg_bulkload #repmgr
pg15: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json wal2mongo decoderbufs decoder_raw mimeo pg_fact_loader pg_bulkload #repmgr
pg14: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json wal2mongo decoderbufs decoder_raw mimeo pg_fact_loader pg_bulkload #repmgr
pg13: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json wal2mongo decoderbufs decoder_raw mimeo pg_fact_loader pg_bulkload #repmgr
```


### Ubuntu 24.04 noble Compatible (u24)

```yaml
pg17: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json decoderbufs decoder_raw mimeo pg_fact_loader #wal2mongo #repmgr #pg_bulkload
pg16: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json wal2mongo decoderbufs decoder_raw mimeo pg_fact_loader pg_bulkload #repmgr
pg15: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json wal2mongo decoderbufs decoder_raw mimeo pg_fact_loader pg_bulkload #repmgr
pg14: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json wal2mongo decoderbufs decoder_raw mimeo pg_fact_loader pg_bulkload #repmgr
pg13: pglogical pglogical_ticker pgl_ddl_deploy pg_failover_slots wal2json wal2mongo decoderbufs decoder_raw mimeo pg_fact_loader pg_bulkload #repmgr
```



--------

## RPM Packages


| Package | Version | License | RPM | RPM Package | 17 | 16 | 15 | 14 | 13 | Description |
|---------|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|-------------|
| [pglogical](/pglogical) | 2.4.5 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pglogical_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | PostgreSQL Logical Replication |
| [pglogical_ticker](/pglogical_ticker) | 1.4 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pglogical_ticker_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Have an accurate view on pglogical replication delay |
| [pgl_ddl_deploy](/pgl_ddl_deploy) | 2.2 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `pgl_ddl_deploy_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | automated ddl deployment using pglogical |
| [pg_failover_slots](/pg_failover_slots) | 1.0.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_failover_slots_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | PG Failover Slots extension |
| [wal2json](/wal2json) | 2.5.3 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `wal2json_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Changing data capture in JSON format |
| [wal2mongo](/wal2mongo) | 1.0.7 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `wal2mongo_$v*` |  | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | PostgreSQL logical decoding output plugin for MongoDB |
| [decoderbufs](/decoderbufs) | 0.1.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `postgres-decoderbufs_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Logical decoding plugin that delivers WAL stream changes using a Protocol Buffer format |
| [decoder_raw](/decoder_raw) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `decoder_raw_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Output plugin for logical replication in Raw SQL format |
| [pgoutput](/pgoutput) | - | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql$v-contrib` | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | Logical Replication output plugin |
| [test_decoding](/test_decoding) | - | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql$v-contrib` | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | SQL-based test/example module for WAL logical decoding |
| [mimeo](/mimeo) | 1.5.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `mimeo_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Extension for specialized, per-table replication between PostgreSQL instances |
| [repmgr](/repmgr) | 5.4 | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | `repmgr_$v*` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Replication manager for PostgreSQL |
| [pg_fact_loader](/pg_fact_loader) | 2.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `pg_fact_loader_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | build fact tables with Postgres |
| [pg_bulkload](/pg_bulkload) | 3.1.21 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `pg_bulkload_$v*` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | pg_bulkload is a high speed data loading utility for PostgreSQL |



### RHEL 8 Compatible (el8)

```yaml
pg17: pglogical_17* pglogical_ticker_17* pgl_ddl_deploy_17* pg_failover_slots_17* wal2json_17* postgres-decoderbufs_17* decoder_raw_17* mimeo_17 pg_fact_loader_17* #wal2mongo_17* #repmgr_17* #pg_bulkload_17*
pg16: pglogical_16* pglogical_ticker_16* pgl_ddl_deploy_16* pg_failover_slots_16* wal2json_16* wal2mongo_16* postgres-decoderbufs_16* decoder_raw_16* mimeo_16 pg_fact_loader_16* pg_bulkload_16* #repmgr_16*
pg15: pglogical_15* pglogical_ticker_15* pgl_ddl_deploy_15* pg_failover_slots_15* wal2json_15* wal2mongo_15* postgres-decoderbufs_15* decoder_raw_15* mimeo_15 pg_fact_loader_15* pg_bulkload_15* #repmgr_15*
pg14: pglogical_14* pglogical_ticker_14* pgl_ddl_deploy_14* pg_failover_slots_14* wal2json_14* wal2mongo_14* postgres-decoderbufs_14* decoder_raw_14* mimeo_14 pg_fact_loader_14* pg_bulkload_14* #repmgr_14*
pg13: pglogical_13* pglogical_ticker_13* pgl_ddl_deploy_13* pg_failover_slots_13* wal2json_13* wal2mongo_13* postgres-decoderbufs_13* decoder_raw_13* mimeo_13 pg_fact_loader_13* pg_bulkload_13* #repmgr_13*
```


### RHEL 9 Compatible (el9)

```yaml
pg17: pglogical_17* pglogical_ticker_17* pgl_ddl_deploy_17* pg_failover_slots_17* wal2json_17* postgres-decoderbufs_17* decoder_raw_17* mimeo_17 pg_fact_loader_17* #wal2mongo_17* #repmgr_17* #pg_bulkload_17*
pg16: pglogical_16* pglogical_ticker_16* pgl_ddl_deploy_16* pg_failover_slots_16* wal2json_16* wal2mongo_16* postgres-decoderbufs_16* decoder_raw_16* mimeo_16 pg_fact_loader_16* pg_bulkload_16* #repmgr_16*
pg15: pglogical_15* pglogical_ticker_15* pgl_ddl_deploy_15* pg_failover_slots_15* wal2json_15* wal2mongo_15* postgres-decoderbufs_15* decoder_raw_15* mimeo_15 pg_fact_loader_15* pg_bulkload_15* #repmgr_15*
pg14: pglogical_14* pglogical_ticker_14* pgl_ddl_deploy_14* pg_failover_slots_14* wal2json_14* wal2mongo_14* postgres-decoderbufs_14* decoder_raw_14* mimeo_14 pg_fact_loader_14* pg_bulkload_14* #repmgr_14*
pg13: pglogical_13* pglogical_ticker_13* pgl_ddl_deploy_13* pg_failover_slots_13* wal2json_13* wal2mongo_13* postgres-decoderbufs_13* decoder_raw_13* mimeo_13 pg_fact_loader_13* pg_bulkload_13* #repmgr_13*
```



--------

## DEB Packages


| Package | Version | License | DEB | DEB Package | 17 | 16 | 15 | 14 | 13 | Description |
|---------|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|-------------|
| [pglogical](/pglogical) | 2.4.5 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pglogical` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | PostgreSQL Logical Replication |
| [pglogical_ticker](/pglogical_ticker) | 1.4 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pglogical-ticker` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Have an accurate view on pglogical replication delay |
| [pgl_ddl_deploy](/pgl_ddl_deploy) | 2.2 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pgl-ddl-deploy` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | automated ddl deployment using pglogical |
| [pg_failover_slots](/pg_failover_slots) | 1.0.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-failover-slots` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | PG Failover Slots extension |
| [wal2json](/wal2json) | 2.5.3 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-wal2json` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Changing data capture in JSON format |
| [wal2mongo](/wal2mongo) | 1.0.7 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-wal2mongo` |  | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | PostgreSQL logical decoding output plugin for MongoDB |
| [decoderbufs](/decoderbufs) | 0.1.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-decoderbufs` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Logical decoding plugin that delivers WAL stream changes using a Protocol Buffer format |
| [decoder_raw](/decoder_raw) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-decoder-raw` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Output plugin for logical replication in Raw SQL format |
| [pgoutput](/pgoutput) | - | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql-$v` | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | Logical Replication output plugin |
| [test_decoding](/test_decoding) | - | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql-$v` | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | SQL-based test/example module for WAL logical decoding |
| [mimeo](/mimeo) | 1.5.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-mimeo` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Extension for specialized, per-table replication between PostgreSQL instances |
| [repmgr](/repmgr) | 5.4 | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-repmgr` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Replication manager for PostgreSQL |
| [pg_fact_loader](/pg_fact_loader) | 2.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pg-fact-loader` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | build fact tables with Postgres |
| [pg_bulkload](/pg_bulkload) | 3.1.21 | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-bulkload` |  | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | pg_bulkload is a high speed data loading utility for PostgreSQL |



### Debian 12 bookworm Compatible (d12)

```yaml
pg17: postgresql-17-pglogical postgresql-17-pglogical-ticker postgresql-17-pgl-ddl-deploy postgresql-17-pg-failover-slots postgresql-17-wal2json postgresql-17-decoderbufs postgresql-17-decoder-raw postgresql-17-mimeo postgresql-17-pg-fact-loader #postgresql-17-wal2mongo #postgresql-17-repmgr #postgresql-17-pg-bulkload
pg16: postgresql-16-pglogical postgresql-16-pglogical-ticker postgresql-16-pgl-ddl-deploy postgresql-16-pg-failover-slots postgresql-16-wal2json postgresql-16-wal2mongo postgresql-16-decoderbufs postgresql-16-decoder-raw postgresql-16-mimeo postgresql-16-pg-fact-loader postgresql-16-pg-bulkload #postgresql-16-repmgr
pg15: postgresql-15-pglogical postgresql-15-pglogical-ticker postgresql-15-pgl-ddl-deploy postgresql-15-pg-failover-slots postgresql-15-wal2json postgresql-15-wal2mongo postgresql-15-decoderbufs postgresql-15-decoder-raw postgresql-15-mimeo postgresql-15-pg-fact-loader postgresql-15-pg-bulkload #postgresql-15-repmgr
pg14: postgresql-14-pglogical postgresql-14-pglogical-ticker postgresql-14-pgl-ddl-deploy postgresql-14-pg-failover-slots postgresql-14-wal2json postgresql-14-wal2mongo postgresql-14-decoderbufs postgresql-14-decoder-raw postgresql-14-mimeo postgresql-14-pg-fact-loader postgresql-14-pg-bulkload #postgresql-14-repmgr
pg13: postgresql-13-pglogical postgresql-13-pglogical-ticker postgresql-13-pgl-ddl-deploy postgresql-13-pg-failover-slots postgresql-13-wal2json postgresql-13-wal2mongo postgresql-13-decoderbufs postgresql-13-decoder-raw postgresql-13-mimeo postgresql-13-pg-fact-loader postgresql-13-pg-bulkload #postgresql-13-repmgr
```


### Ubuntu 24.04 jammy Compatible (u22)

```yaml
pg17: postgresql-17-pglogical postgresql-17-pglogical-ticker postgresql-17-pgl-ddl-deploy postgresql-17-pg-failover-slots postgresql-17-wal2json postgresql-17-decoderbufs postgresql-17-decoder-raw postgresql-17-mimeo postgresql-17-pg-fact-loader #postgresql-17-wal2mongo #postgresql-17-repmgr #postgresql-17-pg-bulkload
pg16: postgresql-16-pglogical postgresql-16-pglogical-ticker postgresql-16-pgl-ddl-deploy postgresql-16-pg-failover-slots postgresql-16-wal2json postgresql-16-wal2mongo postgresql-16-decoderbufs postgresql-16-decoder-raw postgresql-16-mimeo postgresql-16-pg-fact-loader postgresql-16-pg-bulkload #postgresql-16-repmgr
pg15: postgresql-15-pglogical postgresql-15-pglogical-ticker postgresql-15-pgl-ddl-deploy postgresql-15-pg-failover-slots postgresql-15-wal2json postgresql-15-wal2mongo postgresql-15-decoderbufs postgresql-15-decoder-raw postgresql-15-mimeo postgresql-15-pg-fact-loader postgresql-15-pg-bulkload #postgresql-15-repmgr
pg14: postgresql-14-pglogical postgresql-14-pglogical-ticker postgresql-14-pgl-ddl-deploy postgresql-14-pg-failover-slots postgresql-14-wal2json postgresql-14-wal2mongo postgresql-14-decoderbufs postgresql-14-decoder-raw postgresql-14-mimeo postgresql-14-pg-fact-loader postgresql-14-pg-bulkload #postgresql-14-repmgr
pg13: postgresql-13-pglogical postgresql-13-pglogical-ticker postgresql-13-pgl-ddl-deploy postgresql-13-pg-failover-slots postgresql-13-wal2json postgresql-13-wal2mongo postgresql-13-decoderbufs postgresql-13-decoder-raw postgresql-13-mimeo postgresql-13-pg-fact-loader postgresql-13-pg-bulkload #postgresql-13-repmgr
```


### Ubuntu 24.04 noble Compatible (u24)

```yaml
pg17: postgresql-17-pglogical postgresql-17-pglogical-ticker postgresql-17-pgl-ddl-deploy postgresql-17-pg-failover-slots postgresql-17-wal2json postgresql-17-decoderbufs postgresql-17-decoder-raw postgresql-17-mimeo postgresql-17-pg-fact-loader #postgresql-17-wal2mongo #postgresql-17-repmgr #postgresql-17-pg-bulkload
pg16: postgresql-16-pglogical postgresql-16-pglogical-ticker postgresql-16-pgl-ddl-deploy postgresql-16-pg-failover-slots postgresql-16-wal2json postgresql-16-wal2mongo postgresql-16-decoderbufs postgresql-16-decoder-raw postgresql-16-mimeo postgresql-16-pg-fact-loader postgresql-16-pg-bulkload #postgresql-16-repmgr
pg15: postgresql-15-pglogical postgresql-15-pglogical-ticker postgresql-15-pgl-ddl-deploy postgresql-15-pg-failover-slots postgresql-15-wal2json postgresql-15-wal2mongo postgresql-15-decoderbufs postgresql-15-decoder-raw postgresql-15-mimeo postgresql-15-pg-fact-loader postgresql-15-pg-bulkload #postgresql-15-repmgr
pg14: postgresql-14-pglogical postgresql-14-pglogical-ticker postgresql-14-pgl-ddl-deploy postgresql-14-pg-failover-slots postgresql-14-wal2json postgresql-14-wal2mongo postgresql-14-decoderbufs postgresql-14-decoder-raw postgresql-14-mimeo postgresql-14-pg-fact-loader postgresql-14-pg-bulkload #postgresql-14-repmgr
pg13: postgresql-13-pglogical postgresql-13-pglogical-ticker postgresql-13-pgl-ddl-deploy postgresql-13-pg-failover-slots postgresql-13-wal2json postgresql-13-wal2mongo postgresql-13-decoderbufs postgresql-13-decoder-raw postgresql-13-mimeo postgresql-13-pg-fact-loader postgresql-13-pg-bulkload #postgresql-13-repmgr
```



--------

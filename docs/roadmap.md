# Roadmap

Extensions to be included and extensions will not be included

--------

## TODO

**TBD**:

- [pgai](https://github.com/timescale/pgai)
- [pg-rag](https://github.com/nearform/pg-rag)
- [onesparse](https://github.com/OneSparse/OneSparse)
- [synchdb](https://github.com/Hornetlabs/synchdb) (break deb packages)
- [orioledb](https://github.com/orioledb/orioledb)

**Recently Added**:

- documentdb
- [omnigres](https://omnigres.com/)
- [pg_documentdb_core](https://github.com/microsoft/documentdb/tree/main/pg_documentdb_core), and ferretdb
- [pg_tracing](https://github.com/DataDog/pg_tracing) 0.1.2
- [pg_curl](https://github.com/RekGRpth/pg_curl) 2.4
- [pgxicor](https://github.com/Florents-Tselai/pgxicor) 0.1.0
- [sparql](https://github.com/lacanoid/pgsparql) 1.0
- [pgjq](https://github.com/Florents-Tselai/pgJQ) 0.1.0
- [hashtypes](https://github.com/adjust/hashtypes/) 0.1.5
- [db_migrator](https://github.com/cybertec-postgresql/db_migrator) 1.0.0
- [vchord_bm25](https://github.com/tensorchord/VectorChord-bm25) (vchord_bm25) 0.1.0
- [prometheus_fdw](https://github.com/tembo-io/prometheus_fdw/) 0.2.1
- [pg_task](https://github.com/RekGRpth/pg_task)
- [pg_readme](https://github.com/bigsmoke/pg_readme)
- [vasco](https://github.com/Florents-Tselai/vasco) Maximal Information Coefficient (MIC) Extension for Postgres C GPL-3.0 FUNC
- [ddsketch](https://github.com/tvondra/ddsketch)
- [omnisketch](https://github.com/tvondra/omnisketch) PostgreSQL, C, omnisketch implemented as Postgres extension
- [data_historization](https://github.com/rodo/postgresql-data-historization) 1.1.0  PLPGSQL Script to historize data in partitionned table (plpgsql)
- [pg_upless](https://pgxn.org/dist/pg_upless/0.0.2/) PostgreSQL Extension to Detect Useless UPDATE
- [floatfile](https://github.com/pjungwir/floatfile) 1.3.1 C MIT
- [pg_duration](https://github.com/jkosh44/pg_duration/) 1.0.1 A PostgreSQL extension for a time based duration type.
- [pg_mooncake](https://github.com/Mooncake-Labs/pg_mooncake/releases/tag/v0.1.2) 0.1.2
- [pg_collection](https://github.com/aws/pgcollection) 0.9.0
- [pg_duckdb](https://github.com/duckdb/pg_duckdb/releases/tag/v0.3.1) 0.2.0
- [pg_bzip](https://github.com/steve-chavez/pg_bzip) v1.0.0
- increase citus release number to overwrite PGDG stuff


**Waiting on PostgreSQL 17 support**:

- [plprql](https://github.com/kaspermarstal/plprql): wait on pg17
- [hydra](https://github.com/hydradatabase/hydra): waiting on citus_columnar pg17 support
- [age](https://github.com/apache/age) missing EL packages
- pg_tde
- odbc_fdw
- jdbc_fdw
- db2_fdw
- mongo_fdw
- kafka_fdw
- wal2mongo
- [upid](https://github.com/carderne/upid): wait on pg17 https://github.com/carderne/upid/issues
- [pg_kaboom](https://github.com/pgguru/pg_kaboom/)
- logfmt
- wiltondb

**Waiting on License Update**:

- [jsonb_apply](https://github.com/Florents-Tselai/jsonb_apply) 0.1.0


**Porting missing RPMs from DEB**:

- mobilitydb
- rdkit
- hstore_pllua
- hstore_plluau
- debversion
- pg_rrule

**Porting missing DEBs from RPM**:

- pg_strom
- faker
- dbt2
- pg_top
- multicorn
- odbc_fdw
- jdbc_fdw
- tds_fdw
- db2_fdw
- sqlite_fdw
- pgbouncer_fdw
- mongo_fdw
- hdfs_fdw
- pg_dbms_metadata
- pg_dbms_lock
- pg_dbms_job


--------

## Candidate

- [dsef](https://github.com/ardentperf/dsef/)
- [pg_mustach](https://github.com/RekGRpth/pg_mustach) 1.0.0
- is_jsonb_valid https://github.com/furstenheim/is_jsonb_valid
- pg_kafka https://github.com/xstevens/pg_kafka
- pg_jieba https://github.com/jaiminpan/pg_jieba
- OneSparse https://github.com/OneSparse/OneSparse
- PipelineDB https://github.com/pipelinedb/pipelinedb
- SQL Firewall https://github.com/uptimejp/sql_firewall
- zcurve https://github.com/bmuratshin/zcurve
- PG dot net https://github.com/Brick-Abode/pldotnet/releases
- pg_scws: https://github.com/jaiminpan/pg_scws
- themsis: https://github.com/cossacklabs/pg_themis
- pgspeck https://github.com/johto/pgspeck
- lsm3 https://github.com/postgrespro/lsm3
- monq https://github.com/postgrespro/monq
- pg_badplan https://github.com/trustly/pg_badplan
- pg_recall https://github.com/mreithub/pg_recall
- pgfsm https://github.com/michelp/pgfsm
- pg_trgm pro https://github.com/postgrespro/pg_trgm_pro
- weighted_mean https://github.com/Kozea/weighted_mean
- kmeans https://github.com/umitanuki/kmeans-postgresql

Resource:

- [PGXN](https://pgxn.org/)
- [PGRPMS](https://git.postgresql.org/gitweb/?p=pgrpms.git;a=summary)
- [PGDEBS](https://salsa.debian.org/postgresql)
- [1000+ PG Extension Gist](https://gist.github.com/joelonsql/e5aa27f8cc9bd22b8999b7de8aee9d47)


--------

## Retired

- parquet_s3_fdw: retired due to too much duckdb better alternatives
- pg_tier: retired due to parquet_s3_fdw deps
- pg_mon: retired due to pg17 in-compatibility
- pg_search: retired due to moving to official release procedure
- pg_bm25: retired due to renaming to pg_search
- pg_analytics: retired due to moving to official release procedure, and once renaming to pg_lakehouse
- pg_lakehouse: retired due to renaming back to pg_analytics
- pg_sparse: retired due to merge into pgvector, and no longer maintained
- mysqlcompat: retire due to conflict func with higher version of PG
- pg_comparator: retired due to removing from PGDG repo 
- pg_proctab: retired due to covered by pgnodemx
- pg_statviz: broken deps and replaceable functionality
- [pg_net](https://github.com/supabase/pg_net)             : retired due to moving into PGDG repo
- [pg_tle](https://github.com/aws/pg_tle)                  : retired due to moving into PGDG repo
- [pg_bigm](https://github.com/pgbigm/pg_bigm)             : retired due to moving into PGDG repo
- [pgsql-http](https://github.com/pramsey/pgsql-http)      : retired due to moving into PGDG repo
- [pgsql-gzip](https://github.com/pramsey/pgsql-gzip)      : retired due to moving into PGDG repo
- [pg_dirtyread](https://github.com/df7cb/pg_dirtyread)    : retired due to moving into PGDG repo
- [pointcloud](https://github.com/pgpointcloud/pointcloud) : retired due to moving into PGDG repo
- pg_top: retired due to too much trouble
- pg_timeit: retired due incompatible on arm64
- vacuumlo & oid2name: binary command, actually they are not extensions
- pgdd: remove due to not actively maintained and legacy pgrx version


--------

## Not Planned

- pg_top: not ready due to cmake error
- pg_quack, we already have a pg_lakehouse
- pg_telemetry, we already have better observability
- pgx_ulid, https://github.com/pksunkara/pgx_ulid, already covered by pg_idkit (MIT, but RUST)
- embedding: obsolete
- zson https://github.com/postgrespro/zson MIT C (too old)
- pghydro https://github.com/pghydro/pghydro C GPL-2.0 6.6 (no makefile)
- pg_natural_sort_order https://github.com/Zeleo/pg_natural_sort_order (too old)
- pg_query_state https://github.com/postgrespro/pg_query_state
- pgsampler https://github.com/no0p/pgsampler
- pg_lz4 https://github.com/zilder/pg_lz4
- pg_amqp https://github.com/omniti-labs/pg_amqp
- tinyint https://github.com/umitanuki/tinyint-postgresql
- pg_blkchain https://github.com/blkchain/pg_blkchain
- hashtypes https://github.com/pandrewhk/hashtypes
- foreign_table_exposer https://github.com/komamitsu/foreign_table_exposer
- ldap_fdw https://github.com/guedes/ldap_fdw
- pg_backtrace https://github.com/postgrespro/pg_backtrace (only works on PG12)
- connection_limits https://github.com/tvondra/connection_limits
- fixeddecimal https://github.com/2ndQuadrant/fixeddecimal
- fuzzywuzzy https://github.com/hooopo/pg-fuzzywuzzy
- pg_paxos https://github.com/microsoft/pg_paxos

# SIM


> SIM: Protocol Simulation & heterogeneous DBMS Compatibility: Oracle, MSSQL, DB2, MySQL, Memcached, and Babelfish!
## Extensions


There are 12 available extensions in this category:

[`orafce`](/orafce) [`pgtt`](/pgtt) [`session_variable`](/session_variable) [`pg_statement_rollback`](/pg_statement_rollback) [`pg_dbms_metadata`](/pg_dbms_metadata) [`pg_dbms_lock`](/pg_dbms_lock) [`pg_dbms_job`](/pg_dbms_job) [`babelfishpg_common`](/babelfishpg_common) [`babelfishpg_tsql`](/babelfishpg_tsql) [`babelfishpg_tds`](/babelfishpg_tds) [`babelfishpg_money`](/babelfishpg_money) [`pgmemcache`](/pgmemcache)


| ID | Extension | Version | Package | License | RPM | DEB | Website | `Bin` | `LOAD` | `DYLIB` | `DDL` | Description |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:-------:|:-----:|:------:|:-------:|:-----:|-------------|
| 9000 | [orafce](/orafce) | 4.13 | [orafce](/orafce) | **<span class="tcblue">BSD-0</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/orafce/orafce) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Functions and operators that emulate a subset of functions and packages from the Oracle RDBMS |
| 9010 | [pgtt](/pgtt) | 4.0.0 | [pgtt](/pgtt) | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/darold/pgtt) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Extension to add Global Temporary Tables feature to PostgreSQL |
| 9020 | [session_variable](/session_variable) | 3.4 | [session_variable](/session_variable) | **<span class="tcwarn">GPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/splendiddata/session_variable) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Registration and manipulation of session variables and constants |
| 9030 | [pg_statement_rollback](/pg_statement_rollback) | 1.4 | [pg_statement_rollback](/pg_statement_rollback) | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/lzlabs/pg_statement_rollback) |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | Server side rollback at statement level for PostgreSQL like Oracle or DB2 |
| 9040 | [pg_dbms_metadata](/pg_dbms_metadata) | 1.0.0 | [pg_dbms_metadata](/pg_dbms_metadata) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** |  | [LINK](https://github.com/HexaCluster/pg_dbms_metadata) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Extension to add Oracle DBMS_METADATA compatibility to PostgreSQL |
| 9050 | [pg_dbms_lock](/pg_dbms_lock) | 1.0.0 | [pg_dbms_lock](/pg_dbms_lock) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** |  | [LINK](https://github.com/HexaCluster/pg_dbms_lock) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Extension to add Oracle DBMS_LOCK full compatibility to PostgreSQL |
| 9060 | [pg_dbms_job](/pg_dbms_job) | 1.5.0 | [pg_dbms_job](/pg_dbms_job) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** |  | [LINK](https://github.com/MigOpsRepos/pg_dbms_job) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Extension to add Oracle DBMS_JOB full compatibility to PostgreSQL |
| 9100 | [babelfishpg_common](/babelfishpg_common) | 3.3.3 | [babelfishpg_common](/babelfishpg_common) | **<span class="tccyan">Apache-2</span>** | **<span class="tcpurple">WILTON</span>** | **<span class="tcpurple">WILTON</span>** | [LINK](https://babelfishpg.org/) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | SQL Server Transact SQL Datatype Support |
| 9110 | [babelfishpg_tsql](/babelfishpg_tsql) | 3.3.1 | [babelfishpg_tsql](/babelfishpg_tsql) | **<span class="tccyan">Apache-2</span>** | **<span class="tcpurple">WILTON</span>** | **<span class="tcpurple">WILTON</span>** | [LINK](https://babelfishpg.org/) |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | SQL Server Transact SQL compatibility |
| 9120 | [babelfishpg_tds](/babelfishpg_tds) | 1.0.0 | [babelfishpg_tds](/babelfishpg_tds) | **<span class="tccyan">Apache-2</span>** | **<span class="tcpurple">WILTON</span>** | **<span class="tcpurple">WILTON</span>** | [LINK](https://babelfishpg.org/) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | SQL Server TDS protocol extension |
| 9130 | [babelfishpg_money](/babelfishpg_money) | 1.1.0 | [babelfishpg_money](/babelfishpg_money) | **<span class="tccyan">Apache-2</span>** | **<span class="tcpurple">WILTON</span>** | **<span class="tcpurple">WILTON</span>** | [LINK](https://babelfishpg.org/) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | SQL Server Money Data Type |
| 9200 | [pgmemcache](/pgmemcache) | 2.3.0 | [pgmemcache](/pgmemcache) | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/ohmu/pgmemcache) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | memcached interface |



```yaml
pg17: orafce pgtt session_variable pg_statement_rollback pgmemcache #pg_dbms_metadata #pg_dbms_lock #pg_dbms_job #babelfishpg_common #babelfishpg_tsql #babelfishpg_tds #babelfishpg_money
pg16: orafce pgtt session_variable pg_statement_rollback pgmemcache #pg_dbms_metadata #pg_dbms_lock #pg_dbms_job #babelfishpg_common #babelfishpg_tsql #babelfishpg_tds #babelfishpg_money
pg15: orafce pgtt session_variable pg_statement_rollback pgmemcache #pg_dbms_metadata #pg_dbms_lock #pg_dbms_job #babelfishpg_common #babelfishpg_tsql #babelfishpg_tds #babelfishpg_money
pg14: orafce pgtt session_variable pg_statement_rollback pgmemcache #pg_dbms_metadata #pg_dbms_lock #pg_dbms_job #babelfishpg_common #babelfishpg_tsql #babelfishpg_tds #babelfishpg_money
pg13: orafce pgtt session_variable pg_statement_rollback pgmemcache #pg_dbms_metadata #pg_dbms_lock #pg_dbms_job #babelfishpg_common #babelfishpg_tsql #babelfishpg_tds #babelfishpg_money
pg12: orafce pgtt session_variable pg_statement_rollback pgmemcache #pg_dbms_metadata #pg_dbms_lock #pg_dbms_job #babelfishpg_common #babelfishpg_tsql #babelfishpg_tds #babelfishpg_money
```



--------

## RPM Packages


| Package | Version | License | RPM | RPM Package | 17 | 16 | 15 | 14 | 13 | 12 | Description |
|---------|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|:--:|-------------|
| [orafce](/orafce) | 4.13 | **<span class="tcblue">BSD-0</span>** | **<span class="tccyan">PGDG</span>** | `orafce_$v*` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Functions and operators that emulate a subset of functions and packages from the Oracle RDBMS |
| [pgtt](/pgtt) | 4.0.0 | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | `pgtt_$v*` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Extension to add Global Temporary Tables feature to PostgreSQL |
| [session_variable](/session_variable) | 3.4 | **<span class="tcwarn">GPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `session_variable_$v*` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Registration and manipulation of session variables and constants |
| [pg_statement_rollback](/pg_statement_rollback) | 1.4 | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | `pg_statement_rollback_$v*` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Server side rollback at statement level for PostgreSQL like Oracle or DB2 |
| [pg_dbms_metadata](/pg_dbms_metadata) | 1.0.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pg_dbms_metadata_$v*` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Extension to add Oracle DBMS_METADATA compatibility to PostgreSQL |
| [pg_dbms_lock](/pg_dbms_lock) | 1.0.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pg_dbms_lock_$v*` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Extension to add Oracle DBMS_LOCK full compatibility to PostgreSQL |
| [pg_dbms_job](/pg_dbms_job) | 1.5.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pg_dbms_job_$v*` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Extension to add Oracle DBMS_JOB full compatibility to PostgreSQL |
| [babelfishpg_common](/babelfishpg_common) | 3.3.3 | **<span class="tccyan">Apache-2</span>** | **<span class="tcpurple">WILTON</span>** | `babelfishpg-common*` |  |  | <span class="tcblue">✔</span> |  |  |  | SQL Server Transact SQL Datatype Support |
| [babelfishpg_tsql](/babelfishpg_tsql) | 3.3.1 | **<span class="tccyan">Apache-2</span>** | **<span class="tcpurple">WILTON</span>** | `babelfishpg-tsql*` |  |  | <span class="tcblue">✔</span> |  |  |  | SQL Server Transact SQL compatibility |
| [babelfishpg_tds](/babelfishpg_tds) | 1.0.0 | **<span class="tccyan">Apache-2</span>** | **<span class="tcpurple">WILTON</span>** | `babelfishpg-tds*` |  |  | <span class="tcblue">✔</span> |  |  |  | SQL Server TDS protocol extension |
| [babelfishpg_money](/babelfishpg_money) | 1.1.0 | **<span class="tccyan">Apache-2</span>** | **<span class="tcpurple">WILTON</span>** | `babelfishpg-money*` |  |  | <span class="tcblue">✔</span> |  |  |  | SQL Server Money Data Type |
| [pgmemcache](/pgmemcache) | 2.3.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `pgmemcache_$v*` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | memcached interface |



```yaml
pg17: orafce_17* pgtt_17* session_variable_17* pg_statement_rollback_17* pg_dbms_metadata_17* pg_dbms_lock_17* pgmemcache_17* #pg_dbms_job_17* #babelfishpg-common* #babelfishpg-tsql* #babelfishpg-tds* #babelfishpg-money*
pg16: orafce_16* pgtt_16* session_variable_16* pg_statement_rollback_16* pg_dbms_metadata_16* pg_dbms_lock_16* pgmemcache_16* #pg_dbms_job_16* #babelfishpg-common* #babelfishpg-tsql* #babelfishpg-tds* #babelfishpg-money*
pg15: orafce_15* pgtt_15* session_variable_15* pg_statement_rollback_15* pg_dbms_metadata_15* pg_dbms_lock_15* pgmemcache_15* #pg_dbms_job_15* #babelfishpg-common* #babelfishpg-tsql* #babelfishpg-tds* #babelfishpg-money*
pg14: orafce_14* pgtt_14* session_variable_14* pg_statement_rollback_14* pg_dbms_metadata_14* pg_dbms_lock_14* pgmemcache_14* #pg_dbms_job_14* #babelfishpg-common* #babelfishpg-tsql* #babelfishpg-tds* #babelfishpg-money*
pg13: orafce_13* pgtt_13* session_variable_13* pg_statement_rollback_13* pg_dbms_metadata_13* pg_dbms_lock_13* pgmemcache_13* #pg_dbms_job_13* #babelfishpg-common* #babelfishpg-tsql* #babelfishpg-tds* #babelfishpg-money*
pg12: orafce_12* pgtt_12* session_variable_12* pg_statement_rollback_12* pg_dbms_metadata_12* pg_dbms_lock_12* pgmemcache_12* #pg_dbms_job_12* #babelfishpg-common* #babelfishpg-tsql* #babelfishpg-tds* #babelfishpg-money*
```



--------

## DEB Packages


| Package | Version | License | DEB | DEB Package | 17 | 16 | 15 | 14 | 13 | 12 | Description |
|---------|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|:--:|-------------|
| [orafce](/orafce) | 4.13 | **<span class="tcblue">BSD-0</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-orafce` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Functions and operators that emulate a subset of functions and packages from the Oracle RDBMS |
| [pgtt](/pgtt) | 4.0.0 | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pgtt` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Extension to add Global Temporary Tables feature to PostgreSQL |
| [session_variable](/session_variable) | 3.4 | **<span class="tcwarn">GPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-session-variable` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Registration and manipulation of session variables and constants |
| [pg_statement_rollback](/pg_statement_rollback) | 1.4 | **<span class="tcblue">ISC</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-statement-rollback` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Server side rollback at statement level for PostgreSQL like Oracle or DB2 |
| [babelfishpg_common](/babelfishpg_common) | 3.3.3 | **<span class="tccyan">Apache-2</span>** | **<span class="tcpurple">WILTON</span>** | `babelfishpg-common` |  |  | <span class="tcblue">✔</span> |  |  |  | SQL Server Transact SQL Datatype Support |
| [babelfishpg_tsql](/babelfishpg_tsql) | 3.3.1 | **<span class="tccyan">Apache-2</span>** | **<span class="tcpurple">WILTON</span>** | `babelfishpg-tsql` |  |  | <span class="tcblue">✔</span> |  |  |  | SQL Server Transact SQL compatibility |
| [babelfishpg_tds](/babelfishpg_tds) | 1.0.0 | **<span class="tccyan">Apache-2</span>** | **<span class="tcpurple">WILTON</span>** | `babelfishpg-tds` |  |  | <span class="tcblue">✔</span> |  |  |  | SQL Server TDS protocol extension |
| [babelfishpg_money](/babelfishpg_money) | 1.1.0 | **<span class="tccyan">Apache-2</span>** | **<span class="tcpurple">WILTON</span>** | `babelfishpg-money` |  |  | <span class="tcblue">✔</span> |  |  |  | SQL Server Money Data Type |
| [pgmemcache](/pgmemcache) | 2.3.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pgmemcache` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | memcached interface |



```yaml
pg17: orafce_17* pgtt_17* session_variable_17* pg_statement_rollback_17* pg_dbms_metadata_17* pg_dbms_lock_17* pgmemcache_17* #pg_dbms_job_17* #babelfishpg-common* #babelfishpg-tsql* #babelfishpg-tds* #babelfishpg-money*
pg16: orafce_16* pgtt_16* session_variable_16* pg_statement_rollback_16* pg_dbms_metadata_16* pg_dbms_lock_16* pgmemcache_16* #pg_dbms_job_16* #babelfishpg-common* #babelfishpg-tsql* #babelfishpg-tds* #babelfishpg-money*
pg15: orafce_15* pgtt_15* session_variable_15* pg_statement_rollback_15* pg_dbms_metadata_15* pg_dbms_lock_15* pgmemcache_15* #pg_dbms_job_15* #babelfishpg-common* #babelfishpg-tsql* #babelfishpg-tds* #babelfishpg-money*
pg14: orafce_14* pgtt_14* session_variable_14* pg_statement_rollback_14* pg_dbms_metadata_14* pg_dbms_lock_14* pgmemcache_14* #pg_dbms_job_14* #babelfishpg-common* #babelfishpg-tsql* #babelfishpg-tds* #babelfishpg-money*
pg13: orafce_13* pgtt_13* session_variable_13* pg_statement_rollback_13* pg_dbms_metadata_13* pg_dbms_lock_13* pgmemcache_13* #pg_dbms_job_13* #babelfishpg-common* #babelfishpg-tsql* #babelfishpg-tds* #babelfishpg-money*
pg12: orafce_12* pgtt_12* session_variable_12* pg_statement_rollback_12* pg_dbms_metadata_12* pg_dbms_lock_12* pgmemcache_12* #pg_dbms_job_12* #babelfishpg-common* #babelfishpg-tsql* #babelfishpg-tds* #babelfishpg-money*
```



--------


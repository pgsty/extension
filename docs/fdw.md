# FDW


> FDW: Wrappers & Multicorn for FDW Development, Access other DBMS: MySQL, Mongo, SQLite, MSSQL, Oracle, HDFS, DB2,...
## Extensions


There are 22 available extensions in this category:

[`wrappers`](/wrappers) [`multicorn`](/multicorn) [`odbc_fdw`](/odbc_fdw) [`jdbc_fdw`](/jdbc_fdw) [`pgspider_ext`](/pgspider_ext) [`mysql_fdw`](/mysql_fdw) [`oracle_fdw`](/oracle_fdw) [`tds_fdw`](/tds_fdw) [`db2_fdw`](/db2_fdw) [`sqlite_fdw`](/sqlite_fdw) [`pgbouncer_fdw`](/pgbouncer_fdw) [`mongo_fdw`](/mongo_fdw) [`redis_fdw`](/redis_fdw) [`redis`](/redis) [`kafka_fdw`](/kafka_fdw) [`hdfs_fdw`](/hdfs_fdw) [`firebird_fdw`](/firebird_fdw) [`aws_s3`](/aws_s3) [`log_fdw`](/log_fdw) [`dblink`](/dblink) [`file_fdw`](/file_fdw) [`postgres_fdw`](/postgres_fdw)


| ID | Extension | Version | Package | License | RPM | DEB | Website | `Bin` | `LOAD` | `DYLIB` | `DDL` | Description |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:-------:|:-----:|:------:|:-------:|:-----:|-------------|
| 8500 | [wrappers](/wrappers) | 0.4.5 | [wrappers](/wrappers) | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/supabase/wrappers) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Foreign data wrappers developed by Supabase |
| 8510 | [multicorn](/multicorn) | 3.0 | [multicorn](/multicorn) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** |  | [LINK](https://github.com/pgsql-io/multicorn2) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Fetch foreign data in Python in your PostgreSQL server. |
| 8520 | [odbc_fdw](/odbc_fdw) | 0.5.1 | [odbc_fdw](/odbc_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** |  | [LINK](https://github.com/CartoDB/odbc_fdw) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Foreign data wrapper for accessing remote databases using ODBC |
| 8530 | [jdbc_fdw](/jdbc_fdw) | 1.2 | [jdbc_fdw](/jdbc_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** |  | [LINK](https://github.com/pgspider/jdbc_fdw) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | foreign-data wrapper for remote servers available over JDBC |
| 8540 | [pgspider_ext](/pgspider_ext) | 1.3.0 | [pgspider_ext](/pgspider_ext) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/pgspider/pgspider_ext) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | foreign-data wrapper for remote PGSpider servers |
| 8600 | [mysql_fdw](/mysql_fdw) | 2.9.2 | [mysql_fdw](/mysql_fdw) | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/EnterpriseDB/mysql_fdw) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Foreign data wrapper for querying a MySQL server |
| 8610 | [oracle_fdw](/oracle_fdw) | 2.7.0 | [oracle_fdw](/oracle_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/laurenz/oracle_fdw) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | foreign data wrapper for Oracle access |
| 8620 | [tds_fdw](/tds_fdw) | 2.0.4 | [tds_fdw](/tds_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/tds-fdw/tds_fdw) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Foreign data wrapper for querying a TDS database (Sybase or Microsoft SQL Server) |
| 8630 | [db2_fdw](/db2_fdw) | 6.0.1 | [db2_fdw](/db2_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** |  | [LINK](https://github.com/wolfgangbrandl/db2_fdw) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | foreign data wrapper for DB2 access |
| 8640 | [sqlite_fdw](/sqlite_fdw) | 2.5.0 | [sqlite_fdw](/sqlite_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/pgspider/sqlite_fdw) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | SQLite Foreign Data Wrapper |
| 8650 | [pgbouncer_fdw](/pgbouncer_fdw) | 1.3.0 | [pgbouncer_fdw](/pgbouncer_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** |  | [LINK](https://github.com/CrunchyData/pgbouncer_fdw) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Extension for querying PgBouncer stats from normal SQL views & running pgbouncer commands from normal SQL functions |
| 8700 | [mongo_fdw](/mongo_fdw) | 1.1 | [mongo_fdw](/mongo_fdw) | **<span class="tcwarn">LGPLv3</span>** | **<span class="tccyan">PGDG</span>** |  | [LINK](https://github.com/EnterpriseDB/mongo_fdw) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | foreign data wrapper for MongoDB access |
| 8710 | [redis_fdw](/redis_fdw) | 1.0 | [redis_fdw](/redis_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/pg-redis-fdw/redis_fdw) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Foreign data wrapper for querying a Redis server |
| 8720 | [redis](/redis) | 0.0.1 | [pg_redis_pubsub](/redis) | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/brettlaforge/pg_redis_pubsub) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Send redis pub/sub messages to Redis from PostgreSQL Directly |
| 8730 | [kafka_fdw](/kafka_fdw) | 0.0.3 | [kafka_fdw](/kafka_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/adjust/kafka_fdw) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | kafka Foreign Data Wrapper for CSV formatted messages |
| 8740 | [hdfs_fdw](/hdfs_fdw) | 2.3.2 | [hdfs_fdw](/hdfs_fdw) | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** |  | [LINK](https://github.com/EnterpriseDB/hdfs_fdw) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | foreign-data wrapper for remote hdfs servers |
| 8750 | [firebird_fdw](/firebird_fdw) | 1.4.0 | [firebird_fdw](/firebird_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/ibarwick/firebird_fdw) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Foreign data wrapper for Firebird |
| 8800 | [aws_s3](/aws_s3) | 0.0.1 | [aws_s3](/aws_s3) | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/chimpler/postgres-aws-s3) |  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | aws_s3 postgres extension to import/export data from/to s3 |
| 8810 | [log_fdw](/log_fdw) | 1.4 | [log_fdw](/log_fdw) | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/aws/postgresql-logfdw) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | foreign-data wrapper for Postgres log file access |
| 8970 | [dblink](/dblink) | 1.2 | [dblink](/dblink) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | **<span class="tcblue">CONTRIB</span>** | [LINK](https://www.postgresql.org/docs/current/dblink.html) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | connect to other PostgreSQL databases from within a database |
| 8980 | [file_fdw](/file_fdw) | 1.0 | [file_fdw](/file_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | **<span class="tcblue">CONTRIB</span>** | [LINK](https://www.postgresql.org/docs/current/file-fdw.html) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | foreign-data wrapper for flat file access |
| 8990 | [postgres_fdw](/postgres_fdw) | 1.1 | [postgres_fdw](/postgres_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | **<span class="tcblue">CONTRIB</span>** | [LINK](https://www.postgresql.org/docs/current/postgres-fdw.html) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | foreign-data wrapper for remote PostgreSQL servers |



### RHEL 8 Compatible (el8)

```yaml
pg17: wrappers multicorn odbc_fdw pgspider_ext mysql_fdw tds_fdw sqlite_fdw pgbouncer_fdw redis_fdw pg_redis_pubsub hdfs_fdw firebird_fdw aws_s3 log_fdw #jdbc_fdw #oracle_fdw #db2_fdw #mongo_fdw #kafka_fdw
pg16: wrappers multicorn odbc_fdw jdbc_fdw pgspider_ext mysql_fdw tds_fdw sqlite_fdw pgbouncer_fdw mongo_fdw redis_fdw pg_redis_pubsub kafka_fdw hdfs_fdw firebird_fdw aws_s3 log_fdw #oracle_fdw #db2_fdw
pg15: wrappers multicorn odbc_fdw jdbc_fdw pgspider_ext mysql_fdw tds_fdw sqlite_fdw pgbouncer_fdw mongo_fdw redis_fdw pg_redis_pubsub kafka_fdw hdfs_fdw firebird_fdw aws_s3 log_fdw #oracle_fdw #db2_fdw
pg14: wrappers multicorn odbc_fdw jdbc_fdw mysql_fdw tds_fdw sqlite_fdw pgbouncer_fdw mongo_fdw redis_fdw pg_redis_pubsub kafka_fdw hdfs_fdw firebird_fdw aws_s3 log_fdw #pgspider_ext #oracle_fdw #db2_fdw
pg13: multicorn odbc_fdw jdbc_fdw mysql_fdw tds_fdw sqlite_fdw pgbouncer_fdw mongo_fdw redis_fdw pg_redis_pubsub kafka_fdw hdfs_fdw firebird_fdw aws_s3 #wrappers #pgspider_ext #oracle_fdw #db2_fdw #log_fdw
```


### RHEL 9 Compatible (el9)

```yaml
pg17: wrappers multicorn odbc_fdw pgspider_ext mysql_fdw tds_fdw sqlite_fdw pgbouncer_fdw redis_fdw pg_redis_pubsub hdfs_fdw firebird_fdw aws_s3 log_fdw #jdbc_fdw #oracle_fdw #db2_fdw #mongo_fdw #kafka_fdw
pg16: wrappers multicorn odbc_fdw jdbc_fdw pgspider_ext mysql_fdw tds_fdw sqlite_fdw pgbouncer_fdw mongo_fdw redis_fdw pg_redis_pubsub kafka_fdw hdfs_fdw firebird_fdw aws_s3 log_fdw #oracle_fdw #db2_fdw
pg15: wrappers multicorn odbc_fdw jdbc_fdw pgspider_ext mysql_fdw tds_fdw sqlite_fdw pgbouncer_fdw mongo_fdw redis_fdw pg_redis_pubsub kafka_fdw hdfs_fdw firebird_fdw aws_s3 log_fdw #oracle_fdw #db2_fdw
pg14: wrappers multicorn odbc_fdw jdbc_fdw mysql_fdw tds_fdw sqlite_fdw pgbouncer_fdw mongo_fdw redis_fdw pg_redis_pubsub kafka_fdw hdfs_fdw firebird_fdw aws_s3 log_fdw #pgspider_ext #oracle_fdw #db2_fdw
pg13: multicorn odbc_fdw jdbc_fdw mysql_fdw tds_fdw sqlite_fdw pgbouncer_fdw mongo_fdw redis_fdw pg_redis_pubsub kafka_fdw hdfs_fdw firebird_fdw aws_s3 #wrappers #pgspider_ext #oracle_fdw #db2_fdw #log_fdw
```


### Debian 12 bookworm Compatible (d12)

```yaml
pg17: wrappers pgspider_ext mysql_fdw tds_fdw redis_fdw pg_redis_pubsub firebird_fdw aws_s3 log_fdw #multicorn #odbc_fdw #jdbc_fdw #oracle_fdw #db2_fdw #sqlite_fdw #pgbouncer_fdw #mongo_fdw #kafka_fdw #hdfs_fdw
pg16: wrappers pgspider_ext mysql_fdw tds_fdw sqlite_fdw redis_fdw pg_redis_pubsub kafka_fdw firebird_fdw aws_s3 log_fdw #multicorn #odbc_fdw #jdbc_fdw #oracle_fdw #db2_fdw #pgbouncer_fdw #mongo_fdw #hdfs_fdw
pg15: wrappers pgspider_ext mysql_fdw tds_fdw sqlite_fdw redis_fdw pg_redis_pubsub kafka_fdw firebird_fdw aws_s3 log_fdw #multicorn #odbc_fdw #jdbc_fdw #oracle_fdw #db2_fdw #pgbouncer_fdw #mongo_fdw #hdfs_fdw
pg14: wrappers mysql_fdw tds_fdw sqlite_fdw redis_fdw pg_redis_pubsub kafka_fdw firebird_fdw aws_s3 log_fdw #multicorn #odbc_fdw #jdbc_fdw #pgspider_ext #oracle_fdw #db2_fdw #pgbouncer_fdw #mongo_fdw #hdfs_fdw
pg13: mysql_fdw tds_fdw sqlite_fdw redis_fdw pg_redis_pubsub kafka_fdw firebird_fdw aws_s3 #wrappers #multicorn #odbc_fdw #jdbc_fdw #pgspider_ext #oracle_fdw #db2_fdw #pgbouncer_fdw #mongo_fdw #hdfs_fdw #log_fdw
```


### Ubuntu 24.04 jammy Compatible (u22)

```yaml
pg17: wrappers pgspider_ext mysql_fdw tds_fdw redis_fdw pg_redis_pubsub firebird_fdw aws_s3 log_fdw #multicorn #odbc_fdw #jdbc_fdw #oracle_fdw #db2_fdw #sqlite_fdw #pgbouncer_fdw #mongo_fdw #kafka_fdw #hdfs_fdw
pg16: wrappers pgspider_ext mysql_fdw tds_fdw sqlite_fdw redis_fdw pg_redis_pubsub kafka_fdw firebird_fdw aws_s3 log_fdw #multicorn #odbc_fdw #jdbc_fdw #oracle_fdw #db2_fdw #pgbouncer_fdw #mongo_fdw #hdfs_fdw
pg15: wrappers pgspider_ext mysql_fdw tds_fdw sqlite_fdw redis_fdw pg_redis_pubsub kafka_fdw firebird_fdw aws_s3 log_fdw #multicorn #odbc_fdw #jdbc_fdw #oracle_fdw #db2_fdw #pgbouncer_fdw #mongo_fdw #hdfs_fdw
pg14: wrappers mysql_fdw tds_fdw sqlite_fdw redis_fdw pg_redis_pubsub kafka_fdw firebird_fdw aws_s3 log_fdw #multicorn #odbc_fdw #jdbc_fdw #pgspider_ext #oracle_fdw #db2_fdw #pgbouncer_fdw #mongo_fdw #hdfs_fdw
pg13: mysql_fdw tds_fdw sqlite_fdw redis_fdw pg_redis_pubsub kafka_fdw firebird_fdw aws_s3 #wrappers #multicorn #odbc_fdw #jdbc_fdw #pgspider_ext #oracle_fdw #db2_fdw #pgbouncer_fdw #mongo_fdw #hdfs_fdw #log_fdw
```


### Ubuntu 24.04 noble Compatible (u24)

```yaml
pg17: wrappers pgspider_ext mysql_fdw tds_fdw redis_fdw pg_redis_pubsub firebird_fdw aws_s3 log_fdw #multicorn #odbc_fdw #jdbc_fdw #oracle_fdw #db2_fdw #sqlite_fdw #pgbouncer_fdw #mongo_fdw #kafka_fdw #hdfs_fdw
pg16: wrappers pgspider_ext mysql_fdw tds_fdw sqlite_fdw redis_fdw pg_redis_pubsub kafka_fdw firebird_fdw aws_s3 log_fdw #multicorn #odbc_fdw #jdbc_fdw #oracle_fdw #db2_fdw #pgbouncer_fdw #mongo_fdw #hdfs_fdw
pg15: wrappers pgspider_ext mysql_fdw tds_fdw sqlite_fdw redis_fdw pg_redis_pubsub kafka_fdw firebird_fdw aws_s3 log_fdw #multicorn #odbc_fdw #jdbc_fdw #oracle_fdw #db2_fdw #pgbouncer_fdw #mongo_fdw #hdfs_fdw
pg14: wrappers mysql_fdw tds_fdw sqlite_fdw redis_fdw pg_redis_pubsub kafka_fdw firebird_fdw aws_s3 log_fdw #multicorn #odbc_fdw #jdbc_fdw #pgspider_ext #oracle_fdw #db2_fdw #pgbouncer_fdw #mongo_fdw #hdfs_fdw
pg13: mysql_fdw tds_fdw sqlite_fdw redis_fdw pg_redis_pubsub kafka_fdw firebird_fdw aws_s3 #wrappers #multicorn #odbc_fdw #jdbc_fdw #pgspider_ext #oracle_fdw #db2_fdw #pgbouncer_fdw #mongo_fdw #hdfs_fdw #log_fdw
```



--------

## RPM Packages


| Package | Version | License | RPM | RPM Package | 17 | 16 | 15 | 14 | 13 | Description |
|---------|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|-------------|
| [wrappers](/wrappers) | 0.4.4 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `wrappers_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | Foreign data wrappers developed by Supabase |
| [multicorn](/multicorn) | 3.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `multicorn2_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Fetch foreign data in Python in your PostgreSQL server. |
| [odbc_fdw](/odbc_fdw) | 0.5.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `odbc_fdw_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Foreign data wrapper for accessing remote databases using ODBC |
| [jdbc_fdw](/jdbc_fdw) | 1.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `jdbc_fdw_$v*` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | foreign-data wrapper for remote servers available over JDBC |
| [pgspider_ext](/pgspider_ext) | 1.3.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pgspider_ext_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |  | foreign-data wrapper for remote PGSpider servers |
| [mysql_fdw](/mysql_fdw) | 2.9.2 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `mysql_fdw_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Foreign data wrapper for querying a MySQL server |
| [oracle_fdw](/oracle_fdw) | 2.7.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `oracle_fdw_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | foreign data wrapper for Oracle access |
| [tds_fdw](/tds_fdw) | 2.0.4 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `tds_fdw_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Foreign data wrapper for querying a TDS database (Sybase or Microsoft SQL Server) |
| [db2_fdw](/db2_fdw) | 6.0.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `db2_fdw_$v*` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | foreign data wrapper for DB2 access |
| [sqlite_fdw](/sqlite_fdw) | 2.5.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `sqlite_fdw_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | SQLite Foreign Data Wrapper |
| [pgbouncer_fdw](/pgbouncer_fdw) | 1.3.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pgbouncer_fdw_$v` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Extension for querying PgBouncer stats from normal SQL views & running pgbouncer commands from normal SQL functions |
| [mongo_fdw](/mongo_fdw) | 1.1 | **<span class="tcwarn">LGPLv3</span>** | **<span class="tccyan">PGDG</span>** | `mongo_fdw_$v*` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | foreign data wrapper for MongoDB access |
| [redis_fdw](/redis_fdw) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `redis_fdw_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Foreign data wrapper for querying a Redis server |
| [pg_redis_pubsub](/redis) | 0.0.1 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_redis_pubsub_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Send redis pub/sub messages to Redis from PostgreSQL Directly |
| [kafka_fdw](/kafka_fdw) | 0.0.3 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `kafka_fdw_$v` |  | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | kafka Foreign Data Wrapper for CSV formatted messages |
| [hdfs_fdw](/hdfs_fdw) | 2.3.2 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `hdfs_fdw_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | foreign-data wrapper for remote hdfs servers |
| [firebird_fdw](/firebird_fdw) | 1.4.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `firebird_fdw_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Foreign data wrapper for Firebird |
| [aws_s3](/aws_s3) | 0.0.1 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `aws_s3_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | aws_s3 postgres extension to import/export data from/to s3 |
| [log_fdw](/log_fdw) | 1.4 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `log_fdw_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | foreign-data wrapper for Postgres log file access |
| [dblink](/dblink) | 1.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql$v-contrib` | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | connect to other PostgreSQL databases from within a database |
| [file_fdw](/file_fdw) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql$v-contrib` | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | foreign-data wrapper for flat file access |
| [postgres_fdw](/postgres_fdw) | 1.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql$v-contrib` | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | foreign-data wrapper for remote PostgreSQL servers |



### RHEL 8 Compatible (el8)

```yaml
pg17: wrappers_17 multicorn2_17* odbc_fdw_17* pgspider_ext_17* mysql_fdw_17* tds_fdw_17* sqlite_fdw_17* pgbouncer_fdw_17 redis_fdw_17* pg_redis_pubsub_17* hdfs_fdw_17* firebird_fdw_17 aws_s3_17 log_fdw_17* #jdbc_fdw_17* #oracle_fdw_17* #db2_fdw_17* #mongo_fdw_17* #kafka_fdw_17
pg16: wrappers_16 multicorn2_16* odbc_fdw_16* jdbc_fdw_16* pgspider_ext_16* mysql_fdw_16* tds_fdw_16* sqlite_fdw_16* pgbouncer_fdw_16 mongo_fdw_16* redis_fdw_16* pg_redis_pubsub_16* kafka_fdw_16 hdfs_fdw_16* firebird_fdw_16 aws_s3_16 log_fdw_16* #oracle_fdw_16* #db2_fdw_16*
pg15: wrappers_15 multicorn2_15* odbc_fdw_15* jdbc_fdw_15* pgspider_ext_15* mysql_fdw_15* tds_fdw_15* sqlite_fdw_15* pgbouncer_fdw_15 mongo_fdw_15* redis_fdw_15* pg_redis_pubsub_15* kafka_fdw_15 hdfs_fdw_15* firebird_fdw_15 aws_s3_15 log_fdw_15* #oracle_fdw_15* #db2_fdw_15*
pg14: wrappers_14 multicorn2_14* odbc_fdw_14* jdbc_fdw_14* mysql_fdw_14* tds_fdw_14* sqlite_fdw_14* pgbouncer_fdw_14 mongo_fdw_14* redis_fdw_14* pg_redis_pubsub_14* kafka_fdw_14 hdfs_fdw_14* firebird_fdw_14 aws_s3_14 log_fdw_14* #pgspider_ext_14* #oracle_fdw_14* #db2_fdw_14*
pg13: multicorn2_13* odbc_fdw_13* jdbc_fdw_13* mysql_fdw_13* tds_fdw_13* sqlite_fdw_13* pgbouncer_fdw_13 mongo_fdw_13* redis_fdw_13* pg_redis_pubsub_13* kafka_fdw_13 hdfs_fdw_13* firebird_fdw_13 aws_s3_13 #wrappers_13 #pgspider_ext_13* #oracle_fdw_13* #db2_fdw_13* #log_fdw_13*
```


### RHEL 9 Compatible (el9)

```yaml
pg17: wrappers_17 multicorn2_17* odbc_fdw_17* pgspider_ext_17* mysql_fdw_17* tds_fdw_17* sqlite_fdw_17* pgbouncer_fdw_17 redis_fdw_17* pg_redis_pubsub_17* hdfs_fdw_17* firebird_fdw_17 aws_s3_17 log_fdw_17* #jdbc_fdw_17* #oracle_fdw_17* #db2_fdw_17* #mongo_fdw_17* #kafka_fdw_17
pg16: wrappers_16 multicorn2_16* odbc_fdw_16* jdbc_fdw_16* pgspider_ext_16* mysql_fdw_16* tds_fdw_16* sqlite_fdw_16* pgbouncer_fdw_16 mongo_fdw_16* redis_fdw_16* pg_redis_pubsub_16* kafka_fdw_16 hdfs_fdw_16* firebird_fdw_16 aws_s3_16 log_fdw_16* #oracle_fdw_16* #db2_fdw_16*
pg15: wrappers_15 multicorn2_15* odbc_fdw_15* jdbc_fdw_15* pgspider_ext_15* mysql_fdw_15* tds_fdw_15* sqlite_fdw_15* pgbouncer_fdw_15 mongo_fdw_15* redis_fdw_15* pg_redis_pubsub_15* kafka_fdw_15 hdfs_fdw_15* firebird_fdw_15 aws_s3_15 log_fdw_15* #oracle_fdw_15* #db2_fdw_15*
pg14: wrappers_14 multicorn2_14* odbc_fdw_14* jdbc_fdw_14* mysql_fdw_14* tds_fdw_14* sqlite_fdw_14* pgbouncer_fdw_14 mongo_fdw_14* redis_fdw_14* pg_redis_pubsub_14* kafka_fdw_14 hdfs_fdw_14* firebird_fdw_14 aws_s3_14 log_fdw_14* #pgspider_ext_14* #oracle_fdw_14* #db2_fdw_14*
pg13: multicorn2_13* odbc_fdw_13* jdbc_fdw_13* mysql_fdw_13* tds_fdw_13* sqlite_fdw_13* pgbouncer_fdw_13 mongo_fdw_13* redis_fdw_13* pg_redis_pubsub_13* kafka_fdw_13 hdfs_fdw_13* firebird_fdw_13 aws_s3_13 #wrappers_13 #pgspider_ext_13* #oracle_fdw_13* #db2_fdw_13* #log_fdw_13*
```



--------

## DEB Packages


| Package | Version | License | DEB | DEB Package | 17 | 16 | 15 | 14 | 13 | Description |
|---------|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|-------------|
| [wrappers](/wrappers) | 0.4.4 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-wrappers` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | Foreign data wrappers developed by Supabase |
| [pgspider_ext](/pgspider_ext) | 1.3.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pgspider-ext` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  | foreign-data wrapper for remote PGSpider servers |
| [mysql_fdw](/mysql_fdw) | 2.9.2 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-mysql-fdw` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Foreign data wrapper for querying a MySQL server |
| [oracle_fdw](/oracle_fdw) | 2.7.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-oracle-fdw` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | foreign data wrapper for Oracle access |
| [tds_fdw](/tds_fdw) | 2.0.4 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-tds-fdw` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Foreign data wrapper for querying a TDS database (Sybase or Microsoft SQL Server) |
| [sqlite_fdw](/sqlite_fdw) | 2.5.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-sqlite-fdw` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | SQLite Foreign Data Wrapper |
| [redis_fdw](/redis_fdw) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-redis-fdw` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Foreign data wrapper for querying a Redis server |
| [pg_redis_pubsub](/redis) | 0.0.1 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-redis-pubsub` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Send redis pub/sub messages to Redis from PostgreSQL Directly |
| [kafka_fdw](/kafka_fdw) | 0.0.3 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-kafka-fdw` |  | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | kafka Foreign Data Wrapper for CSV formatted messages |
| [firebird_fdw](/firebird_fdw) | 1.4.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-firebird-fdw` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Foreign data wrapper for Firebird |
| [aws_s3](/aws_s3) | 0.0.1 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-aws-s3` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | aws_s3 postgres extension to import/export data from/to s3 |
| [log_fdw](/log_fdw) | 1.4 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-log-fdw` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | foreign-data wrapper for Postgres log file access |
| [dblink](/dblink) | 1.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql-$v` | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | connect to other PostgreSQL databases from within a database |
| [file_fdw](/file_fdw) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql-$v` | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | foreign-data wrapper for flat file access |
| [postgres_fdw](/postgres_fdw) | 1.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql-$v` | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | foreign-data wrapper for remote PostgreSQL servers |



### Debian 12 bookworm Compatible (d12)

```yaml
pg17: postgresql-17-wrappers postgresql-17-pgspider-ext postgresql-17-mysql-fdw postgresql-17-tds-fdw postgresql-17-redis-fdw postgresql-17-pg-redis-pubsub postgresql-17-firebird-fdw postgresql-17-aws-s3 postgresql-17-log-fdw # #postgresql-17-oracle-fdw #postgresql-17-sqlite-fdw #postgresql-17-kafka-fdw
pg16: postgresql-16-wrappers postgresql-16-pgspider-ext postgresql-16-mysql-fdw postgresql-16-tds-fdw postgresql-16-sqlite-fdw postgresql-16-redis-fdw postgresql-16-pg-redis-pubsub postgresql-16-kafka-fdw postgresql-16-firebird-fdw postgresql-16-aws-s3 postgresql-16-log-fdw # #postgresql-16-oracle-fdw
pg15: postgresql-15-wrappers postgresql-15-pgspider-ext postgresql-15-mysql-fdw postgresql-15-tds-fdw postgresql-15-sqlite-fdw postgresql-15-redis-fdw postgresql-15-pg-redis-pubsub postgresql-15-kafka-fdw postgresql-15-firebird-fdw postgresql-15-aws-s3 postgresql-15-log-fdw # #postgresql-15-oracle-fdw
pg14: postgresql-14-wrappers postgresql-14-mysql-fdw postgresql-14-tds-fdw postgresql-14-sqlite-fdw postgresql-14-redis-fdw postgresql-14-pg-redis-pubsub postgresql-14-kafka-fdw postgresql-14-firebird-fdw postgresql-14-aws-s3 postgresql-14-log-fdw # #postgresql-14-pgspider-ext #postgresql-14-oracle-fdw
pg13: postgresql-13-mysql-fdw postgresql-13-tds-fdw postgresql-13-sqlite-fdw postgresql-13-redis-fdw postgresql-13-pg-redis-pubsub postgresql-13-kafka-fdw postgresql-13-firebird-fdw postgresql-13-aws-s3 #postgresql-13-wrappers # #postgresql-13-pgspider-ext #postgresql-13-oracle-fdw #postgresql-13-log-fdw
```


### Ubuntu 24.04 jammy Compatible (u22)

```yaml
pg17: postgresql-17-wrappers postgresql-17-pgspider-ext postgresql-17-mysql-fdw postgresql-17-tds-fdw postgresql-17-redis-fdw postgresql-17-pg-redis-pubsub postgresql-17-firebird-fdw postgresql-17-aws-s3 postgresql-17-log-fdw # #postgresql-17-oracle-fdw #postgresql-17-sqlite-fdw #postgresql-17-kafka-fdw
pg16: postgresql-16-wrappers postgresql-16-pgspider-ext postgresql-16-mysql-fdw postgresql-16-tds-fdw postgresql-16-sqlite-fdw postgresql-16-redis-fdw postgresql-16-pg-redis-pubsub postgresql-16-kafka-fdw postgresql-16-firebird-fdw postgresql-16-aws-s3 postgresql-16-log-fdw # #postgresql-16-oracle-fdw
pg15: postgresql-15-wrappers postgresql-15-pgspider-ext postgresql-15-mysql-fdw postgresql-15-tds-fdw postgresql-15-sqlite-fdw postgresql-15-redis-fdw postgresql-15-pg-redis-pubsub postgresql-15-kafka-fdw postgresql-15-firebird-fdw postgresql-15-aws-s3 postgresql-15-log-fdw # #postgresql-15-oracle-fdw
pg14: postgresql-14-wrappers postgresql-14-mysql-fdw postgresql-14-tds-fdw postgresql-14-sqlite-fdw postgresql-14-redis-fdw postgresql-14-pg-redis-pubsub postgresql-14-kafka-fdw postgresql-14-firebird-fdw postgresql-14-aws-s3 postgresql-14-log-fdw # #postgresql-14-pgspider-ext #postgresql-14-oracle-fdw
pg13: postgresql-13-mysql-fdw postgresql-13-tds-fdw postgresql-13-sqlite-fdw postgresql-13-redis-fdw postgresql-13-pg-redis-pubsub postgresql-13-kafka-fdw postgresql-13-firebird-fdw postgresql-13-aws-s3 #postgresql-13-wrappers # #postgresql-13-pgspider-ext #postgresql-13-oracle-fdw #postgresql-13-log-fdw
```


### Ubuntu 24.04 noble Compatible (u24)

```yaml
pg17: postgresql-17-wrappers postgresql-17-pgspider-ext postgresql-17-mysql-fdw postgresql-17-tds-fdw postgresql-17-redis-fdw postgresql-17-pg-redis-pubsub postgresql-17-firebird-fdw postgresql-17-aws-s3 postgresql-17-log-fdw # #postgresql-17-oracle-fdw #postgresql-17-sqlite-fdw #postgresql-17-kafka-fdw
pg16: postgresql-16-wrappers postgresql-16-pgspider-ext postgresql-16-mysql-fdw postgresql-16-tds-fdw postgresql-16-sqlite-fdw postgresql-16-redis-fdw postgresql-16-pg-redis-pubsub postgresql-16-kafka-fdw postgresql-16-firebird-fdw postgresql-16-aws-s3 postgresql-16-log-fdw # #postgresql-16-oracle-fdw
pg15: postgresql-15-wrappers postgresql-15-pgspider-ext postgresql-15-mysql-fdw postgresql-15-tds-fdw postgresql-15-sqlite-fdw postgresql-15-redis-fdw postgresql-15-pg-redis-pubsub postgresql-15-kafka-fdw postgresql-15-firebird-fdw postgresql-15-aws-s3 postgresql-15-log-fdw # #postgresql-15-oracle-fdw
pg14: postgresql-14-wrappers postgresql-14-mysql-fdw postgresql-14-tds-fdw postgresql-14-sqlite-fdw postgresql-14-redis-fdw postgresql-14-pg-redis-pubsub postgresql-14-kafka-fdw postgresql-14-firebird-fdw postgresql-14-aws-s3 postgresql-14-log-fdw # #postgresql-14-pgspider-ext #postgresql-14-oracle-fdw
pg13: postgresql-13-mysql-fdw postgresql-13-tds-fdw postgresql-13-sqlite-fdw postgresql-13-redis-fdw postgresql-13-pg-redis-pubsub postgresql-13-kafka-fdw postgresql-13-firebird-fdw postgresql-13-aws-s3 #postgresql-13-wrappers # #postgresql-13-pgspider-ext #postgresql-13-oracle-fdw #postgresql-13-log-fdw
```



--------

# pg_redis_pubsub


> [pg_redis_pubsub](https://github.com/brettlaforge/pg_redis_pubsub): Send redis pub/sub messages to Redis from PostgreSQL Directly
>
> https://github.com/brettlaforge/pg_redis_pubsub


-------


## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [redis](https://github.com/brettlaforge/pg_redis_pubsub) | 0.0.1 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |



| Package | Tags | Schemas | Requires | Required by | Comment | Description |
|---------|------|---------|----------|-------------|:-------:|-------------|
| [pg_redis_pubsub](/redis) |  |  |  |  |  | Send redis pub/sub messages to Redis from PostgreSQL Directly |





```sql
CREATE EXTENSION redis;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.0.1 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_redis_pubsub_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 0.0.1 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-redis-pubsub` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pg_redis_pubsub` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_redis_pubsub"]}'
```


Install `pg_redis_pubsub` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_redis_pubsub_17*;
dnf install pg_redis_pubsub_16*;
dnf install pg_redis_pubsub_15*;
dnf install pg_redis_pubsub_14*;
dnf install pg_redis_pubsub_13*;
dnf install pg_redis_pubsub_12*;
```


Install `pg_redis_pubsub` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-redis-pubsub;
apt install postgresql-16-pg-redis-pubsub;
apt install postgresql-15-pg-redis-pubsub;
apt install postgresql-14-pg-redis-pubsub;
apt install postgresql-13-pg-redis-pubsub;
apt install postgresql-12-pg-redis-pubsub;
```


-----------


## Category: FDW


| ID | Extension | Version | Package | License | RPM | DEB | PL | Tags | Schemas | Requires | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:--:|------|---------|----------|:------:|:-------:|:-----:|:-------:|:-------:|
| 8500 | [wrappers](/wrappers) | 0.4.3 | [wrappers](/wrappers) | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` | `pgrx` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |
| 8510 | [multicorn](/multicorn) | 3.0 | [multicorn](/multicorn) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 8520 | [odbc_fdw](/odbc_fdw) | 0.5.1 | [odbc_fdw](/odbc_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** |  | `C` |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 8530 | [jdbc_fdw](/jdbc_fdw) | 1.2 | [jdbc_fdw](/jdbc_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** |  | `C` |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 8600 | [mysql_fdw](/mysql_fdw) | 1.2 | [mysql_fdw](/mysql_fdw) | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 8610 | [oracle_fdw](/oracle_fdw) | 1.2 | [oracle_fdw](/oracle_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  | `non-free` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 8620 | [tds_fdw](/tds_fdw) | 2.0.4 | [tds_fdw](/tds_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 8630 | [db2_fdw](/db2_fdw) | 6.0.1 | [db2_fdw](/db2_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** |  |  | `non-free` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 8640 | [sqlite_fdw](/sqlite_fdw) | 1.1 | [sqlite_fdw](/sqlite_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 8650 | [pgbouncer_fdw](/pgbouncer_fdw) | 1.2.0 | [pgbouncer_fdw](/pgbouncer_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 8700 | [mongo_fdw](/mongo_fdw) | 1.1 | [mongo_fdw](/mongo_fdw) | **<span class="tcwarn">LGPLv3</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 8710 | [redis_fdw](/redis_fdw) | 1.0 | [redis_fdw](/redis_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |  |
| 8720 | [redis](/redis) | 0.0.1 | [pg_redis_pubsub](/redis) | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |
| 8730 | [kafka_fdw](/kafka_fdw) | 0.0.3 | [kafka_fdw](/kafka_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 8740 | [hdfs_fdw](/hdfs_fdw) | 2.0.5 | [hdfs_fdw](/hdfs_fdw) | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 8750 | [firebird_fdw](/firebird_fdw) | 1.4.0 | [firebird_fdw](/firebird_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 8800 | [aws_s3](/aws_s3) | 0.0.1 | [aws_s3](/aws_s3) | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` |  |  |  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 8810 | [log_fdw](/log_fdw) | 1.4 | [log_fdw](/log_fdw) | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |  |
| 8970 | [dblink](/dblink) | 1.2 | [dblink](/dblink) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | **<span class="tcblue">CONTRIB</span>** | `C` |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 8980 | [file_fdw](/file_fdw) | 1.0 | [file_fdw](/file_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | **<span class="tcblue">CONTRIB</span>** | `C` |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 8990 | [postgres_fdw](/postgres_fdw) | 1.1 | [postgres_fdw](/postgres_fdw) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | **<span class="tcblue">CONTRIB</span>** | `C` |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |




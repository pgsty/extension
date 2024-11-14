# pg_redis_pubsub


> [pg_redis_pubsub](https://github.com/brettlaforge/pg_redis_pubsub): Send redis pub/sub messages to Redis from PostgreSQL Directly
>
> https://github.com/brettlaforge/pg_redis_pubsub





[FDW](/fdw) extensions: [`wrappers`](/wrappers), [`multicorn`](/multicorn), [`odbc_fdw`](/odbc_fdw), [`jdbc_fdw`](/jdbc_fdw), [`mysql_fdw`](/mysql_fdw), [`oracle_fdw`](/oracle_fdw), [`tds_fdw`](/tds_fdw), [`db2_fdw`](/db2_fdw), [`sqlite_fdw`](/sqlite_fdw), [`pgbouncer_fdw`](/pgbouncer_fdw), [`mongo_fdw`](/mongo_fdw), [`redis_fdw`](/redis_fdw), [`redis`](/redis), [`kafka_fdw`](/kafka_fdw), [`hdfs_fdw`](/hdfs_fdw), [`firebird_fdw`](/firebird_fdw), [`aws_s3`](/aws_s3), [`log_fdw`](/log_fdw), [`dblink`](/dblink), [`file_fdw`](/file_fdw), [`postgres_fdw`](/postgres_fdw)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [redis](https://github.com/brettlaforge/pg_redis_pubsub) | 0.0.1 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_redis_pubsub](/redis) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION redis;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.0.1 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_redis_pubsub_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 0.0.1 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-redis-pubsub` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pg_redis_pubsub` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_redis_pubsub"]}'
```


Install `pg_redis_pubsub` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install pg_redis_pubsub_17*;
yum install pg_redis_pubsub_16*;
yum install pg_redis_pubsub_15*;
yum install pg_redis_pubsub_14*;
yum install pg_redis_pubsub_13*;
yum install pg_redis_pubsub_12*;
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




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_redis_pubsub_17*` | `pg_redis_pubsub_16*` | `pg_redis_pubsub_15*` | `pg_redis_pubsub_14*` | `pg_redis_pubsub_13*` | `pg_redis_pubsub_12*` |
| `el9` | `pg_redis_pubsub_17*` | `pg_redis_pubsub_16*` | `pg_redis_pubsub_15*` | `pg_redis_pubsub_14*` | `pg_redis_pubsub_13*` | `pg_redis_pubsub_12*` |
| `d12` | `postgresql-17-pg-redis-pubsub` | `postgresql-16-pg-redis-pubsub` | `postgresql-15-pg-redis-pubsub` | `postgresql-14-pg-redis-pubsub` | `postgresql-13-pg-redis-pubsub` | `postgresql-12-pg-redis-pubsub` |
| `u22` | `postgresql-17-pg-redis-pubsub` | `postgresql-16-pg-redis-pubsub` | `postgresql-15-pg-redis-pubsub` | `postgresql-14-pg-redis-pubsub` | `postgresql-13-pg-redis-pubsub` | `postgresql-12-pg-redis-pubsub` |
| `u24` | `postgresql-17-pg-redis-pubsub` | `postgresql-16-pg-redis-pubsub` | `postgresql-15-pg-redis-pubsub` | `postgresql-14-pg-redis-pubsub` | `postgresql-13-pg-redis-pubsub` | `postgresql-12-pg-redis-pubsub` |






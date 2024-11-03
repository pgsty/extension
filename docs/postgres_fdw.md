# postgres_fdw


> [postgres_fdw](https://www.postgresql.org/docs/current/postgres-fdw.html): foreign-data wrapper for remote PostgreSQL servers
>
> https://www.postgresql.org/docs/current/postgres-fdw.html





[FDW](/fdw) extensions: [`wrappers`](/wrappers), [`multicorn`](/multicorn), [`odbc_fdw`](/odbc_fdw), [`jdbc_fdw`](/jdbc_fdw), [`mysql_fdw`](/mysql_fdw), [`oracle_fdw`](/oracle_fdw), [`tds_fdw`](/tds_fdw), [`db2_fdw`](/db2_fdw), [`sqlite_fdw`](/sqlite_fdw), [`pgbouncer_fdw`](/pgbouncer_fdw), [`mongo_fdw`](/mongo_fdw), [`redis_fdw`](/redis_fdw), [`redis`](/redis), [`kafka_fdw`](/kafka_fdw), [`hdfs_fdw`](/hdfs_fdw), [`firebird_fdw`](/firebird_fdw), [`aws_s3`](/aws_s3), [`log_fdw`](/log_fdw), [`dblink`](/dblink), [`file_fdw`](/file_fdw), [`postgres_fdw`](/postgres_fdw)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [postgres_fdw](https://www.postgresql.org/docs/current/postgres-fdw.html) | 1.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | **<span class="tcblue">CONTRIB</span>** | `C` |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |



| Package | Tags | Schemas | Requires | Required by |
|---------|------|---------|----------|-------------|
| [postgres_fdw](/postgres_fdw) |  |  |  |  |





```sql
CREATE EXTENSION postgres_fdw;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql$v-contrib` | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** |  |
| [DEB](/deb) | 1.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql-$v` | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** |  |



Install `postgres_fdw` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["postgres_fdw"]}'
```


Install `postgres_fdw` [RPM](/rpm) from the **<span class="tcblue">CONTRIB</span>** **YUM** repo:

```bash
dnf install postgresql17-contrib;
dnf install postgresql16-contrib;
dnf install postgresql15-contrib;
dnf install postgresql14-contrib;
dnf install postgresql13-contrib;
dnf install postgresql12-contrib;
```


Install `postgres_fdw` [DEB](/deb) from the **<span class="tcblue">CONTRIB</span>** **APT** repo:

```bash
apt install postgresql-17;
apt install postgresql-16;
apt install postgresql-15;
apt install postgresql-14;
apt install postgresql-13;
apt install postgresql-12;
```








# sqlite_fdw


> [sqlite_fdw](https://github.com/pgspider/sqlite_fdw): SQLite Foreign Data Wrapper
>
> https://github.com/pgspider/sqlite_fdw





[FDW](/fdw) extensions: [`wrappers`](/wrappers), [`multicorn`](/multicorn), [`odbc_fdw`](/odbc_fdw), [`jdbc_fdw`](/jdbc_fdw), [`mysql_fdw`](/mysql_fdw), [`oracle_fdw`](/oracle_fdw), [`tds_fdw`](/tds_fdw), [`db2_fdw`](/db2_fdw), [`sqlite_fdw`](/sqlite_fdw), [`pgbouncer_fdw`](/pgbouncer_fdw), [`mongo_fdw`](/mongo_fdw), [`redis_fdw`](/redis_fdw), [`redis`](/redis), [`kafka_fdw`](/kafka_fdw), [`hdfs_fdw`](/hdfs_fdw), [`firebird_fdw`](/firebird_fdw), [`aws_s3`](/aws_s3), [`log_fdw`](/log_fdw), [`dblink`](/dblink), [`file_fdw`](/file_fdw), [`postgres_fdw`](/postgres_fdw)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [sqlite_fdw](https://github.com/pgspider/sqlite_fdw) | 1.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [sqlite_fdw](/sqlite_fdw) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION sqlite_fdw;
```
> **Comment**: missing deb pg17 package
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `sqlite_fdw_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 2.4.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-sqlite-fdw` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `sqlite_fdw` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["sqlite_fdw"]}'
```


Install `sqlite_fdw` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install sqlite_fdw_17*;
yum install sqlite_fdw_16*;
yum install sqlite_fdw_15*;
yum install sqlite_fdw_14*;
yum install sqlite_fdw_13*;
yum install sqlite_fdw_12*;
```


Install `sqlite_fdw` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-sqlite-fdw;
apt install postgresql-16-sqlite-fdw;
apt install postgresql-15-sqlite-fdw;
apt install postgresql-14-sqlite-fdw;
apt install postgresql-13-sqlite-fdw;
apt install postgresql-12-sqlite-fdw;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `sqlite_fdw_17*` | `sqlite_fdw_16*` | `sqlite_fdw_15*` | `sqlite_fdw_14*` | `sqlite_fdw_13*` | `sqlite_fdw_12*` |
| `el9` | `sqlite_fdw_17*` | `sqlite_fdw_16*` | `sqlite_fdw_15*` | `sqlite_fdw_14*` | `sqlite_fdw_13*` | `sqlite_fdw_12*` |
| `d12` | `postgresql-17-sqlite-fdw` | `postgresql-16-sqlite-fdw` | `postgresql-15-sqlite-fdw` | `postgresql-14-sqlite-fdw` | `postgresql-13-sqlite-fdw` | `postgresql-12-sqlite-fdw` |
| `u22` | `postgresql-17-sqlite-fdw` | `postgresql-16-sqlite-fdw` | `postgresql-15-sqlite-fdw` | `postgresql-14-sqlite-fdw` | `postgresql-13-sqlite-fdw` | `postgresql-12-sqlite-fdw` |
| `u24` | `postgresql-17-sqlite-fdw` | `postgresql-16-sqlite-fdw` | `postgresql-15-sqlite-fdw` | `postgresql-14-sqlite-fdw` | `postgresql-13-sqlite-fdw` | `postgresql-12-sqlite-fdw` |






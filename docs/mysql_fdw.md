# mysql_fdw


> [mysql_fdw](https://github.com/EnterpriseDB/mysql_fdw): Foreign data wrapper for querying a MySQL server
>
> https://github.com/EnterpriseDB/mysql_fdw





[FDW](/fdw) extensions: [`wrappers`](/wrappers), [`multicorn`](/multicorn), [`odbc_fdw`](/odbc_fdw), [`jdbc_fdw`](/jdbc_fdw), [`pgspider_ext`](/pgspider_ext), [`mysql_fdw`](/mysql_fdw), [`oracle_fdw`](/oracle_fdw), [`tds_fdw`](/tds_fdw), [`db2_fdw`](/db2_fdw), [`sqlite_fdw`](/sqlite_fdw), [`pgbouncer_fdw`](/pgbouncer_fdw), [`mongo_fdw`](/mongo_fdw), [`redis_fdw`](/redis_fdw), [`redis`](/redis), [`kafka_fdw`](/kafka_fdw), [`hdfs_fdw`](/hdfs_fdw), [`firebird_fdw`](/firebird_fdw), [`aws_s3`](/aws_s3), [`log_fdw`](/log_fdw), [`dblink`](/dblink), [`file_fdw`](/file_fdw), [`postgres_fdw`](/postgres_fdw)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [mysql_fdw](https://github.com/EnterpriseDB/mysql_fdw) | 2.9.2 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [mysql_fdw](/mysql_fdw) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION mysql_fdw;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 2.9.2 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `mysql_fdw_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 2.9.2 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-mysql-fdw` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `mysql_fdw` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add mysql_fdw
```


Install `mysql_fdw` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["mysql_fdw"]}'
```


Install `mysql_fdw` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install mysql_fdw_17*;
dnf install mysql_fdw_16*;
dnf install mysql_fdw_15*;
dnf install mysql_fdw_14*;
dnf install mysql_fdw_13*;
```


Install `mysql_fdw` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-mysql-fdw;
apt install postgresql-16-mysql-fdw;
apt install postgresql-15-mysql-fdw;
apt install postgresql-14-mysql-fdw;
apt install postgresql-13-mysql-fdw;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `mysql_fdw_17*` | `mysql_fdw_16*` | `mysql_fdw_15*` | `mysql_fdw_14*` | `mysql_fdw_13*` |
| `el9` | `mysql_fdw_17*` | `mysql_fdw_16*` | `mysql_fdw_15*` | `mysql_fdw_14*` | `mysql_fdw_13*` |
| `d12` | `postgresql-17-mysql-fdw` | `postgresql-16-mysql-fdw` | `postgresql-15-mysql-fdw` | `postgresql-14-mysql-fdw` | `postgresql-13-mysql-fdw` |
| `u22` | `postgresql-17-mysql-fdw` | `postgresql-16-mysql-fdw` | `postgresql-15-mysql-fdw` | `postgresql-14-mysql-fdw` | `postgresql-13-mysql-fdw` |
| `u24` | `postgresql-17-mysql-fdw` | `postgresql-16-mysql-fdw` | `postgresql-15-mysql-fdw` | `postgresql-14-mysql-fdw` | `postgresql-13-mysql-fdw` |






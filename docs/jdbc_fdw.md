# jdbc_fdw


> [jdbc_fdw](https://github.com/pgspider/jdbc_fdw): foreign-data wrapper for remote servers available over JDBC
>
> https://github.com/pgspider/jdbc_fdw





[FDW](/fdw) extensions: [`wrappers`](/wrappers), [`multicorn`](/multicorn), [`odbc_fdw`](/odbc_fdw), [`jdbc_fdw`](/jdbc_fdw), [`pgspider_ext`](/pgspider_ext), [`mysql_fdw`](/mysql_fdw), [`oracle_fdw`](/oracle_fdw), [`tds_fdw`](/tds_fdw), [`db2_fdw`](/db2_fdw), [`sqlite_fdw`](/sqlite_fdw), [`pgbouncer_fdw`](/pgbouncer_fdw), [`mongo_fdw`](/mongo_fdw), [`redis_fdw`](/redis_fdw), [`redis`](/redis), [`kafka_fdw`](/kafka_fdw), [`hdfs_fdw`](/hdfs_fdw), [`firebird_fdw`](/firebird_fdw), [`aws_s3`](/aws_s3), [`log_fdw`](/log_fdw), [`dblink`](/dblink), [`file_fdw`](/file_fdw), [`postgres_fdw`](/postgres_fdw)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [jdbc_fdw](https://github.com/pgspider/jdbc_fdw) | 1.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** |  | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [jdbc_fdw](/jdbc_fdw) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcred">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcred">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `u22` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `u24` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |





```sql
CREATE EXTENSION jdbc_fdw;
```
> **Comment**: missing el.aarch64
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `jdbc_fdw_$v*` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | `java-11-openjdk-headless` |



Install `jdbc_fdw` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add jdbc_fdw
```


Install `jdbc_fdw` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["jdbc_fdw"]}'
```


Install `jdbc_fdw` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install jdbc_fdw_16*;
dnf install jdbc_fdw_15*;
dnf install jdbc_fdw_14*;
dnf install jdbc_fdw_13*;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcred">✘</span> | `jdbc_fdw_16*` | `jdbc_fdw_15*` | `jdbc_fdw_14*` | `jdbc_fdw_13*` |
| `el9` | <span class="tcred">✘</span> | `jdbc_fdw_16*` | `jdbc_fdw_15*` | `jdbc_fdw_14*` | `jdbc_fdw_13*` |
| `d12` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `u22` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `u24` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |






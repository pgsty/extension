# odbc_fdw


> [odbc_fdw](https://github.com/CartoDB/odbc_fdw): Foreign data wrapper for accessing remote databases using ODBC
>
> https://github.com/CartoDB/odbc_fdw





[FDW](/fdw) extensions: [`wrappers`](/wrappers), [`multicorn`](/multicorn), [`odbc_fdw`](/odbc_fdw), [`jdbc_fdw`](/jdbc_fdw), [`mysql_fdw`](/mysql_fdw), [`oracle_fdw`](/oracle_fdw), [`tds_fdw`](/tds_fdw), [`db2_fdw`](/db2_fdw), [`sqlite_fdw`](/sqlite_fdw), [`pgbouncer_fdw`](/pgbouncer_fdw), [`mongo_fdw`](/mongo_fdw), [`redis_fdw`](/redis_fdw), [`redis`](/redis), [`kafka_fdw`](/kafka_fdw), [`hdfs_fdw`](/hdfs_fdw), [`firebird_fdw`](/firebird_fdw), [`aws_s3`](/aws_s3), [`log_fdw`](/log_fdw), [`dblink`](/dblink), [`file_fdw`](/file_fdw), [`postgres_fdw`](/postgres_fdw)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [odbc_fdw](https://github.com/CartoDB/odbc_fdw) | 0.5.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** |  | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [odbc_fdw](/odbc_fdw) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `u22` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `u24` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |





```sql
CREATE EXTENSION odbc_fdw;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.5.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `odbc_fdw_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | `unixODBC` |



Install `odbc_fdw` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add odbc_fdw
```


Install `odbc_fdw` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["odbc_fdw"]}'
```


Install `odbc_fdw` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install odbc_fdw_17*;
dnf install odbc_fdw_16*;
dnf install odbc_fdw_15*;
dnf install odbc_fdw_14*;
dnf install odbc_fdw_13*;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `odbc_fdw_17*` | `odbc_fdw_16*` | `odbc_fdw_15*` | `odbc_fdw_14*` | `odbc_fdw_13*` |
| `el9` | `odbc_fdw_17*` | `odbc_fdw_16*` | `odbc_fdw_15*` | `odbc_fdw_14*` | `odbc_fdw_13*` |
| `d12` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `u22` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `u24` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |






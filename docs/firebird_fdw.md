# firebird_fdw


> [firebird_fdw](https://github.com/ibarwick/firebird_fdw): Foreign data wrapper for Firebird
>
> https://github.com/ibarwick/firebird_fdw





[FDW](/fdw) extensions: [`wrappers`](/wrappers), [`multicorn`](/multicorn), [`odbc_fdw`](/odbc_fdw), [`jdbc_fdw`](/jdbc_fdw), [`mysql_fdw`](/mysql_fdw), [`oracle_fdw`](/oracle_fdw), [`tds_fdw`](/tds_fdw), [`db2_fdw`](/db2_fdw), [`sqlite_fdw`](/sqlite_fdw), [`pgbouncer_fdw`](/pgbouncer_fdw), [`mongo_fdw`](/mongo_fdw), [`redis_fdw`](/redis_fdw), [`redis`](/redis), [`kafka_fdw`](/kafka_fdw), [`hdfs_fdw`](/hdfs_fdw), [`firebird_fdw`](/firebird_fdw), [`aws_s3`](/aws_s3), [`log_fdw`](/log_fdw), [`dblink`](/dblink), [`file_fdw`](/file_fdw), [`postgres_fdw`](/postgres_fdw)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [firebird_fdw](https://github.com/ibarwick/firebird_fdw) | 1.4.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [firebird_fdw](/firebird_fdw) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION firebird_fdw;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `firebird_fdw_17` | `firebird_fdw_16` | `firebird_fdw_15` | `firebird_fdw_14` | `firebird_fdw_13` | `firebird_fdw_12` |
| `el9` | `firebird_fdw_17` | `firebird_fdw_16` | `firebird_fdw_15` | `firebird_fdw_14` | `firebird_fdw_13` | `firebird_fdw_12` |
| `d12` | `postgresql-17-firebird-fdw` | `postgresql-16-firebird-fdw` | `postgresql-15-firebird-fdw` | `postgresql-14-firebird-fdw` | `postgresql-13-firebird-fdw` | `postgresql-12-firebird-fdw` |
| `u22` | `postgresql-17-firebird-fdw` | `postgresql-16-firebird-fdw` | `postgresql-15-firebird-fdw` | `postgresql-14-firebird-fdw` | `postgresql-13-firebird-fdw` | `postgresql-12-firebird-fdw` |
| `u24` | `postgresql-17-firebird-fdw` | `postgresql-16-firebird-fdw` | `postgresql-15-firebird-fdw` | `postgresql-14-firebird-fdw` | `postgresql-13-firebird-fdw` | `postgresql-12-firebird-fdw` |



Install `firebird_fdw` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["firebird_fdw"]}'
```


Install `firebird_fdw` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install firebird_fdw_17;
yum install firebird_fdw_16;
yum install firebird_fdw_15;
yum install firebird_fdw_14;
yum install firebird_fdw_13;
yum install firebird_fdw_12;
```


Install `firebird_fdw` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-firebird-fdw;
apt install postgresql-16-firebird-fdw;
apt install postgresql-15-firebird-fdw;
apt install postgresql-14-firebird-fdw;
apt install postgresql-13-firebird-fdw;
apt install postgresql-12-firebird-fdw;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `firebird_fdw_17` | `firebird_fdw_16` | `firebird_fdw_15` | `firebird_fdw_14` | `firebird_fdw_13` | `firebird_fdw_12` |
| `el9` | `firebird_fdw_17` | `firebird_fdw_16` | `firebird_fdw_15` | `firebird_fdw_14` | `firebird_fdw_13` | `firebird_fdw_12` |
| `d12` | `postgresql-17-firebird-fdw` | `postgresql-16-firebird-fdw` | `postgresql-15-firebird-fdw` | `postgresql-14-firebird-fdw` | `postgresql-13-firebird-fdw` | `postgresql-12-firebird-fdw` |
| `u22` | `postgresql-17-firebird-fdw` | `postgresql-16-firebird-fdw` | `postgresql-15-firebird-fdw` | `postgresql-14-firebird-fdw` | `postgresql-13-firebird-fdw` | `postgresql-12-firebird-fdw` |
| `u24` | `postgresql-17-firebird-fdw` | `postgresql-16-firebird-fdw` | `postgresql-15-firebird-fdw` | `postgresql-14-firebird-fdw` | `postgresql-13-firebird-fdw` | `postgresql-12-firebird-fdw` |






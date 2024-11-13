# aws_s3


> [aws_s3](https://github.com/chimpler/postgres-aws-s3): aws_s3 postgres extension to import/export data from/to s3
>
> https://github.com/chimpler/postgres-aws-s3





[FDW](/fdw) extensions: [`wrappers`](/wrappers), [`multicorn`](/multicorn), [`odbc_fdw`](/odbc_fdw), [`jdbc_fdw`](/jdbc_fdw), [`mysql_fdw`](/mysql_fdw), [`oracle_fdw`](/oracle_fdw), [`tds_fdw`](/tds_fdw), [`db2_fdw`](/db2_fdw), [`sqlite_fdw`](/sqlite_fdw), [`pgbouncer_fdw`](/pgbouncer_fdw), [`mongo_fdw`](/mongo_fdw), [`redis_fdw`](/redis_fdw), [`redis`](/redis), [`kafka_fdw`](/kafka_fdw), [`hdfs_fdw`](/hdfs_fdw), [`firebird_fdw`](/firebird_fdw), [`aws_s3`](/aws_s3), [`log_fdw`](/log_fdw), [`dblink`](/dblink), [`file_fdw`](/file_fdw), [`postgres_fdw`](/postgres_fdw)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [aws_s3](https://github.com/chimpler/postgres-aws-s3) | 0.0.1 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [aws_s3](/aws_s3) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION aws_s3;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `aws_s3_17` | `aws_s3_16` | `aws_s3_15` | `aws_s3_14` | `aws_s3_13` | `aws_s3_12` |
| `el9` | `aws_s3_17` | `aws_s3_16` | `aws_s3_15` | `aws_s3_14` | `aws_s3_13` | `aws_s3_12` |
| `d12` | `postgresql-17-aws-s3` | `postgresql-16-aws-s3` | `postgresql-15-aws-s3` | `postgresql-14-aws-s3` | `postgresql-13-aws-s3` | `postgresql-12-aws-s3` |
| `u22` | `postgresql-17-aws-s3` | `postgresql-16-aws-s3` | `postgresql-15-aws-s3` | `postgresql-14-aws-s3` | `postgresql-13-aws-s3` | `postgresql-12-aws-s3` |
| `u24` | `postgresql-17-aws-s3` | `postgresql-16-aws-s3` | `postgresql-15-aws-s3` | `postgresql-14-aws-s3` | `postgresql-13-aws-s3` | `postgresql-12-aws-s3` |



Install `aws_s3` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["aws_s3"]}'
```


Install `aws_s3` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install aws_s3_17;
yum install aws_s3_16;
yum install aws_s3_15;
yum install aws_s3_14;
yum install aws_s3_13;
yum install aws_s3_12;
```


Install `aws_s3` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-aws-s3;
apt install postgresql-16-aws-s3;
apt install postgresql-15-aws-s3;
apt install postgresql-14-aws-s3;
apt install postgresql-13-aws-s3;
apt install postgresql-12-aws-s3;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `aws_s3_17` | `aws_s3_16` | `aws_s3_15` | `aws_s3_14` | `aws_s3_13` | `aws_s3_12` |
| `el9` | `aws_s3_17` | `aws_s3_16` | `aws_s3_15` | `aws_s3_14` | `aws_s3_13` | `aws_s3_12` |
| `d12` | `postgresql-17-aws-s3` | `postgresql-16-aws-s3` | `postgresql-15-aws-s3` | `postgresql-14-aws-s3` | `postgresql-13-aws-s3` | `postgresql-12-aws-s3` |
| `u22` | `postgresql-17-aws-s3` | `postgresql-16-aws-s3` | `postgresql-15-aws-s3` | `postgresql-14-aws-s3` | `postgresql-13-aws-s3` | `postgresql-12-aws-s3` |
| `u24` | `postgresql-17-aws-s3` | `postgresql-16-aws-s3` | `postgresql-15-aws-s3` | `postgresql-14-aws-s3` | `postgresql-13-aws-s3` | `postgresql-12-aws-s3` |






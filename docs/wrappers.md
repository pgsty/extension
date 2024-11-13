# wrappers


> [wrappers](https://github.com/supabase/wrappers): Foreign data wrappers developed by Supabase
>
> https://github.com/supabase/wrappers





[FDW](/fdw) extensions: [`wrappers`](/wrappers), [`multicorn`](/multicorn), [`odbc_fdw`](/odbc_fdw), [`jdbc_fdw`](/jdbc_fdw), [`mysql_fdw`](/mysql_fdw), [`oracle_fdw`](/oracle_fdw), [`tds_fdw`](/tds_fdw), [`db2_fdw`](/db2_fdw), [`sqlite_fdw`](/sqlite_fdw), [`pgbouncer_fdw`](/pgbouncer_fdw), [`mongo_fdw`](/mongo_fdw), [`redis_fdw`](/redis_fdw), [`redis`](/redis), [`kafka_fdw`](/kafka_fdw), [`hdfs_fdw`](/hdfs_fdw), [`firebird_fdw`](/firebird_fdw), [`aws_s3`](/aws_s3), [`log_fdw`](/log_fdw), [`dblink`](/dblink), [`file_fdw`](/file_fdw), [`postgres_fdw`](/postgres_fdw)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [wrappers](https://github.com/supabase/wrappers) | 0.4.3 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [wrappers](/wrappers) | `pgrx` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION wrappers;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `wrappers_17` | `wrappers_16` | `wrappers_15` | `wrappers_14` | `wrappers_13` | `wrappers_12` |
| `el9` | `wrappers_17` | `wrappers_16` | `wrappers_15` | `wrappers_14` | `wrappers_13` | `wrappers_12` |
| `d12` | `postgresql-17-wrappers` | `postgresql-16-wrappers` | `postgresql-15-wrappers` | `postgresql-14-wrappers` | `postgresql-13-wrappers` | `postgresql-12-wrappers` |
| `u22` | `postgresql-17-wrappers` | `postgresql-16-wrappers` | `postgresql-15-wrappers` | `postgresql-14-wrappers` | `postgresql-13-wrappers` | `postgresql-12-wrappers` |
| `u24` | `postgresql-17-wrappers` | `postgresql-16-wrappers` | `postgresql-15-wrappers` | `postgresql-14-wrappers` | `postgresql-13-wrappers` | `postgresql-12-wrappers` |



Install `wrappers` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["wrappers"]}'
```


Install `wrappers` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install wrappers_17;
yum install wrappers_16;
yum install wrappers_15;
yum install wrappers_14;
yum install wrappers_13;
yum install wrappers_12;
```


Install `wrappers` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-wrappers;
apt install postgresql-16-wrappers;
apt install postgresql-15-wrappers;
apt install postgresql-14-wrappers;
apt install postgresql-13-wrappers;
apt install postgresql-12-wrappers;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `wrappers_17` | `wrappers_16` | `wrappers_15` | `wrappers_14` | `wrappers_13` | `wrappers_12` |
| `el9` | `wrappers_17` | `wrappers_16` | `wrappers_15` | `wrappers_14` | `wrappers_13` | `wrappers_12` |
| `d12` | `postgresql-17-wrappers` | `postgresql-16-wrappers` | `postgresql-15-wrappers` | `postgresql-14-wrappers` | `postgresql-13-wrappers` | `postgresql-12-wrappers` |
| `u22` | `postgresql-17-wrappers` | `postgresql-16-wrappers` | `postgresql-15-wrappers` | `postgresql-14-wrappers` | `postgresql-13-wrappers` | `postgresql-12-wrappers` |
| `u24` | `postgresql-17-wrappers` | `postgresql-16-wrappers` | `postgresql-15-wrappers` | `postgresql-14-wrappers` | `postgresql-13-wrappers` | `postgresql-12-wrappers` |






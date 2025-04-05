# wrappers


> [wrappers](https://github.com/supabase/wrappers): Foreign data wrappers developed by Supabase
>
> https://github.com/supabase/wrappers





[FDW](/fdw) extensions: [`wrappers`](/wrappers), [`multicorn`](/multicorn), [`odbc_fdw`](/odbc_fdw), [`jdbc_fdw`](/jdbc_fdw), [`pgspider_ext`](/pgspider_ext), [`mysql_fdw`](/mysql_fdw), [`oracle_fdw`](/oracle_fdw), [`tds_fdw`](/tds_fdw), [`db2_fdw`](/db2_fdw), [`sqlite_fdw`](/sqlite_fdw), [`pgbouncer_fdw`](/pgbouncer_fdw), [`mongo_fdw`](/mongo_fdw), [`redis_fdw`](/redis_fdw), [`redis`](/redis), [`kafka_fdw`](/kafka_fdw), [`hdfs_fdw`](/hdfs_fdw), [`firebird_fdw`](/firebird_fdw), [`aws_s3`](/aws_s3), [`log_fdw`](/log_fdw), [`dblink`](/dblink), [`file_fdw`](/file_fdw), [`postgres_fdw`](/postgres_fdw)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [wrappers](https://github.com/supabase/wrappers) | 0.4.5 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [wrappers](/wrappers) | `pgrx`, `supabase` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |





```sql
CREATE EXTENSION wrappers;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.4.5 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `wrappers_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  |
| [DEB](/deb) | 0.4.5 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-wrappers` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  |



Install `wrappers` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add wrappers
```


Install `wrappers` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["wrappers"]}'
```


Install `wrappers` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install wrappers_17;
dnf install wrappers_16;
dnf install wrappers_15;
dnf install wrappers_14;
```


Install `wrappers` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-wrappers;
apt install postgresql-16-wrappers;
apt install postgresql-15-wrappers;
apt install postgresql-14-wrappers;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `wrappers_17` | `wrappers_16` | `wrappers_15` | `wrappers_14` | <span class="tcred">✘</span> |
| `el9` | `wrappers_17` | `wrappers_16` | `wrappers_15` | `wrappers_14` | <span class="tcred">✘</span> |
| `d12` | `postgresql-17-wrappers` | `postgresql-16-wrappers` | `postgresql-15-wrappers` | `postgresql-14-wrappers` | <span class="tcred">✘</span> |
| `u22` | `postgresql-17-wrappers` | `postgresql-16-wrappers` | `postgresql-15-wrappers` | `postgresql-14-wrappers` | <span class="tcred">✘</span> |
| `u24` | `postgresql-17-wrappers` | `postgresql-16-wrappers` | `postgresql-15-wrappers` | `postgresql-14-wrappers` | <span class="tcred">✘</span> |






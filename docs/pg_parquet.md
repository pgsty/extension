# pg_parquet


> [pg_parquet](https://github.com/CrunchyData/pg_parquet/): copy data between Postgres and Parquet
>
> https://github.com/CrunchyData/pg_parquet/





[OLAP](/olap) extensions: [`citus`](/citus), [`citus_columnar`](/citus_columnar), [`columnar`](/columnar), [`pg_analytics`](/pg_analytics), [`pg_duckdb`](/pg_duckdb), [`duckdb_fdw`](/duckdb_fdw), [`pg_parquet`](/pg_parquet), [`pg_fkpart`](/pg_fkpart), [`pg_partman`](/pg_partman), [`plproxy`](/plproxy), [`pg_strom`](/pg_strom), [`tablefunc`](/tablefunc)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_parquet](https://github.com/CrunchyData/pg_parquet/) | 0.1.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_parquet](/pg_parquet) | `pgrx` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'pg_parquet'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION pg_parquet;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.1.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_parquet_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  |  |
| [DEB](/deb) | 0.1.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-parquet` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  |  |



Install `pg_parquet` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_parquet"]}'
```


Install `pg_parquet` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install pg_parquet_17;
yum install pg_parquet_16;
yum install pg_parquet_15;
yum install pg_parquet_14;
yum install pg_parquet_13;
yum install pg_parquet_12;
```


Install `pg_parquet` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-parquet;
apt install postgresql-16-pg-parquet;
apt install postgresql-15-pg-parquet;
apt install postgresql-14-pg-parquet;
apt install postgresql-13-pg-parquet;
apt install postgresql-12-pg-parquet;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_parquet_17` | `pg_parquet_16` | `pg_parquet_15` | `pg_parquet_14` | `pg_parquet_13` | `pg_parquet_12` |
| `el9` | `pg_parquet_17` | `pg_parquet_16` | `pg_parquet_15` | `pg_parquet_14` | `pg_parquet_13` | `pg_parquet_12` |
| `d12` | `postgresql-17-pg-parquet` | `postgresql-16-pg-parquet` | `postgresql-15-pg-parquet` | `postgresql-14-pg-parquet` | `postgresql-13-pg-parquet` | `postgresql-12-pg-parquet` |
| `u22` | `postgresql-17-pg-parquet` | `postgresql-16-pg-parquet` | `postgresql-15-pg-parquet` | `postgresql-14-pg-parquet` | `postgresql-13-pg-parquet` | `postgresql-12-pg-parquet` |
| `u24` | `postgresql-17-pg-parquet` | `postgresql-16-pg-parquet` | `postgresql-15-pg-parquet` | `postgresql-14-pg-parquet` | `postgresql-13-pg-parquet` | `postgresql-12-pg-parquet` |






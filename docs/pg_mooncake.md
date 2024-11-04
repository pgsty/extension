# pg_mooncake


> [pg_mooncake](https://github.com/Mooncake-Labs/pg_mooncake): Columnstore Table in Postgres
>
> https://github.com/Mooncake-Labs/pg_mooncake





[OLAP](/olap) extensions: [`citus`](/citus), [`citus_columnar`](/citus_columnar), [`columnar`](/columnar), [`pg_analytics`](/pg_analytics), [`pg_duckdb`](/pg_duckdb), [`pg_mooncake`](/pg_mooncake), [`duckdb_fdw`](/duckdb_fdw), [`pg_parquet`](/pg_parquet), [`pg_fkpart`](/pg_fkpart), [`pg_partman`](/pg_partman), [`plproxy`](/plproxy), [`pg_strom`](/pg_strom), [`tablefunc`](/tablefunc)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [pg_mooncake](https://github.com/Mooncake-Labs/pg_mooncake) | 0.0.1 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C++` |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Package | Tags | Schemas | Requires | Required by |
|---------|------|---------|----------|-------------|
| [pg_mooncake](/pg_mooncake) |  |  |  |  |



```bash
shared_preload_libraries = 'pg_mooncake'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION pg_mooncake;
```
> **Comment**: conflict on libduckdb with pg_duckdb/duckdb_fdw
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.0.1 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_mooncake_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  |  |  |
| [DEB](/deb) | 0.0.1 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-mooncake` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  |  |  |



Install `pg_mooncake` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_mooncake"]}'
```


Install `pg_mooncake` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_mooncake_17*;
dnf install pg_mooncake_16*;
dnf install pg_mooncake_15*;
```


Install `pg_mooncake` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-mooncake;
apt install postgresql-16-pg-mooncake;
apt install postgresql-15-pg-mooncake;
```







--------

## Usage

Beware that this package is conflict with the official `pg_duckdb` extension due to use the same `libduckdb.so` under same path.




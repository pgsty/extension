# citus


> [citus](https://github.com/citusdata/citus): Citus columnar storage engine
>
> https://github.com/citusdata/citus





[OLAP](/olap) extensions: [`citus`](/citus), [`citus_columnar`](/citus_columnar), [`columnar`](/columnar), [`pg_analytics`](/pg_analytics), [`pg_duckdb`](/pg_duckdb), [`pg_mooncake`](/pg_mooncake), [`duckdb_fdw`](/duckdb_fdw), [`pg_parquet`](/pg_parquet), [`pg_fkpart`](/pg_fkpart), [`pg_partman`](/pg_partman), [`plproxy`](/plproxy), [`pg_strom`](/pg_strom), [`tablefunc`](/tablefunc)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [citus_columnar](https://github.com/citusdata/citus) | 11.3-1 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcgreen">CITUS</span>** |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Package | Tags | Schemas | Requires | Required by |
|---------|------|---------|----------|-------------|
| [citus](/citus_columnar) |  | `pg_catalog` |  |  |





```sql
CREATE EXTENSION citus_columnar;
```
> **Comment**: conflict with hydra columnar, no pg17, no noble, no arm64
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| Distro-citus | 12.1-1 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tccyan">PGDG</span>** | `citus_$v*` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| Distro-citus | 12.1-1 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcgreen">CITUS</span>** | `postgresql-$v-citus-12.1` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `citus` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["citus"]}'
```


Install `citus` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install citus_16*;
dnf install citus_15*;
dnf install citus_14*;
dnf install citus_13*;
dnf install citus_12*;
```


Install `citus` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-16-citus-12.1;
apt install postgresql-15-citus-12.1;
apt install postgresql-14-citus-12.1;
apt install postgresql-13-citus-12.1;
apt install postgresql-12-citus-12.1;
```








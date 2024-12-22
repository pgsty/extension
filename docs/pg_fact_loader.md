# pg_fact_loader


> [pg_fact_loader](https://github.com/enova/pg_fact_loader): build fact tables with Postgres
>
> https://github.com/enova/pg_fact_loader





[ETL](/etl) extensions: [`pglogical`](/pglogical), [`pglogical_origin`](/pglogical_origin), [`pglogical_ticker`](/pglogical_ticker), [`pgl_ddl_deploy`](/pgl_ddl_deploy), [`pg_failover_slots`](/pg_failover_slots), [`wal2json`](/wal2json), [`wal2mongo`](/wal2mongo), [`decoderbufs`](/decoderbufs), [`decoder_raw`](/decoder_raw), [`pgoutput`](/pgoutput), [`test_decoding`](/test_decoding), [`mimeo`](/mimeo), [`repmgr`](/repmgr), [`pg_fact_loader`](/pg_fact_loader), [`pg_bulkload`](/pg_bulkload)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_fact_loader](https://github.com/enova/pg_fact_loader) | 2.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_fact_loader](/pg_fact_loader) |  | `fact_loader` |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_fact_loader;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 2.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `pg_fact_loader_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 2.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pg-fact-loader` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pg_fact_loader` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_fact_loader"]}'
```


Install `pg_fact_loader` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pg_fact_loader_17*;
dnf install pg_fact_loader_16*;
dnf install pg_fact_loader_15*;
dnf install pg_fact_loader_14*;
dnf install pg_fact_loader_13*;
dnf install pg_fact_loader_12*;
```


Install `pg_fact_loader` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pg-fact-loader;
apt install postgresql-16-pg-fact-loader;
apt install postgresql-15-pg-fact-loader;
apt install postgresql-14-pg-fact-loader;
apt install postgresql-13-pg-fact-loader;
apt install postgresql-12-pg-fact-loader;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_fact_loader_17*` | `pg_fact_loader_16*` | `pg_fact_loader_15*` | `pg_fact_loader_14*` | `pg_fact_loader_13*` | `pg_fact_loader_12*` |
| `el9` | `pg_fact_loader_17*` | `pg_fact_loader_16*` | `pg_fact_loader_15*` | `pg_fact_loader_14*` | `pg_fact_loader_13*` | `pg_fact_loader_12*` |
| `d12` | `postgresql-17-pg-fact-loader` | `postgresql-16-pg-fact-loader` | `postgresql-15-pg-fact-loader` | `postgresql-14-pg-fact-loader` | `postgresql-13-pg-fact-loader` | `postgresql-12-pg-fact-loader` |
| `u22` | `postgresql-17-pg-fact-loader` | `postgresql-16-pg-fact-loader` | `postgresql-15-pg-fact-loader` | `postgresql-14-pg-fact-loader` | `postgresql-13-pg-fact-loader` | `postgresql-12-pg-fact-loader` |
| `u24` | `postgresql-17-pg-fact-loader` | `postgresql-16-pg-fact-loader` | `postgresql-15-pg-fact-loader` | `postgresql-14-pg-fact-loader` | `postgresql-13-pg-fact-loader` | `postgresql-12-pg-fact-loader` |






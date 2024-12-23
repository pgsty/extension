# pg_bulkload


> [pg_bulkload](https://github.com/ossc-db/pg_bulkload): pg_bulkload is a high speed data loading utility for PostgreSQL
>
> https://github.com/ossc-db/pg_bulkload





[ETL](/etl) extensions: [`pglogical`](/pglogical), [`pglogical_origin`](/pglogical_origin), [`pglogical_ticker`](/pglogical_ticker), [`pgl_ddl_deploy`](/pgl_ddl_deploy), [`pg_failover_slots`](/pg_failover_slots), [`wal2json`](/wal2json), [`wal2mongo`](/wal2mongo), [`decoderbufs`](/decoderbufs), [`decoder_raw`](/decoder_raw), [`pgoutput`](/pgoutput), [`test_decoding`](/test_decoding), [`mimeo`](/mimeo), [`repmgr`](/repmgr), [`pg_fact_loader`](/pg_fact_loader), [`pg_bulkload`](/pg_bulkload)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_bulkload](https://github.com/ossc-db/pg_bulkload) | 3.1.21 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| **<span class="tcwarn">✔</span>** |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_bulkload](/pg_bulkload) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcred">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcred">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcred">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcred">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcred">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_bulkload;
```
> **Comment**: pg17 not ready yet
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 3.1.21 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `pg_bulkload_$v*` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 3.1.21 | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-bulkload` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pg_bulkload` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_bulkload
```


Install `pg_bulkload` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_bulkload"]}'
```


Install `pg_bulkload` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pg_bulkload_16*;
dnf install pg_bulkload_15*;
dnf install pg_bulkload_14*;
dnf install pg_bulkload_13*;
dnf install pg_bulkload_12*;
```


Install `pg_bulkload` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-16-pg-bulkload;
apt install postgresql-15-pg-bulkload;
apt install postgresql-14-pg-bulkload;
apt install postgresql-13-pg-bulkload;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcred">✘</span> | `pg_bulkload_16*` | `pg_bulkload_15*` | `pg_bulkload_14*` | `pg_bulkload_13*` |
| `el9` | <span class="tcred">✘</span> | `pg_bulkload_16*` | `pg_bulkload_15*` | `pg_bulkload_14*` | `pg_bulkload_13*` |
| `d12` | <span class="tcred">✘</span> | `postgresql-16-pg-bulkload` | `postgresql-15-pg-bulkload` | `postgresql-14-pg-bulkload` | `postgresql-13-pg-bulkload` |
| `u22` | <span class="tcred">✘</span> | `postgresql-16-pg-bulkload` | `postgresql-15-pg-bulkload` | `postgresql-14-pg-bulkload` | `postgresql-13-pg-bulkload` |
| `u24` | <span class="tcred">✘</span> | `postgresql-16-pg-bulkload` | `postgresql-15-pg-bulkload` | `postgresql-14-pg-bulkload` | `postgresql-13-pg-bulkload` |






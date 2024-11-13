# pg_bulkload


> [pg_bulkload](https://github.com/ossc-db/pg_bulkload): pg_bulkload is a high speed data loading utility for PostgreSQL
>
> https://github.com/ossc-db/pg_bulkload





[ETL](/etl) extensions: [`pglogical`](/pglogical), [`pglogical_origin`](/pglogical_origin), [`pglogical_ticker`](/pglogical_ticker), [`pgl_ddl_deploy`](/pgl_ddl_deploy), [`pg_failover_slots`](/pg_failover_slots), [`wal2json`](/wal2json), [`wal2mongo`](/wal2mongo), [`decoderbufs`](/decoderbufs), [`decoder_raw`](/decoder_raw), [`test_decoding`](/test_decoding), [`mimeo`](/mimeo), [`repmgr`](/repmgr), [`pg_fact_loader`](/pg_fact_loader), [`pg_bulkload`](/pg_bulkload)


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



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_bulkload;
```
> **Comment**: pg17 not ready yet
-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_bulkload_17*` | `pg_bulkload_16*` | `pg_bulkload_15*` | `pg_bulkload_14*` | `pg_bulkload_13*` | `pg_bulkload_12*` |
| `el9` | `pg_bulkload_17*` | `pg_bulkload_16*` | `pg_bulkload_15*` | `pg_bulkload_14*` | `pg_bulkload_13*` | `pg_bulkload_12*` |
| `d12` | `postgresql-17-pg-bulkload` | `postgresql-16-pg-bulkload` | `postgresql-15-pg-bulkload` | `postgresql-14-pg-bulkload` | `postgresql-13-pg-bulkload` | `postgresql-12-pg-bulkload` |
| `u22` | `postgresql-17-pg-bulkload` | `postgresql-16-pg-bulkload` | `postgresql-15-pg-bulkload` | `postgresql-14-pg-bulkload` | `postgresql-13-pg-bulkload` | `postgresql-12-pg-bulkload` |
| `u24` | `postgresql-17-pg-bulkload` | `postgresql-16-pg-bulkload` | `postgresql-15-pg-bulkload` | `postgresql-14-pg-bulkload` | `postgresql-13-pg-bulkload` | `postgresql-12-pg-bulkload` |



Install `pg_bulkload` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_bulkload"]}'
```


Install `pg_bulkload` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install pg_bulkload_17*;
yum install pg_bulkload_16*;
yum install pg_bulkload_15*;
yum install pg_bulkload_14*;
yum install pg_bulkload_13*;
yum install pg_bulkload_12*;
```


Install `pg_bulkload` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pg-bulkload;
apt install postgresql-16-pg-bulkload;
apt install postgresql-15-pg-bulkload;
apt install postgresql-14-pg-bulkload;
apt install postgresql-13-pg-bulkload;
apt install postgresql-12-pg-bulkload;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_bulkload_17*` | `pg_bulkload_16*` | `pg_bulkload_15*` | `pg_bulkload_14*` | `pg_bulkload_13*` | `pg_bulkload_12*` |
| `el9` | `pg_bulkload_17*` | `pg_bulkload_16*` | `pg_bulkload_15*` | `pg_bulkload_14*` | `pg_bulkload_13*` | `pg_bulkload_12*` |
| `d12` | `postgresql-17-pg-bulkload` | `postgresql-16-pg-bulkload` | `postgresql-15-pg-bulkload` | `postgresql-14-pg-bulkload` | `postgresql-13-pg-bulkload` | `postgresql-12-pg-bulkload` |
| `u22` | `postgresql-17-pg-bulkload` | `postgresql-16-pg-bulkload` | `postgresql-15-pg-bulkload` | `postgresql-14-pg-bulkload` | `postgresql-13-pg-bulkload` | `postgresql-12-pg-bulkload` |
| `u24` | `postgresql-17-pg-bulkload` | `postgresql-16-pg-bulkload` | `postgresql-15-pg-bulkload` | `postgresql-14-pg-bulkload` | `postgresql-13-pg-bulkload` | `postgresql-12-pg-bulkload` |






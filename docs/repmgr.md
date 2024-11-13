# repmgr


> [repmgr](https://github.com/EnterpriseDB/repmgr): Replication manager for PostgreSQL
>
> https://github.com/EnterpriseDB/repmgr





[ETL](/etl) extensions: [`pglogical`](/pglogical), [`pglogical_origin`](/pglogical_origin), [`pglogical_ticker`](/pglogical_ticker), [`pgl_ddl_deploy`](/pgl_ddl_deploy), [`pg_failover_slots`](/pg_failover_slots), [`wal2json`](/wal2json), [`wal2mongo`](/wal2mongo), [`decoderbufs`](/decoderbufs), [`decoder_raw`](/decoder_raw), [`test_decoding`](/test_decoding), [`mimeo`](/mimeo), [`repmgr`](/repmgr), [`pg_fact_loader`](/pg_fact_loader), [`pg_bulkload`](/pg_bulkload)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [repmgr](https://github.com/EnterpriseDB/repmgr) | 5.4 | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [repmgr](/repmgr) | `not-used` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION repmgr;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `repmgr_17*` | `repmgr_16*` | `repmgr_15*` | `repmgr_14*` | `repmgr_13*` | `repmgr_12*` |
| `el9` | `repmgr_17*` | `repmgr_16*` | `repmgr_15*` | `repmgr_14*` | `repmgr_13*` | `repmgr_12*` |
| `d12` | `postgresql-17-repmgr` | `postgresql-16-repmgr` | `postgresql-15-repmgr` | `postgresql-14-repmgr` | `postgresql-13-repmgr` | `postgresql-12-repmgr` |
| `u22` | `postgresql-17-repmgr` | `postgresql-16-repmgr` | `postgresql-15-repmgr` | `postgresql-14-repmgr` | `postgresql-13-repmgr` | `postgresql-12-repmgr` |
| `u24` | `postgresql-17-repmgr` | `postgresql-16-repmgr` | `postgresql-15-repmgr` | `postgresql-14-repmgr` | `postgresql-13-repmgr` | `postgresql-12-repmgr` |



Install `repmgr` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["repmgr"]}'
```


Install `repmgr` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install repmgr_17*;
yum install repmgr_16*;
yum install repmgr_15*;
yum install repmgr_14*;
yum install repmgr_13*;
yum install repmgr_12*;
```


Install `repmgr` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-repmgr;
apt install postgresql-16-repmgr;
apt install postgresql-15-repmgr;
apt install postgresql-14-repmgr;
apt install postgresql-13-repmgr;
apt install postgresql-12-repmgr;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `repmgr_17*` | `repmgr_16*` | `repmgr_15*` | `repmgr_14*` | `repmgr_13*` | `repmgr_12*` |
| `el9` | `repmgr_17*` | `repmgr_16*` | `repmgr_15*` | `repmgr_14*` | `repmgr_13*` | `repmgr_12*` |
| `d12` | `postgresql-17-repmgr` | `postgresql-16-repmgr` | `postgresql-15-repmgr` | `postgresql-14-repmgr` | `postgresql-13-repmgr` | `postgresql-12-repmgr` |
| `u22` | `postgresql-17-repmgr` | `postgresql-16-repmgr` | `postgresql-15-repmgr` | `postgresql-14-repmgr` | `postgresql-13-repmgr` | `postgresql-12-repmgr` |
| `u24` | `postgresql-17-repmgr` | `postgresql-16-repmgr` | `postgresql-15-repmgr` | `postgresql-14-repmgr` | `postgresql-13-repmgr` | `postgresql-12-repmgr` |






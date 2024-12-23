# repmgr


> [repmgr](https://github.com/EnterpriseDB/repmgr): Replication manager for PostgreSQL
>
> https://github.com/EnterpriseDB/repmgr





[ETL](/etl) extensions: [`pglogical`](/pglogical), [`pglogical_origin`](/pglogical_origin), [`pglogical_ticker`](/pglogical_ticker), [`pgl_ddl_deploy`](/pgl_ddl_deploy), [`pg_failover_slots`](/pg_failover_slots), [`wal2json`](/wal2json), [`wal2mongo`](/wal2mongo), [`decoderbufs`](/decoderbufs), [`decoder_raw`](/decoder_raw), [`pgoutput`](/pgoutput), [`test_decoding`](/test_decoding), [`mimeo`](/mimeo), [`repmgr`](/repmgr), [`pg_fact_loader`](/pg_fact_loader), [`pg_bulkload`](/pg_bulkload)


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



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcred">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcred">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcred">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcred">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcred">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION repmgr;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 5.4 | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | `repmgr_$v*` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 5.4 | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-repmgr` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `repmgr` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add repmgr
```


Install `repmgr` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["repmgr"]}'
```


Install `repmgr` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install repmgr_16*;
dnf install repmgr_15*;
dnf install repmgr_14*;
dnf install repmgr_13*;
dnf install repmgr_12*;
```


Install `repmgr` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-16-repmgr;
apt install postgresql-15-repmgr;
apt install postgresql-14-repmgr;
apt install postgresql-13-repmgr;
apt install postgresql-12-repmgr;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcred">✘</span> | `repmgr_16*` | `repmgr_15*` | `repmgr_14*` | `repmgr_13*` |
| `el9` | <span class="tcred">✘</span> | `repmgr_16*` | `repmgr_15*` | `repmgr_14*` | `repmgr_13*` |
| `d12` | <span class="tcred">✘</span> | `postgresql-16-repmgr` | `postgresql-15-repmgr` | `postgresql-14-repmgr` | `postgresql-13-repmgr` |
| `u22` | <span class="tcred">✘</span> | `postgresql-16-repmgr` | `postgresql-15-repmgr` | `postgresql-14-repmgr` | `postgresql-13-repmgr` |
| `u24` | <span class="tcred">✘</span> | `postgresql-16-repmgr` | `postgresql-15-repmgr` | `postgresql-14-repmgr` | `postgresql-13-repmgr` |






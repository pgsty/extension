# pglogical_ticker


> [pglogical_ticker](https://github.com/enova/pglogical_ticker): Have an accurate view on pglogical replication delay
>
> https://github.com/enova/pglogical_ticker





[ETL](/etl) extensions: [`pglogical`](/pglogical), [`pglogical_origin`](/pglogical_origin), [`pglogical_ticker`](/pglogical_ticker), [`pgl_ddl_deploy`](/pgl_ddl_deploy), [`pg_failover_slots`](/pg_failover_slots), [`db_migrator`](/db_migrator), [`wal2json`](/wal2json), [`wal2mongo`](/wal2mongo), [`decoderbufs`](/decoderbufs), [`decoder_raw`](/decoder_raw), [`pgoutput`](/pgoutput), [`test_decoding`](/test_decoding), [`mimeo`](/mimeo), [`repmgr`](/repmgr), [`pg_fact_loader`](/pg_fact_loader), [`pg_bulkload`](/pg_bulkload)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pglogical_ticker](https://github.com/enova/pglogical_ticker) | 1.4.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pglogical_ticker](/pglogical_ticker) |  | `pglogical_ticker` | [`pglogical`](pglogical) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'pglogical_ticker'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION pglogical_ticker CASCADE;
```
> **Comment**: require a patch on el
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.4.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pglogical_ticker_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | `pglogical_$v` |
| [DEB](/deb) | 1.4.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pglogical-ticker` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | `postgresql-$v-pglogical` |



Install `pglogical_ticker` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pglogical_ticker
```


Install `pglogical_ticker` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pglogical_ticker"]}'
```


Install `pglogical_ticker` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pglogical_ticker_17*;
dnf install pglogical_ticker_16*;
dnf install pglogical_ticker_15*;
dnf install pglogical_ticker_14*;
dnf install pglogical_ticker_13*;
```


Install `pglogical_ticker` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pglogical-ticker;
apt install postgresql-16-pglogical-ticker;
apt install postgresql-15-pglogical-ticker;
apt install postgresql-14-pglogical-ticker;
apt install postgresql-13-pglogical-ticker;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pglogical_ticker_17*` | `pglogical_ticker_16*` | `pglogical_ticker_15*` | `pglogical_ticker_14*` | `pglogical_ticker_13*` |
| `el9` | `pglogical_ticker_17*` | `pglogical_ticker_16*` | `pglogical_ticker_15*` | `pglogical_ticker_14*` | `pglogical_ticker_13*` |
| `d12` | `postgresql-17-pglogical-ticker` | `postgresql-16-pglogical-ticker` | `postgresql-15-pglogical-ticker` | `postgresql-14-pglogical-ticker` | `postgresql-13-pglogical-ticker` |
| `u22` | `postgresql-17-pglogical-ticker` | `postgresql-16-pglogical-ticker` | `postgresql-15-pglogical-ticker` | `postgresql-14-pglogical-ticker` | `postgresql-13-pglogical-ticker` |
| `u24` | `postgresql-17-pglogical-ticker` | `postgresql-16-pglogical-ticker` | `postgresql-15-pglogical-ticker` | `postgresql-14-pglogical-ticker` | `postgresql-13-pglogical-ticker` |






# pglogical_ticker


> [pglogical_ticker](https://github.com/enova/pglogical_ticker): Have an accurate view on pglogical replication delay
>
> https://github.com/enova/pglogical_ticker





[ETL](/etl) extensions: [`pglogical`](/pglogical), [`pglogical_origin`](/pglogical_origin), [`pglogical_ticker`](/pglogical_ticker), [`pgl_ddl_deploy`](/pgl_ddl_deploy), [`pg_failover_slots`](/pg_failover_slots), [`wal2json`](/wal2json), [`wal2mongo`](/wal2mongo), [`decoderbufs`](/decoderbufs), [`decoder_raw`](/decoder_raw), [`test_decoding`](/test_decoding), [`mimeo`](/mimeo), [`repmgr`](/repmgr), [`pg_fact_loader`](/pg_fact_loader), [`pg_bulkload`](/pg_bulkload)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [pglogical_ticker](https://github.com/enova/pglogical_ticker) | 1.4 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** | `C` |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Package | Tags | Schemas | Requires | Required by |
|---------|------|---------|----------|-------------|
| [pglogical_ticker](/pglogical_ticker) |  | `pglogical_ticker` | [`pglogical`](pglogical) |  |



```bash
shared_preload_libraries = 'pglogical_ticker'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION pglogical_ticker CASCADE;
```
> **Comment**: require a patch on el
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.4.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pglogical_ticker_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | `pglogical_$v` |
| [DEB](/deb) | 1.4 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pglogical-ticker` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | `postgresql-$v-pglogical` |



Install `pglogical_ticker` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

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
dnf install pglogical_ticker_12*;
```


Install `pglogical_ticker` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pglogical-ticker;
apt install postgresql-16-pglogical-ticker;
apt install postgresql-15-pglogical-ticker;
apt install postgresql-14-pglogical-ticker;
apt install postgresql-13-pglogical-ticker;
apt install postgresql-12-pglogical-ticker;
```








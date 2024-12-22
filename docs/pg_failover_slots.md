# pg_failover_slots


> [pg_failover_slots](https://github.com/EnterpriseDB/pg_failover_slots): PG Failover Slots extension
>
> https://github.com/EnterpriseDB/pg_failover_slots





[ETL](/etl) extensions: [`pglogical`](/pglogical), [`pglogical_origin`](/pglogical_origin), [`pglogical_ticker`](/pglogical_ticker), [`pgl_ddl_deploy`](/pgl_ddl_deploy), [`pg_failover_slots`](/pg_failover_slots), [`wal2json`](/wal2json), [`wal2mongo`](/wal2mongo), [`decoderbufs`](/decoderbufs), [`decoder_raw`](/decoder_raw), [`pgoutput`](/pgoutput), [`test_decoding`](/test_decoding), [`mimeo`](/mimeo), [`repmgr`](/repmgr), [`pg_fact_loader`](/pg_fact_loader), [`pg_bulkload`](/pg_bulkload)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_failover_slots](https://github.com/EnterpriseDB/pg_failover_slots) | 1.0.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_failover_slots](/pg_failover_slots) | `nil-lic` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'pg_failover_slots'; # add this extension to postgresql.conf
```



-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_failover_slots_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.0.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-failover-slots` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pg_failover_slots` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_failover_slots"]}'
```


Install `pg_failover_slots` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_failover_slots_17*;
dnf install pg_failover_slots_16*;
dnf install pg_failover_slots_15*;
dnf install pg_failover_slots_14*;
dnf install pg_failover_slots_13*;
dnf install pg_failover_slots_12*;
```


Install `pg_failover_slots` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-failover-slots;
apt install postgresql-16-pg-failover-slots;
apt install postgresql-15-pg-failover-slots;
apt install postgresql-14-pg-failover-slots;
apt install postgresql-13-pg-failover-slots;
apt install postgresql-12-pg-failover-slots;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_failover_slots_17*` | `pg_failover_slots_16*` | `pg_failover_slots_15*` | `pg_failover_slots_14*` | `pg_failover_slots_13*` | `pg_failover_slots_12*` |
| `el9` | `pg_failover_slots_17*` | `pg_failover_slots_16*` | `pg_failover_slots_15*` | `pg_failover_slots_14*` | `pg_failover_slots_13*` | `pg_failover_slots_12*` |
| `d12` | `postgresql-17-pg-failover-slots` | `postgresql-16-pg-failover-slots` | `postgresql-15-pg-failover-slots` | `postgresql-14-pg-failover-slots` | `postgresql-13-pg-failover-slots` | `postgresql-12-pg-failover-slots` |
| `u22` | `postgresql-17-pg-failover-slots` | `postgresql-16-pg-failover-slots` | `postgresql-15-pg-failover-slots` | `postgresql-14-pg-failover-slots` | `postgresql-13-pg-failover-slots` | `postgresql-12-pg-failover-slots` |
| `u24` | `postgresql-17-pg-failover-slots` | `postgresql-16-pg-failover-slots` | `postgresql-15-pg-failover-slots` | `postgresql-14-pg-failover-slots` | `postgresql-13-pg-failover-slots` | `postgresql-12-pg-failover-slots` |






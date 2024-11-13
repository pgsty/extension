# wal2mongo


> [wal2mongo](https://github.com/HighgoSoftware/wal2mongo): PostgreSQL logical decoding output plugin for MongoDB
>
> https://github.com/HighgoSoftware/wal2mongo





[ETL](/etl) extensions: [`pglogical`](/pglogical), [`pglogical_origin`](/pglogical_origin), [`pglogical_ticker`](/pglogical_ticker), [`pgl_ddl_deploy`](/pgl_ddl_deploy), [`pg_failover_slots`](/pg_failover_slots), [`wal2json`](/wal2json), [`wal2mongo`](/wal2mongo), [`decoderbufs`](/decoderbufs), [`decoder_raw`](/decoder_raw), [`test_decoding`](/test_decoding), [`mimeo`](/mimeo), [`repmgr`](/repmgr), [`pg_fact_loader`](/pg_fact_loader), [`pg_bulkload`](/pg_bulkload)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [wal2mongo](https://github.com/HighgoSoftware/wal2mongo) | 1.0.7 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [wal2mongo](/wal2mongo) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `wal2mongo_17*` | `wal2mongo_16*` | `wal2mongo_15*` | `wal2mongo_14*` | `wal2mongo_13*` | `wal2mongo_12*` |
| `el9` | `wal2mongo_17*` | `wal2mongo_16*` | `wal2mongo_15*` | `wal2mongo_14*` | `wal2mongo_13*` | `wal2mongo_12*` |
| `d12` | `postgresql-17-wal2mongo` | `postgresql-16-wal2mongo` | `postgresql-15-wal2mongo` | `postgresql-14-wal2mongo` | `postgresql-13-wal2mongo` | `postgresql-12-wal2mongo` |
| `u22` | `postgresql-17-wal2mongo` | `postgresql-16-wal2mongo` | `postgresql-15-wal2mongo` | `postgresql-14-wal2mongo` | `postgresql-13-wal2mongo` | `postgresql-12-wal2mongo` |
| `u24` | `postgresql-17-wal2mongo` | `postgresql-16-wal2mongo` | `postgresql-15-wal2mongo` | `postgresql-14-wal2mongo` | `postgresql-13-wal2mongo` | `postgresql-12-wal2mongo` |



Install `wal2mongo` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["wal2mongo"]}'
```


Install `wal2mongo` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install wal2mongo_17*;
yum install wal2mongo_16*;
yum install wal2mongo_15*;
yum install wal2mongo_14*;
yum install wal2mongo_13*;
yum install wal2mongo_12*;
```


Install `wal2mongo` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-wal2mongo;
apt install postgresql-16-wal2mongo;
apt install postgresql-15-wal2mongo;
apt install postgresql-14-wal2mongo;
apt install postgresql-13-wal2mongo;
apt install postgresql-12-wal2mongo;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `wal2mongo_17*` | `wal2mongo_16*` | `wal2mongo_15*` | `wal2mongo_14*` | `wal2mongo_13*` | `wal2mongo_12*` |
| `el9` | `wal2mongo_17*` | `wal2mongo_16*` | `wal2mongo_15*` | `wal2mongo_14*` | `wal2mongo_13*` | `wal2mongo_12*` |
| `d12` | `postgresql-17-wal2mongo` | `postgresql-16-wal2mongo` | `postgresql-15-wal2mongo` | `postgresql-14-wal2mongo` | `postgresql-13-wal2mongo` | `postgresql-12-wal2mongo` |
| `u22` | `postgresql-17-wal2mongo` | `postgresql-16-wal2mongo` | `postgresql-15-wal2mongo` | `postgresql-14-wal2mongo` | `postgresql-13-wal2mongo` | `postgresql-12-wal2mongo` |
| `u24` | `postgresql-17-wal2mongo` | `postgresql-16-wal2mongo` | `postgresql-15-wal2mongo` | `postgresql-14-wal2mongo` | `postgresql-13-wal2mongo` | `postgresql-12-wal2mongo` |






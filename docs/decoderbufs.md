# decoderbufs


> [decoderbufs](https://github.com/debezium/postgres-decoderbufs): Logical decoding plugin that delivers WAL stream changes using a Protocol Buffer format
>
> https://github.com/debezium/postgres-decoderbufs





[ETL](/etl) extensions: [`pglogical`](/pglogical), [`pglogical_origin`](/pglogical_origin), [`pglogical_ticker`](/pglogical_ticker), [`pgl_ddl_deploy`](/pgl_ddl_deploy), [`pg_failover_slots`](/pg_failover_slots), [`wal2json`](/wal2json), [`wal2mongo`](/wal2mongo), [`decoderbufs`](/decoderbufs), [`decoder_raw`](/decoder_raw), [`test_decoding`](/test_decoding), [`mimeo`](/mimeo), [`repmgr`](/repmgr), [`pg_fact_loader`](/pg_fact_loader), [`pg_bulkload`](/pg_bulkload)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [decoderbufs](https://github.com/debezium/postgres-decoderbufs) | 0.1.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [decoderbufs](/decoderbufs) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.1.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `postgres-decoderbufs_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 0.1.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-decoderbufs` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `decoderbufs` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["decoderbufs"]}'
```


Install `decoderbufs` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install postgres-decoderbufs_17*;
yum install postgres-decoderbufs_16*;
yum install postgres-decoderbufs_15*;
yum install postgres-decoderbufs_14*;
yum install postgres-decoderbufs_13*;
yum install postgres-decoderbufs_12*;
```


Install `decoderbufs` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-decoderbufs;
apt install postgresql-16-decoderbufs;
apt install postgresql-15-decoderbufs;
apt install postgresql-14-decoderbufs;
apt install postgresql-13-decoderbufs;
apt install postgresql-12-decoderbufs;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `postgres-decoderbufs_17*` | `postgres-decoderbufs_16*` | `postgres-decoderbufs_15*` | `postgres-decoderbufs_14*` | `postgres-decoderbufs_13*` | `postgres-decoderbufs_12*` |
| `el9` | `postgres-decoderbufs_17*` | `postgres-decoderbufs_16*` | `postgres-decoderbufs_15*` | `postgres-decoderbufs_14*` | `postgres-decoderbufs_13*` | `postgres-decoderbufs_12*` |
| `d12` | `postgresql-17-decoderbufs` | `postgresql-16-decoderbufs` | `postgresql-15-decoderbufs` | `postgresql-14-decoderbufs` | `postgresql-13-decoderbufs` | `postgresql-12-decoderbufs` |
| `u22` | `postgresql-17-decoderbufs` | `postgresql-16-decoderbufs` | `postgresql-15-decoderbufs` | `postgresql-14-decoderbufs` | `postgresql-13-decoderbufs` | `postgresql-12-decoderbufs` |
| `u24` | `postgresql-17-decoderbufs` | `postgresql-16-decoderbufs` | `postgresql-15-decoderbufs` | `postgresql-14-decoderbufs` | `postgresql-13-decoderbufs` | `postgresql-12-decoderbufs` |






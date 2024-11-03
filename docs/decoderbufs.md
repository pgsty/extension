# decoderbufs


> [decoderbufs](https://github.com/debezium/postgres-decoderbufs): Logical decoding plugin that delivers WAL stream changes using a Protocol Buffer format
>
> https://github.com/debezium/postgres-decoderbufs





[ETL](/etl) extensions: [`pglogical`](/pglogical), [`pglogical_origin`](/pglogical_origin), [`pglogical_ticker`](/pglogical_ticker), [`pgl_ddl_deploy`](/pgl_ddl_deploy), [`pg_failover_slots`](/pg_failover_slots), [`wal2json`](/wal2json), [`wal2mongo`](/wal2mongo), [`decoderbufs`](/decoderbufs), [`decoder_raw`](/decoder_raw), [`test_decoding`](/test_decoding), [`mimeo`](/mimeo), [`repmgr`](/repmgr), [`pg_fact_loader`](/pg_fact_loader), [`pg_bulkload`](/pg_bulkload)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [decoderbufs](https://github.com/debezium/postgres-decoderbufs) | 0.1.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |



| Package | Tags | Schemas | Requires | Required by |
|---------|------|---------|----------|-------------|
| [decoderbufs](/decoderbufs) |  |  |  |  |





-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.1.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `postgres-decoderbufs_$v*` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 0.1.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-decoderbufs` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `decoderbufs` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["decoderbufs"]}'
```


Install `decoderbufs` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install postgres-decoderbufs_16*;
dnf install postgres-decoderbufs_15*;
dnf install postgres-decoderbufs_14*;
dnf install postgres-decoderbufs_13*;
dnf install postgres-decoderbufs_12*;
```


Install `decoderbufs` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-16-decoderbufs;
apt install postgresql-15-decoderbufs;
apt install postgresql-14-decoderbufs;
apt install postgresql-13-decoderbufs;
apt install postgresql-12-decoderbufs;
```








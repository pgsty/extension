# decoder_raw


> [decoder_raw](https://github.com/michaelpq/pg_plugins/blob/main/decoder_raw/): Output plugin for logical replication in Raw SQL format
>
> https://github.com/michaelpq/pg_plugins/blob/main/decoder_raw/





[ETL](/etl) extensions: [`pglogical`](/pglogical), [`pglogical_origin`](/pglogical_origin), [`pglogical_ticker`](/pglogical_ticker), [`pgl_ddl_deploy`](/pgl_ddl_deploy), [`pg_failover_slots`](/pg_failover_slots), [`wal2json`](/wal2json), [`wal2mongo`](/wal2mongo), [`decoderbufs`](/decoderbufs), [`decoder_raw`](/decoder_raw), [`test_decoding`](/test_decoding), [`mimeo`](/mimeo), [`repmgr`](/repmgr), [`pg_fact_loader`](/pg_fact_loader), [`pg_bulkload`](/pg_bulkload)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [decoder_raw](https://github.com/michaelpq/pg_plugins/blob/main/decoder_raw/) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [decoder_raw](/decoder_raw) |  |  |  |  |



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
| [RPM](/rpm) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `decoder_raw_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-decoder-raw` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `decoder_raw` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["decoder_raw"]}'
```


Install `decoder_raw` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install decoder_raw_17*;
yum install decoder_raw_16*;
yum install decoder_raw_15*;
yum install decoder_raw_14*;
yum install decoder_raw_13*;
yum install decoder_raw_12*;
```


Install `decoder_raw` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-decoder-raw;
apt install postgresql-16-decoder-raw;
apt install postgresql-15-decoder-raw;
apt install postgresql-14-decoder-raw;
apt install postgresql-13-decoder-raw;
apt install postgresql-12-decoder-raw;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `decoder_raw_17*` | `decoder_raw_16*` | `decoder_raw_15*` | `decoder_raw_14*` | `decoder_raw_13*` | `decoder_raw_12*` |
| `el9` | `decoder_raw_17*` | `decoder_raw_16*` | `decoder_raw_15*` | `decoder_raw_14*` | `decoder_raw_13*` | `decoder_raw_12*` |
| `d12` | `postgresql-17-decoder-raw` | `postgresql-16-decoder-raw` | `postgresql-15-decoder-raw` | `postgresql-14-decoder-raw` | `postgresql-13-decoder-raw` | `postgresql-12-decoder-raw` |
| `u22` | `postgresql-17-decoder-raw` | `postgresql-16-decoder-raw` | `postgresql-15-decoder-raw` | `postgresql-14-decoder-raw` | `postgresql-13-decoder-raw` | `postgresql-12-decoder-raw` |
| `u24` | `postgresql-17-decoder-raw` | `postgresql-16-decoder-raw` | `postgresql-15-decoder-raw` | `postgresql-14-decoder-raw` | `postgresql-13-decoder-raw` | `postgresql-12-decoder-raw` |






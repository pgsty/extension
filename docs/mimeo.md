# mimeo


> [mimeo](https://github.com/omniti-labs/mimeo): Extension for specialized, per-table replication between PostgreSQL instances
>
> https://github.com/omniti-labs/mimeo





[ETL](/etl) extensions: [`pglogical`](/pglogical), [`pglogical_origin`](/pglogical_origin), [`pglogical_ticker`](/pglogical_ticker), [`pgl_ddl_deploy`](/pgl_ddl_deploy), [`pg_failover_slots`](/pg_failover_slots), [`wal2json`](/wal2json), [`wal2mongo`](/wal2mongo), [`decoderbufs`](/decoderbufs), [`decoder_raw`](/decoder_raw), [`test_decoding`](/test_decoding), [`mimeo`](/mimeo), [`repmgr`](/repmgr), [`pg_fact_loader`](/pg_fact_loader), [`pg_bulkload`](/pg_bulkload)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [mimeo](https://github.com/omniti-labs/mimeo) | 1.5.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** | `SQL` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [mimeo](/mimeo) |  |  | [`dblink`](dblink) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION mimeo CASCADE;
```
> **Comment**: name conflict with pg_partman
-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `mimeo_17` | `mimeo_16` | `mimeo_15` | `mimeo_14` | `mimeo_13` | `mimeo_12` |
| `el9` | `mimeo_17` | `mimeo_16` | `mimeo_15` | `mimeo_14` | `mimeo_13` | `mimeo_12` |
| `d12` | `postgresql-17-mimeo` | `postgresql-16-mimeo` | `postgresql-15-mimeo` | `postgresql-14-mimeo` | `postgresql-13-mimeo` | `postgresql-12-mimeo` |
| `u22` | `postgresql-17-mimeo` | `postgresql-16-mimeo` | `postgresql-15-mimeo` | `postgresql-14-mimeo` | `postgresql-13-mimeo` | `postgresql-12-mimeo` |
| `u24` | `postgresql-17-mimeo` | `postgresql-16-mimeo` | `postgresql-15-mimeo` | `postgresql-14-mimeo` | `postgresql-13-mimeo` | `postgresql-12-mimeo` |



Install `mimeo` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["mimeo"]}'
```


Install `mimeo` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install mimeo_17;
yum install mimeo_16;
yum install mimeo_15;
yum install mimeo_14;
yum install mimeo_13;
yum install mimeo_12;
```


Install `mimeo` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-mimeo;
apt install postgresql-16-mimeo;
apt install postgresql-15-mimeo;
apt install postgresql-14-mimeo;
apt install postgresql-13-mimeo;
apt install postgresql-12-mimeo;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `mimeo_17` | `mimeo_16` | `mimeo_15` | `mimeo_14` | `mimeo_13` | `mimeo_12` |
| `el9` | `mimeo_17` | `mimeo_16` | `mimeo_15` | `mimeo_14` | `mimeo_13` | `mimeo_12` |
| `d12` | `postgresql-17-mimeo` | `postgresql-16-mimeo` | `postgresql-15-mimeo` | `postgresql-14-mimeo` | `postgresql-13-mimeo` | `postgresql-12-mimeo` |
| `u22` | `postgresql-17-mimeo` | `postgresql-16-mimeo` | `postgresql-15-mimeo` | `postgresql-14-mimeo` | `postgresql-13-mimeo` | `postgresql-12-mimeo` |
| `u24` | `postgresql-17-mimeo` | `postgresql-16-mimeo` | `postgresql-15-mimeo` | `postgresql-14-mimeo` | `postgresql-13-mimeo` | `postgresql-12-mimeo` |






# pglogical


> [pglogical](https://github.com/2ndQuadrant/pglogical): PostgreSQL Logical Replication
>
> https://github.com/2ndQuadrant/pglogical





[ETL](/etl) extensions: [`pglogical`](/pglogical), [`pglogical_origin`](/pglogical_origin), [`pglogical_ticker`](/pglogical_ticker), [`pgl_ddl_deploy`](/pgl_ddl_deploy), [`pg_failover_slots`](/pg_failover_slots), [`wal2json`](/wal2json), [`wal2mongo`](/wal2mongo), [`decoderbufs`](/decoderbufs), [`decoder_raw`](/decoder_raw), [`pgoutput`](/pgoutput), [`test_decoding`](/test_decoding), [`mimeo`](/mimeo), [`repmgr`](/repmgr), [`pg_fact_loader`](/pg_fact_loader), [`pg_bulkload`](/pg_bulkload)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pglogical](https://github.com/2ndQuadrant/pglogical) | 2.4.5 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pglogical](/pglogical) |  | `pglogical` |  | [`pglogical_ticker`](/pglogical_ticker), [`pgl_ddl_deploy`](/pgl_ddl_deploy) |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pglogical;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 2.4.5 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pglogical_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 2.4.5 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pglogical` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pglogical` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pglogical"]}'
```


Install `pglogical` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pglogical_17*;
dnf install pglogical_16*;
dnf install pglogical_15*;
dnf install pglogical_14*;
dnf install pglogical_13*;
dnf install pglogical_12*;
```


Install `pglogical` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pglogical;
apt install postgresql-16-pglogical;
apt install postgresql-15-pglogical;
apt install postgresql-14-pglogical;
apt install postgresql-13-pglogical;
apt install postgresql-12-pglogical;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pglogical_17*` | `pglogical_16*` | `pglogical_15*` | `pglogical_14*` | `pglogical_13*` | `pglogical_12*` |
| `el9` | `pglogical_17*` | `pglogical_16*` | `pglogical_15*` | `pglogical_14*` | `pglogical_13*` | `pglogical_12*` |
| `d12` | `postgresql-17-pglogical` | `postgresql-16-pglogical` | `postgresql-15-pglogical` | `postgresql-14-pglogical` | `postgresql-13-pglogical` | `postgresql-12-pglogical` |
| `u22` | `postgresql-17-pglogical` | `postgresql-16-pglogical` | `postgresql-15-pglogical` | `postgresql-14-pglogical` | `postgresql-13-pglogical` | `postgresql-12-pglogical` |
| `u24` | `postgresql-17-pglogical` | `postgresql-16-pglogical` | `postgresql-15-pglogical` | `postgresql-14-pglogical` | `postgresql-13-pglogical` | `postgresql-12-pglogical` |






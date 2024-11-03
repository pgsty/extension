# pgl_ddl_deploy


> [pgl_ddl_deploy](https://github.com/enova/pgl_ddl_deploy): automated ddl deployment using pglogical
>
> https://github.com/enova/pgl_ddl_deploy





[ETL](/etl) extensions: [`pglogical`](/pglogical), [`pglogical_origin`](/pglogical_origin), [`pglogical_ticker`](/pglogical_ticker), [`pgl_ddl_deploy`](/pgl_ddl_deploy), [`pg_failover_slots`](/pg_failover_slots), [`wal2json`](/wal2json), [`wal2mongo`](/wal2mongo), [`decoderbufs`](/decoderbufs), [`decoder_raw`](/decoder_raw), [`test_decoding`](/test_decoding), [`mimeo`](/mimeo), [`repmgr`](/repmgr), [`pg_fact_loader`](/pg_fact_loader), [`pg_bulkload`](/pg_bulkload)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [pgl_ddl_deploy](https://github.com/enova/pgl_ddl_deploy) | 2.2 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |



| Package | Tags | Schemas | Requires | Required by |
|---------|------|---------|----------|-------------|
| [pgl_ddl_deploy](/pgl_ddl_deploy) |  | `pgl_ddl_deploy` | [`pglogical`](pglogical) |  |





```sql
CREATE EXTENSION pgl_ddl_deploy CASCADE;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 2.2 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `pgl_ddl_deploy_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | `pglogical_$v` |
| [DEB](/deb) | 2.2 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pgl-ddl-deploy` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | `postgresql-$v-pglogical` |



Install `pgl_ddl_deploy` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgl_ddl_deploy"]}'
```


Install `pgl_ddl_deploy` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pgl_ddl_deploy_17*;
dnf install pgl_ddl_deploy_16*;
dnf install pgl_ddl_deploy_15*;
dnf install pgl_ddl_deploy_14*;
dnf install pgl_ddl_deploy_13*;
dnf install pgl_ddl_deploy_12*;
```


Install `pgl_ddl_deploy` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pgl-ddl-deploy;
apt install postgresql-16-pgl-ddl-deploy;
apt install postgresql-15-pgl-ddl-deploy;
apt install postgresql-14-pgl-ddl-deploy;
apt install postgresql-13-pgl-ddl-deploy;
apt install postgresql-12-pgl-ddl-deploy;
```








# pgnodemx


> [pgnodemx](https://github.com/markwkm/pg_proctab): PostgreSQL extension to access the OS process table
>
> https://github.com/markwkm/pg_proctab





[STAT](/stat) extensions: [`pg_profile`](/pg_profile), [`pg_show_plans`](/pg_show_plans), [`pg_stat_kcache`](/pg_stat_kcache), [`pg_stat_monitor`](/pg_stat_monitor), [`pg_qualstats`](/pg_qualstats), [`pg_store_plans`](/pg_store_plans), [`pg_track_settings`](/pg_track_settings), [`pg_wait_sampling`](/pg_wait_sampling), [`system_stats`](/system_stats), [`meta`](/meta), [`pgnodemx`](/pgnodemx), [`pg_proctab`](/pg_proctab), [`pg_sqlog`](/pg_sqlog), [`bgw_replstatus`](/bgw_replstatus), [`pgmeminfo`](/pgmeminfo), [`toastinfo`](/toastinfo), [`explain_ui`](/explain_ui), [`pg_relusage`](/pg_relusage), [`pagevis`](/pagevis), [`powa`](/powa), [`pageinspect`](/pageinspect), [`pgrowlocks`](/pgrowlocks), [`sslinfo`](/sslinfo), [`pg_buffercache`](/pg_buffercache), [`pg_walinspect`](/pg_walinspect), [`pg_freespacemap`](/pg_freespacemap), [`pg_visibility`](/pg_visibility), [`pgstattuple`](/pgstattuple), [`auto_explain`](/auto_explain), [`pg_stat_statements`](/pg_stat_statements)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_proctab](https://github.com/markwkm/pg_proctab) | 0.0.10-compat | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgnodemx](/pg_proctab) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_proctab;
```
> **Comment**: from pgnodemx
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| Distro-pgnodemx | 1.7 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `pgnodemx_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| Distro-pgnodemx | 1.7 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pgnodemx` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pgnodemx` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgnodemx"]}'
```


Install `pgnodemx` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pgnodemx_17;
dnf install pgnodemx_16;
dnf install pgnodemx_15;
dnf install pgnodemx_14;
dnf install pgnodemx_13;
dnf install pgnodemx_12;
```


Install `pgnodemx` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pgnodemx;
apt install postgresql-16-pgnodemx;
apt install postgresql-15-pgnodemx;
apt install postgresql-14-pgnodemx;
apt install postgresql-13-pgnodemx;
apt install postgresql-12-pgnodemx;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgnodemx_17` | `pgnodemx_16` | `pgnodemx_15` | `pgnodemx_14` | `pgnodemx_13` | `pgnodemx_12` |
| `el9` | `pgnodemx_17` | `pgnodemx_16` | `pgnodemx_15` | `pgnodemx_14` | `pgnodemx_13` | `pgnodemx_12` |
| `d12` | `postgresql-17-pgnodemx` | `postgresql-16-pgnodemx` | `postgresql-15-pgnodemx` | `postgresql-14-pgnodemx` | `postgresql-13-pgnodemx` | `postgresql-12-pgnodemx` |
| `u22` | `postgresql-17-pgnodemx` | `postgresql-16-pgnodemx` | `postgresql-15-pgnodemx` | `postgresql-14-pgnodemx` | `postgresql-13-pgnodemx` | `postgresql-12-pgnodemx` |
| `u24` | `postgresql-17-pgnodemx` | `postgresql-16-pgnodemx` | `postgresql-15-pgnodemx` | `postgresql-14-pgnodemx` | `postgresql-13-pgnodemx` | `postgresql-12-pgnodemx` |






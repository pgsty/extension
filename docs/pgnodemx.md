# pgnodemx


> [pgnodemx](https://github.com/CrunchyData/pgnodemx): Capture node OS metrics via SQL queries
>
> https://github.com/CrunchyData/pgnodemx





[STAT](/stat) extensions: [`pg_profile`](/pg_profile), [`pg_show_plans`](/pg_show_plans), [`pg_stat_kcache`](/pg_stat_kcache), [`pg_stat_monitor`](/pg_stat_monitor), [`pg_qualstats`](/pg_qualstats), [`pg_store_plans`](/pg_store_plans), [`pg_track_settings`](/pg_track_settings), [`pg_wait_sampling`](/pg_wait_sampling), [`system_stats`](/system_stats), [`meta`](/meta), [`pgnodemx`](/pgnodemx), [`pg_proctab`](/pg_proctab), [`pg_sqlog`](/pg_sqlog), [`bgw_replstatus`](/bgw_replstatus), [`pgmeminfo`](/pgmeminfo), [`toastinfo`](/toastinfo), [`explain_ui`](/explain_ui), [`pg_relusage`](/pg_relusage), [`pg_top`](/pg_top), [`pagevis`](/pagevis), [`powa`](/powa), [`pageinspect`](/pageinspect), [`pgrowlocks`](/pgrowlocks), [`sslinfo`](/sslinfo), [`pg_buffercache`](/pg_buffercache), [`pg_walinspect`](/pg_walinspect), [`pg_freespacemap`](/pg_freespacemap), [`pg_visibility`](/pg_visibility), [`pgstattuple`](/pgstattuple), [`auto_explain`](/auto_explain), [`pg_stat_statements`](/pg_stat_statements)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgnodemx](https://github.com/CrunchyData/pgnodemx) | 1.7 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgnodemx](/pgnodemx) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pgnodemx;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgnodemx_17` | `pgnodemx_16` | `pgnodemx_15` | `pgnodemx_14` | `pgnodemx_13` | `pgnodemx_12` |
| `el9` | `pgnodemx_17` | `pgnodemx_16` | `pgnodemx_15` | `pgnodemx_14` | `pgnodemx_13` | `pgnodemx_12` |
| `d12` | `postgresql-17-pgnodemx` | `postgresql-16-pgnodemx` | `postgresql-15-pgnodemx` | `postgresql-14-pgnodemx` | `postgresql-13-pgnodemx` | `postgresql-12-pgnodemx` |
| `u22` | `postgresql-17-pgnodemx` | `postgresql-16-pgnodemx` | `postgresql-15-pgnodemx` | `postgresql-14-pgnodemx` | `postgresql-13-pgnodemx` | `postgresql-12-pgnodemx` |
| `u24` | `postgresql-17-pgnodemx` | `postgresql-16-pgnodemx` | `postgresql-15-pgnodemx` | `postgresql-14-pgnodemx` | `postgresql-13-pgnodemx` | `postgresql-12-pgnodemx` |



Install `pgnodemx` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgnodemx"]}'
```


Install `pgnodemx` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install pgnodemx_17;
yum install pgnodemx_16;
yum install pgnodemx_15;
yum install pgnodemx_14;
yum install pgnodemx_13;
yum install pgnodemx_12;
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






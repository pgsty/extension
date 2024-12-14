# pg_qualstats


> [pg_qualstats](https://github.com/powa-team/pg_qualstats): An extension collecting statistics about quals
>
> https://github.com/powa-team/pg_qualstats





[STAT](/stat) extensions: [`pg_profile`](/pg_profile), [`pg_show_plans`](/pg_show_plans), [`pg_stat_kcache`](/pg_stat_kcache), [`pg_stat_monitor`](/pg_stat_monitor), [`pg_qualstats`](/pg_qualstats), [`pg_store_plans`](/pg_store_plans), [`pg_track_settings`](/pg_track_settings), [`pg_wait_sampling`](/pg_wait_sampling), [`system_stats`](/system_stats), [`meta`](/meta), [`pgnodemx`](/pgnodemx), [`pg_proctab`](/pg_proctab), [`pg_sqlog`](/pg_sqlog), [`bgw_replstatus`](/bgw_replstatus), [`pgmeminfo`](/pgmeminfo), [`toastinfo`](/toastinfo), [`explain_ui`](/explain_ui), [`pg_relusage`](/pg_relusage), [`pg_top`](/pg_top), [`pagevis`](/pagevis), [`powa`](/powa), [`pageinspect`](/pageinspect), [`pgrowlocks`](/pgrowlocks), [`sslinfo`](/sslinfo), [`pg_buffercache`](/pg_buffercache), [`pg_walinspect`](/pg_walinspect), [`pg_freespacemap`](/pg_freespacemap), [`pg_visibility`](/pg_visibility), [`pgstattuple`](/pgstattuple), [`auto_explain`](/auto_explain), [`pg_stat_statements`](/pg_stat_statements)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_qualstats](https://github.com/powa-team/pg_qualstats) | 2.1.1 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_qualstats](/pg_qualstats) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'pg_qualstats'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION pg_qualstats;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 2.1.1 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `pg_qualstats_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 2.1.1 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pg-qualstats` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pg_qualstats` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_qualstats"]}'
```


Install `pg_qualstats` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pg_qualstats_17*;
dnf install pg_qualstats_16*;
dnf install pg_qualstats_15*;
dnf install pg_qualstats_14*;
dnf install pg_qualstats_13*;
dnf install pg_qualstats_12*;
```


Install `pg_qualstats` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pg-qualstats;
apt install postgresql-16-pg-qualstats;
apt install postgresql-15-pg-qualstats;
apt install postgresql-14-pg-qualstats;
apt install postgresql-13-pg-qualstats;
apt install postgresql-12-pg-qualstats;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_qualstats_17*` | `pg_qualstats_16*` | `pg_qualstats_15*` | `pg_qualstats_14*` | `pg_qualstats_13*` | `pg_qualstats_12*` |
| `el9` | `pg_qualstats_17*` | `pg_qualstats_16*` | `pg_qualstats_15*` | `pg_qualstats_14*` | `pg_qualstats_13*` | `pg_qualstats_12*` |
| `d12` | `postgresql-17-pg-qualstats` | `postgresql-16-pg-qualstats` | `postgresql-15-pg-qualstats` | `postgresql-14-pg-qualstats` | `postgresql-13-pg-qualstats` | `postgresql-12-pg-qualstats` |
| `u22` | `postgresql-17-pg-qualstats` | `postgresql-16-pg-qualstats` | `postgresql-15-pg-qualstats` | `postgresql-14-pg-qualstats` | `postgresql-13-pg-qualstats` | `postgresql-12-pg-qualstats` |
| `u24` | `postgresql-17-pg-qualstats` | `postgresql-16-pg-qualstats` | `postgresql-15-pg-qualstats` | `postgresql-14-pg-qualstats` | `postgresql-13-pg-qualstats` | `postgresql-12-pg-qualstats` |






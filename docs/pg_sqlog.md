# pg_sqlog


> [pg_sqlog](https://github.com/kouber/pg_sqlog): Provide SQL interface to logs
>
> https://github.com/kouber/pg_sqlog





[STAT](/stat) extensions: [`pg_profile`](/pg_profile), [`pg_show_plans`](/pg_show_plans), [`pg_stat_kcache`](/pg_stat_kcache), [`pg_stat_monitor`](/pg_stat_monitor), [`pg_qualstats`](/pg_qualstats), [`pg_store_plans`](/pg_store_plans), [`pg_track_settings`](/pg_track_settings), [`pg_wait_sampling`](/pg_wait_sampling), [`system_stats`](/system_stats), [`meta`](/meta), [`pgnodemx`](/pgnodemx), [`pg_proctab`](/pg_proctab), [`pg_sqlog`](/pg_sqlog), [`bgw_replstatus`](/bgw_replstatus), [`pgmeminfo`](/pgmeminfo), [`toastinfo`](/toastinfo), [`explain_ui`](/explain_ui), [`pg_relusage`](/pg_relusage), [`pagevis`](/pagevis), [`powa`](/powa), [`pageinspect`](/pageinspect), [`pgrowlocks`](/pgrowlocks), [`sslinfo`](/sslinfo), [`pg_buffercache`](/pg_buffercache), [`pg_walinspect`](/pg_walinspect), [`pg_freespacemap`](/pg_freespacemap), [`pg_visibility`](/pg_visibility), [`pgstattuple`](/pgstattuple), [`auto_explain`](/auto_explain), [`pg_stat_statements`](/pg_stat_statements)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_sqlog](https://github.com/kouber/pg_sqlog) | 1.6 | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_sqlog](/pg_sqlog) |  | `sqlog` | [`file_fdw`](file_fdw) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_sqlog CASCADE;
```
> **Comment**: require certain params
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.6 | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_sqlog_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.6 | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-sqlog` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pg_sqlog` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_sqlog"]}'
```


Install `pg_sqlog` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_sqlog_17*;
dnf install pg_sqlog_16*;
dnf install pg_sqlog_15*;
dnf install pg_sqlog_14*;
dnf install pg_sqlog_13*;
dnf install pg_sqlog_12*;
```


Install `pg_sqlog` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-sqlog;
apt install postgresql-16-pg-sqlog;
apt install postgresql-15-pg-sqlog;
apt install postgresql-14-pg-sqlog;
apt install postgresql-13-pg-sqlog;
apt install postgresql-12-pg-sqlog;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_sqlog_17*` | `pg_sqlog_16*` | `pg_sqlog_15*` | `pg_sqlog_14*` | `pg_sqlog_13*` | `pg_sqlog_12*` |
| `el9` | `pg_sqlog_17*` | `pg_sqlog_16*` | `pg_sqlog_15*` | `pg_sqlog_14*` | `pg_sqlog_13*` | `pg_sqlog_12*` |
| `d12` | `postgresql-17-pg-sqlog` | `postgresql-16-pg-sqlog` | `postgresql-15-pg-sqlog` | `postgresql-14-pg-sqlog` | `postgresql-13-pg-sqlog` | `postgresql-12-pg-sqlog` |
| `u22` | `postgresql-17-pg-sqlog` | `postgresql-16-pg-sqlog` | `postgresql-15-pg-sqlog` | `postgresql-14-pg-sqlog` | `postgresql-13-pg-sqlog` | `postgresql-12-pg-sqlog` |
| `u24` | `postgresql-17-pg-sqlog` | `postgresql-16-pg-sqlog` | `postgresql-15-pg-sqlog` | `postgresql-14-pg-sqlog` | `postgresql-13-pg-sqlog` | `postgresql-12-pg-sqlog` |






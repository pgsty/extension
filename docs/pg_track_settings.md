# pg_track_settings


> [pg_track_settings](https://github.com/rjuju/pg_track_settings): Track settings changes
>
> https://github.com/rjuju/pg_track_settings





[STAT](/stat) extensions: [`pg_profile`](/pg_profile), [`pg_show_plans`](/pg_show_plans), [`pg_stat_kcache`](/pg_stat_kcache), [`pg_stat_monitor`](/pg_stat_monitor), [`pg_qualstats`](/pg_qualstats), [`pg_store_plans`](/pg_store_plans), [`pg_track_settings`](/pg_track_settings), [`pg_wait_sampling`](/pg_wait_sampling), [`system_stats`](/system_stats), [`meta`](/meta), [`pgnodemx`](/pgnodemx), [`pg_proctab`](/pg_proctab), [`pg_sqlog`](/pg_sqlog), [`bgw_replstatus`](/bgw_replstatus), [`pgmeminfo`](/pgmeminfo), [`toastinfo`](/toastinfo), [`explain_ui`](/explain_ui), [`pg_relusage`](/pg_relusage), [`pg_top`](/pg_top), [`pagevis`](/pagevis), [`powa`](/powa), [`pageinspect`](/pageinspect), [`pgrowlocks`](/pgrowlocks), [`sslinfo`](/sslinfo), [`pg_buffercache`](/pg_buffercache), [`pg_walinspect`](/pg_walinspect), [`pg_freespacemap`](/pg_freespacemap), [`pg_visibility`](/pg_visibility), [`pgstattuple`](/pgstattuple), [`auto_explain`](/auto_explain), [`pg_stat_statements`](/pg_stat_statements)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_track_settings](https://github.com/rjuju/pg_track_settings) | 2.1.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_track_settings](/pg_track_settings) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_track_settings;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_track_settings_17*` | `pg_track_settings_16*` | `pg_track_settings_15*` | `pg_track_settings_14*` | `pg_track_settings_13*` | `pg_track_settings_12*` |
| `el9` | `pg_track_settings_17*` | `pg_track_settings_16*` | `pg_track_settings_15*` | `pg_track_settings_14*` | `pg_track_settings_13*` | `pg_track_settings_12*` |
| `d12` | `postgresql-17-pg-track-settings` | `postgresql-16-pg-track-settings` | `postgresql-15-pg-track-settings` | `postgresql-14-pg-track-settings` | `postgresql-13-pg-track-settings` | `postgresql-12-pg-track-settings` |
| `u22` | `postgresql-17-pg-track-settings` | `postgresql-16-pg-track-settings` | `postgresql-15-pg-track-settings` | `postgresql-14-pg-track-settings` | `postgresql-13-pg-track-settings` | `postgresql-12-pg-track-settings` |
| `u24` | `postgresql-17-pg-track-settings` | `postgresql-16-pg-track-settings` | `postgresql-15-pg-track-settings` | `postgresql-14-pg-track-settings` | `postgresql-13-pg-track-settings` | `postgresql-12-pg-track-settings` |



Install `pg_track_settings` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_track_settings"]}'
```


Install `pg_track_settings` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install pg_track_settings_17*;
yum install pg_track_settings_16*;
yum install pg_track_settings_15*;
yum install pg_track_settings_14*;
yum install pg_track_settings_13*;
yum install pg_track_settings_12*;
```


Install `pg_track_settings` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pg-track-settings;
apt install postgresql-16-pg-track-settings;
apt install postgresql-15-pg-track-settings;
apt install postgresql-14-pg-track-settings;
apt install postgresql-13-pg-track-settings;
apt install postgresql-12-pg-track-settings;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_track_settings_17*` | `pg_track_settings_16*` | `pg_track_settings_15*` | `pg_track_settings_14*` | `pg_track_settings_13*` | `pg_track_settings_12*` |
| `el9` | `pg_track_settings_17*` | `pg_track_settings_16*` | `pg_track_settings_15*` | `pg_track_settings_14*` | `pg_track_settings_13*` | `pg_track_settings_12*` |
| `d12` | `postgresql-17-pg-track-settings` | `postgresql-16-pg-track-settings` | `postgresql-15-pg-track-settings` | `postgresql-14-pg-track-settings` | `postgresql-13-pg-track-settings` | `postgresql-12-pg-track-settings` |
| `u22` | `postgresql-17-pg-track-settings` | `postgresql-16-pg-track-settings` | `postgresql-15-pg-track-settings` | `postgresql-14-pg-track-settings` | `postgresql-13-pg-track-settings` | `postgresql-12-pg-track-settings` |
| `u24` | `postgresql-17-pg-track-settings` | `postgresql-16-pg-track-settings` | `postgresql-15-pg-track-settings` | `postgresql-14-pg-track-settings` | `postgresql-13-pg-track-settings` | `postgresql-12-pg-track-settings` |






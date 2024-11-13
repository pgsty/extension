# auto_explain


> [auto_explain](https://www.postgresql.org/docs/current/auto-explain.html): Provides a means for logging execution plans of slow statements automatically
>
> https://www.postgresql.org/docs/current/auto-explain.html





[STAT](/stat) extensions: [`pg_profile`](/pg_profile), [`pg_show_plans`](/pg_show_plans), [`pg_stat_kcache`](/pg_stat_kcache), [`pg_stat_monitor`](/pg_stat_monitor), [`pg_qualstats`](/pg_qualstats), [`pg_store_plans`](/pg_store_plans), [`pg_track_settings`](/pg_track_settings), [`pg_wait_sampling`](/pg_wait_sampling), [`system_stats`](/system_stats), [`meta`](/meta), [`pgnodemx`](/pgnodemx), [`pg_proctab`](/pg_proctab), [`pg_sqlog`](/pg_sqlog), [`bgw_replstatus`](/bgw_replstatus), [`pgmeminfo`](/pgmeminfo), [`toastinfo`](/toastinfo), [`explain_ui`](/explain_ui), [`pg_relusage`](/pg_relusage), [`pg_top`](/pg_top), [`pagevis`](/pagevis), [`powa`](/powa), [`pageinspect`](/pageinspect), [`pgrowlocks`](/pgrowlocks), [`sslinfo`](/sslinfo), [`pg_buffercache`](/pg_buffercache), [`pg_walinspect`](/pg_walinspect), [`pg_freespacemap`](/pg_freespacemap), [`pg_visibility`](/pg_visibility), [`pgstattuple`](/pgstattuple), [`auto_explain`](/auto_explain), [`pg_stat_statements`](/pg_stat_statements)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [auto_explain](https://www.postgresql.org/docs/current/auto-explain.html) | - | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | **<span class="tcblue">CONTRIB</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [auto_explain](/auto_explain) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'auto_explain'; # add this extension to postgresql.conf
```



-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `postgresql17-contrib` | `postgresql16-contrib` | `postgresql15-contrib` | `postgresql14-contrib` | `postgresql13-contrib` | `postgresql12-contrib` |
| `el9` | `postgresql17-contrib` | `postgresql16-contrib` | `postgresql15-contrib` | `postgresql14-contrib` | `postgresql13-contrib` | `postgresql12-contrib` |
| `d12` | `postgresql-17` | `postgresql-16` | `postgresql-15` | `postgresql-14` | `postgresql-13` | `postgresql-12` |
| `u22` | `postgresql-17` | `postgresql-16` | `postgresql-15` | `postgresql-14` | `postgresql-13` | `postgresql-12` |
| `u24` | `postgresql-17` | `postgresql-16` | `postgresql-15` | `postgresql-14` | `postgresql-13` | `postgresql-12` |



Install `auto_explain` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["auto_explain"]}'
```


Install `auto_explain` [RPM](/rpm) from the **<span class="tcblue">CONTRIB</span>** **YUM** repo:

```bash
yum install postgresql17-contrib;
yum install postgresql16-contrib;
yum install postgresql15-contrib;
yum install postgresql14-contrib;
yum install postgresql13-contrib;
yum install postgresql12-contrib;
```


Install `auto_explain` [DEB](/deb) from the **<span class="tcblue">CONTRIB</span>** **APT** repo:

```bash
apt install postgresql-17;
apt install postgresql-16;
apt install postgresql-15;
apt install postgresql-14;
apt install postgresql-13;
apt install postgresql-12;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `postgresql17-contrib` | `postgresql16-contrib` | `postgresql15-contrib` | `postgresql14-contrib` | `postgresql13-contrib` | `postgresql12-contrib` |
| `el9` | `postgresql17-contrib` | `postgresql16-contrib` | `postgresql15-contrib` | `postgresql14-contrib` | `postgresql13-contrib` | `postgresql12-contrib` |
| `d12` | `postgresql-17` | `postgresql-16` | `postgresql-15` | `postgresql-14` | `postgresql-13` | `postgresql-12` |
| `u22` | `postgresql-17` | `postgresql-16` | `postgresql-15` | `postgresql-14` | `postgresql-13` | `postgresql-12` |
| `u24` | `postgresql-17` | `postgresql-16` | `postgresql-15` | `postgresql-14` | `postgresql-13` | `postgresql-12` |






# toastinfo


> [toastinfo](https://github.com/credativ/toastinfo): show details on toasted datums
>
> https://github.com/credativ/toastinfo





[STAT](/stat) extensions: [`pg_profile`](/pg_profile), [`pg_show_plans`](/pg_show_plans), [`pg_stat_kcache`](/pg_stat_kcache), [`pg_stat_monitor`](/pg_stat_monitor), [`pg_qualstats`](/pg_qualstats), [`pg_store_plans`](/pg_store_plans), [`pg_track_settings`](/pg_track_settings), [`pg_wait_sampling`](/pg_wait_sampling), [`system_stats`](/system_stats), [`meta`](/meta), [`pgnodemx`](/pgnodemx), [`pg_proctab`](/pg_proctab), [`pg_sqlog`](/pg_sqlog), [`bgw_replstatus`](/bgw_replstatus), [`pgmeminfo`](/pgmeminfo), [`toastinfo`](/toastinfo), [`explain_ui`](/explain_ui), [`pg_relusage`](/pg_relusage), [`pg_top`](/pg_top), [`pagevis`](/pagevis), [`powa`](/powa), [`pageinspect`](/pageinspect), [`pgrowlocks`](/pgrowlocks), [`sslinfo`](/sslinfo), [`pg_buffercache`](/pg_buffercache), [`pg_walinspect`](/pg_walinspect), [`pg_freespacemap`](/pg_freespacemap), [`pg_visibility`](/pg_visibility), [`pgstattuple`](/pgstattuple), [`auto_explain`](/auto_explain), [`pg_stat_statements`](/pg_stat_statements)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [toastinfo](https://github.com/credativ/toastinfo) | 1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [toastinfo](/toastinfo) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION toastinfo;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `toastinfo_17*` | `toastinfo_16*` | `toastinfo_15*` | `toastinfo_14*` | `toastinfo_13*` | `toastinfo_12*` |
| `el9` | `toastinfo_17*` | `toastinfo_16*` | `toastinfo_15*` | `toastinfo_14*` | `toastinfo_13*` | `toastinfo_12*` |
| `d12` | `postgresql-17-toastinfo` | `postgresql-16-toastinfo` | `postgresql-15-toastinfo` | `postgresql-14-toastinfo` | `postgresql-13-toastinfo` | `postgresql-12-toastinfo` |
| `u22` | `postgresql-17-toastinfo` | `postgresql-16-toastinfo` | `postgresql-15-toastinfo` | `postgresql-14-toastinfo` | `postgresql-13-toastinfo` | `postgresql-12-toastinfo` |
| `u24` | `postgresql-17-toastinfo` | `postgresql-16-toastinfo` | `postgresql-15-toastinfo` | `postgresql-14-toastinfo` | `postgresql-13-toastinfo` | `postgresql-12-toastinfo` |



Install `toastinfo` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["toastinfo"]}'
```


Install `toastinfo` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install toastinfo_17*;
yum install toastinfo_16*;
yum install toastinfo_15*;
yum install toastinfo_14*;
yum install toastinfo_13*;
yum install toastinfo_12*;
```


Install `toastinfo` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-toastinfo;
apt install postgresql-16-toastinfo;
apt install postgresql-15-toastinfo;
apt install postgresql-14-toastinfo;
apt install postgresql-13-toastinfo;
apt install postgresql-12-toastinfo;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `toastinfo_17*` | `toastinfo_16*` | `toastinfo_15*` | `toastinfo_14*` | `toastinfo_13*` | `toastinfo_12*` |
| `el9` | `toastinfo_17*` | `toastinfo_16*` | `toastinfo_15*` | `toastinfo_14*` | `toastinfo_13*` | `toastinfo_12*` |
| `d12` | `postgresql-17-toastinfo` | `postgresql-16-toastinfo` | `postgresql-15-toastinfo` | `postgresql-14-toastinfo` | `postgresql-13-toastinfo` | `postgresql-12-toastinfo` |
| `u22` | `postgresql-17-toastinfo` | `postgresql-16-toastinfo` | `postgresql-15-toastinfo` | `postgresql-14-toastinfo` | `postgresql-13-toastinfo` | `postgresql-12-toastinfo` |
| `u24` | `postgresql-17-toastinfo` | `postgresql-16-toastinfo` | `postgresql-15-toastinfo` | `postgresql-14-toastinfo` | `postgresql-13-toastinfo` | `postgresql-12-toastinfo` |






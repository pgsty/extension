# bgw_replstatus


> [bgw_replstatus](https://github.com/mhagander/bgw_replstatus): Small PostgreSQL background worker to report whether a node is a replication master or standby
>
> https://github.com/mhagander/bgw_replstatus





[STAT](/stat) extensions: [`pg_profile`](/pg_profile), [`pg_show_plans`](/pg_show_plans), [`pg_stat_kcache`](/pg_stat_kcache), [`pg_stat_monitor`](/pg_stat_monitor), [`pg_qualstats`](/pg_qualstats), [`pg_store_plans`](/pg_store_plans), [`pg_track_settings`](/pg_track_settings), [`pg_wait_sampling`](/pg_wait_sampling), [`system_stats`](/system_stats), [`meta`](/meta), [`pgnodemx`](/pgnodemx), [`pg_proctab`](/pg_proctab), [`pg_sqlog`](/pg_sqlog), [`bgw_replstatus`](/bgw_replstatus), [`pgmeminfo`](/pgmeminfo), [`toastinfo`](/toastinfo), [`explain_ui`](/explain_ui), [`pg_relusage`](/pg_relusage), [`pagevis`](/pagevis), [`powa`](/powa), [`pageinspect`](/pageinspect), [`pgrowlocks`](/pgrowlocks), [`sslinfo`](/sslinfo), [`pg_buffercache`](/pg_buffercache), [`pg_walinspect`](/pg_walinspect), [`pg_freespacemap`](/pg_freespacemap), [`pg_visibility`](/pg_visibility), [`pgstattuple`](/pgstattuple), [`auto_explain`](/auto_explain), [`pg_stat_statements`](/pg_stat_statements)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [bgw_replstatus](https://github.com/mhagander/bgw_replstatus) | 1.0.6 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [bgw_replstatus](/bgw_replstatus) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'bgw_replstatus'; # add this extension to postgresql.conf
```



-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0.6 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `bgw_replstatus_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 1.0.6 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-bgw-replstatus` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `bgw_replstatus` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add bgw_replstatus
```


Install `bgw_replstatus` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["bgw_replstatus"]}'
```


Install `bgw_replstatus` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install bgw_replstatus_17*;
dnf install bgw_replstatus_16*;
dnf install bgw_replstatus_15*;
dnf install bgw_replstatus_14*;
dnf install bgw_replstatus_13*;
```


Install `bgw_replstatus` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-bgw-replstatus;
apt install postgresql-16-bgw-replstatus;
apt install postgresql-15-bgw-replstatus;
apt install postgresql-14-bgw-replstatus;
apt install postgresql-13-bgw-replstatus;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `bgw_replstatus_17*` | `bgw_replstatus_16*` | `bgw_replstatus_15*` | `bgw_replstatus_14*` | `bgw_replstatus_13*` |
| `el9` | `bgw_replstatus_17*` | `bgw_replstatus_16*` | `bgw_replstatus_15*` | `bgw_replstatus_14*` | `bgw_replstatus_13*` |
| `d12` | `postgresql-17-bgw-replstatus` | `postgresql-16-bgw-replstatus` | `postgresql-15-bgw-replstatus` | `postgresql-14-bgw-replstatus` | `postgresql-13-bgw-replstatus` |
| `u22` | `postgresql-17-bgw-replstatus` | `postgresql-16-bgw-replstatus` | `postgresql-15-bgw-replstatus` | `postgresql-14-bgw-replstatus` | `postgresql-13-bgw-replstatus` |
| `u24` | `postgresql-17-bgw-replstatus` | `postgresql-16-bgw-replstatus` | `postgresql-15-bgw-replstatus` | `postgresql-14-bgw-replstatus` | `postgresql-13-bgw-replstatus` |






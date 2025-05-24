# pg_stat_kcache


> [pg_stat_kcache](https://github.com/powa-team/pg_stat_kcache): Kernel statistics gathering
>
> https://github.com/powa-team/pg_stat_kcache





[STAT](/stat) extensions: [`pg_profile`](/pg_profile), [`pg_tracing`](/pg_tracing), [`pg_show_plans`](/pg_show_plans), [`pg_stat_kcache`](/pg_stat_kcache), [`pg_stat_monitor`](/pg_stat_monitor), [`pg_qualstats`](/pg_qualstats), [`pg_store_plans`](/pg_store_plans), [`pg_track_settings`](/pg_track_settings), [`pg_wait_sampling`](/pg_wait_sampling), [`pgsentinel`](/pgsentinel), [`system_stats`](/system_stats), [`meta`](/meta), [`pgnodemx`](/pgnodemx), [`pg_proctab`](/pg_proctab), [`pg_sqlog`](/pg_sqlog), [`bgw_replstatus`](/bgw_replstatus), [`pgmeminfo`](/pgmeminfo), [`toastinfo`](/toastinfo), [`explain_ui`](/explain_ui), [`pg_relusage`](/pg_relusage), [`pagevis`](/pagevis), [`powa`](/powa), [`pg_overexplain`](/pg_overexplain), [`pg_logicalinspect`](/pg_logicalinspect), [`pageinspect`](/pageinspect), [`pgrowlocks`](/pgrowlocks), [`sslinfo`](/sslinfo), [`pg_buffercache`](/pg_buffercache), [`pg_walinspect`](/pg_walinspect), [`pg_freespacemap`](/pg_freespacemap), [`pg_visibility`](/pg_visibility), [`pgstattuple`](/pgstattuple), [`auto_explain`](/auto_explain), [`pg_stat_statements`](/pg_stat_statements)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_stat_kcache](https://github.com/powa-team/pg_stat_kcache) | 2.3.0 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_stat_kcache](/pg_stat_kcache) |  |  | [`pg_stat_statements`](pg_stat_statements) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'pg_stat_kcache'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION pg_stat_kcache CASCADE;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 2.3.0 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `pg_stat_kcache_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 2.3.0 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pg-stat-kcache` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pg_stat_kcache` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_stat_kcache
```


Install `pg_stat_kcache` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_stat_kcache"]}'
```


Install `pg_stat_kcache` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pg_stat_kcache_17*;
dnf install pg_stat_kcache_16*;
dnf install pg_stat_kcache_15*;
dnf install pg_stat_kcache_14*;
dnf install pg_stat_kcache_13*;
```


Install `pg_stat_kcache` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pg-stat-kcache;
apt install postgresql-16-pg-stat-kcache;
apt install postgresql-15-pg-stat-kcache;
apt install postgresql-14-pg-stat-kcache;
apt install postgresql-13-pg-stat-kcache;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_stat_kcache_17*` | `pg_stat_kcache_16*` | `pg_stat_kcache_15*` | `pg_stat_kcache_14*` | `pg_stat_kcache_13*` |
| `el9` | `pg_stat_kcache_17*` | `pg_stat_kcache_16*` | `pg_stat_kcache_15*` | `pg_stat_kcache_14*` | `pg_stat_kcache_13*` |
| `d12` | `postgresql-17-pg-stat-kcache` | `postgresql-16-pg-stat-kcache` | `postgresql-15-pg-stat-kcache` | `postgresql-14-pg-stat-kcache` | `postgresql-13-pg-stat-kcache` |
| `u22` | `postgresql-17-pg-stat-kcache` | `postgresql-16-pg-stat-kcache` | `postgresql-15-pg-stat-kcache` | `postgresql-14-pg-stat-kcache` | `postgresql-13-pg-stat-kcache` |
| `u24` | `postgresql-17-pg-stat-kcache` | `postgresql-16-pg-stat-kcache` | `postgresql-15-pg-stat-kcache` | `postgresql-14-pg-stat-kcache` | `postgresql-13-pg-stat-kcache` |






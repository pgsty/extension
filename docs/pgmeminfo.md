# pgmeminfo


> [pgmeminfo](https://github.com/okbob/pgmeminfo): show memory usage
>
> https://github.com/okbob/pgmeminfo





[STAT](/stat) extensions: [`pg_profile`](/pg_profile), [`pg_tracing`](/pg_tracing), [`pg_show_plans`](/pg_show_plans), [`pg_stat_kcache`](/pg_stat_kcache), [`pg_stat_monitor`](/pg_stat_monitor), [`pg_qualstats`](/pg_qualstats), [`pg_store_plans`](/pg_store_plans), [`pg_track_settings`](/pg_track_settings), [`pg_wait_sampling`](/pg_wait_sampling), [`pgsentinel`](/pgsentinel), [`system_stats`](/system_stats), [`meta`](/meta), [`pgnodemx`](/pgnodemx), [`pg_proctab`](/pg_proctab), [`pg_sqlog`](/pg_sqlog), [`bgw_replstatus`](/bgw_replstatus), [`pgmeminfo`](/pgmeminfo), [`toastinfo`](/toastinfo), [`explain_ui`](/explain_ui), [`pg_relusage`](/pg_relusage), [`pagevis`](/pagevis), [`powa`](/powa), [`pg_overexplain`](/pg_overexplain), [`pg_logicalinspect`](/pg_logicalinspect), [`pageinspect`](/pageinspect), [`pgrowlocks`](/pgrowlocks), [`sslinfo`](/sslinfo), [`pg_buffercache`](/pg_buffercache), [`pg_walinspect`](/pg_walinspect), [`pg_freespacemap`](/pg_freespacemap), [`pg_visibility`](/pg_visibility), [`pgstattuple`](/pgstattuple), [`auto_explain`](/auto_explain), [`pg_stat_statements`](/pg_stat_statements)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgmeminfo](https://github.com/okbob/pgmeminfo) | 1.0.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgmeminfo](/pgmeminfo) | `pgdg-flaw` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pgmeminfo;
```
> **Comment**: no pg14,13,12 on el8/9 pgdg repo
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `pgmeminfo_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.0.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pgmeminfo` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pgmeminfo` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pgmeminfo
```


Install `pgmeminfo` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgmeminfo"]}'
```


Install `pgmeminfo` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pgmeminfo_17*;
dnf install pgmeminfo_16*;
dnf install pgmeminfo_15*;
dnf install pgmeminfo_14*;
dnf install pgmeminfo_13*;
```


Install `pgmeminfo` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pgmeminfo;
apt install postgresql-16-pgmeminfo;
apt install postgresql-15-pgmeminfo;
apt install postgresql-14-pgmeminfo;
apt install postgresql-13-pgmeminfo;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgmeminfo_17*` | `pgmeminfo_16*` | `pgmeminfo_15*` | `pgmeminfo_14*` | `pgmeminfo_13*` |
| `el9` | `pgmeminfo_17*` | `pgmeminfo_16*` | `pgmeminfo_15*` | `pgmeminfo_14*` | `pgmeminfo_13*` |
| `d12` | `postgresql-17-pgmeminfo` | `postgresql-16-pgmeminfo` | `postgresql-15-pgmeminfo` | `postgresql-14-pgmeminfo` | `postgresql-13-pgmeminfo` |
| `u22` | `postgresql-17-pgmeminfo` | `postgresql-16-pgmeminfo` | `postgresql-15-pgmeminfo` | `postgresql-14-pgmeminfo` | `postgresql-13-pgmeminfo` |
| `u24` | `postgresql-17-pgmeminfo` | `postgresql-16-pgmeminfo` | `postgresql-15-pgmeminfo` | `postgresql-14-pgmeminfo` | `postgresql-13-pgmeminfo` |






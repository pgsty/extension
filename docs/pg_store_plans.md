# pg_store_plans


> [pg_store_plans](https://github.com/ossc-db/pg_store_plans): track plan statistics of all SQL statements executed
>
> https://github.com/ossc-db/pg_store_plans





[STAT](/stat) extensions: [`pg_profile`](/pg_profile), [`pg_tracing`](/pg_tracing), [`pg_show_plans`](/pg_show_plans), [`pg_stat_kcache`](/pg_stat_kcache), [`pg_stat_monitor`](/pg_stat_monitor), [`pg_qualstats`](/pg_qualstats), [`pg_store_plans`](/pg_store_plans), [`pg_track_settings`](/pg_track_settings), [`pg_wait_sampling`](/pg_wait_sampling), [`pgsentinel`](/pgsentinel), [`system_stats`](/system_stats), [`meta`](/meta), [`pgnodemx`](/pgnodemx), [`pg_proctab`](/pg_proctab), [`pg_sqlog`](/pg_sqlog), [`bgw_replstatus`](/bgw_replstatus), [`pgmeminfo`](/pgmeminfo), [`toastinfo`](/toastinfo), [`explain_ui`](/explain_ui), [`pg_relusage`](/pg_relusage), [`pagevis`](/pagevis), [`powa`](/powa), [`pg_overexplain`](/pg_overexplain), [`pg_logicalinspect`](/pg_logicalinspect), [`pageinspect`](/pageinspect), [`pgrowlocks`](/pgrowlocks), [`sslinfo`](/sslinfo), [`pg_buffercache`](/pg_buffercache), [`pg_walinspect`](/pg_walinspect), [`pg_freespacemap`](/pg_freespacemap), [`pg_visibility`](/pg_visibility), [`pgstattuple`](/pgstattuple), [`auto_explain`](/auto_explain), [`pg_stat_statements`](/pg_stat_statements)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_store_plans](https://github.com/ossc-db/pg_store_plans) | 1.8 | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_store_plans](/pg_store_plans) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'pg_store_plans'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION pg_store_plans;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.8 | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_store_plans_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.8 | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-store-plan` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pg_store_plans` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_store_plans
```


Install `pg_store_plans` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_store_plans"]}'
```


Install `pg_store_plans` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_store_plans_17*;
dnf install pg_store_plans_16*;
dnf install pg_store_plans_15*;
dnf install pg_store_plans_14*;
dnf install pg_store_plans_13*;
```


Install `pg_store_plans` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-store-plan;
apt install postgresql-16-pg-store-plan;
apt install postgresql-15-pg-store-plan;
apt install postgresql-14-pg-store-plan;
apt install postgresql-13-pg-store-plan;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_store_plans_17*` | `pg_store_plans_16*` | `pg_store_plans_15*` | `pg_store_plans_14*` | `pg_store_plans_13*` |
| `el9` | `pg_store_plans_17*` | `pg_store_plans_16*` | `pg_store_plans_15*` | `pg_store_plans_14*` | `pg_store_plans_13*` |
| `d12` | `postgresql-17-pg-store-plan` | `postgresql-16-pg-store-plan` | `postgresql-15-pg-store-plan` | `postgresql-14-pg-store-plan` | `postgresql-13-pg-store-plan` |
| `u22` | `postgresql-17-pg-store-plan` | `postgresql-16-pg-store-plan` | `postgresql-15-pg-store-plan` | `postgresql-14-pg-store-plan` | `postgresql-13-pg-store-plan` |
| `u24` | `postgresql-17-pg-store-plan` | `postgresql-16-pg-store-plan` | `postgresql-15-pg-store-plan` | `postgresql-14-pg-store-plan` | `postgresql-13-pg-store-plan` |






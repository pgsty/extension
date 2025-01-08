# powa


> [powa](https://github.com/powa-team/powa): PostgreSQL Workload Analyser-core
>
> https://github.com/powa-team/powa





[STAT](/stat) extensions: [`pg_profile`](/pg_profile), [`pg_show_plans`](/pg_show_plans), [`pg_stat_kcache`](/pg_stat_kcache), [`pg_stat_monitor`](/pg_stat_monitor), [`pg_qualstats`](/pg_qualstats), [`pg_store_plans`](/pg_store_plans), [`pg_track_settings`](/pg_track_settings), [`pg_wait_sampling`](/pg_wait_sampling), [`system_stats`](/system_stats), [`meta`](/meta), [`pgnodemx`](/pgnodemx), [`pg_proctab`](/pg_proctab), [`pg_sqlog`](/pg_sqlog), [`bgw_replstatus`](/bgw_replstatus), [`pgmeminfo`](/pgmeminfo), [`toastinfo`](/toastinfo), [`explain_ui`](/explain_ui), [`pg_relusage`](/pg_relusage), [`pagevis`](/pagevis), [`powa`](/powa), [`pageinspect`](/pageinspect), [`pgrowlocks`](/pgrowlocks), [`sslinfo`](/sslinfo), [`pg_buffercache`](/pg_buffercache), [`pg_walinspect`](/pg_walinspect), [`pg_freespacemap`](/pg_freespacemap), [`pg_visibility`](/pg_visibility), [`pgstattuple`](/pgstattuple), [`auto_explain`](/auto_explain), [`pg_stat_statements`](/pg_stat_statements)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [powa](https://github.com/powa-team/powa) | 5.0.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [powa](/powa) |  | `public` | [`plpgsql`](plpgsql), [`pg_stat_statements`](pg_stat_statements), [`btree_gist`](btree_gist) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION powa CASCADE;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 5.0.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `powa_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 5.0.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-powa` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `powa` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add powa
```


Install `powa` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["powa"]}'
```


Install `powa` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install powa_17*;
dnf install powa_16*;
dnf install powa_15*;
dnf install powa_14*;
dnf install powa_13*;
```


Install `powa` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-powa;
apt install postgresql-16-powa;
apt install postgresql-15-powa;
apt install postgresql-14-powa;
apt install postgresql-13-powa;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `powa_17*` | `powa_16*` | `powa_15*` | `powa_14*` | `powa_13*` |
| `el9` | `powa_17*` | `powa_16*` | `powa_15*` | `powa_14*` | `powa_13*` |
| `d12` | `postgresql-17-powa` | `postgresql-16-powa` | `postgresql-15-powa` | `postgresql-14-powa` | `postgresql-13-powa` |
| `u22` | `postgresql-17-powa` | `postgresql-16-powa` | `postgresql-15-powa` | `postgresql-14-powa` | `postgresql-13-powa` |
| `u24` | `postgresql-17-powa` | `postgresql-16-powa` | `postgresql-15-powa` | `postgresql-14-powa` | `postgresql-13-powa` |






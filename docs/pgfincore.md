# pgfincore


> [pgfincore](https://github.com/klando/pgfincore): examine and manage the os buffer cache
>
> https://github.com/klando/pgfincore





[ADMIN](/admin) extensions: [`pg_repack`](/pg_repack), [`pg_squeeze`](/pg_squeeze), [`pg_dirtyread`](/pg_dirtyread), [`pgfincore`](/pgfincore), [`ddlx`](/ddlx), [`prioritize`](/prioritize), [`pg_checksums`](/pg_checksums), [`pg_readonly`](/pg_readonly), [`pg_upless`](/pg_upless), [`pg_permissions`](/pg_permissions), [`pgautofailover`](/pgautofailover), [`pg_catcheck`](/pg_catcheck), [`pre_prepare`](/pre_prepare), [`pgcozy`](/pgcozy), [`pg_orphaned`](/pg_orphaned), [`pg_crash`](/pg_crash), [`pg_cheat_funcs`](/pg_cheat_funcs), [`fio`](/fio), [`pg_savior`](/pg_savior), [`safeupdate`](/safeupdate), [`pg_drop_events`](/pg_drop_events), [`table_log`](/table_log), [`pg_prewarm`](/pg_prewarm), [`pgagent`](/pgagent), [`pgpool_adm`](/pgpool_adm), [`lo`](/lo), [`pgpool_recovery`](/pgpool_recovery), [`pgpool_regclass`](/pgpool_regclass), [`basic_archive`](/basic_archive), [`basebackup_to_shell`](/basebackup_to_shell), [`old_snapshot`](/old_snapshot), [`adminpack`](/adminpack), [`amcheck`](/amcheck), [`pg_surgery`](/pg_surgery)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgfincore](https://github.com/klando/pgfincore) | 1.3.1 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgfincore](/pgfincore) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pgfincore;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.3.1 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `pgfincore_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 1.3.1 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pgfincore` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pgfincore` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pgfincore
```


Install `pgfincore` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgfincore"]}'
```


Install `pgfincore` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pgfincore_17*;
dnf install pgfincore_16*;
dnf install pgfincore_15*;
dnf install pgfincore_14*;
dnf install pgfincore_13*;
```


Install `pgfincore` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pgfincore;
apt install postgresql-16-pgfincore;
apt install postgresql-15-pgfincore;
apt install postgresql-14-pgfincore;
apt install postgresql-13-pgfincore;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgfincore_17*` | `pgfincore_16*` | `pgfincore_15*` | `pgfincore_14*` | `pgfincore_13*` |
| `el9` | `pgfincore_17*` | `pgfincore_16*` | `pgfincore_15*` | `pgfincore_14*` | `pgfincore_13*` |
| `d12` | `postgresql-17-pgfincore` | `postgresql-16-pgfincore` | `postgresql-15-pgfincore` | `postgresql-14-pgfincore` | `postgresql-13-pgfincore` |
| `u22` | `postgresql-17-pgfincore` | `postgresql-16-pgfincore` | `postgresql-15-pgfincore` | `postgresql-14-pgfincore` | `postgresql-13-pgfincore` |
| `u24` | `postgresql-17-pgfincore` | `postgresql-16-pgfincore` | `postgresql-15-pgfincore` | `postgresql-14-pgfincore` | `postgresql-13-pgfincore` |






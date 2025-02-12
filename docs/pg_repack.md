# pg_repack


> [pg_repack](https://github.com/reorg/pg_repack): Reorganize tables in PostgreSQL databases with minimal locks
>
> https://github.com/reorg/pg_repack





[ADMIN](/admin) extensions: [`pg_repack`](/pg_repack), [`pg_squeeze`](/pg_squeeze), [`pg_dirtyread`](/pg_dirtyread), [`pgfincore`](/pgfincore), [`pg_cooldown`](/pg_cooldown), [`ddlx`](/ddlx), [`prioritize`](/prioritize), [`pg_checksums`](/pg_checksums), [`pg_readonly`](/pg_readonly), [`pg_upless`](/pg_upless), [`pg_permissions`](/pg_permissions), [`pgautofailover`](/pgautofailover), [`pg_catcheck`](/pg_catcheck), [`pre_prepare`](/pre_prepare), [`pgcozy`](/pgcozy), [`pg_orphaned`](/pg_orphaned), [`pg_crash`](/pg_crash), [`pg_cheat_funcs`](/pg_cheat_funcs), [`fio`](/fio), [`pg_savior`](/pg_savior), [`safeupdate`](/safeupdate), [`pg_drop_events`](/pg_drop_events), [`table_log`](/table_log), [`pgagent`](/pgagent), [`pg_prewarm`](/pg_prewarm), [`pgpool_adm`](/pgpool_adm), [`pgpool_recovery`](/pgpool_recovery), [`lo`](/lo), [`pgpool_regclass`](/pgpool_regclass), [`basic_archive`](/basic_archive), [`basebackup_to_shell`](/basebackup_to_shell), [`old_snapshot`](/old_snapshot), [`adminpack`](/adminpack), [`amcheck`](/amcheck), [`pg_surgery`](/pg_surgery)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_repack](https://github.com/reorg/pg_repack) | 1.5.2 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| **<span class="tccyan">✔</span>** |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_repack](/pg_repack) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_repack;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.5.2 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `pg_repack_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 1.5.2 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-repack` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pg_repack` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_repack
```


Install `pg_repack` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_repack"]}'
```


Install `pg_repack` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pg_repack_17*;
dnf install pg_repack_16*;
dnf install pg_repack_15*;
dnf install pg_repack_14*;
dnf install pg_repack_13*;
```


Install `pg_repack` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-repack;
apt install postgresql-16-repack;
apt install postgresql-15-repack;
apt install postgresql-14-repack;
apt install postgresql-13-repack;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_repack_17*` | `pg_repack_16*` | `pg_repack_15*` | `pg_repack_14*` | `pg_repack_13*` |
| `el9` | `pg_repack_17*` | `pg_repack_16*` | `pg_repack_15*` | `pg_repack_14*` | `pg_repack_13*` |
| `d12` | `postgresql-17-repack` | `postgresql-16-repack` | `postgresql-15-repack` | `postgresql-14-repack` | `postgresql-13-repack` |
| `u22` | `postgresql-17-repack` | `postgresql-16-repack` | `postgresql-15-repack` | `postgresql-14-repack` | `postgresql-13-repack` |
| `u24` | `postgresql-17-repack` | `postgresql-16-repack` | `postgresql-15-repack` | `postgresql-14-repack` | `postgresql-13-repack` |






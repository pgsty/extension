# pg_cheat_funcs


> [pg_cheat_funcs](https://github.com/MasaoFujii/pg_cheat_funcs): Provides cheat (but useful) functions
>
> https://github.com/MasaoFujii/pg_cheat_funcs





[ADMIN](/admin) extensions: [`pg_repack`](/pg_repack), [`pg_squeeze`](/pg_squeeze), [`pg_dirtyread`](/pg_dirtyread), [`pgfincore`](/pgfincore), [`ddlx`](/ddlx), [`prioritize`](/prioritize), [`pg_checksums`](/pg_checksums), [`pg_readonly`](/pg_readonly), [`pg_upless`](/pg_upless), [`pg_permissions`](/pg_permissions), [`pgautofailover`](/pgautofailover), [`pg_catcheck`](/pg_catcheck), [`pre_prepare`](/pre_prepare), [`pgcozy`](/pgcozy), [`pg_orphaned`](/pg_orphaned), [`pg_crash`](/pg_crash), [`pg_cheat_funcs`](/pg_cheat_funcs), [`fio`](/fio), [`pg_savior`](/pg_savior), [`safeupdate`](/safeupdate), [`pg_drop_events`](/pg_drop_events), [`table_log`](/table_log), [`pgagent`](/pgagent), [`pg_prewarm`](/pg_prewarm), [`pgpool_adm`](/pgpool_adm), [`pgpool_recovery`](/pgpool_recovery), [`lo`](/lo), [`basic_archive`](/basic_archive), [`pgpool_regclass`](/pgpool_regclass), [`basebackup_to_shell`](/basebackup_to_shell), [`old_snapshot`](/old_snapshot), [`adminpack`](/adminpack), [`amcheck`](/amcheck), [`pg_surgery`](/pg_surgery)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_cheat_funcs](https://github.com/MasaoFujii/pg_cheat_funcs) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_cheat_funcs](/pg_cheat_funcs) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_cheat_funcs;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_cheat_funcs_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-cheat-funcs` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pg_cheat_funcs` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_cheat_funcs
```


Install `pg_cheat_funcs` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_cheat_funcs"]}'
```


Install `pg_cheat_funcs` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_cheat_funcs_17*;
dnf install pg_cheat_funcs_16*;
dnf install pg_cheat_funcs_15*;
dnf install pg_cheat_funcs_14*;
dnf install pg_cheat_funcs_13*;
```


Install `pg_cheat_funcs` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-cheat-funcs;
apt install postgresql-16-pg-cheat-funcs;
apt install postgresql-15-pg-cheat-funcs;
apt install postgresql-14-pg-cheat-funcs;
apt install postgresql-13-pg-cheat-funcs;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_cheat_funcs_17*` | `pg_cheat_funcs_16*` | `pg_cheat_funcs_15*` | `pg_cheat_funcs_14*` | `pg_cheat_funcs_13*` |
| `el9` | `pg_cheat_funcs_17*` | `pg_cheat_funcs_16*` | `pg_cheat_funcs_15*` | `pg_cheat_funcs_14*` | `pg_cheat_funcs_13*` |
| `d12` | `postgresql-17-pg-cheat-funcs` | `postgresql-16-pg-cheat-funcs` | `postgresql-15-pg-cheat-funcs` | `postgresql-14-pg-cheat-funcs` | `postgresql-13-pg-cheat-funcs` |
| `u22` | `postgresql-17-pg-cheat-funcs` | `postgresql-16-pg-cheat-funcs` | `postgresql-15-pg-cheat-funcs` | `postgresql-14-pg-cheat-funcs` | `postgresql-13-pg-cheat-funcs` |
| `u24` | `postgresql-17-pg-cheat-funcs` | `postgresql-16-pg-cheat-funcs` | `postgresql-15-pg-cheat-funcs` | `postgresql-14-pg-cheat-funcs` | `postgresql-13-pg-cheat-funcs` |






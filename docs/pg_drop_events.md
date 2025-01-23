# pg_drop_events


> [pg_drop_events](https://github.com/bolajiwahab/pg_drop_events): logs transaction ids of drop table, drop column, drop materialized view statements
>
> https://github.com/bolajiwahab/pg_drop_events





[ADMIN](/admin) extensions: [`pg_repack`](/pg_repack), [`pg_squeeze`](/pg_squeeze), [`pg_dirtyread`](/pg_dirtyread), [`pgfincore`](/pgfincore), [`ddlx`](/ddlx), [`prioritize`](/prioritize), [`pg_checksums`](/pg_checksums), [`pg_readonly`](/pg_readonly), [`pg_upless`](/pg_upless), [`pg_permissions`](/pg_permissions), [`pgautofailover`](/pgautofailover), [`pg_catcheck`](/pg_catcheck), [`pre_prepare`](/pre_prepare), [`pgcozy`](/pgcozy), [`pg_orphaned`](/pg_orphaned), [`pg_crash`](/pg_crash), [`pg_cheat_funcs`](/pg_cheat_funcs), [`fio`](/fio), [`pg_savior`](/pg_savior), [`safeupdate`](/safeupdate), [`pg_drop_events`](/pg_drop_events), [`table_log`](/table_log), [`pgagent`](/pgagent), [`pg_prewarm`](/pg_prewarm), [`pgpool_adm`](/pgpool_adm), [`pgpool_recovery`](/pgpool_recovery), [`lo`](/lo), [`basic_archive`](/basic_archive), [`pgpool_regclass`](/pgpool_regclass), [`basebackup_to_shell`](/basebackup_to_shell), [`old_snapshot`](/old_snapshot), [`adminpack`](/adminpack), [`amcheck`](/amcheck), [`pg_surgery`](/pg_surgery)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_drop_events](https://github.com/bolajiwahab/pg_drop_events) | 0.1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_drop_events](/pg_drop_events) |  | `public` | [`plpgsql`](plpgsql) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_drop_events CASCADE;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pg_drop_events_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 0.1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-drop-events` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pg_drop_events` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_drop_events
```


Install `pg_drop_events` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_drop_events"]}'
```


Install `pg_drop_events` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pg_drop_events_17*;
dnf install pg_drop_events_16*;
dnf install pg_drop_events_15*;
dnf install pg_drop_events_14*;
dnf install pg_drop_events_13*;
```


Install `pg_drop_events` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pg-drop-events;
apt install postgresql-16-pg-drop-events;
apt install postgresql-15-pg-drop-events;
apt install postgresql-14-pg-drop-events;
apt install postgresql-13-pg-drop-events;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_drop_events_17*` | `pg_drop_events_16*` | `pg_drop_events_15*` | `pg_drop_events_14*` | `pg_drop_events_13*` |
| `el9` | `pg_drop_events_17*` | `pg_drop_events_16*` | `pg_drop_events_15*` | `pg_drop_events_14*` | `pg_drop_events_13*` |
| `d12` | `postgresql-17-pg-drop-events` | `postgresql-16-pg-drop-events` | `postgresql-15-pg-drop-events` | `postgresql-14-pg-drop-events` | `postgresql-13-pg-drop-events` |
| `u22` | `postgresql-17-pg-drop-events` | `postgresql-16-pg-drop-events` | `postgresql-15-pg-drop-events` | `postgresql-14-pg-drop-events` | `postgresql-13-pg-drop-events` |
| `u24` | `postgresql-17-pg-drop-events` | `postgresql-16-pg-drop-events` | `postgresql-15-pg-drop-events` | `postgresql-14-pg-drop-events` | `postgresql-13-pg-drop-events` |






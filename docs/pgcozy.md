# pgcozy


> [pgcozy](https://github.com/vventirozos/pgcozy): Pre-warming shared buffers according to previous pg_buffercache snapshots for PostgreSQL.
>
> https://github.com/vventirozos/pgcozy





[ADMIN](/admin) extensions: [`pg_repack`](/pg_repack), [`pg_squeeze`](/pg_squeeze), [`pg_dirtyread`](/pg_dirtyread), [`pgfincore`](/pgfincore), [`ddlx`](/ddlx), [`prioritize`](/prioritize), [`pg_checksums`](/pg_checksums), [`pg_readonly`](/pg_readonly), [`pg_upless`](/pg_upless), [`pg_permissions`](/pg_permissions), [`pgautofailover`](/pgautofailover), [`pg_catcheck`](/pg_catcheck), [`pre_prepare`](/pre_prepare), [`pgcozy`](/pgcozy), [`pg_orphaned`](/pg_orphaned), [`pg_crash`](/pg_crash), [`pg_cheat_funcs`](/pg_cheat_funcs), [`fio`](/fio), [`pg_savior`](/pg_savior), [`safeupdate`](/safeupdate), [`pg_drop_events`](/pg_drop_events), [`table_log`](/table_log), [`pg_prewarm`](/pg_prewarm), [`pgagent`](/pgagent), [`pgpool_adm`](/pgpool_adm), [`lo`](/lo), [`pgpool_recovery`](/pgpool_recovery), [`pgpool_regclass`](/pgpool_regclass), [`basic_archive`](/basic_archive), [`basebackup_to_shell`](/basebackup_to_shell), [`old_snapshot`](/old_snapshot), [`adminpack`](/adminpack), [`amcheck`](/amcheck), [`pg_surgery`](/pg_surgery)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgcozy](https://github.com/vventirozos/pgcozy) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |  |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgcozy](/pgcozy) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pgcozy;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pgcozy_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pgcozy` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pgcozy` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pgcozy
```


Install `pgcozy` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgcozy"]}'
```


Install `pgcozy` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pgcozy_17;
dnf install pgcozy_16;
dnf install pgcozy_15;
dnf install pgcozy_14;
dnf install pgcozy_13;
```


Install `pgcozy` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pgcozy;
apt install postgresql-16-pgcozy;
apt install postgresql-15-pgcozy;
apt install postgresql-14-pgcozy;
apt install postgresql-13-pgcozy;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgcozy_17` | `pgcozy_16` | `pgcozy_15` | `pgcozy_14` | `pgcozy_13` |
| `el9` | `pgcozy_17` | `pgcozy_16` | `pgcozy_15` | `pgcozy_14` | `pgcozy_13` |
| `d12` | `postgresql-17-pgcozy` | `postgresql-16-pgcozy` | `postgresql-15-pgcozy` | `postgresql-14-pgcozy` | `postgresql-13-pgcozy` |
| `u22` | `postgresql-17-pgcozy` | `postgresql-16-pgcozy` | `postgresql-15-pgcozy` | `postgresql-14-pgcozy` | `postgresql-13-pgcozy` |
| `u24` | `postgresql-17-pgcozy` | `postgresql-16-pgcozy` | `postgresql-15-pgcozy` | `postgresql-14-pgcozy` | `postgresql-13-pgcozy` |






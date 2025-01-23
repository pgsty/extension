# pgautofailover


> [pgautofailover](https://github.com/hapostgres/pg_auto_failover): pg_auto_failover
>
> https://github.com/hapostgres/pg_auto_failover





[ADMIN](/admin) extensions: [`pg_repack`](/pg_repack), [`pg_squeeze`](/pg_squeeze), [`pg_dirtyread`](/pg_dirtyread), [`pgfincore`](/pgfincore), [`ddlx`](/ddlx), [`prioritize`](/prioritize), [`pg_checksums`](/pg_checksums), [`pg_readonly`](/pg_readonly), [`pg_upless`](/pg_upless), [`pg_permissions`](/pg_permissions), [`pgautofailover`](/pgautofailover), [`pg_catcheck`](/pg_catcheck), [`pre_prepare`](/pre_prepare), [`pgcozy`](/pgcozy), [`pg_orphaned`](/pg_orphaned), [`pg_crash`](/pg_crash), [`pg_cheat_funcs`](/pg_cheat_funcs), [`fio`](/fio), [`pg_savior`](/pg_savior), [`safeupdate`](/safeupdate), [`pg_drop_events`](/pg_drop_events), [`table_log`](/table_log), [`pgagent`](/pgagent), [`pg_prewarm`](/pg_prewarm), [`pgpool_adm`](/pgpool_adm), [`pgpool_recovery`](/pgpool_recovery), [`lo`](/lo), [`basic_archive`](/basic_archive), [`pgpool_regclass`](/pgpool_regclass), [`basebackup_to_shell`](/basebackup_to_shell), [`old_snapshot`](/old_snapshot), [`adminpack`](/adminpack), [`amcheck`](/amcheck), [`pg_surgery`](/pg_surgery)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgautofailover](https://github.com/hapostgres/pg_auto_failover) | 2.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgautofailover](/pgautofailover) |  |  | [`btree_gist`](btree_gist) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcred">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcred">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'pgautofailover'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION pgautofailover CASCADE;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 2.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pg_auto_failover_$v*` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 2.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-auto-failover` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pgautofailover` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pgautofailover
```


Install `pgautofailover` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgautofailover"]}'
```


Install `pgautofailover` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pg_auto_failover_16*;
dnf install pg_auto_failover_15*;
dnf install pg_auto_failover_14*;
dnf install pg_auto_failover_13*;
```


Install `pgautofailover` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-auto-failover;
apt install postgresql-16-auto-failover;
apt install postgresql-15-auto-failover;
apt install postgresql-14-auto-failover;
apt install postgresql-13-auto-failover;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcred">✘</span> | `pg_auto_failover_16*` | `pg_auto_failover_15*` | `pg_auto_failover_14*` | `pg_auto_failover_13*` |
| `el9` | <span class="tcred">✘</span> | `pg_auto_failover_16*` | `pg_auto_failover_15*` | `pg_auto_failover_14*` | `pg_auto_failover_13*` |
| `d12` | `postgresql-17-auto-failover` | `postgresql-16-auto-failover` | `postgresql-15-auto-failover` | `postgresql-14-auto-failover` | `postgresql-13-auto-failover` |
| `u22` | `postgresql-17-auto-failover` | `postgresql-16-auto-failover` | `postgresql-15-auto-failover` | `postgresql-14-auto-failover` | `postgresql-13-auto-failover` |
| `u24` | `postgresql-17-auto-failover` | `postgresql-16-auto-failover` | `postgresql-15-auto-failover` | `postgresql-14-auto-failover` | `postgresql-13-auto-failover` |






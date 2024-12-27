# pg_squeeze


> [pg_squeeze](https://github.com/cybertec-postgresql/pg_squeeze): A tool to remove unused space from a relation.
>
> https://github.com/cybertec-postgresql/pg_squeeze





[ADMIN](/admin) extensions: [`pg_repack`](/pg_repack), [`pg_squeeze`](/pg_squeeze), [`pg_dirtyread`](/pg_dirtyread), [`pgfincore`](/pgfincore), [`ddlx`](/ddlx), [`prioritize`](/prioritize), [`pg_checksums`](/pg_checksums), [`pg_readonly`](/pg_readonly), [`safeupdate`](/safeupdate), [`pg_permissions`](/pg_permissions), [`pgautofailover`](/pgautofailover), [`pg_catcheck`](/pg_catcheck), [`pre_prepare`](/pre_prepare), [`pgcozy`](/pgcozy), [`pg_orphaned`](/pg_orphaned), [`pg_crash`](/pg_crash), [`pg_cheat_funcs`](/pg_cheat_funcs), [`pg_savior`](/pg_savior), [`table_log`](/table_log), [`fio`](/fio), [`pgpool_adm`](/pgpool_adm), [`pgpool_recovery`](/pgpool_recovery), [`pgpool_regclass`](/pgpool_regclass), [`pgagent`](/pgagent), [`pg_prewarm`](/pg_prewarm), [`lo`](/lo), [`basic_archive`](/basic_archive), [`basebackup_to_shell`](/basebackup_to_shell), [`old_snapshot`](/old_snapshot), [`adminpack`](/adminpack), [`amcheck`](/amcheck), [`pg_surgery`](/pg_surgery)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_squeeze](https://github.com/cybertec-postgresql/pg_squeeze) | 1.7 | **<span class="tcblue">BSD-2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_squeeze](/pg_squeeze) |  | `squeeze` |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'pg_squeeze'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION pg_squeeze;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.7 | **<span class="tcblue">BSD-2</span>** | **<span class="tccyan">PGDG</span>** | `pg_squeeze_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 1.7 | **<span class="tcblue">BSD-2</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-squeeze` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pg_squeeze` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_squeeze
```


Install `pg_squeeze` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_squeeze"]}'
```


Install `pg_squeeze` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pg_squeeze_17*;
dnf install pg_squeeze_16*;
dnf install pg_squeeze_15*;
dnf install pg_squeeze_14*;
dnf install pg_squeeze_13*;
```


Install `pg_squeeze` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-squeeze;
apt install postgresql-16-squeeze;
apt install postgresql-15-squeeze;
apt install postgresql-14-squeeze;
apt install postgresql-13-squeeze;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_squeeze_17*` | `pg_squeeze_16*` | `pg_squeeze_15*` | `pg_squeeze_14*` | `pg_squeeze_13*` |
| `el9` | `pg_squeeze_17*` | `pg_squeeze_16*` | `pg_squeeze_15*` | `pg_squeeze_14*` | `pg_squeeze_13*` |
| `d12` | `postgresql-17-squeeze` | `postgresql-16-squeeze` | `postgresql-15-squeeze` | `postgresql-14-squeeze` | `postgresql-13-squeeze` |
| `u22` | `postgresql-17-squeeze` | `postgresql-16-squeeze` | `postgresql-15-squeeze` | `postgresql-14-squeeze` | `postgresql-13-squeeze` |
| `u24` | `postgresql-17-squeeze` | `postgresql-16-squeeze` | `postgresql-15-squeeze` | `postgresql-14-squeeze` | `postgresql-13-squeeze` |






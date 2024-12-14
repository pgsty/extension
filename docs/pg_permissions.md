# pg_permissions


> [pg_permissions](https://github.com/cybertec-postgresql/pg_permissions): view object permissions and compare them with the desired state
>
> https://github.com/cybertec-postgresql/pg_permissions





[ADMIN](/admin) extensions: [`pg_repack`](/pg_repack), [`pg_squeeze`](/pg_squeeze), [`pg_dirtyread`](/pg_dirtyread), [`pgfincore`](/pgfincore), [`ddlx`](/ddlx), [`prioritize`](/prioritize), [`pg_checksums`](/pg_checksums), [`pg_readonly`](/pg_readonly), [`safeupdate`](/safeupdate), [`pg_permissions`](/pg_permissions), [`pgautofailover`](/pgautofailover), [`pg_catcheck`](/pg_catcheck), [`pre_prepare`](/pre_prepare), [`pgcozy`](/pgcozy), [`pg_orphaned`](/pg_orphaned), [`pg_crash`](/pg_crash), [`pg_cheat_funcs`](/pg_cheat_funcs), [`pg_savior`](/pg_savior), [`table_log`](/table_log), [`pg_fio`](/pg_fio), [`pgpool_adm`](/pgpool_adm), [`pgpool_recovery`](/pgpool_recovery), [`pgpool_regclass`](/pgpool_regclass), [`pgagent`](/pgagent), [`vacuumlo`](/vacuumlo), [`pg_prewarm`](/pg_prewarm), [`oid2name`](/oid2name), [`lo`](/lo), [`basic_archive`](/basic_archive), [`basebackup_to_shell`](/basebackup_to_shell), [`old_snapshot`](/old_snapshot), [`adminpack`](/adminpack), [`amcheck`](/amcheck), [`pg_surgery`](/pg_surgery)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_permissions](https://github.com/cybertec-postgresql/pg_permissions) | 1.3 | **<span class="tcblue">BSD-2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_permissions](/pg_permissions) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_permissions;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.3 | **<span class="tcblue">BSD-2</span>** | **<span class="tccyan">PGDG</span>** | `pg_permissions_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 1.3 | **<span class="tcblue">BSD-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-permissions` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pg_permissions` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_permissions"]}'
```


Install `pg_permissions` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pg_permissions_17*;
dnf install pg_permissions_16*;
dnf install pg_permissions_15*;
dnf install pg_permissions_14*;
dnf install pg_permissions_13*;
dnf install pg_permissions_12*;
```


Install `pg_permissions` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pg-permissions;
apt install postgresql-16-pg-permissions;
apt install postgresql-15-pg-permissions;
apt install postgresql-14-pg-permissions;
apt install postgresql-13-pg-permissions;
apt install postgresql-12-pg-permissions;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_permissions_17*` | `pg_permissions_16*` | `pg_permissions_15*` | `pg_permissions_14*` | `pg_permissions_13*` | `pg_permissions_12*` |
| `el9` | `pg_permissions_17*` | `pg_permissions_16*` | `pg_permissions_15*` | `pg_permissions_14*` | `pg_permissions_13*` | `pg_permissions_12*` |
| `d12` | `postgresql-17-pg-permissions` | `postgresql-16-pg-permissions` | `postgresql-15-pg-permissions` | `postgresql-14-pg-permissions` | `postgresql-13-pg-permissions` | `postgresql-12-pg-permissions` |
| `u22` | `postgresql-17-pg-permissions` | `postgresql-16-pg-permissions` | `postgresql-15-pg-permissions` | `postgresql-14-pg-permissions` | `postgresql-13-pg-permissions` | `postgresql-12-pg-permissions` |
| `u24` | `postgresql-17-pg-permissions` | `postgresql-16-pg-permissions` | `postgresql-15-pg-permissions` | `postgresql-14-pg-permissions` | `postgresql-13-pg-permissions` | `postgresql-12-pg-permissions` |






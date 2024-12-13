# pg_checksums


> [pg_checksums](https://github.com/credativ/pg_checksums): Activate/deactivate/verify checksums in offline Postgres clusters
>
> https://github.com/credativ/pg_checksums





[ADMIN](/admin) extensions: [`pg_repack`](/pg_repack), [`pg_squeeze`](/pg_squeeze), [`pg_dirtyread`](/pg_dirtyread), [`pgfincore`](/pgfincore), [`ddlx`](/ddlx), [`prioritize`](/prioritize), [`pg_checksums`](/pg_checksums), [`pg_readonly`](/pg_readonly), [`safeupdate`](/safeupdate), [`pg_permissions`](/pg_permissions), [`pgautofailover`](/pgautofailover), [`pg_catcheck`](/pg_catcheck), [`pre_prepare`](/pre_prepare), [`pgcozy`](/pgcozy), [`pg_orphaned`](/pg_orphaned), [`pg_crash`](/pg_crash), [`pg_cheat_funcs`](/pg_cheat_funcs), [`pg_savior`](/pg_savior), [`table_log`](/table_log), [`pg_fio`](/pg_fio), [`pgpool_adm`](/pgpool_adm), [`pgpool_recovery`](/pgpool_recovery), [`pgpool_regclass`](/pgpool_regclass), [`pgagent`](/pgagent), [`vacuumlo`](/vacuumlo), [`pg_prewarm`](/pg_prewarm), [`oid2name`](/oid2name), [`lo`](/lo), [`basic_archive`](/basic_archive), [`basebackup_to_shell`](/basebackup_to_shell), [`old_snapshot`](/old_snapshot), [`adminpack`](/adminpack), [`amcheck`](/amcheck), [`pg_surgery`](/pg_surgery)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_checksums](https://github.com/credativ/pg_checksums) | 1.1 | **<span class="tcblue">BSD-2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_checksums](/pg_checksums) | `bin` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.1 | **<span class="tcblue">BSD-2</span>** | **<span class="tccyan">PGDG</span>** | `pg_checksums_$v*` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 1.1 | **<span class="tcblue">BSD-2</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pg-checksums` |  | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pg_checksums` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_checksums"]}'
```


Install `pg_checksums` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install pg_checksums_17*;
yum install pg_checksums_16*;
yum install pg_checksums_15*;
yum install pg_checksums_14*;
yum install pg_checksums_13*;
yum install pg_checksums_12*;
```


Install `pg_checksums` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pg-checksums;
apt install postgresql-16-pg-checksums;
apt install postgresql-15-pg-checksums;
apt install postgresql-14-pg-checksums;
apt install postgresql-13-pg-checksums;
apt install postgresql-12-pg-checksums;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_checksums_17*` | `pg_checksums_16*` | `pg_checksums_15*` | `pg_checksums_14*` | `pg_checksums_13*` | `pg_checksums_12*` |
| `el9` | `pg_checksums_17*` | `pg_checksums_16*` | `pg_checksums_15*` | `pg_checksums_14*` | `pg_checksums_13*` | `pg_checksums_12*` |
| `d12` | `postgresql-17-pg-checksums` | `postgresql-16-pg-checksums` | `postgresql-15-pg-checksums` | `postgresql-14-pg-checksums` | `postgresql-13-pg-checksums` | `postgresql-12-pg-checksums` |
| `u22` | `postgresql-17-pg-checksums` | `postgresql-16-pg-checksums` | `postgresql-15-pg-checksums` | `postgresql-14-pg-checksums` | `postgresql-13-pg-checksums` | `postgresql-12-pg-checksums` |
| `u24` | `postgresql-17-pg-checksums` | `postgresql-16-pg-checksums` | `postgresql-15-pg-checksums` | `postgresql-14-pg-checksums` | `postgresql-13-pg-checksums` | `postgresql-12-pg-checksums` |






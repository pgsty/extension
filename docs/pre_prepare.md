# preprepare


> [preprepare](https://github.com/dimitri/preprepare): Pre Prepare your Statement server side
>
> https://github.com/dimitri/preprepare





[ADMIN](/admin) extensions: [`pg_repack`](/pg_repack), [`pg_squeeze`](/pg_squeeze), [`pg_dirtyread`](/pg_dirtyread), [`pgfincore`](/pgfincore), [`pgdd`](/pgdd), [`ddlx`](/ddlx), [`prioritize`](/prioritize), [`pg_checksums`](/pg_checksums), [`pg_readonly`](/pg_readonly), [`safeupdate`](/safeupdate), [`pg_permissions`](/pg_permissions), [`pgautofailover`](/pgautofailover), [`pg_catcheck`](/pg_catcheck), [`pre_prepare`](/pre_prepare), [`pgcozy`](/pgcozy), [`pg_orphaned`](/pg_orphaned), [`pg_crash`](/pg_crash), [`pg_cheat_funcs`](/pg_cheat_funcs), [`pg_savior`](/pg_savior), [`table_log`](/table_log), [`pg_fio`](/pg_fio), [`pgpool_adm`](/pgpool_adm), [`pgpool_recovery`](/pgpool_recovery), [`pgpool_regclass`](/pgpool_regclass), [`pgagent`](/pgagent), [`vacuumlo`](/vacuumlo), [`pg_prewarm`](/pg_prewarm), [`oid2name`](/oid2name), [`lo`](/lo), [`basic_archive`](/basic_archive), [`basebackup_to_shell`](/basebackup_to_shell), [`old_snapshot`](/old_snapshot), [`adminpack`](/adminpack), [`amcheck`](/amcheck), [`pg_surgery`](/pg_surgery)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pre_prepare](https://github.com/dimitri/preprepare) | 0.4 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [preprepare](/pre_prepare) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pre_prepare;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `preprepare_17*` | `preprepare_16*` | `preprepare_15*` | `preprepare_14*` | `preprepare_13*` | `preprepare_12*` |
| `el9` | `preprepare_17*` | `preprepare_16*` | `preprepare_15*` | `preprepare_14*` | `preprepare_13*` | `preprepare_12*` |
| `d12` | `postgresql-17-preprepare` | `postgresql-16-preprepare` | `postgresql-15-preprepare` | `postgresql-14-preprepare` | `postgresql-13-preprepare` | `postgresql-12-preprepare` |
| `u22` | `postgresql-17-preprepare` | `postgresql-16-preprepare` | `postgresql-15-preprepare` | `postgresql-14-preprepare` | `postgresql-13-preprepare` | `postgresql-12-preprepare` |
| `u24` | `postgresql-17-preprepare` | `postgresql-16-preprepare` | `postgresql-15-preprepare` | `postgresql-14-preprepare` | `postgresql-13-preprepare` | `postgresql-12-preprepare` |



Install `preprepare` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["preprepare"]}'
```


Install `preprepare` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install preprepare_17*;
yum install preprepare_16*;
yum install preprepare_15*;
yum install preprepare_14*;
yum install preprepare_13*;
yum install preprepare_12*;
```


Install `preprepare` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-preprepare;
apt install postgresql-16-preprepare;
apt install postgresql-15-preprepare;
apt install postgresql-14-preprepare;
apt install postgresql-13-preprepare;
apt install postgresql-12-preprepare;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `preprepare_17*` | `preprepare_16*` | `preprepare_15*` | `preprepare_14*` | `preprepare_13*` | `preprepare_12*` |
| `el9` | `preprepare_17*` | `preprepare_16*` | `preprepare_15*` | `preprepare_14*` | `preprepare_13*` | `preprepare_12*` |
| `d12` | `postgresql-17-preprepare` | `postgresql-16-preprepare` | `postgresql-15-preprepare` | `postgresql-14-preprepare` | `postgresql-13-preprepare` | `postgresql-12-preprepare` |
| `u22` | `postgresql-17-preprepare` | `postgresql-16-preprepare` | `postgresql-15-preprepare` | `postgresql-14-preprepare` | `postgresql-13-preprepare` | `postgresql-12-preprepare` |
| `u24` | `postgresql-17-preprepare` | `postgresql-16-preprepare` | `postgresql-15-preprepare` | `postgresql-14-preprepare` | `postgresql-13-preprepare` | `postgresql-12-preprepare` |






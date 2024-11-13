# safeupdate


> [safeupdate](https://github.com/eradman/pg-safeupdate): Require criteria for UPDATE and DELETE
>
> https://github.com/eradman/pg-safeupdate





[ADMIN](/admin) extensions: [`pg_repack`](/pg_repack), [`pg_squeeze`](/pg_squeeze), [`pg_dirtyread`](/pg_dirtyread), [`pgfincore`](/pgfincore), [`pgdd`](/pgdd), [`ddlx`](/ddlx), [`prioritize`](/prioritize), [`pg_checksums`](/pg_checksums), [`pg_readonly`](/pg_readonly), [`safeupdate`](/safeupdate), [`pg_permissions`](/pg_permissions), [`pgautofailover`](/pgautofailover), [`pg_catcheck`](/pg_catcheck), [`pre_prepare`](/pre_prepare), [`pgcozy`](/pgcozy), [`pg_orphaned`](/pg_orphaned), [`pg_crash`](/pg_crash), [`pg_cheat_funcs`](/pg_cheat_funcs), [`pg_savior`](/pg_savior), [`table_log`](/table_log), [`pg_fio`](/pg_fio), [`pgpool_adm`](/pgpool_adm), [`pgpool_recovery`](/pgpool_recovery), [`pgpool_regclass`](/pgpool_regclass), [`pgagent`](/pgagent), [`vacuumlo`](/vacuumlo), [`pg_prewarm`](/pg_prewarm), [`oid2name`](/oid2name), [`lo`](/lo), [`basic_archive`](/basic_archive), [`basebackup_to_shell`](/basebackup_to_shell), [`old_snapshot`](/old_snapshot), [`adminpack`](/adminpack), [`amcheck`](/amcheck), [`pg_surgery`](/pg_surgery)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [safeupdate](https://github.com/eradman/pg-safeupdate) | 1.4 | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [safeupdate](/safeupdate) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION safeupdate;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `safeupdate_17*` | `safeupdate_16*` | `safeupdate_15*` | `safeupdate_14*` | `safeupdate_13*` | `safeupdate_12*` |
| `el9` | `safeupdate_17*` | `safeupdate_16*` | `safeupdate_15*` | `safeupdate_14*` | `safeupdate_13*` | `safeupdate_12*` |
| `d12` | `postgresql-17-pg-safeupdate` | `postgresql-16-pg-safeupdate` | `postgresql-15-pg-safeupdate` | `postgresql-14-pg-safeupdate` | `postgresql-13-pg-safeupdate` | `postgresql-12-pg-safeupdate` |
| `u22` | `postgresql-17-pg-safeupdate` | `postgresql-16-pg-safeupdate` | `postgresql-15-pg-safeupdate` | `postgresql-14-pg-safeupdate` | `postgresql-13-pg-safeupdate` | `postgresql-12-pg-safeupdate` |
| `u24` | `postgresql-17-pg-safeupdate` | `postgresql-16-pg-safeupdate` | `postgresql-15-pg-safeupdate` | `postgresql-14-pg-safeupdate` | `postgresql-13-pg-safeupdate` | `postgresql-12-pg-safeupdate` |



Install `safeupdate` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["safeupdate"]}'
```


Install `safeupdate` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install safeupdate_17*;
yum install safeupdate_16*;
yum install safeupdate_15*;
yum install safeupdate_14*;
yum install safeupdate_13*;
yum install safeupdate_12*;
```


Install `safeupdate` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pg-safeupdate;
apt install postgresql-16-pg-safeupdate;
apt install postgresql-15-pg-safeupdate;
apt install postgresql-14-pg-safeupdate;
apt install postgresql-13-pg-safeupdate;
apt install postgresql-12-pg-safeupdate;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `safeupdate_17*` | `safeupdate_16*` | `safeupdate_15*` | `safeupdate_14*` | `safeupdate_13*` | `safeupdate_12*` |
| `el9` | `safeupdate_17*` | `safeupdate_16*` | `safeupdate_15*` | `safeupdate_14*` | `safeupdate_13*` | `safeupdate_12*` |
| `d12` | `postgresql-17-pg-safeupdate` | `postgresql-16-pg-safeupdate` | `postgresql-15-pg-safeupdate` | `postgresql-14-pg-safeupdate` | `postgresql-13-pg-safeupdate` | `postgresql-12-pg-safeupdate` |
| `u22` | `postgresql-17-pg-safeupdate` | `postgresql-16-pg-safeupdate` | `postgresql-15-pg-safeupdate` | `postgresql-14-pg-safeupdate` | `postgresql-13-pg-safeupdate` | `postgresql-12-pg-safeupdate` |
| `u24` | `postgresql-17-pg-safeupdate` | `postgresql-16-pg-safeupdate` | `postgresql-15-pg-safeupdate` | `postgresql-14-pg-safeupdate` | `postgresql-13-pg-safeupdate` | `postgresql-12-pg-safeupdate` |






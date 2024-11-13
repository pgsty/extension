# pg_squeeze


> [pg_squeeze](https://github.com/cybertec-postgresql/pg_squeeze): A tool to remove unused space from a relation.
>
> https://github.com/cybertec-postgresql/pg_squeeze





[ADMIN](/admin) extensions: [`pg_repack`](/pg_repack), [`pg_squeeze`](/pg_squeeze), [`pg_dirtyread`](/pg_dirtyread), [`pgfincore`](/pgfincore), [`pgdd`](/pgdd), [`ddlx`](/ddlx), [`prioritize`](/prioritize), [`pg_checksums`](/pg_checksums), [`pg_readonly`](/pg_readonly), [`safeupdate`](/safeupdate), [`pg_permissions`](/pg_permissions), [`pgautofailover`](/pgautofailover), [`pg_catcheck`](/pg_catcheck), [`pre_prepare`](/pre_prepare), [`pgcozy`](/pgcozy), [`pg_orphaned`](/pg_orphaned), [`pg_crash`](/pg_crash), [`pg_cheat_funcs`](/pg_cheat_funcs), [`pg_savior`](/pg_savior), [`table_log`](/table_log), [`pg_fio`](/pg_fio), [`pgpool_adm`](/pgpool_adm), [`pgpool_recovery`](/pgpool_recovery), [`pgpool_regclass`](/pgpool_regclass), [`pgagent`](/pgagent), [`vacuumlo`](/vacuumlo), [`pg_prewarm`](/pg_prewarm), [`oid2name`](/oid2name), [`lo`](/lo), [`basic_archive`](/basic_archive), [`basebackup_to_shell`](/basebackup_to_shell), [`old_snapshot`](/old_snapshot), [`adminpack`](/adminpack), [`amcheck`](/amcheck), [`pg_surgery`](/pg_surgery)


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



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'pg_squeeze'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION pg_squeeze;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_squeeze_17*` | `pg_squeeze_16*` | `pg_squeeze_15*` | `pg_squeeze_14*` | `pg_squeeze_13*` | `pg_squeeze_12*` |
| `el9` | `pg_squeeze_17*` | `pg_squeeze_16*` | `pg_squeeze_15*` | `pg_squeeze_14*` | `pg_squeeze_13*` | `pg_squeeze_12*` |
| `d12` | `postgresql-17-squeeze` | `postgresql-16-squeeze` | `postgresql-15-squeeze` | `postgresql-14-squeeze` | `postgresql-13-squeeze` | `postgresql-12-squeeze` |
| `u22` | `postgresql-17-squeeze` | `postgresql-16-squeeze` | `postgresql-15-squeeze` | `postgresql-14-squeeze` | `postgresql-13-squeeze` | `postgresql-12-squeeze` |
| `u24` | `postgresql-17-squeeze` | `postgresql-16-squeeze` | `postgresql-15-squeeze` | `postgresql-14-squeeze` | `postgresql-13-squeeze` | `postgresql-12-squeeze` |



Install `pg_squeeze` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_squeeze"]}'
```


Install `pg_squeeze` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install pg_squeeze_17*;
yum install pg_squeeze_16*;
yum install pg_squeeze_15*;
yum install pg_squeeze_14*;
yum install pg_squeeze_13*;
yum install pg_squeeze_12*;
```


Install `pg_squeeze` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-squeeze;
apt install postgresql-16-squeeze;
apt install postgresql-15-squeeze;
apt install postgresql-14-squeeze;
apt install postgresql-13-squeeze;
apt install postgresql-12-squeeze;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_squeeze_17*` | `pg_squeeze_16*` | `pg_squeeze_15*` | `pg_squeeze_14*` | `pg_squeeze_13*` | `pg_squeeze_12*` |
| `el9` | `pg_squeeze_17*` | `pg_squeeze_16*` | `pg_squeeze_15*` | `pg_squeeze_14*` | `pg_squeeze_13*` | `pg_squeeze_12*` |
| `d12` | `postgresql-17-squeeze` | `postgresql-16-squeeze` | `postgresql-15-squeeze` | `postgresql-14-squeeze` | `postgresql-13-squeeze` | `postgresql-12-squeeze` |
| `u22` | `postgresql-17-squeeze` | `postgresql-16-squeeze` | `postgresql-15-squeeze` | `postgresql-14-squeeze` | `postgresql-13-squeeze` | `postgresql-12-squeeze` |
| `u24` | `postgresql-17-squeeze` | `postgresql-16-squeeze` | `postgresql-15-squeeze` | `postgresql-14-squeeze` | `postgresql-13-squeeze` | `postgresql-12-squeeze` |






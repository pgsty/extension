# pg_fio


> [pg_fio](https://github.com/csimsek/pgsql-fio): PostgreSQL File I/O Functions
>
> https://github.com/csimsek/pgsql-fio





[ADMIN](/admin) extensions: [`pg_repack`](/pg_repack), [`pg_squeeze`](/pg_squeeze), [`pg_dirtyread`](/pg_dirtyread), [`pgfincore`](/pgfincore), [`ddlx`](/ddlx), [`prioritize`](/prioritize), [`pg_checksums`](/pg_checksums), [`pg_readonly`](/pg_readonly), [`safeupdate`](/safeupdate), [`pg_permissions`](/pg_permissions), [`pgautofailover`](/pgautofailover), [`pg_catcheck`](/pg_catcheck), [`pre_prepare`](/pre_prepare), [`pgcozy`](/pgcozy), [`pg_orphaned`](/pg_orphaned), [`pg_crash`](/pg_crash), [`pg_cheat_funcs`](/pg_cheat_funcs), [`pg_savior`](/pg_savior), [`table_log`](/table_log), [`pg_fio`](/pg_fio), [`pgpool_adm`](/pgpool_adm), [`pgpool_recovery`](/pgpool_recovery), [`pgpool_regclass`](/pgpool_regclass), [`pgagent`](/pgagent), [`pg_prewarm`](/pg_prewarm), [`lo`](/lo), [`basic_archive`](/basic_archive), [`basebackup_to_shell`](/basebackup_to_shell), [`old_snapshot`](/old_snapshot), [`adminpack`](/adminpack), [`amcheck`](/amcheck), [`pg_surgery`](/pg_surgery)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_fio](https://github.com/csimsek/pgsql-fio) | 1.0 | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_fio](/pg_fio) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_fio;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0 | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_fio_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.0 | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-fio` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pg_fio` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_fio"]}'
```


Install `pg_fio` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_fio_17;
dnf install pg_fio_16;
dnf install pg_fio_15;
dnf install pg_fio_14;
dnf install pg_fio_13;
dnf install pg_fio_12;
```


Install `pg_fio` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-fio;
apt install postgresql-16-pg-fio;
apt install postgresql-15-pg-fio;
apt install postgresql-14-pg-fio;
apt install postgresql-13-pg-fio;
apt install postgresql-12-pg-fio;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_fio_17` | `pg_fio_16` | `pg_fio_15` | `pg_fio_14` | `pg_fio_13` | `pg_fio_12` |
| `el9` | `pg_fio_17` | `pg_fio_16` | `pg_fio_15` | `pg_fio_14` | `pg_fio_13` | `pg_fio_12` |
| `d12` | `postgresql-17-pg-fio` | `postgresql-16-pg-fio` | `postgresql-15-pg-fio` | `postgresql-14-pg-fio` | `postgresql-13-pg-fio` | `postgresql-12-pg-fio` |
| `u22` | `postgresql-17-pg-fio` | `postgresql-16-pg-fio` | `postgresql-15-pg-fio` | `postgresql-14-pg-fio` | `postgresql-13-pg-fio` | `postgresql-12-pg-fio` |
| `u24` | `postgresql-17-pg-fio` | `postgresql-16-pg-fio` | `postgresql-15-pg-fio` | `postgresql-14-pg-fio` | `postgresql-13-pg-fio` | `postgresql-12-pg-fio` |






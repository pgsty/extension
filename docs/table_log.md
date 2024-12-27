# table_log


> [table_log](https://github.com/df7cb/table_log): record table modification logs and PITR for table/row
>
> https://github.com/df7cb/table_log





[ADMIN](/admin) extensions: [`pg_repack`](/pg_repack), [`pg_squeeze`](/pg_squeeze), [`pg_dirtyread`](/pg_dirtyread), [`pgfincore`](/pgfincore), [`ddlx`](/ddlx), [`prioritize`](/prioritize), [`pg_checksums`](/pg_checksums), [`pg_readonly`](/pg_readonly), [`safeupdate`](/safeupdate), [`pg_permissions`](/pg_permissions), [`pgautofailover`](/pgautofailover), [`pg_catcheck`](/pg_catcheck), [`pre_prepare`](/pre_prepare), [`pgcozy`](/pgcozy), [`pg_orphaned`](/pg_orphaned), [`pg_crash`](/pg_crash), [`pg_cheat_funcs`](/pg_cheat_funcs), [`pg_savior`](/pg_savior), [`table_log`](/table_log), [`fio`](/fio), [`pgpool_adm`](/pgpool_adm), [`pgpool_recovery`](/pgpool_recovery), [`pgpool_regclass`](/pgpool_regclass), [`pgagent`](/pgagent), [`pg_prewarm`](/pg_prewarm), [`lo`](/lo), [`basic_archive`](/basic_archive), [`basebackup_to_shell`](/basebackup_to_shell), [`old_snapshot`](/old_snapshot), [`adminpack`](/adminpack), [`amcheck`](/amcheck), [`pg_surgery`](/pg_surgery)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [table_log](https://github.com/df7cb/table_log) | 0.6.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [table_log](/table_log) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION table_log;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.6.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `table_log_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 0.6.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-tablelog` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `table_log` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add table_log
```


Install `table_log` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["table_log"]}'
```


Install `table_log` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install table_log_17;
dnf install table_log_16;
dnf install table_log_15;
dnf install table_log_14;
dnf install table_log_13;
```


Install `table_log` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-tablelog;
apt install postgresql-16-tablelog;
apt install postgresql-15-tablelog;
apt install postgresql-14-tablelog;
apt install postgresql-13-tablelog;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `table_log_17` | `table_log_16` | `table_log_15` | `table_log_14` | `table_log_13` |
| `el9` | `table_log_17` | `table_log_16` | `table_log_15` | `table_log_14` | `table_log_13` |
| `d12` | `postgresql-17-tablelog` | `postgresql-16-tablelog` | `postgresql-15-tablelog` | `postgresql-14-tablelog` | `postgresql-13-tablelog` |
| `u22` | `postgresql-17-tablelog` | `postgresql-16-tablelog` | `postgresql-15-tablelog` | `postgresql-14-tablelog` | `postgresql-13-tablelog` |
| `u24` | `postgresql-17-tablelog` | `postgresql-16-tablelog` | `postgresql-15-tablelog` | `postgresql-14-tablelog` | `postgresql-13-tablelog` |






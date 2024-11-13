# pgpool


> [pgpool](https://pgpool.net/): Administrative functions for pgPool
>
> https://pgpool.net/





[ADMIN](/admin) extensions: [`pg_repack`](/pg_repack), [`pg_squeeze`](/pg_squeeze), [`pg_dirtyread`](/pg_dirtyread), [`pgfincore`](/pgfincore), [`pgdd`](/pgdd), [`ddlx`](/ddlx), [`prioritize`](/prioritize), [`pg_checksums`](/pg_checksums), [`pg_readonly`](/pg_readonly), [`safeupdate`](/safeupdate), [`pg_permissions`](/pg_permissions), [`pgautofailover`](/pgautofailover), [`pg_catcheck`](/pg_catcheck), [`pre_prepare`](/pre_prepare), [`pgcozy`](/pgcozy), [`pg_orphaned`](/pg_orphaned), [`pg_crash`](/pg_crash), [`pg_cheat_funcs`](/pg_cheat_funcs), [`pg_savior`](/pg_savior), [`table_log`](/table_log), [`pg_fio`](/pg_fio), [`pgpool_adm`](/pgpool_adm), [`pgpool_recovery`](/pgpool_recovery), [`pgpool_regclass`](/pgpool_regclass), [`pgagent`](/pgagent), [`vacuumlo`](/vacuumlo), [`pg_prewarm`](/pg_prewarm), [`oid2name`](/oid2name), [`lo`](/lo), [`basic_archive`](/basic_archive), [`basebackup_to_shell`](/basebackup_to_shell), [`old_snapshot`](/old_snapshot), [`adminpack`](/adminpack), [`amcheck`](/amcheck), [`pg_surgery`](/pg_surgery)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgpool_adm](https://pgpool.net/) | 1.5 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgpool](/pgpool_adm) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pgpool_adm;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgpool-II-pg17-extensions` | `pgpool-II-pg16-extensions` | `pgpool-II-pg15-extensions` | `pgpool-II-pg14-extensions` | `pgpool-II-pg13-extensions` | `pgpool-II-pg12-extensions` |
| `el9` | `pgpool-II-pg17-extensions` | `pgpool-II-pg16-extensions` | `pgpool-II-pg15-extensions` | `pgpool-II-pg14-extensions` | `pgpool-II-pg13-extensions` | `pgpool-II-pg12-extensions` |
| `d12` | `postgresql-17-pgpool2` | `postgresql-16-pgpool2` | `postgresql-15-pgpool2` | `postgresql-14-pgpool2` | `postgresql-13-pgpool2` | `postgresql-12-pgpool2` |
| `u22` | `postgresql-17-pgpool2` | `postgresql-16-pgpool2` | `postgresql-15-pgpool2` | `postgresql-14-pgpool2` | `postgresql-13-pgpool2` | `postgresql-12-pgpool2` |
| `u24` | `postgresql-17-pgpool2` | `postgresql-16-pgpool2` | `postgresql-15-pgpool2` | `postgresql-14-pgpool2` | `postgresql-13-pgpool2` | `postgresql-12-pgpool2` |



Install `pgpool` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgpool"]}'
```


Install `pgpool` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install pgpool-II-pg17-extensions;
yum install pgpool-II-pg16-extensions;
yum install pgpool-II-pg15-extensions;
yum install pgpool-II-pg14-extensions;
yum install pgpool-II-pg13-extensions;
yum install pgpool-II-pg12-extensions;
```


Install `pgpool` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pgpool2;
apt install postgresql-16-pgpool2;
apt install postgresql-15-pgpool2;
apt install postgresql-14-pgpool2;
apt install postgresql-13-pgpool2;
apt install postgresql-12-pgpool2;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgpool-II-pg17-extensions` | `pgpool-II-pg16-extensions` | `pgpool-II-pg15-extensions` | `pgpool-II-pg14-extensions` | `pgpool-II-pg13-extensions` | `pgpool-II-pg12-extensions` |
| `el9` | `pgpool-II-pg17-extensions` | `pgpool-II-pg16-extensions` | `pgpool-II-pg15-extensions` | `pgpool-II-pg14-extensions` | `pgpool-II-pg13-extensions` | `pgpool-II-pg12-extensions` |
| `d12` | `postgresql-17-pgpool2` | `postgresql-16-pgpool2` | `postgresql-15-pgpool2` | `postgresql-14-pgpool2` | `postgresql-13-pgpool2` | `postgresql-12-pgpool2` |
| `u22` | `postgresql-17-pgpool2` | `postgresql-16-pgpool2` | `postgresql-15-pgpool2` | `postgresql-14-pgpool2` | `postgresql-13-pgpool2` | `postgresql-12-pgpool2` |
| `u24` | `postgresql-17-pgpool2` | `postgresql-16-pgpool2` | `postgresql-15-pgpool2` | `postgresql-14-pgpool2` | `postgresql-13-pgpool2` | `postgresql-12-pgpool2` |






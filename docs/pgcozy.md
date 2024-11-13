# pgcozy


> [pgcozy](https://github.com/vventirozos/pgcozy): Pre-warming shared buffers according to previous pg_buffercache snapshots for PostgreSQL.
>
> https://github.com/vventirozos/pgcozy





[ADMIN](/admin) extensions: [`pg_repack`](/pg_repack), [`pg_squeeze`](/pg_squeeze), [`pg_dirtyread`](/pg_dirtyread), [`pgfincore`](/pgfincore), [`pgdd`](/pgdd), [`ddlx`](/ddlx), [`prioritize`](/prioritize), [`pg_checksums`](/pg_checksums), [`pg_readonly`](/pg_readonly), [`safeupdate`](/safeupdate), [`pg_permissions`](/pg_permissions), [`pgautofailover`](/pgautofailover), [`pg_catcheck`](/pg_catcheck), [`pre_prepare`](/pre_prepare), [`pgcozy`](/pgcozy), [`pg_orphaned`](/pg_orphaned), [`pg_crash`](/pg_crash), [`pg_cheat_funcs`](/pg_cheat_funcs), [`pg_savior`](/pg_savior), [`table_log`](/table_log), [`pg_fio`](/pg_fio), [`pgpool_adm`](/pgpool_adm), [`pgpool_recovery`](/pgpool_recovery), [`pgpool_regclass`](/pgpool_regclass), [`pgagent`](/pgagent), [`vacuumlo`](/vacuumlo), [`pg_prewarm`](/pg_prewarm), [`oid2name`](/oid2name), [`lo`](/lo), [`basic_archive`](/basic_archive), [`basebackup_to_shell`](/basebackup_to_shell), [`old_snapshot`](/old_snapshot), [`adminpack`](/adminpack), [`amcheck`](/amcheck), [`pg_surgery`](/pg_surgery)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgcozy](https://github.com/vventirozos/pgcozy) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |  |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgcozy](/pgcozy) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pgcozy;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgcozy_17` | `pgcozy_16` | `pgcozy_15` | `pgcozy_14` | `pgcozy_13` | `pgcozy_12` |
| `el9` | `pgcozy_17` | `pgcozy_16` | `pgcozy_15` | `pgcozy_14` | `pgcozy_13` | `pgcozy_12` |
| `d12` | `postgresql-17-pgcozy` | `postgresql-16-pgcozy` | `postgresql-15-pgcozy` | `postgresql-14-pgcozy` | `postgresql-13-pgcozy` | `postgresql-12-pgcozy` |
| `u22` | `postgresql-17-pgcozy` | `postgresql-16-pgcozy` | `postgresql-15-pgcozy` | `postgresql-14-pgcozy` | `postgresql-13-pgcozy` | `postgresql-12-pgcozy` |
| `u24` | `postgresql-17-pgcozy` | `postgresql-16-pgcozy` | `postgresql-15-pgcozy` | `postgresql-14-pgcozy` | `postgresql-13-pgcozy` | `postgresql-12-pgcozy` |



Install `pgcozy` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgcozy"]}'
```


Install `pgcozy` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install pgcozy_17;
yum install pgcozy_16;
yum install pgcozy_15;
yum install pgcozy_14;
yum install pgcozy_13;
yum install pgcozy_12;
```


Install `pgcozy` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pgcozy;
apt install postgresql-16-pgcozy;
apt install postgresql-15-pgcozy;
apt install postgresql-14-pgcozy;
apt install postgresql-13-pgcozy;
apt install postgresql-12-pgcozy;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgcozy_17` | `pgcozy_16` | `pgcozy_15` | `pgcozy_14` | `pgcozy_13` | `pgcozy_12` |
| `el9` | `pgcozy_17` | `pgcozy_16` | `pgcozy_15` | `pgcozy_14` | `pgcozy_13` | `pgcozy_12` |
| `d12` | `postgresql-17-pgcozy` | `postgresql-16-pgcozy` | `postgresql-15-pgcozy` | `postgresql-14-pgcozy` | `postgresql-13-pgcozy` | `postgresql-12-pgcozy` |
| `u22` | `postgresql-17-pgcozy` | `postgresql-16-pgcozy` | `postgresql-15-pgcozy` | `postgresql-14-pgcozy` | `postgresql-13-pgcozy` | `postgresql-12-pgcozy` |
| `u24` | `postgresql-17-pgcozy` | `postgresql-16-pgcozy` | `postgresql-15-pgcozy` | `postgresql-14-pgcozy` | `postgresql-13-pgcozy` | `postgresql-12-pgcozy` |






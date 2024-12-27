# pgagent


> [pgagent](https://www.pgadmin.org/docs/pgadmin4/development/pgagent.html): A PostgreSQL job scheduler
>
> https://www.pgadmin.org/docs/pgadmin4/development/pgagent.html





[ADMIN](/admin) extensions: [`pg_repack`](/pg_repack), [`pg_squeeze`](/pg_squeeze), [`pg_dirtyread`](/pg_dirtyread), [`pgfincore`](/pgfincore), [`ddlx`](/ddlx), [`prioritize`](/prioritize), [`pg_checksums`](/pg_checksums), [`pg_readonly`](/pg_readonly), [`safeupdate`](/safeupdate), [`pg_permissions`](/pg_permissions), [`pgautofailover`](/pgautofailover), [`pg_catcheck`](/pg_catcheck), [`pre_prepare`](/pre_prepare), [`pgcozy`](/pgcozy), [`pg_orphaned`](/pg_orphaned), [`pg_crash`](/pg_crash), [`pg_cheat_funcs`](/pg_cheat_funcs), [`pg_savior`](/pg_savior), [`table_log`](/table_log), [`fio`](/fio), [`pgpool_adm`](/pgpool_adm), [`pgpool_recovery`](/pgpool_recovery), [`pgpool_regclass`](/pgpool_regclass), [`pgagent`](/pgagent), [`pg_prewarm`](/pg_prewarm), [`lo`](/lo), [`basic_archive`](/basic_archive), [`basebackup_to_shell`](/basebackup_to_shell), [`old_snapshot`](/old_snapshot), [`adminpack`](/adminpack), [`amcheck`](/amcheck), [`pg_surgery`](/pg_surgery)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgagent](https://www.pgadmin.org/docs/pgadmin4/development/pgagent.html) | 4.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgagent](/pgagent) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pgagent;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 4.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pgagent_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 4.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pgagent` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pgagent` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pgagent
```


Install `pgagent` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgagent"]}'
```


Install `pgagent` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pgagent_17*;
dnf install pgagent_16*;
dnf install pgagent_15*;
dnf install pgagent_14*;
dnf install pgagent_13*;
```


Install `pgagent` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install pgagent;
apt install pgagent;
apt install pgagent;
apt install pgagent;
apt install pgagent;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgagent_17*` | `pgagent_16*` | `pgagent_15*` | `pgagent_14*` | `pgagent_13*` |
| `el9` | `pgagent_17*` | `pgagent_16*` | `pgagent_15*` | `pgagent_14*` | `pgagent_13*` |
| `d12` | `pgagent` | `pgagent` | `pgagent` | `pgagent` | `pgagent` |
| `u22` | `pgagent` | `pgagent` | `pgagent` | `pgagent` | `pgagent` |
| `u24` | `pgagent` | `pgagent` | `pgagent` | `pgagent` | `pgagent` |






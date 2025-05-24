# pg_statement_rollback


> [pg_statement_rollback](https://github.com/lzlabs/pg_statement_rollback): Server side rollback at statement level for PostgreSQL like Oracle or DB2
>
> https://github.com/lzlabs/pg_statement_rollback





[SIM](/sim) extensions: [`documentdb`](/documentdb), [`documentdb_core`](/documentdb_core), [`documentdb_distributed`](/documentdb_distributed), [`orafce`](/orafce), [`pgtt`](/pgtt), [`session_variable`](/session_variable), [`pg_statement_rollback`](/pg_statement_rollback), [`pg_dbms_metadata`](/pg_dbms_metadata), [`pg_dbms_lock`](/pg_dbms_lock), [`pg_dbms_job`](/pg_dbms_job), [`babelfishpg_common`](/babelfishpg_common), [`babelfishpg_tsql`](/babelfishpg_tsql), [`babelfishpg_tds`](/babelfishpg_tds), [`babelfishpg_money`](/babelfishpg_money), [`spat`](/spat), [`pgmemcache`](/pgmemcache)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_statement_rollback](https://github.com/lzlabs/pg_statement_rollback) | 1.4 | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_statement_rollback](/pg_statement_rollback) | `oracle` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'pg_statement_rollback'; # add this extension to postgresql.conf
```



-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.4 | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | `pg_statement_rollback_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 1.4 | **<span class="tcblue">ISC</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-statement-rollback` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pg_statement_rollback` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_statement_rollback
```


Install `pg_statement_rollback` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_statement_rollback"]}'
```


Install `pg_statement_rollback` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pg_statement_rollback_17*;
dnf install pg_statement_rollback_16*;
dnf install pg_statement_rollback_15*;
dnf install pg_statement_rollback_14*;
dnf install pg_statement_rollback_13*;
```


Install `pg_statement_rollback` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-statement-rollback;
apt install postgresql-16-pg-statement-rollback;
apt install postgresql-15-pg-statement-rollback;
apt install postgresql-14-pg-statement-rollback;
apt install postgresql-13-pg-statement-rollback;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_statement_rollback_17*` | `pg_statement_rollback_16*` | `pg_statement_rollback_15*` | `pg_statement_rollback_14*` | `pg_statement_rollback_13*` |
| `el9` | `pg_statement_rollback_17*` | `pg_statement_rollback_16*` | `pg_statement_rollback_15*` | `pg_statement_rollback_14*` | `pg_statement_rollback_13*` |
| `d12` | `postgresql-17-pg-statement-rollback` | `postgresql-16-pg-statement-rollback` | `postgresql-15-pg-statement-rollback` | `postgresql-14-pg-statement-rollback` | `postgresql-13-pg-statement-rollback` |
| `u22` | `postgresql-17-pg-statement-rollback` | `postgresql-16-pg-statement-rollback` | `postgresql-15-pg-statement-rollback` | `postgresql-14-pg-statement-rollback` | `postgresql-13-pg-statement-rollback` |
| `u24` | `postgresql-17-pg-statement-rollback` | `postgresql-16-pg-statement-rollback` | `postgresql-15-pg-statement-rollback` | `postgresql-14-pg-statement-rollback` | `postgresql-13-pg-statement-rollback` |






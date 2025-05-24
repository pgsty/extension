# session_variable


> [session_variable](https://github.com/splendiddata/session_variable): Registration and manipulation of session variables and constants
>
> https://github.com/splendiddata/session_variable





[SIM](/sim) extensions: [`documentdb`](/documentdb), [`documentdb_core`](/documentdb_core), [`documentdb_distributed`](/documentdb_distributed), [`orafce`](/orafce), [`pgtt`](/pgtt), [`session_variable`](/session_variable), [`pg_statement_rollback`](/pg_statement_rollback), [`pg_dbms_metadata`](/pg_dbms_metadata), [`pg_dbms_lock`](/pg_dbms_lock), [`pg_dbms_job`](/pg_dbms_job), [`babelfishpg_common`](/babelfishpg_common), [`babelfishpg_tsql`](/babelfishpg_tsql), [`babelfishpg_tds`](/babelfishpg_tds), [`babelfishpg_money`](/babelfishpg_money), [`spat`](/spat), [`pgmemcache`](/pgmemcache)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [session_variable](https://github.com/splendiddata/session_variable) | 3.4 | **<span class="tcwarn">GPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [session_variable](/session_variable) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION session_variable;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 3.4 | **<span class="tcwarn">GPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `session_variable_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 3.4 | **<span class="tcwarn">GPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-session-variable` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `session_variable` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add session_variable
```


Install `session_variable` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["session_variable"]}'
```


Install `session_variable` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install session_variable_17*;
dnf install session_variable_16*;
dnf install session_variable_15*;
dnf install session_variable_14*;
dnf install session_variable_13*;
```


Install `session_variable` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-session-variable;
apt install postgresql-16-session-variable;
apt install postgresql-15-session-variable;
apt install postgresql-14-session-variable;
apt install postgresql-13-session-variable;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `session_variable_17*` | `session_variable_16*` | `session_variable_15*` | `session_variable_14*` | `session_variable_13*` |
| `el9` | `session_variable_17*` | `session_variable_16*` | `session_variable_15*` | `session_variable_14*` | `session_variable_13*` |
| `d12` | `postgresql-17-session-variable` | `postgresql-16-session-variable` | `postgresql-15-session-variable` | `postgresql-14-session-variable` | `postgresql-13-session-variable` |
| `u22` | `postgresql-17-session-variable` | `postgresql-16-session-variable` | `postgresql-15-session-variable` | `postgresql-14-session-variable` | `postgresql-13-session-variable` |
| `u24` | `postgresql-17-session-variable` | `postgresql-16-session-variable` | `postgresql-15-session-variable` | `postgresql-14-session-variable` | `postgresql-13-session-variable` |






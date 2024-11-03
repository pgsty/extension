# pg_statement_rollback


> [pg_statement_rollback](https://github.com/lzlabs/pg_statement_rollback): Server side rollback at statement level for PostgreSQL like Oracle or DB2
>
> https://github.com/lzlabs/pg_statement_rollback





[SIM](/sim) extensions: [`orafce`](/orafce), [`pgtt`](/pgtt), [`session_variable`](/session_variable), [`pg_statement_rollback`](/pg_statement_rollback), [`pg_dbms_metadata`](/pg_dbms_metadata), [`pg_dbms_lock`](/pg_dbms_lock), [`pg_dbms_job`](/pg_dbms_job), [`babelfishpg_common`](/babelfishpg_common), [`babelfishpg_tsql`](/babelfishpg_tsql), [`babelfishpg_tds`](/babelfishpg_tds), [`babelfishpg_money`](/babelfishpg_money), [`pgmemcache`](/pgmemcache)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [pg_statement_rollback](https://github.com/lzlabs/pg_statement_rollback) | 1.4 | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |



| Package | Tags | Schemas | Requires | Required by |
|---------|------|---------|----------|-------------|
| [pg_statement_rollback](/pg_statement_rollback) | `oracle` |  |  |  |



```bash
shared_preload_libraries = 'pg_statement_rollback'; # add this extension to postgresql.conf
```



-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.4 | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | `pg_statement_rollback_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 1.4 | **<span class="tcblue">ISC</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-statement-rollback` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pg_statement_rollback` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

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
dnf install pg_statement_rollback_12*;
```


Install `pg_statement_rollback` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pg-statement-rollback;
apt install postgresql-16-pg-statement-rollback;
apt install postgresql-15-pg-statement-rollback;
apt install postgresql-14-pg-statement-rollback;
apt install postgresql-13-pg-statement-rollback;
apt install postgresql-12-pg-statement-rollback;
```








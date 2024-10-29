# pgtt


> [pgtt](https://github.com/darold/pgtt): Extension to add Global Temporary Tables feature to PostgreSQL
>
> https://github.com/darold/pgtt


-------


## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [pgtt](https://github.com/darold/pgtt) | 4.0.0 | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |



| Package | Tags | Schemas | Requires | Required by | Comment | Description |
|---------|------|---------|----------|-------------|:-------:|-------------|
| [pgtt](/pgtt) | `oracle` |  |  |  |  | Extension to add Global Temporary Tables feature to PostgreSQL |





```sql
CREATE EXTENSION pgtt;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 4.0.0 | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | `pgtt_$v*` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |
| [DEB](/deb) | 4.0.0 | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pgtt` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |



Install `pgtt` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgtt"]}'
```


Install `pgtt` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pgtt_17*;
dnf install pgtt_16*;
dnf install pgtt_15*;
dnf install pgtt_14*;
dnf install pgtt_13*;
dnf install pgtt_12*;
```


Install `pgtt` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pgtt;
apt install postgresql-16-pgtt;
apt install postgresql-15-pgtt;
apt install postgresql-14-pgtt;
apt install postgresql-13-pgtt;
apt install postgresql-12-pgtt;
```


-----------


## Category: SIM


| ID | Extension | Version | Package | License | RPM | DEB | PL | Tags | Schemas | Requires | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:--:|------|---------|----------|:------:|:-------:|:-----:|:-------:|:-------:|
| 9000 | [orafce](/orafce) | 4.13 | [orafce](/orafce) | **<span class="tcblue">BSD-0</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  | `oracle` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 9010 | [pgtt](/pgtt) | 4.0.0 | [pgtt](/pgtt) | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  | `oracle` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 9020 | [session_variable](/session_variable) | 3.4 | [session_variable](/session_variable) | **<span class="tcwarn">GPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |
| 9030 | [pg_statement_rollback](/pg_statement_rollback) | 1.4 | [pg_statement_rollback](/pg_statement_rollback) | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` | `oracle` |  |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9040 | [pg_dbms_metadata](/pg_dbms_metadata) | 1.0.0 | [pg_dbms_metadata](/pg_dbms_metadata) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** |  |  | `oracle` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 9050 | [pg_dbms_lock](/pg_dbms_lock) | 1.0.0 | [pg_dbms_lock](/pg_dbms_lock) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** |  |  | `oracle` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 9060 | [pg_dbms_job](/pg_dbms_job) | 1.5.0 | [pg_dbms_job](/pg_dbms_job) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** |  |  | `oracle`, `dep-break` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 9100 | [babelfishpg_common](/babelfishpg_common) | 3.3.3 | [babelfishpg_common](/babelfishpg_common) | **<span class="tccyan">Apache-2</span>** | **<span class="tcorange">WILTON</span>** | **<span class="tcorange">WILTON</span>** |  | `mssql` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 9110 | [babelfishpg_tsql](/babelfishpg_tsql) | 3.3.1 | [babelfishpg_tsql](/babelfishpg_tsql) | **<span class="tccyan">Apache-2</span>** | **<span class="tcorange">WILTON</span>** | **<span class="tcorange">WILTON</span>** |  | `mssql` |  | [`babelfishpg_common`](babelfishpg_common), [`uuid-ossp`](uuid-ossp) | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 9120 | [babelfishpg_tds](/babelfishpg_tds) | 1.0.0 | [babelfishpg_tds](/babelfishpg_tds) | **<span class="tccyan">Apache-2</span>** | **<span class="tcorange">WILTON</span>** | **<span class="tcorange">WILTON</span>** |  | `mssql` |  | [`babelfishpg_tsql`](babelfishpg_tsql) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 9130 | [babelfishpg_money](/babelfishpg_money) | 1.1.0 | [babelfishpg_money](/babelfishpg_money) | **<span class="tccyan">Apache-2</span>** | **<span class="tcorange">WILTON</span>** | **<span class="tcorange">WILTON</span>** |  | `mssql` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |
| 9200 | [pgmemcache](/pgmemcache) | 2.3.0 | [pgmemcache](/pgmemcache) | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |




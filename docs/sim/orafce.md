# orafce


> [orafce](/https://github.com/orafce/orafce): Functions and operators that emulate a subset of functions and packages from the Oracle RDBMS


-------

## Extension


| ID | Extension | Version | License | RPM | DEB | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` | Requires |
|:--:|-----------|:-------:|:-------:|:---:|:---:|:------:|:-------:|:-----:|:-------:|:-------:|----------|
| 9000 | [orafce](https://github.com/orafce/orafce) | 4.13 | **<span class="tcblue">BSD-0</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |





```sql
CREATE EXTENSION orafce;
```


-----------


## Packages


| OS | Version | License | RPM | RPM Package | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 4.13 | **<span class="tcblue">BSD-0</span>** | **<span class="tccyan">PGDG</span>** | `orafce_$v*` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |
| [DEB](/deb) | 4.13 | **<span class="tcblue">BSD-0</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-orafce` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |



Install `orafce` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install orafce_17*;
dnf install orafce_16*;
dnf install orafce_15*;
dnf install orafce_14*;
dnf install orafce_13*;
dnf install orafce_12*;
```


Install `orafce` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-orafce;
apt install postgresql-16-orafce;
apt install postgresql-15-orafce;
apt install postgresql-14-orafce;
apt install postgresql-13-orafce;
apt install postgresql-12-orafce;
```


-----------


## Category: SIM


| ID | Extension | Version | Package | License | RPM | DEB | lang | Tags | Schemas | Requires | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:----:|------|---------|----------|:------:|:-------:|:-----:|:-------:|:-------:|
| 9000 | [orafce](/sim/orafce) | 4.13 | [orafce](/sim/orafce) | **<span class="tcblue">BSD-0</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  | `oracle` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 9010 | [pgtt](/sim/pgtt) | 4.0.0 | [pgtt](/sim/pgtt) | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  | `oracle` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 9020 | [session_variable](/sim/session_variable) | 3.4 | [session_variable](/sim/session_variable) | **<span class="tcwarn">GPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | C |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |
| 9030 | [pg_statement_rollback](/sim/pg_statement_rollback) | 1.4 | [pg_statement_rollback](/sim/pg_statement_rollback) | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** | C | `oracle` |  |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9040 | [pg_dbms_metadata](/sim/pg_dbms_metadata) | 1.0.0 | [pg_dbms_metadata](/sim/pg_dbms_metadata) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | PGDG |  | `oracle` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 9050 | [pg_dbms_lock](/sim/pg_dbms_lock) | 1.0.0 | [pg_dbms_lock](/sim/pg_dbms_lock) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | PGDG |  | `oracle` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 9060 | [pg_dbms_job](/sim/pg_dbms_job) | 1.5.0 | [pg_dbms_job](/sim/pg_dbms_job) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | PGDG |  | `oracle`, `dep-break` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 9100 | [babelfishpg_common](/sim/babelfishpg_common) | 3.3.3 | [babelfishpg_common](/sim/babelfishpg_common) | **<span class="tccyan">Apache-2</span>** | **<span class="tcorange">WILTON</span>** | **<span class="tcorange">WILTON</span>** |  | `mssql` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 9110 | [babelfishpg_tsql](/sim/babelfishpg_tsql) | 3.3.1 | [babelfishpg_tsql](/sim/babelfishpg_tsql) | **<span class="tccyan">Apache-2</span>** | **<span class="tcorange">WILTON</span>** | **<span class="tcorange">WILTON</span>** |  | `mssql` |  | [`babelfishpg_common`](/sim/babelfishpg_common), [`uuid-ossp`](/func/uuid-ossp) | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 9120 | [babelfishpg_tds](/sim/babelfishpg_tds) | 1.0.0 | [babelfishpg_tds](/sim/babelfishpg_tds) | **<span class="tccyan">Apache-2</span>** | **<span class="tcorange">WILTON</span>** | **<span class="tcorange">WILTON</span>** |  | `mssql` |  | [`babelfishpg_tsql`](/sim/babelfishpg_tsql) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 9130 | [babelfishpg_money](/sim/babelfishpg_money) | 1.1.0 | [babelfishpg_money](/sim/babelfishpg_money) | **<span class="tccyan">Apache-2</span>** | **<span class="tcorange">WILTON</span>** | **<span class="tcorange">WILTON</span>** |  | `mssql` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |
| 9200 | [pgmemcache](/sim/pgmemcache) | 2.3.0 | [pgmemcache](/sim/pgmemcache) | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |




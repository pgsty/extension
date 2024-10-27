# babelfishpg_money


> [babelfishpg_money](/https://babelfishpg.org/): SQL Server Money Data Type


-------

## Extension


| ID | Extension | Version | License | RPM | DEB | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` | Requires |
|:--:|-----------|:-------:|:-------:|:---:|:---:|:------:|:-------:|:-----:|:-------:|:-------:|----------|
| 9130 | [babelfishpg_money](https://babelfishpg.org/) | 1.1.0 | **<span class="tccyan">Apache-2</span>** | **<span class="tcorange">WILTON</span>** | **<span class="tcorange">WILTON</span>** |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |


> **Comment**: works on wiltondb fork


```sql
CREATE EXTENSION babelfishpg_money;
```


-----------


## Packages


| OS | Version | License | RPM | RPM Package | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.1.0 | **<span class="tccyan">Apache-2</span>** | **<span class="tcorange">WILTON</span>** | `babelfishpg-money*` |  |  | <span class="tcblue">✔</span> |  |  |  |  |
| [DEB](/deb) | 1.1.0 | **<span class="tccyan">Apache-2</span>** | **<span class="tcorange">WILTON</span>** | `babelfishpg-money` |  |  | <span class="tcblue">✔</span> |  |  |  |  |



Install `babelfishpg_money` [RPM](/rpm) from the **<span class="tcorange">WILTON</span>** **YUM** repo:

```bash
dnf install babelfishpg-money*;
```


Install `babelfishpg_money` [DEB](/deb) from the **<span class="tcorange">WILTON</span>** **APT** repo:

```bash
apt install babelfishpg-money;
```


-----------


## Category: SIM


| ID | Extension | Version | Package | License | RPM | DEB | lang | Tags | Schemas | Requires | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:----:|------|---------|----------|:------:|:-------:|:-----:|:-------:|:-------:|
| 9000 | [orafce](/orafce) | 4.13 | [orafce](/orafce) | **<span class="tcblue">BSD-0</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  | `oracle` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 9010 | [pgtt](/pgtt) | 4.0.0 | [pgtt](/pgtt) | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  | `oracle` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 9020 | [session_variable](/session_variable) | 3.4 | [session_variable](/session_variable) | **<span class="tcwarn">GPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | C |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |
| 9030 | [pg_statement_rollback](/pg_statement_rollback) | 1.4 | [pg_statement_rollback](/pg_statement_rollback) | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** | C | `oracle` |  |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |
| 9040 | [pg_dbms_metadata](/pg_dbms_metadata) | 1.0.0 | [pg_dbms_metadata](/pg_dbms_metadata) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | PGDG |  | `oracle` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 9050 | [pg_dbms_lock](/pg_dbms_lock) | 1.0.0 | [pg_dbms_lock](/pg_dbms_lock) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | PGDG |  | `oracle` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 9060 | [pg_dbms_job](/pg_dbms_job) | 1.5.0 | [pg_dbms_job](/pg_dbms_job) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | PGDG |  | `oracle`, `dep-break` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |
| 9100 | [babelfishpg_common](/babelfishpg_common) | 3.3.3 | [babelfishpg_common](/babelfishpg_common) | **<span class="tccyan">Apache-2</span>** | **<span class="tcorange">WILTON</span>** | **<span class="tcorange">WILTON</span>** |  | `mssql` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 9110 | [babelfishpg_tsql](/babelfishpg_tsql) | 3.3.1 | [babelfishpg_tsql](/babelfishpg_tsql) | **<span class="tccyan">Apache-2</span>** | **<span class="tcorange">WILTON</span>** | **<span class="tcorange">WILTON</span>** |  | `mssql` |  | [`babelfishpg_common`](babelfishpg_common), [`uuid-ossp`](uuid-ossp) | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 9120 | [babelfishpg_tds](/babelfishpg_tds) | 1.0.0 | [babelfishpg_tds](/babelfishpg_tds) | **<span class="tccyan">Apache-2</span>** | **<span class="tcorange">WILTON</span>** | **<span class="tcorange">WILTON</span>** |  | `mssql` |  | [`babelfishpg_tsql`](babelfishpg_tsql) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 9130 | [babelfishpg_money](/babelfishpg_money) | 1.1.0 | [babelfishpg_money](/babelfishpg_money) | **<span class="tccyan">Apache-2</span>** | **<span class="tcorange">WILTON</span>** | **<span class="tcorange">WILTON</span>** |  | `mssql` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |
| 9200 | [pgmemcache](/pgmemcache) | 2.3.0 | [pgmemcache](/pgmemcache) | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |




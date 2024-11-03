# babelfishpg_common


> [babelfishpg_common](https://babelfishpg.org/): SQL Server Transact SQL Datatype Support
>
> https://babelfishpg.org/





[SIM](/sim) extensions: [`orafce`](/orafce), [`pgtt`](/pgtt), [`session_variable`](/session_variable), [`pg_statement_rollback`](/pg_statement_rollback), [`pg_dbms_metadata`](/pg_dbms_metadata), [`pg_dbms_lock`](/pg_dbms_lock), [`pg_dbms_job`](/pg_dbms_job), [`babelfishpg_common`](/babelfishpg_common), [`babelfishpg_tsql`](/babelfishpg_tsql), [`babelfishpg_tds`](/babelfishpg_tds), [`babelfishpg_money`](/babelfishpg_money), [`pgmemcache`](/pgmemcache)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [babelfishpg_common](https://babelfishpg.org/) | 3.3.3 | **<span class="tccyan">Apache-2</span>** | **<span class="tcpurple">WILTON</span>** | **<span class="tcpurple">WILTON</span>** |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Package | Tags | Schemas | Requires | Required by |
|---------|------|---------|----------|-------------|
| [babelfishpg_common](/babelfishpg_common) | `mssql` |  |  | [`babelfishpg_tsql`](/babelfishpg_tsql) |





```sql
CREATE EXTENSION babelfishpg_common;
```
> **Comment**: works on wiltondb kernel fork
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 3.3.3 | **<span class="tccyan">Apache-2</span>** | **<span class="tcpurple">WILTON</span>** | `babelfishpg-common*` |  |  | **<span class="tcpurple">✔</span>** |  |  |  |  |
| [DEB](/deb) | 3.3.3 | **<span class="tccyan">Apache-2</span>** | **<span class="tcpurple">WILTON</span>** | `babelfishpg-common` |  |  | **<span class="tcpurple">✔</span>** |  |  |  |  |



Install `babelfishpg_common` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["babelfishpg_common"]}'
```


Install `babelfishpg_common` [RPM](/rpm) from the **<span class="tcpurple">WILTON</span>** **YUM** repo:

```bash
dnf instsall babelfishpg-common*;
```


Install `babelfishpg_common` [DEB](/deb) from the **<span class="tcpurple">WILTON</span>** **APT** repo:

```bash
apt install babelfishpg-common;
```








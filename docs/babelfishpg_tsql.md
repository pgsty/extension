# babelfishpg_tsql


> [babelfishpg_tsql](https://babelfishpg.org/): SQL Server Transact SQL compatibility
>
> https://babelfishpg.org/





[SIM](/sim) extensions: [`orafce`](/orafce), [`pgtt`](/pgtt), [`session_variable`](/session_variable), [`pg_statement_rollback`](/pg_statement_rollback), [`pg_dbms_metadata`](/pg_dbms_metadata), [`pg_dbms_lock`](/pg_dbms_lock), [`pg_dbms_job`](/pg_dbms_job), [`babelfishpg_common`](/babelfishpg_common), [`babelfishpg_tsql`](/babelfishpg_tsql), [`babelfishpg_tds`](/babelfishpg_tds), [`babelfishpg_money`](/babelfishpg_money), [`pgmemcache`](/pgmemcache)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [babelfishpg_tsql](https://babelfishpg.org/) | 3.3.1 | **<span class="tccyan">Apache-2</span>** | **<span class="tcpurple">WILTON</span>** | **<span class="tcpurple">WILTON</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [babelfishpg_tsql](/babelfishpg_tsql) | `mssql` |  | [`babelfishpg_common`](babelfishpg_common), [`uuid-ossp`](uuid-ossp) | [`babelfishpg_tds`](/babelfishpg_tds) |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> |
| `el9` | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> |
| `d12` | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> |
| `u22` | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> |
| `u24` | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> |



```bash
shared_preload_libraries = 'babelfishpg_tsql'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION babelfishpg_tsql CASCADE;
```
> **Comment**: works on wiltondb kernel fork
-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` |
| `el9` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` |
| `d12` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` |
| `u22` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` |
| `u24` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` |



Install `babelfishpg_tsql` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["babelfishpg_tsql"]}'
```


Install `babelfishpg_tsql` [RPM](/rpm) from the **<span class="tcpurple">WILTON</span>** **YUM** repo:

```bash
dnf install babelfishpg-tsql*;
```


Install `babelfishpg_tsql` [DEB](/deb) from the **<span class="tcpurple">WILTON</span>** **APT** repo:

```bash
apt install babelfishpg-tsql;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` |
| `el9` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` |
| `d12` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` |
| `u22` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` |
| `u24` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` |






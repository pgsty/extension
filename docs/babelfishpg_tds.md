# babelfishpg_tds


> [babelfishpg_tds](https://babelfishpg.org/): SQL Server TDS protocol extension
>
> https://babelfishpg.org/





[SIM](/sim) extensions: [`orafce`](/orafce), [`pgtt`](/pgtt), [`session_variable`](/session_variable), [`pg_statement_rollback`](/pg_statement_rollback), [`pg_dbms_metadata`](/pg_dbms_metadata), [`pg_dbms_lock`](/pg_dbms_lock), [`pg_dbms_job`](/pg_dbms_job), [`babelfishpg_common`](/babelfishpg_common), [`babelfishpg_tsql`](/babelfishpg_tsql), [`babelfishpg_tds`](/babelfishpg_tds), [`babelfishpg_money`](/babelfishpg_money), [`pgmemcache`](/pgmemcache)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [babelfishpg_tds](https://babelfishpg.org/) | 1.0.0 | **<span class="tccyan">Apache-2</span>** | **<span class="tcpurple">WILTON</span>** | **<span class="tcpurple">WILTON</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [babelfishpg_tds](/babelfishpg_tds) | `mssql` |  | [`babelfishpg_tsql`](babelfishpg_tsql) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> |
| `el9` | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> |
| `d12` | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> |
| `u22` | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> |
| `u24` | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> |





```sql
CREATE EXTENSION babelfishpg_tds CASCADE;
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



Install `babelfishpg_tds` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["babelfishpg_tds"]}'
```


Install `babelfishpg_tds` [RPM](/rpm) from the **<span class="tcpurple">WILTON</span>** **YUM** repo:

```bash
dnf install babelfishpg-tds*;
```


Install `babelfishpg_tds` [DEB](/deb) from the **<span class="tcpurple">WILTON</span>** **APT** repo:

```bash
apt install babelfishpg-tds;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` |
| `el9` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` |
| `d12` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` |
| `u22` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` |
| `u24` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` | `wiltondb` |





--------

## Usage

Install `go-sqlcmd`:

```bash
curl -LO https://github.com/microsoft/go-sqlcmd/releases/download/v1.4.0/sqlcmd-v1.4.0-linux-amd64.tar.bz2
tar xjvf sqlcmd-v1.4.0-linux-amd64.tar.bz2
sudo mv sqlcmd* /usr/bin/
```

Try go-sqlcmd

```bash
$ sqlcmd -S 10.10.10.10,1433 -U dbuser_mssql -P DBUser.MSSQL
1> select @@version
2> go
version                                                                                                                                                                                                                                                         
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Babelfish for PostgreSQL with SQL Server Compatibility - 12.0.2000.8
Oct 22 2023 17:48:32
Copyright (c) Amazon Web Services
PostgreSQL 15.4 (EL 1:15.4.wiltondb3.3_2-2.el8) on x86_64-redhat-linux-gnu (Babelfish 3.3.0)                                        

(1 row affected)
```

Access pigsty exposed primary/replica service port

```bash 
sqlcmd -S 10.10.10.11,5433 -U dbuser_mssql -P DBUser.MSSQL

sqlcmd -S 10.10.10.11,5434 -U dbuser_mssql -P DBUser.MSSQL
```

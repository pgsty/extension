# pgmemcache


> [pgmemcache](https://github.com/ohmu/pgmemcache): memcached interface
>
> https://github.com/ohmu/pgmemcache





[SIM](/sim) extensions: [`orafce`](/orafce), [`pgtt`](/pgtt), [`session_variable`](/session_variable), [`pg_statement_rollback`](/pg_statement_rollback), [`pg_dbms_metadata`](/pg_dbms_metadata), [`pg_dbms_lock`](/pg_dbms_lock), [`pg_dbms_job`](/pg_dbms_job), [`babelfishpg_common`](/babelfishpg_common), [`babelfishpg_tsql`](/babelfishpg_tsql), [`babelfishpg_tds`](/babelfishpg_tds), [`babelfishpg_money`](/babelfishpg_money), [`pgmemcache`](/pgmemcache)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgmemcache](https://github.com/ohmu/pgmemcache) | 2.3.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgmemcache](/pgmemcache) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pgmemcache;
```
> **Comment**: missing 14,13,12 on el pgdg
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 2.3.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `pgmemcache_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |  |  |  |
| [DEB](/deb) | 2.3.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pgmemcache` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |  |  |  |



Install `pgmemcache` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgmemcache"]}'
```


Install `pgmemcache` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install pgmemcache_17*;
yum install pgmemcache_16*;
yum install pgmemcache_15*;
yum install pgmemcache_14*;
yum install pgmemcache_13*;
yum install pgmemcache_12*;
```


Install `pgmemcache` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pgmemcache;
apt install postgresql-16-pgmemcache;
apt install postgresql-15-pgmemcache;
apt install postgresql-14-pgmemcache;
apt install postgresql-13-pgmemcache;
apt install postgresql-12-pgmemcache;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgmemcache_17*` | `pgmemcache_16*` | `pgmemcache_15*` | `pgmemcache_14*` | `pgmemcache_13*` | `pgmemcache_12*` |
| `el9` | `pgmemcache_17*` | `pgmemcache_16*` | `pgmemcache_15*` | `pgmemcache_14*` | `pgmemcache_13*` | `pgmemcache_12*` |
| `d12` | `postgresql-17-pgmemcache` | `postgresql-16-pgmemcache` | `postgresql-15-pgmemcache` | `postgresql-14-pgmemcache` | `postgresql-13-pgmemcache` | `postgresql-12-pgmemcache` |
| `u22` | `postgresql-17-pgmemcache` | `postgresql-16-pgmemcache` | `postgresql-15-pgmemcache` | `postgresql-14-pgmemcache` | `postgresql-13-pgmemcache` | `postgresql-12-pgmemcache` |
| `u24` | `postgresql-17-pgmemcache` | `postgresql-16-pgmemcache` | `postgresql-15-pgmemcache` | `postgresql-14-pgmemcache` | `postgresql-13-pgmemcache` | `postgresql-12-pgmemcache` |






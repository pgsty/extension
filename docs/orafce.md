# orafce


> [orafce](https://github.com/orafce/orafce): Functions and operators that emulate a subset of functions and packages from the Oracle RDBMS
>
> https://github.com/orafce/orafce





[SIM](/sim) extensions: [`orafce`](/orafce), [`pgtt`](/pgtt), [`session_variable`](/session_variable), [`pg_statement_rollback`](/pg_statement_rollback), [`pg_dbms_metadata`](/pg_dbms_metadata), [`pg_dbms_lock`](/pg_dbms_lock), [`pg_dbms_job`](/pg_dbms_job), [`babelfishpg_common`](/babelfishpg_common), [`babelfishpg_tsql`](/babelfishpg_tsql), [`babelfishpg_tds`](/babelfishpg_tds), [`babelfishpg_money`](/babelfishpg_money), [`pgmemcache`](/pgmemcache)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [orafce](https://github.com/orafce/orafce) | 4.14 | **<span class="tcblue">BSD-0</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [orafce](/orafce) | `oracle` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION orafce;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 4.14 | **<span class="tcblue">BSD-0</span>** | **<span class="tccyan">PGDG</span>** | `orafce_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 4.13 | **<span class="tcblue">BSD-0</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-orafce` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `orafce` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["orafce"]}'
```


Install `orafce` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install orafce_17*;
yum install orafce_16*;
yum install orafce_15*;
yum install orafce_14*;
yum install orafce_13*;
yum install orafce_12*;
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




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `orafce_17*` | `orafce_16*` | `orafce_15*` | `orafce_14*` | `orafce_13*` | `orafce_12*` |
| `el9` | `orafce_17*` | `orafce_16*` | `orafce_15*` | `orafce_14*` | `orafce_13*` | `orafce_12*` |
| `d12` | `postgresql-17-orafce` | `postgresql-16-orafce` | `postgresql-15-orafce` | `postgresql-14-orafce` | `postgresql-13-orafce` | `postgresql-12-orafce` |
| `u22` | `postgresql-17-orafce` | `postgresql-16-orafce` | `postgresql-15-orafce` | `postgresql-14-orafce` | `postgresql-13-orafce` | `postgresql-12-orafce` |
| `u24` | `postgresql-17-orafce` | `postgresql-16-orafce` | `postgresql-15-orafce` | `postgresql-14-orafce` | `postgresql-13-orafce` | `postgresql-12-orafce` |






# pgtt


> [pgtt](https://github.com/darold/pgtt): Extension to add Global Temporary Tables feature to PostgreSQL
>
> https://github.com/darold/pgtt





[SIM](/sim) extensions: [`orafce`](/orafce), [`pgtt`](/pgtt), [`session_variable`](/session_variable), [`pg_statement_rollback`](/pg_statement_rollback), [`pg_dbms_metadata`](/pg_dbms_metadata), [`pg_dbms_lock`](/pg_dbms_lock), [`pg_dbms_job`](/pg_dbms_job), [`babelfishpg_common`](/babelfishpg_common), [`babelfishpg_tsql`](/babelfishpg_tsql), [`babelfishpg_tds`](/babelfishpg_tds), [`babelfishpg_money`](/babelfishpg_money), [`pgmemcache`](/pgmemcache)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgtt](https://github.com/darold/pgtt) | 4.0.0 | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgtt](/pgtt) | `oracle` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pgtt;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgtt_17*` | `pgtt_16*` | `pgtt_15*` | `pgtt_14*` | `pgtt_13*` | `pgtt_12*` |
| `el9` | `pgtt_17*` | `pgtt_16*` | `pgtt_15*` | `pgtt_14*` | `pgtt_13*` | `pgtt_12*` |
| `d12` | `postgresql-17-pgtt` | `postgresql-16-pgtt` | `postgresql-15-pgtt` | `postgresql-14-pgtt` | `postgresql-13-pgtt` | `postgresql-12-pgtt` |
| `u22` | `postgresql-17-pgtt` | `postgresql-16-pgtt` | `postgresql-15-pgtt` | `postgresql-14-pgtt` | `postgresql-13-pgtt` | `postgresql-12-pgtt` |
| `u24` | `postgresql-17-pgtt` | `postgresql-16-pgtt` | `postgresql-15-pgtt` | `postgresql-14-pgtt` | `postgresql-13-pgtt` | `postgresql-12-pgtt` |



Install `pgtt` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgtt"]}'
```


Install `pgtt` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install pgtt_17*;
yum install pgtt_16*;
yum install pgtt_15*;
yum install pgtt_14*;
yum install pgtt_13*;
yum install pgtt_12*;
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




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgtt_17*` | `pgtt_16*` | `pgtt_15*` | `pgtt_14*` | `pgtt_13*` | `pgtt_12*` |
| `el9` | `pgtt_17*` | `pgtt_16*` | `pgtt_15*` | `pgtt_14*` | `pgtt_13*` | `pgtt_12*` |
| `d12` | `postgresql-17-pgtt` | `postgresql-16-pgtt` | `postgresql-15-pgtt` | `postgresql-14-pgtt` | `postgresql-13-pgtt` | `postgresql-12-pgtt` |
| `u22` | `postgresql-17-pgtt` | `postgresql-16-pgtt` | `postgresql-15-pgtt` | `postgresql-14-pgtt` | `postgresql-13-pgtt` | `postgresql-12-pgtt` |
| `u24` | `postgresql-17-pgtt` | `postgresql-16-pgtt` | `postgresql-15-pgtt` | `postgresql-14-pgtt` | `postgresql-13-pgtt` | `postgresql-12-pgtt` |






# pg_dbms_metadata


> [pg_dbms_metadata](https://github.com/HexaCluster/pg_dbms_metadata): Extension to add Oracle DBMS_METADATA compatibility to PostgreSQL
>
> https://github.com/HexaCluster/pg_dbms_metadata





[SIM](/sim) extensions: [`orafce`](/orafce), [`pgtt`](/pgtt), [`session_variable`](/session_variable), [`pg_statement_rollback`](/pg_statement_rollback), [`pg_dbms_metadata`](/pg_dbms_metadata), [`pg_dbms_lock`](/pg_dbms_lock), [`pg_dbms_job`](/pg_dbms_job), [`babelfishpg_common`](/babelfishpg_common), [`babelfishpg_tsql`](/babelfishpg_tsql), [`babelfishpg_tds`](/babelfishpg_tds), [`babelfishpg_money`](/babelfishpg_money), [`pgmemcache`](/pgmemcache)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_dbms_metadata](https://github.com/HexaCluster/pg_dbms_metadata) | 1.0.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** |  |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_dbms_metadata](/pg_dbms_metadata) | `oracle` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `u22` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `u24` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |





```sql
CREATE EXTENSION pg_dbms_metadata;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_dbms_metadata_17*` | `pg_dbms_metadata_16*` | `pg_dbms_metadata_15*` | `pg_dbms_metadata_14*` | `pg_dbms_metadata_13*` | `pg_dbms_metadata_12*` |
| `el9` | `pg_dbms_metadata_17*` | `pg_dbms_metadata_16*` | `pg_dbms_metadata_15*` | `pg_dbms_metadata_14*` | `pg_dbms_metadata_13*` | `pg_dbms_metadata_12*` |
| `d12` | `` | `` | `` | `` | `` | `` |
| `u22` | `` | `` | `` | `` | `` | `` |
| `u24` | `` | `` | `` | `` | `` | `` |



Install `pg_dbms_metadata` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_dbms_metadata"]}'
```


Install `pg_dbms_metadata` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install pg_dbms_metadata_17*;
yum install pg_dbms_metadata_16*;
yum install pg_dbms_metadata_15*;
yum install pg_dbms_metadata_14*;
yum install pg_dbms_metadata_13*;
yum install pg_dbms_metadata_12*;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_dbms_metadata_17*` | `pg_dbms_metadata_16*` | `pg_dbms_metadata_15*` | `pg_dbms_metadata_14*` | `pg_dbms_metadata_13*` | `pg_dbms_metadata_12*` |
| `el9` | `pg_dbms_metadata_17*` | `pg_dbms_metadata_16*` | `pg_dbms_metadata_15*` | `pg_dbms_metadata_14*` | `pg_dbms_metadata_13*` | `pg_dbms_metadata_12*` |
| `d12` | `` | `` | `` | `` | `` | `` |
| `u22` | `` | `` | `` | `` | `` | `` |
| `u24` | `` | `` | `` | `` | `` | `` |






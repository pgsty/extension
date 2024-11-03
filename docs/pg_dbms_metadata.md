# pg_dbms_metadata


> [pg_dbms_metadata](https://github.com/HexaCluster/pg_dbms_metadata): Extension to add Oracle DBMS_METADATA compatibility to PostgreSQL
>
> https://github.com/HexaCluster/pg_dbms_metadata





[SIM](/sim) extensions: [`orafce`](/orafce), [`pgtt`](/pgtt), [`session_variable`](/session_variable), [`pg_statement_rollback`](/pg_statement_rollback), [`pg_dbms_metadata`](/pg_dbms_metadata), [`pg_dbms_lock`](/pg_dbms_lock), [`pg_dbms_job`](/pg_dbms_job), [`babelfishpg_common`](/babelfishpg_common), [`babelfishpg_tsql`](/babelfishpg_tsql), [`babelfishpg_tds`](/babelfishpg_tds), [`babelfishpg_money`](/babelfishpg_money), [`pgmemcache`](/pgmemcache)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [pg_dbms_metadata](https://github.com/HexaCluster/pg_dbms_metadata) | 1.0.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |



| Package | Tags | Schemas | Requires | Required by |
|---------|------|---------|----------|-------------|
| [pg_dbms_metadata](/pg_dbms_metadata) | `oracle` |  |  |  |





```sql
CREATE EXTENSION pg_dbms_metadata;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pg_dbms_metadata_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pg_dbms_metadata` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_dbms_metadata"]}'
```


Install `pg_dbms_metadata` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pg_dbms_metadata_17*;
dnf install pg_dbms_metadata_16*;
dnf install pg_dbms_metadata_15*;
dnf install pg_dbms_metadata_14*;
dnf install pg_dbms_metadata_13*;
dnf install pg_dbms_metadata_12*;
```








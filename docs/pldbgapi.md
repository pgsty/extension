# pldebugger


> [pldebugger](https://github.com/EnterpriseDB/pldebugger): server-side support for debugging PL/pgSQL functions
>
> https://github.com/EnterpriseDB/pldebugger





[LANG](/lang) extensions: [`pg_tle`](/pg_tle), [`plv8`](/plv8), [`pllua`](/pllua), [`hstore_pllua`](/hstore_pllua), [`plluau`](/plluau), [`hstore_plluau`](/hstore_plluau), [`plprql`](/plprql), [`pldbgapi`](/pldbgapi), [`plpgsql_check`](/plpgsql_check), [`plprofiler`](/plprofiler), [`plsh`](/plsh), [`pljava`](/pljava), [`plr`](/plr), [`pgtap`](/pgtap), [`faker`](/faker), [`dbt2`](/dbt2), [`pltcl`](/pltcl), [`pltclu`](/pltclu), [`plperl`](/plperl), [`bool_plperl`](/bool_plperl), [`hstore_plperl`](/hstore_plperl), [`jsonb_plperl`](/jsonb_plperl), [`plperlu`](/plperlu), [`bool_plperlu`](/bool_plperlu), [`jsonb_plperlu`](/jsonb_plperlu), [`hstore_plperlu`](/hstore_plperlu), [`plpgsql`](/plpgsql), [`plpython3u`](/plpython3u), [`jsonb_plpython3u`](/jsonb_plpython3u), [`ltree_plpython3u`](/ltree_plpython3u), [`hstore_plpython3u`](/hstore_plpython3u)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [pldbgapi](https://github.com/EnterpriseDB/pldebugger) | 1.1 | **<span class="tccyan">Artistic</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Package | Tags | Schemas | Requires | Required by |
|---------|------|---------|----------|-------------|
| [pldebugger](/pldbgapi) |  |  |  |  |





```sql
CREATE EXTENSION pldbgapi;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.1 | **<span class="tccyan">Artistic</span>** | **<span class="tccyan">PGDG</span>** | `pldebugger_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 1.1 | **<span class="tccyan">Artistic</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pldebugger` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pldebugger` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pldebugger"]}'
```


Install `pldebugger` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pldebugger_17*;
dnf install pldebugger_16*;
dnf install pldebugger_15*;
dnf install pldebugger_14*;
dnf install pldebugger_13*;
dnf install pldebugger_12*;
```


Install `pldebugger` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pldebugger;
apt install postgresql-16-pldebugger;
apt install postgresql-15-pldebugger;
apt install postgresql-14-pldebugger;
apt install postgresql-13-pldebugger;
apt install postgresql-12-pldebugger;
```








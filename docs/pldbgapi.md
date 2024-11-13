# pldebugger


> [pldebugger](https://github.com/EnterpriseDB/pldebugger): server-side support for debugging PL/pgSQL functions
>
> https://github.com/EnterpriseDB/pldebugger





[LANG](/lang) extensions: [`pg_tle`](/pg_tle), [`plv8`](/plv8), [`pllua`](/pllua), [`hstore_pllua`](/hstore_pllua), [`plluau`](/plluau), [`hstore_plluau`](/hstore_plluau), [`plprql`](/plprql), [`pldbgapi`](/pldbgapi), [`plpgsql_check`](/plpgsql_check), [`plprofiler`](/plprofiler), [`plsh`](/plsh), [`pljava`](/pljava), [`plr`](/plr), [`pgtap`](/pgtap), [`faker`](/faker), [`dbt2`](/dbt2), [`pltcl`](/pltcl), [`pltclu`](/pltclu), [`plperl`](/plperl), [`bool_plperl`](/bool_plperl), [`hstore_plperl`](/hstore_plperl), [`jsonb_plperl`](/jsonb_plperl), [`plperlu`](/plperlu), [`bool_plperlu`](/bool_plperlu), [`jsonb_plperlu`](/jsonb_plperlu), [`hstore_plperlu`](/hstore_plperlu), [`plpgsql`](/plpgsql), [`plpython3u`](/plpython3u), [`jsonb_plpython3u`](/jsonb_plpython3u), [`ltree_plpython3u`](/ltree_plpython3u), [`hstore_plpython3u`](/hstore_plpython3u)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pldbgapi](https://github.com/EnterpriseDB/pldebugger) | 1.1 | **<span class="tccyan">Artistic</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pldebugger](/pldbgapi) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pldbgapi;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pldebugger_17*` | `pldebugger_16*` | `pldebugger_15*` | `pldebugger_14*` | `pldebugger_13*` | `pldebugger_12*` |
| `el9` | `pldebugger_17*` | `pldebugger_16*` | `pldebugger_15*` | `pldebugger_14*` | `pldebugger_13*` | `pldebugger_12*` |
| `d12` | `postgresql-17-pldebugger` | `postgresql-16-pldebugger` | `postgresql-15-pldebugger` | `postgresql-14-pldebugger` | `postgresql-13-pldebugger` | `postgresql-12-pldebugger` |
| `u22` | `postgresql-17-pldebugger` | `postgresql-16-pldebugger` | `postgresql-15-pldebugger` | `postgresql-14-pldebugger` | `postgresql-13-pldebugger` | `postgresql-12-pldebugger` |
| `u24` | `postgresql-17-pldebugger` | `postgresql-16-pldebugger` | `postgresql-15-pldebugger` | `postgresql-14-pldebugger` | `postgresql-13-pldebugger` | `postgresql-12-pldebugger` |



Install `pldebugger` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pldebugger"]}'
```


Install `pldebugger` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install pldebugger_17*;
yum install pldebugger_16*;
yum install pldebugger_15*;
yum install pldebugger_14*;
yum install pldebugger_13*;
yum install pldebugger_12*;
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




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pldebugger_17*` | `pldebugger_16*` | `pldebugger_15*` | `pldebugger_14*` | `pldebugger_13*` | `pldebugger_12*` |
| `el9` | `pldebugger_17*` | `pldebugger_16*` | `pldebugger_15*` | `pldebugger_14*` | `pldebugger_13*` | `pldebugger_12*` |
| `d12` | `postgresql-17-pldebugger` | `postgresql-16-pldebugger` | `postgresql-15-pldebugger` | `postgresql-14-pldebugger` | `postgresql-13-pldebugger` | `postgresql-12-pldebugger` |
| `u22` | `postgresql-17-pldebugger` | `postgresql-16-pldebugger` | `postgresql-15-pldebugger` | `postgresql-14-pldebugger` | `postgresql-13-pldebugger` | `postgresql-12-pldebugger` |
| `u24` | `postgresql-17-pldebugger` | `postgresql-16-pldebugger` | `postgresql-15-pldebugger` | `postgresql-14-pldebugger` | `postgresql-13-pldebugger` | `postgresql-12-pldebugger` |






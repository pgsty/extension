# dbt2


> [dbt2](https://github.com/nuodb/dbt2/tree/master): OSDL-DBT-2 test kit
>
> https://github.com/nuodb/dbt2/tree/master





[LANG](/lang) extensions: [`pg_tle`](/pg_tle), [`plv8`](/plv8), [`pllua`](/pllua), [`hstore_pllua`](/hstore_pllua), [`plluau`](/plluau), [`hstore_plluau`](/hstore_plluau), [`plprql`](/plprql), [`pldbgapi`](/pldbgapi), [`plpgsql_check`](/plpgsql_check), [`plprofiler`](/plprofiler), [`plsh`](/plsh), [`pljava`](/pljava), [`plr`](/plr), [`pgtap`](/pgtap), [`faker`](/faker), [`dbt2`](/dbt2), [`pltcl`](/pltcl), [`pltclu`](/pltclu), [`plperl`](/plperl), [`bool_plperl`](/bool_plperl), [`hstore_plperl`](/hstore_plperl), [`jsonb_plperl`](/jsonb_plperl), [`plperlu`](/plperlu), [`bool_plperlu`](/bool_plperlu), [`jsonb_plperlu`](/jsonb_plperlu), [`hstore_plperlu`](/hstore_plperlu), [`plpgsql`](/plpgsql), [`plpython3u`](/plpython3u), [`jsonb_plpython3u`](/jsonb_plpython3u), [`ltree_plpython3u`](/ltree_plpython3u), [`hstore_plpython3u`](/hstore_plpython3u)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [dbt2](https://github.com/nuodb/dbt2/tree/master) | 0.45.0 | **<span class="tccyan">Artistic</span>** | **<span class="tccyan">PGDG</span>** |  |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [dbt2](/dbt2) | `test` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `u22` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `u24` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |





```sql
CREATE EXTENSION dbt2;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `dbt2-pg17-extensions*` | `dbt2-pg16-extensions*` | `dbt2-pg15-extensions*` | `dbt2-pg14-extensions*` | `dbt2-pg13-extensions*` | `dbt2-pg12-extensions*` |
| `el9` | `dbt2-pg17-extensions*` | `dbt2-pg16-extensions*` | `dbt2-pg15-extensions*` | `dbt2-pg14-extensions*` | `dbt2-pg13-extensions*` | `dbt2-pg12-extensions*` |
| `d12` | `` | `` | `` | `` | `` | `` |
| `u22` | `` | `` | `` | `` | `` | `` |
| `u24` | `` | `` | `` | `` | `` | `` |



Install `dbt2` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["dbt2"]}'
```


Install `dbt2` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install dbt2-pg17-extensions*;
yum install dbt2-pg16-extensions*;
yum install dbt2-pg15-extensions*;
yum install dbt2-pg14-extensions*;
yum install dbt2-pg13-extensions*;
yum install dbt2-pg12-extensions*;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `dbt2-pg17-extensions*` | `dbt2-pg16-extensions*` | `dbt2-pg15-extensions*` | `dbt2-pg14-extensions*` | `dbt2-pg13-extensions*` | `dbt2-pg12-extensions*` |
| `el9` | `dbt2-pg17-extensions*` | `dbt2-pg16-extensions*` | `dbt2-pg15-extensions*` | `dbt2-pg14-extensions*` | `dbt2-pg13-extensions*` | `dbt2-pg12-extensions*` |
| `d12` | `` | `` | `` | `` | `` | `` |
| `u22` | `` | `` | `` | `` | `` | `` |
| `u24` | `` | `` | `` | `` | `` | `` |






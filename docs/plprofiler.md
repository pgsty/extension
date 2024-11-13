# plprofiler


> [plprofiler](https://github.com/bigsql/plprofiler): server-side support for profiling PL/pgSQL functions
>
> https://github.com/bigsql/plprofiler





[LANG](/lang) extensions: [`pg_tle`](/pg_tle), [`plv8`](/plv8), [`pllua`](/pllua), [`hstore_pllua`](/hstore_pllua), [`plluau`](/plluau), [`hstore_plluau`](/hstore_plluau), [`plprql`](/plprql), [`pldbgapi`](/pldbgapi), [`plpgsql_check`](/plpgsql_check), [`plprofiler`](/plprofiler), [`plsh`](/plsh), [`pljava`](/pljava), [`plr`](/plr), [`pgtap`](/pgtap), [`faker`](/faker), [`dbt2`](/dbt2), [`pltcl`](/pltcl), [`pltclu`](/pltclu), [`plperl`](/plperl), [`bool_plperl`](/bool_plperl), [`hstore_plperl`](/hstore_plperl), [`jsonb_plperl`](/jsonb_plperl), [`plperlu`](/plperlu), [`bool_plperlu`](/bool_plperlu), [`jsonb_plperlu`](/jsonb_plperlu), [`hstore_plperlu`](/hstore_plperlu), [`plpgsql`](/plpgsql), [`plpython3u`](/plpython3u), [`jsonb_plpython3u`](/jsonb_plpython3u), [`ltree_plpython3u`](/ltree_plpython3u), [`hstore_plpython3u`](/hstore_plpython3u)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [plprofiler](https://github.com/bigsql/plprofiler) | 4.2 | **<span class="tccyan">Artistic</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [plprofiler](/plprofiler) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION plprofiler;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `plprofiler_17*` | `plprofiler_16*` | `plprofiler_15*` | `plprofiler_14*` | `plprofiler_13*` | `plprofiler_12*` |
| `el9` | `plprofiler_17*` | `plprofiler_16*` | `plprofiler_15*` | `plprofiler_14*` | `plprofiler_13*` | `plprofiler_12*` |
| `d12` | `postgresql-17-plprofiler` | `postgresql-16-plprofiler` | `postgresql-15-plprofiler` | `postgresql-14-plprofiler` | `postgresql-13-plprofiler` | `postgresql-12-plprofiler` |
| `u22` | `postgresql-17-plprofiler` | `postgresql-16-plprofiler` | `postgresql-15-plprofiler` | `postgresql-14-plprofiler` | `postgresql-13-plprofiler` | `postgresql-12-plprofiler` |
| `u24` | `postgresql-17-plprofiler` | `postgresql-16-plprofiler` | `postgresql-15-plprofiler` | `postgresql-14-plprofiler` | `postgresql-13-plprofiler` | `postgresql-12-plprofiler` |



Install `plprofiler` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["plprofiler"]}'
```


Install `plprofiler` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install plprofiler_17*;
yum install plprofiler_16*;
yum install plprofiler_15*;
yum install plprofiler_14*;
yum install plprofiler_13*;
yum install plprofiler_12*;
```


Install `plprofiler` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-plprofiler;
apt install postgresql-16-plprofiler;
apt install postgresql-15-plprofiler;
apt install postgresql-14-plprofiler;
apt install postgresql-13-plprofiler;
apt install postgresql-12-plprofiler;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `plprofiler_17*` | `plprofiler_16*` | `plprofiler_15*` | `plprofiler_14*` | `plprofiler_13*` | `plprofiler_12*` |
| `el9` | `plprofiler_17*` | `plprofiler_16*` | `plprofiler_15*` | `plprofiler_14*` | `plprofiler_13*` | `plprofiler_12*` |
| `d12` | `postgresql-17-plprofiler` | `postgresql-16-plprofiler` | `postgresql-15-plprofiler` | `postgresql-14-plprofiler` | `postgresql-13-plprofiler` | `postgresql-12-plprofiler` |
| `u22` | `postgresql-17-plprofiler` | `postgresql-16-plprofiler` | `postgresql-15-plprofiler` | `postgresql-14-plprofiler` | `postgresql-13-plprofiler` | `postgresql-12-plprofiler` |
| `u24` | `postgresql-17-plprofiler` | `postgresql-16-plprofiler` | `postgresql-15-plprofiler` | `postgresql-14-plprofiler` | `postgresql-13-plprofiler` | `postgresql-12-plprofiler` |






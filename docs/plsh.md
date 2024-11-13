# plsh


> [plsh](https://github.com/petere/plsh): PL/sh procedural language
>
> https://github.com/petere/plsh





[LANG](/lang) extensions: [`pg_tle`](/pg_tle), [`plv8`](/plv8), [`pllua`](/pllua), [`hstore_pllua`](/hstore_pllua), [`plluau`](/plluau), [`hstore_plluau`](/hstore_plluau), [`plprql`](/plprql), [`pldbgapi`](/pldbgapi), [`plpgsql_check`](/plpgsql_check), [`plprofiler`](/plprofiler), [`plsh`](/plsh), [`pljava`](/pljava), [`plr`](/plr), [`pgtap`](/pgtap), [`faker`](/faker), [`dbt2`](/dbt2), [`pltcl`](/pltcl), [`pltclu`](/pltclu), [`plperl`](/plperl), [`bool_plperl`](/bool_plperl), [`hstore_plperl`](/hstore_plperl), [`jsonb_plperl`](/jsonb_plperl), [`plperlu`](/plperlu), [`bool_plperlu`](/bool_plperlu), [`jsonb_plperlu`](/jsonb_plperlu), [`hstore_plperlu`](/hstore_plperlu), [`plpgsql`](/plpgsql), [`plpython3u`](/plpython3u), [`jsonb_plpython3u`](/jsonb_plpython3u), [`ltree_plpython3u`](/ltree_plpython3u), [`hstore_plpython3u`](/hstore_plpython3u)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [plsh](https://github.com/petere/plsh) | 2 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [plsh](/plsh) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION plsh;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `plsh_17*` | `plsh_16*` | `plsh_15*` | `plsh_14*` | `plsh_13*` | `plsh_12*` |
| `el9` | `plsh_17*` | `plsh_16*` | `plsh_15*` | `plsh_14*` | `plsh_13*` | `plsh_12*` |
| `d12` | `postgresql-17-plsh` | `postgresql-16-plsh` | `postgresql-15-plsh` | `postgresql-14-plsh` | `postgresql-13-plsh` | `postgresql-12-plsh` |
| `u22` | `postgresql-17-plsh` | `postgresql-16-plsh` | `postgresql-15-plsh` | `postgresql-14-plsh` | `postgresql-13-plsh` | `postgresql-12-plsh` |
| `u24` | `postgresql-17-plsh` | `postgresql-16-plsh` | `postgresql-15-plsh` | `postgresql-14-plsh` | `postgresql-13-plsh` | `postgresql-12-plsh` |



Install `plsh` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["plsh"]}'
```


Install `plsh` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install plsh_17*;
yum install plsh_16*;
yum install plsh_15*;
yum install plsh_14*;
yum install plsh_13*;
yum install plsh_12*;
```


Install `plsh` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-plsh;
apt install postgresql-16-plsh;
apt install postgresql-15-plsh;
apt install postgresql-14-plsh;
apt install postgresql-13-plsh;
apt install postgresql-12-plsh;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `plsh_17*` | `plsh_16*` | `plsh_15*` | `plsh_14*` | `plsh_13*` | `plsh_12*` |
| `el9` | `plsh_17*` | `plsh_16*` | `plsh_15*` | `plsh_14*` | `plsh_13*` | `plsh_12*` |
| `d12` | `postgresql-17-plsh` | `postgresql-16-plsh` | `postgresql-15-plsh` | `postgresql-14-plsh` | `postgresql-13-plsh` | `postgresql-12-plsh` |
| `u22` | `postgresql-17-plsh` | `postgresql-16-plsh` | `postgresql-15-plsh` | `postgresql-14-plsh` | `postgresql-13-plsh` | `postgresql-12-plsh` |
| `u24` | `postgresql-17-plsh` | `postgresql-16-plsh` | `postgresql-15-plsh` | `postgresql-14-plsh` | `postgresql-13-plsh` | `postgresql-12-plsh` |






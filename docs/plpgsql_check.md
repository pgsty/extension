# plpgsql_check


> [plpgsql_check](https://github.com/okbob/plpgsql_check): extended check for plpgsql functions
>
> https://github.com/okbob/plpgsql_check





[LANG](/lang) extensions: [`pg_tle`](/pg_tle), [`plv8`](/plv8), [`pllua`](/pllua), [`hstore_pllua`](/hstore_pllua), [`plluau`](/plluau), [`hstore_plluau`](/hstore_plluau), [`plprql`](/plprql), [`pldbgapi`](/pldbgapi), [`plpgsql_check`](/plpgsql_check), [`plprofiler`](/plprofiler), [`plsh`](/plsh), [`pljava`](/pljava), [`plr`](/plr), [`pgtap`](/pgtap), [`faker`](/faker), [`dbt2`](/dbt2), [`pltcl`](/pltcl), [`pltclu`](/pltclu), [`plperl`](/plperl), [`bool_plperl`](/bool_plperl), [`hstore_plperl`](/hstore_plperl), [`jsonb_plperl`](/jsonb_plperl), [`plperlu`](/plperlu), [`bool_plperlu`](/bool_plperlu), [`jsonb_plperlu`](/jsonb_plperlu), [`hstore_plperlu`](/hstore_plperlu), [`plpgsql`](/plpgsql), [`plpython3u`](/plpython3u), [`jsonb_plpython3u`](/jsonb_plpython3u), [`ltree_plpython3u`](/ltree_plpython3u), [`hstore_plpython3u`](/hstore_plpython3u)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [plpgsql_check](https://github.com/okbob/plpgsql_check) | 2.7 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [plpgsql_check](/plpgsql_check) |  |  | [`plpgsql`](plpgsql) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'plpgsql_check'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION plpgsql_check CASCADE;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 2.7 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `plpgsql_check_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 2.7 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-plpgsql-check` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `plpgsql_check` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add plpgsql_check
```


Install `plpgsql_check` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["plpgsql_check"]}'
```


Install `plpgsql_check` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install plpgsql_check_17*;
dnf install plpgsql_check_16*;
dnf install plpgsql_check_15*;
dnf install plpgsql_check_14*;
dnf install plpgsql_check_13*;
```


Install `plpgsql_check` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-plpgsql-check;
apt install postgresql-16-plpgsql-check;
apt install postgresql-15-plpgsql-check;
apt install postgresql-14-plpgsql-check;
apt install postgresql-13-plpgsql-check;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `plpgsql_check_17*` | `plpgsql_check_16*` | `plpgsql_check_15*` | `plpgsql_check_14*` | `plpgsql_check_13*` |
| `el9` | `plpgsql_check_17*` | `plpgsql_check_16*` | `plpgsql_check_15*` | `plpgsql_check_14*` | `plpgsql_check_13*` |
| `d12` | `postgresql-17-plpgsql-check` | `postgresql-16-plpgsql-check` | `postgresql-15-plpgsql-check` | `postgresql-14-plpgsql-check` | `postgresql-13-plpgsql-check` |
| `u22` | `postgresql-17-plpgsql-check` | `postgresql-16-plpgsql-check` | `postgresql-15-plpgsql-check` | `postgresql-14-plpgsql-check` | `postgresql-13-plpgsql-check` |
| `u24` | `postgresql-17-plpgsql-check` | `postgresql-16-plpgsql-check` | `postgresql-15-plpgsql-check` | `postgresql-14-plpgsql-check` | `postgresql-13-plpgsql-check` |






# pllua


> [pllua](https://github.com/pllua/pllua): Lua as an untrusted procedural language
>
> https://github.com/pllua/pllua





[LANG](/lang) extensions: [`pg_tle`](/pg_tle), [`plv8`](/plv8), [`pllua`](/pllua), [`hstore_pllua`](/hstore_pllua), [`plluau`](/plluau), [`hstore_plluau`](/hstore_plluau), [`plprql`](/plprql), [`pldbgapi`](/pldbgapi), [`plpgsql_check`](/plpgsql_check), [`plprofiler`](/plprofiler), [`plsh`](/plsh), [`pljava`](/pljava), [`plr`](/plr), [`pgtap`](/pgtap), [`faker`](/faker), [`dbt2`](/dbt2), [`pltcl`](/pltcl), [`pltclu`](/pltclu), [`plperl`](/plperl), [`bool_plperl`](/bool_plperl), [`hstore_plperl`](/hstore_plperl), [`jsonb_plperl`](/jsonb_plperl), [`plperlu`](/plperlu), [`bool_plperlu`](/bool_plperlu), [`jsonb_plperlu`](/jsonb_plperlu), [`hstore_plperlu`](/hstore_plperlu), [`plpgsql`](/plpgsql), [`plpython3u`](/plpython3u), [`jsonb_plpython3u`](/jsonb_plpython3u), [`ltree_plpython3u`](/ltree_plpython3u), [`hstore_plpython3u`](/hstore_plpython3u)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [plluau](https://github.com/pllua/pllua) | 2.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pllua](/plluau) |  | `pg_catalog` |  | [`hstore_plluau`](/hstore_plluau) |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION plluau;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pllua_17*` | `pllua_16*` | `pllua_15*` | `pllua_14*` | `pllua_13*` | `pllua_12*` |
| `el9` | `pllua_17*` | `pllua_16*` | `pllua_15*` | `pllua_14*` | `pllua_13*` | `pllua_12*` |
| `d12` | `postgresql-17-pllua` | `postgresql-16-pllua` | `postgresql-15-pllua` | `postgresql-14-pllua` | `postgresql-13-pllua` | `postgresql-12-pllua` |
| `u22` | `postgresql-17-pllua` | `postgresql-16-pllua` | `postgresql-15-pllua` | `postgresql-14-pllua` | `postgresql-13-pllua` | `postgresql-12-pllua` |
| `u24` | `postgresql-17-pllua` | `postgresql-16-pllua` | `postgresql-15-pllua` | `postgresql-14-pllua` | `postgresql-13-pllua` | `postgresql-12-pllua` |



Install `pllua` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pllua"]}'
```


Install `pllua` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install pllua_17*;
yum install pllua_16*;
yum install pllua_15*;
yum install pllua_14*;
yum install pllua_13*;
yum install pllua_12*;
```


Install `pllua` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pllua;
apt install postgresql-16-pllua;
apt install postgresql-15-pllua;
apt install postgresql-14-pllua;
apt install postgresql-13-pllua;
apt install postgresql-12-pllua;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pllua_17*` | `pllua_16*` | `pllua_15*` | `pllua_14*` | `pllua_13*` | `pllua_12*` |
| `el9` | `pllua_17*` | `pllua_16*` | `pllua_15*` | `pllua_14*` | `pllua_13*` | `pllua_12*` |
| `d12` | `postgresql-17-pllua` | `postgresql-16-pllua` | `postgresql-15-pllua` | `postgresql-14-pllua` | `postgresql-13-pllua` | `postgresql-12-pllua` |
| `u22` | `postgresql-17-pllua` | `postgresql-16-pllua` | `postgresql-15-pllua` | `postgresql-14-pllua` | `postgresql-13-pllua` | `postgresql-12-pllua` |
| `u24` | `postgresql-17-pllua` | `postgresql-16-pllua` | `postgresql-15-pllua` | `postgresql-14-pllua` | `postgresql-13-pllua` | `postgresql-12-pllua` |






# pljava


> [pljava](https://github.com/tada/pljava): PL/Java procedural language (https://tada.github.io/pljava/)
>
> https://github.com/tada/pljava





[LANG](/lang) extensions: [`pg_tle`](/pg_tle), [`plv8`](/plv8), [`pllua`](/pllua), [`hstore_pllua`](/hstore_pllua), [`plluau`](/plluau), [`hstore_plluau`](/hstore_plluau), [`plprql`](/plprql), [`pldbgapi`](/pldbgapi), [`plpgsql_check`](/plpgsql_check), [`plprofiler`](/plprofiler), [`plsh`](/plsh), [`pljava`](/pljava), [`plr`](/plr), [`pgtap`](/pgtap), [`faker`](/faker), [`dbt2`](/dbt2), [`pltcl`](/pltcl), [`pltclu`](/pltclu), [`plperl`](/plperl), [`bool_plperl`](/bool_plperl), [`hstore_plperl`](/hstore_plperl), [`jsonb_plperl`](/jsonb_plperl), [`plperlu`](/plperlu), [`bool_plperlu`](/bool_plperlu), [`jsonb_plperlu`](/jsonb_plperlu), [`hstore_plperlu`](/hstore_plperlu), [`plpgsql`](/plpgsql), [`plpython3u`](/plpython3u), [`jsonb_plpython3u`](/jsonb_plpython3u), [`ltree_plpython3u`](/ltree_plpython3u), [`hstore_plpython3u`](/hstore_plpython3u)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pljava](https://github.com/tada/pljava) | 1.6.6 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pljava](/pljava) | `big-deps` | `sqlj` |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pljava;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pljava_17*` | `pljava_16*` | `pljava_15*` | `pljava_14*` | `pljava_13*` | `pljava_12*` |
| `el9` | `pljava_17*` | `pljava_16*` | `pljava_15*` | `pljava_14*` | `pljava_13*` | `pljava_12*` |
| `d12` | `postgresql-17-pljava` | `postgresql-16-pljava` | `postgresql-15-pljava` | `postgresql-14-pljava` | `postgresql-13-pljava` | `postgresql-12-pljava` |
| `u22` | `postgresql-17-pljava` | `postgresql-16-pljava` | `postgresql-15-pljava` | `postgresql-14-pljava` | `postgresql-13-pljava` | `postgresql-12-pljava` |
| `u24` | `postgresql-17-pljava` | `postgresql-16-pljava` | `postgresql-15-pljava` | `postgresql-14-pljava` | `postgresql-13-pljava` | `postgresql-12-pljava` |



Install `pljava` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pljava"]}'
```


Install `pljava` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install pljava_17*;
yum install pljava_16*;
yum install pljava_15*;
yum install pljava_14*;
yum install pljava_13*;
yum install pljava_12*;
```


Install `pljava` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pljava;
apt install postgresql-16-pljava;
apt install postgresql-15-pljava;
apt install postgresql-14-pljava;
apt install postgresql-13-pljava;
apt install postgresql-12-pljava;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pljava_17*` | `pljava_16*` | `pljava_15*` | `pljava_14*` | `pljava_13*` | `pljava_12*` |
| `el9` | `pljava_17*` | `pljava_16*` | `pljava_15*` | `pljava_14*` | `pljava_13*` | `pljava_12*` |
| `d12` | `postgresql-17-pljava` | `postgresql-16-pljava` | `postgresql-15-pljava` | `postgresql-14-pljava` | `postgresql-13-pljava` | `postgresql-12-pljava` |
| `u22` | `postgresql-17-pljava` | `postgresql-16-pljava` | `postgresql-15-pljava` | `postgresql-14-pljava` | `postgresql-13-pljava` | `postgresql-12-pljava` |
| `u24` | `postgresql-17-pljava` | `postgresql-16-pljava` | `postgresql-15-pljava` | `postgresql-14-pljava` | `postgresql-13-pljava` | `postgresql-12-pljava` |






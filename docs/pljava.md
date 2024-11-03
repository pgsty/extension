# pljava


> [pljava](https://github.com/tada/pljava): PL/Java procedural language (https://tada.github.io/pljava/)
>
> https://github.com/tada/pljava





[LANG](/lang) extensions: [`pg_tle`](/pg_tle), [`plv8`](/plv8), [`pllua`](/pllua), [`hstore_pllua`](/hstore_pllua), [`plluau`](/plluau), [`hstore_plluau`](/hstore_plluau), [`plprql`](/plprql), [`pldbgapi`](/pldbgapi), [`plpgsql_check`](/plpgsql_check), [`plprofiler`](/plprofiler), [`plsh`](/plsh), [`pljava`](/pljava), [`plr`](/plr), [`pgtap`](/pgtap), [`faker`](/faker), [`dbt2`](/dbt2), [`pltcl`](/pltcl), [`pltclu`](/pltclu), [`plperl`](/plperl), [`bool_plperl`](/bool_plperl), [`hstore_plperl`](/hstore_plperl), [`jsonb_plperl`](/jsonb_plperl), [`plperlu`](/plperlu), [`bool_plperlu`](/bool_plperlu), [`jsonb_plperlu`](/jsonb_plperlu), [`hstore_plperlu`](/hstore_plperlu), [`plpgsql`](/plpgsql), [`plpython3u`](/plpython3u), [`jsonb_plpython3u`](/jsonb_plpython3u), [`ltree_plpython3u`](/ltree_plpython3u), [`hstore_plpython3u`](/hstore_plpython3u)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [pljava](https://github.com/tada/pljava) | 1.6.6 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Package | Tags | Schemas | Requires | Required by |
|---------|------|---------|----------|-------------|
| [pljava](/pljava) | `big-deps` | `sqlj` |  |  |





```sql
CREATE EXTENSION pljava;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.6.6 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `pljava_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 1.6.7 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pljava` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pljava` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pljava"]}'
```


Install `pljava` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pljava_17*;
dnf install pljava_16*;
dnf install pljava_15*;
dnf install pljava_14*;
dnf install pljava_13*;
dnf install pljava_12*;
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








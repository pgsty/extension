# pllua


> [pllua](https://github.com/pllua/pllua): Lua as an untrusted procedural language
>
> https://github.com/pllua/pllua





[LANG](/lang) extensions: [`pg_tle`](/pg_tle), [`plv8`](/plv8), [`pllua`](/pllua), [`hstore_pllua`](/hstore_pllua), [`plluau`](/plluau), [`hstore_plluau`](/hstore_plluau), [`plprql`](/plprql), [`pldbgapi`](/pldbgapi), [`plpgsql_check`](/plpgsql_check), [`plprofiler`](/plprofiler), [`plsh`](/plsh), [`pljava`](/pljava), [`plr`](/plr), [`pgtap`](/pgtap), [`faker`](/faker), [`dbt2`](/dbt2), [`pltcl`](/pltcl), [`pltclu`](/pltclu), [`plperl`](/plperl), [`bool_plperl`](/bool_plperl), [`hstore_plperl`](/hstore_plperl), [`jsonb_plperl`](/jsonb_plperl), [`plperlu`](/plperlu), [`bool_plperlu`](/bool_plperlu), [`jsonb_plperlu`](/jsonb_plperlu), [`hstore_plperlu`](/hstore_plperlu), [`plpgsql`](/plpgsql), [`plpython3u`](/plpython3u), [`jsonb_plpython3u`](/jsonb_plpython3u), [`ltree_plpython3u`](/ltree_plpython3u), [`hstore_plpython3u`](/hstore_plpython3u)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [plluau](https://github.com/pllua/pllua) | 2.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Package | Tags | Schemas | Requires | Required by |
|---------|------|---------|----------|-------------|
| [pllua](/plluau) |  | `pg_catalog` |  | [`hstore_plluau`](/hstore_plluau) |





```sql
CREATE EXTENSION plluau;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| Distro-pllua | 2.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `pllua_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| Distro-pllua | 2.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pllua` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pllua` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pllua"]}'
```


Install `pllua` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pllua_17*;
dnf install pllua_16*;
dnf install pllua_15*;
dnf install pllua_14*;
dnf install pllua_13*;
dnf install pllua_12*;
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








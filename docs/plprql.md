# plprql


> [plprql](https://github.com/kaspermarstal/plprql): Use PRQL in PostgreSQL - Pipelined Relational Query Language
>
> https://github.com/kaspermarstal/plprql





[LANG](/lang) extensions: [`pg_tle`](/pg_tle), [`plv8`](/plv8), [`pllua`](/pllua), [`hstore_pllua`](/hstore_pllua), [`plluau`](/plluau), [`hstore_plluau`](/hstore_plluau), [`plprql`](/plprql), [`pldbgapi`](/pldbgapi), [`plpgsql_check`](/plpgsql_check), [`plprofiler`](/plprofiler), [`plsh`](/plsh), [`pljava`](/pljava), [`plr`](/plr), [`pgtap`](/pgtap), [`faker`](/faker), [`dbt2`](/dbt2), [`pltcl`](/pltcl), [`pltclu`](/pltclu), [`plperl`](/plperl), [`bool_plperl`](/bool_plperl), [`hstore_plperl`](/hstore_plperl), [`jsonb_plperl`](/jsonb_plperl), [`plperlu`](/plperlu), [`bool_plperlu`](/bool_plperlu), [`jsonb_plperlu`](/jsonb_plperlu), [`hstore_plperlu`](/hstore_plperlu), [`plpgsql`](/plpgsql), [`plpython3u`](/plpython3u), [`jsonb_plpython3u`](/jsonb_plpython3u), [`ltree_plpython3u`](/ltree_plpython3u), [`hstore_plpython3u`](/hstore_plpython3u)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [plprql](https://github.com/kaspermarstal/plprql) | 0.1.0 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [plprql](/plprql) | `pgrx` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION plprql;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `plprql_17` | `plprql_16` | `plprql_15` | `plprql_14` | `plprql_13` | `plprql_12` |
| `el9` | `plprql_17` | `plprql_16` | `plprql_15` | `plprql_14` | `plprql_13` | `plprql_12` |
| `d12` | `postgresql-17-plprql` | `postgresql-16-plprql` | `postgresql-15-plprql` | `postgresql-14-plprql` | `postgresql-13-plprql` | `postgresql-12-plprql` |
| `u22` | `postgresql-17-plprql` | `postgresql-16-plprql` | `postgresql-15-plprql` | `postgresql-14-plprql` | `postgresql-13-plprql` | `postgresql-12-plprql` |
| `u24` | `postgresql-17-plprql` | `postgresql-16-plprql` | `postgresql-15-plprql` | `postgresql-14-plprql` | `postgresql-13-plprql` | `postgresql-12-plprql` |



Install `plprql` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["plprql"]}'
```


Install `plprql` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install plprql_17;
yum install plprql_16;
yum install plprql_15;
yum install plprql_14;
yum install plprql_13;
yum install plprql_12;
```


Install `plprql` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-plprql;
apt install postgresql-16-plprql;
apt install postgresql-15-plprql;
apt install postgresql-14-plprql;
apt install postgresql-13-plprql;
apt install postgresql-12-plprql;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `plprql_17` | `plprql_16` | `plprql_15` | `plprql_14` | `plprql_13` | `plprql_12` |
| `el9` | `plprql_17` | `plprql_16` | `plprql_15` | `plprql_14` | `plprql_13` | `plprql_12` |
| `d12` | `postgresql-17-plprql` | `postgresql-16-plprql` | `postgresql-15-plprql` | `postgresql-14-plprql` | `postgresql-13-plprql` | `postgresql-12-plprql` |
| `u22` | `postgresql-17-plprql` | `postgresql-16-plprql` | `postgresql-15-plprql` | `postgresql-14-plprql` | `postgresql-13-plprql` | `postgresql-12-plprql` |
| `u24` | `postgresql-17-plprql` | `postgresql-16-plprql` | `postgresql-15-plprql` | `postgresql-14-plprql` | `postgresql-13-plprql` | `postgresql-12-plprql` |






# pg_tle


> [pg_tle](https://github.com/aws/pg_tle): Trusted Language Extensions for PostgreSQL
>
> https://github.com/aws/pg_tle





[LANG](/lang) extensions: [`pg_tle`](/pg_tle), [`plv8`](/plv8), [`pllua`](/pllua), [`hstore_pllua`](/hstore_pllua), [`plluau`](/plluau), [`hstore_plluau`](/hstore_plluau), [`plprql`](/plprql), [`pldbgapi`](/pldbgapi), [`plpgsql_check`](/plpgsql_check), [`plprofiler`](/plprofiler), [`plsh`](/plsh), [`pljava`](/pljava), [`plr`](/plr), [`pgtap`](/pgtap), [`faker`](/faker), [`dbt2`](/dbt2), [`pltcl`](/pltcl), [`pltclu`](/pltclu), [`plperl`](/plperl), [`bool_plperl`](/bool_plperl), [`hstore_plperl`](/hstore_plperl), [`jsonb_plperl`](/jsonb_plperl), [`plperlu`](/plperlu), [`bool_plperlu`](/bool_plperlu), [`jsonb_plperlu`](/jsonb_plperlu), [`hstore_plperlu`](/hstore_plperlu), [`plpgsql`](/plpgsql), [`plpython3u`](/plpython3u), [`jsonb_plpython3u`](/jsonb_plpython3u), [`ltree_plpython3u`](/ltree_plpython3u), [`hstore_plpython3u`](/hstore_plpython3u)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_tle](https://github.com/aws/pg_tle) | 1.5.0 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_tle](/pg_tle) | `both` | `pgtle` |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'pg_tle'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION pg_tle;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.5.0 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_tle_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.5.0 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-tle` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pg_tle` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_tle
```


Install `pg_tle` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_tle"]}'
```


Install `pg_tle` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_tle_17*;
dnf install pg_tle_16*;
dnf install pg_tle_15*;
dnf install pg_tle_14*;
dnf install pg_tle_13*;
```


Install `pg_tle` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-tle;
apt install postgresql-16-pg-tle;
apt install postgresql-15-pg-tle;
apt install postgresql-14-pg-tle;
apt install postgresql-13-pg-tle;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_tle_17*` | `pg_tle_16*` | `pg_tle_15*` | `pg_tle_14*` | `pg_tle_13*` |
| `el9` | `pg_tle_17*` | `pg_tle_16*` | `pg_tle_15*` | `pg_tle_14*` | `pg_tle_13*` |
| `d12` | `postgresql-17-pg-tle` | `postgresql-16-pg-tle` | `postgresql-15-pg-tle` | `postgresql-14-pg-tle` | `postgresql-13-pg-tle` |
| `u22` | `postgresql-17-pg-tle` | `postgresql-16-pg-tle` | `postgresql-15-pg-tle` | `postgresql-14-pg-tle` | `postgresql-13-pg-tle` |
| `u24` | `postgresql-17-pg-tle` | `postgresql-16-pg-tle` | `postgresql-15-pg-tle` | `postgresql-14-pg-tle` | `postgresql-13-pg-tle` |






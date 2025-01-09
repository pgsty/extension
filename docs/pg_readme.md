# pg_readme


> [pg_readme](https://github.com/bigsmoke/pg_readme): Generate a README.md document for a database extension or schema
>
> https://github.com/bigsmoke/pg_readme





[UTIL](/util) extensions: [`zstd`](/zstd), [`gzip`](/gzip), [`http`](/http), [`pg_net`](/pg_net), [`pgjwt`](/pgjwt), [`pg_smtp_client`](/pg_smtp_client), [`pg_html5_email_address`](/pg_html5_email_address), [`url_encode`](/url_encode), [`pgsql_tweaks`](/pgsql_tweaks), [`pg_extra_time`](/pg_extra_time), [`pgpcre`](/pgpcre), [`icu_ext`](/icu_ext), [`pgqr`](/pgqr), [`pg_protobuf`](/pg_protobuf), [`envvar`](/envvar), [`floatfile`](/floatfile), [`pg_readme`](/pg_readme), [`ddl_historization`](/ddl_historization), [`data_historization`](/data_historization), [`schedoc`](/schedoc), [`hashlib`](/hashlib), [`shacrypt`](/shacrypt), [`cryptint`](/cryptint), [`pguecc`](/pguecc)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_readme](https://github.com/bigsmoke/pg_readme) | 0.7.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_readme](/pg_readme) |  |  | [`hstore`](hstore) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_readme CASCADE;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.7.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pg_readme_$v` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 0.7.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-readme` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pg_readme` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_readme
```


Install `pg_readme` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_readme"]}'
```


Install `pg_readme` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pg_readme_17;
dnf install pg_readme_16;
dnf install pg_readme_15;
dnf install pg_readme_14;
dnf install pg_readme_13;
```


Install `pg_readme` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pg-readme;
apt install postgresql-16-pg-readme;
apt install postgresql-15-pg-readme;
apt install postgresql-14-pg-readme;
apt install postgresql-13-pg-readme;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_readme_17` | `pg_readme_16` | `pg_readme_15` | `pg_readme_14` | `pg_readme_13` |
| `el9` | `pg_readme_17` | `pg_readme_16` | `pg_readme_15` | `pg_readme_14` | `pg_readme_13` |
| `d12` | `postgresql-17-pg-readme` | `postgresql-16-pg-readme` | `postgresql-15-pg-readme` | `postgresql-14-pg-readme` | `postgresql-13-pg-readme` |
| `u22` | `postgresql-17-pg-readme` | `postgresql-16-pg-readme` | `postgresql-15-pg-readme` | `postgresql-14-pg-readme` | `postgresql-13-pg-readme` |
| `u24` | `postgresql-17-pg-readme` | `postgresql-16-pg-readme` | `postgresql-15-pg-readme` | `postgresql-14-pg-readme` | `postgresql-13-pg-readme` |






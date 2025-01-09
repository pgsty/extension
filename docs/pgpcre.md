# pgpcre


> [pgpcre](https://github.com/petere/pgpcre): Perl Compatible Regular Expression functions
>
> https://github.com/petere/pgpcre





[UTIL](/util) extensions: [`zstd`](/zstd), [`gzip`](/gzip), [`http`](/http), [`pg_net`](/pg_net), [`pgjwt`](/pgjwt), [`pg_smtp_client`](/pg_smtp_client), [`pg_html5_email_address`](/pg_html5_email_address), [`url_encode`](/url_encode), [`pgsql_tweaks`](/pgsql_tweaks), [`pg_extra_time`](/pg_extra_time), [`pgpcre`](/pgpcre), [`icu_ext`](/icu_ext), [`pgqr`](/pgqr), [`pg_protobuf`](/pg_protobuf), [`envvar`](/envvar), [`floatfile`](/floatfile), [`pg_readme`](/pg_readme), [`ddl_historization`](/ddl_historization), [`data_historization`](/data_historization), [`schedoc`](/schedoc), [`hashlib`](/hashlib), [`shacrypt`](/shacrypt), [`cryptint`](/cryptint), [`pguecc`](/pguecc)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgpcre](https://github.com/petere/pgpcre) | 1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgpcre](/pgpcre) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pgpcre;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pgpcre_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pgpcre` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pgpcre` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pgpcre
```


Install `pgpcre` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgpcre"]}'
```


Install `pgpcre` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pgpcre_17;
dnf install pgpcre_16;
dnf install pgpcre_15;
dnf install pgpcre_14;
dnf install pgpcre_13;
```


Install `pgpcre` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pgpcre;
apt install postgresql-16-pgpcre;
apt install postgresql-15-pgpcre;
apt install postgresql-14-pgpcre;
apt install postgresql-13-pgpcre;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgpcre_17` | `pgpcre_16` | `pgpcre_15` | `pgpcre_14` | `pgpcre_13` |
| `el9` | `pgpcre_17` | `pgpcre_16` | `pgpcre_15` | `pgpcre_14` | `pgpcre_13` |
| `d12` | `postgresql-17-pgpcre` | `postgresql-16-pgpcre` | `postgresql-15-pgpcre` | `postgresql-14-pgpcre` | `postgresql-13-pgpcre` |
| `u22` | `postgresql-17-pgpcre` | `postgresql-16-pgpcre` | `postgresql-15-pgpcre` | `postgresql-14-pgpcre` | `postgresql-13-pgpcre` |
| `u24` | `postgresql-17-pgpcre` | `postgresql-16-pgpcre` | `postgresql-15-pgpcre` | `postgresql-14-pgpcre` | `postgresql-13-pgpcre` |






# shacrypt


> [shacrypt](https://github.com/dverite/postgres-shacrypt): Implements SHA256-CRYPT and SHA512-CRYPT password encryption schemes
>
> https://github.com/dverite/postgres-shacrypt





[UTIL](/util) extensions: [`zstd`](/zstd), [`gzip`](/gzip), [`http`](/http), [`pg_net`](/pg_net), [`pgjwt`](/pgjwt), [`pg_smtp_client`](/pg_smtp_client), [`pg_html5_email_address`](/pg_html5_email_address), [`url_encode`](/url_encode), [`pgsql_tweaks`](/pgsql_tweaks), [`pg_extra_time`](/pg_extra_time), [`pgpcre`](/pgpcre), [`icu_ext`](/icu_ext), [`pgqr`](/pgqr), [`pg_protobuf`](/pg_protobuf), [`envvar`](/envvar), [`floatfile`](/floatfile), [`pg_readme`](/pg_readme), [`ddl_historization`](/ddl_historization), [`data_historization`](/data_historization), [`pg_schedoc`](/pg_schedoc), [`hashlib`](/hashlib), [`shacrypt`](/shacrypt), [`cryptint`](/cryptint), [`pguecc`](/pguecc)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [shacrypt](https://github.com/dverite/postgres-shacrypt) | 1.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [shacrypt](/shacrypt) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION shacrypt;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgres_shacrypt_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-shacrypt` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `shacrypt` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add shacrypt
```


Install `shacrypt` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["shacrypt"]}'
```


Install `shacrypt` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install postgres_shacrypt_17*;
dnf install postgres_shacrypt_16*;
dnf install postgres_shacrypt_15*;
dnf install postgres_shacrypt_14*;
dnf install postgres_shacrypt_13*;
```


Install `shacrypt` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-shacrypt;
apt install postgresql-16-shacrypt;
apt install postgresql-15-shacrypt;
apt install postgresql-14-shacrypt;
apt install postgresql-13-shacrypt;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `postgres_shacrypt_17*` | `postgres_shacrypt_16*` | `postgres_shacrypt_15*` | `postgres_shacrypt_14*` | `postgres_shacrypt_13*` |
| `el9` | `postgres_shacrypt_17*` | `postgres_shacrypt_16*` | `postgres_shacrypt_15*` | `postgres_shacrypt_14*` | `postgres_shacrypt_13*` |
| `d12` | `postgresql-17-shacrypt` | `postgresql-16-shacrypt` | `postgresql-15-shacrypt` | `postgresql-14-shacrypt` | `postgresql-13-shacrypt` |
| `u22` | `postgresql-17-shacrypt` | `postgresql-16-shacrypt` | `postgresql-15-shacrypt` | `postgresql-14-shacrypt` | `postgresql-13-shacrypt` |
| `u24` | `postgresql-17-shacrypt` | `postgresql-16-shacrypt` | `postgresql-15-shacrypt` | `postgresql-14-shacrypt` | `postgresql-13-shacrypt` |






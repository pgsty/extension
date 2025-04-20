# pguecc


> [pg_ecdsa](https://github.com/ameensol/pg-ecdsa): uECC bindings for Postgres
>
> https://github.com/ameensol/pg-ecdsa





[UTIL](/util) extensions: [`gzip`](/gzip), [`bzip`](/bzip), [`zstd`](/zstd), [`http`](/http), [`pg_net`](/pg_net), [`pg_curl`](/pg_curl), [`pgjq`](/pgjq), [`pgjwt`](/pgjwt), [`pg_smtp_client`](/pg_smtp_client), [`pg_html5_email_address`](/pg_html5_email_address), [`url_encode`](/url_encode), [`pgsql_tweaks`](/pgsql_tweaks), [`pg_extra_time`](/pg_extra_time), [`pgpcre`](/pgpcre), [`icu_ext`](/icu_ext), [`pgqr`](/pgqr), [`pg_protobuf`](/pg_protobuf), [`envvar`](/envvar), [`floatfile`](/floatfile), [`pg_readme`](/pg_readme), [`pg_readme_test_extension`](/pg_readme_test_extension), [`ddl_historization`](/ddl_historization), [`data_historization`](/data_historization), [`schedoc`](/schedoc), [`hashlib`](/hashlib), [`xxhash`](/xxhash), [`shacrypt`](/shacrypt), [`cryptint`](/cryptint), [`pguecc`](/pguecc), [`sparql`](/sparql)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pguecc](https://github.com/ameensol/pg-ecdsa) | 1.0 | **<span class="tcblue">BSD-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_ecdsa](/pguecc) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pguecc;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0 | **<span class="tcblue">BSD-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_ecdsa_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.0 | **<span class="tcblue">BSD-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-ecdsa` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pguecc` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pguecc
```


Install `pg_ecdsa` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_ecdsa"]}'
```


Install `pg_ecdsa` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_ecdsa_17*;
dnf install pg_ecdsa_16*;
dnf install pg_ecdsa_15*;
dnf install pg_ecdsa_14*;
dnf install pg_ecdsa_13*;
```


Install `pg_ecdsa` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-ecdsa;
apt install postgresql-16-pg-ecdsa;
apt install postgresql-15-pg-ecdsa;
apt install postgresql-14-pg-ecdsa;
apt install postgresql-13-pg-ecdsa;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_ecdsa_17*` | `pg_ecdsa_16*` | `pg_ecdsa_15*` | `pg_ecdsa_14*` | `pg_ecdsa_13*` |
| `el9` | `pg_ecdsa_17*` | `pg_ecdsa_16*` | `pg_ecdsa_15*` | `pg_ecdsa_14*` | `pg_ecdsa_13*` |
| `d12` | `postgresql-17-pg-ecdsa` | `postgresql-16-pg-ecdsa` | `postgresql-15-pg-ecdsa` | `postgresql-14-pg-ecdsa` | `postgresql-13-pg-ecdsa` |
| `u22` | `postgresql-17-pg-ecdsa` | `postgresql-16-pg-ecdsa` | `postgresql-15-pg-ecdsa` | `postgresql-14-pg-ecdsa` | `postgresql-13-pg-ecdsa` |
| `u24` | `postgresql-17-pg-ecdsa` | `postgresql-16-pg-ecdsa` | `postgresql-15-pg-ecdsa` | `postgresql-14-pg-ecdsa` | `postgresql-13-pg-ecdsa` |






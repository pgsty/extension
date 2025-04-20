# pg_html5_email_address


> [pg_html5_email_address](https://github.com/bigsmoke/pg_html5_email_address): PostgreSQL email validation that is consistent with the HTML5 spec
>
> https://github.com/bigsmoke/pg_html5_email_address





[UTIL](/util) extensions: [`gzip`](/gzip), [`bzip`](/bzip), [`zstd`](/zstd), [`http`](/http), [`pg_net`](/pg_net), [`pg_curl`](/pg_curl), [`pgjq`](/pgjq), [`pgjwt`](/pgjwt), [`pg_smtp_client`](/pg_smtp_client), [`pg_html5_email_address`](/pg_html5_email_address), [`url_encode`](/url_encode), [`pgsql_tweaks`](/pgsql_tweaks), [`pg_extra_time`](/pg_extra_time), [`pgpcre`](/pgpcre), [`icu_ext`](/icu_ext), [`pgqr`](/pgqr), [`pg_protobuf`](/pg_protobuf), [`envvar`](/envvar), [`floatfile`](/floatfile), [`pg_readme`](/pg_readme), [`pg_readme_test_extension`](/pg_readme_test_extension), [`ddl_historization`](/ddl_historization), [`data_historization`](/data_historization), [`schedoc`](/schedoc), [`hashlib`](/hashlib), [`xxhash`](/xxhash), [`shacrypt`](/shacrypt), [`cryptint`](/cryptint), [`pguecc`](/pguecc), [`sparql`](/sparql)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_html5_email_address](https://github.com/bigsmoke/pg_html5_email_address) | 1.2.3 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_html5_email_address](/pg_html5_email_address) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_html5_email_address;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.2.3 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_html5_email_address_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.2.3 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-html5-email-address` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pg_html5_email_address` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_html5_email_address
```


Install `pg_html5_email_address` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_html5_email_address"]}'
```


Install `pg_html5_email_address` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_html5_email_address_17;
dnf install pg_html5_email_address_16;
dnf install pg_html5_email_address_15;
dnf install pg_html5_email_address_14;
dnf install pg_html5_email_address_13;
```


Install `pg_html5_email_address` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-html5-email-address;
apt install postgresql-16-pg-html5-email-address;
apt install postgresql-15-pg-html5-email-address;
apt install postgresql-14-pg-html5-email-address;
apt install postgresql-13-pg-html5-email-address;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_html5_email_address_17` | `pg_html5_email_address_16` | `pg_html5_email_address_15` | `pg_html5_email_address_14` | `pg_html5_email_address_13` |
| `el9` | `pg_html5_email_address_17` | `pg_html5_email_address_16` | `pg_html5_email_address_15` | `pg_html5_email_address_14` | `pg_html5_email_address_13` |
| `d12` | `postgresql-17-pg-html5-email-address` | `postgresql-16-pg-html5-email-address` | `postgresql-15-pg-html5-email-address` | `postgresql-14-pg-html5-email-address` | `postgresql-13-pg-html5-email-address` |
| `u22` | `postgresql-17-pg-html5-email-address` | `postgresql-16-pg-html5-email-address` | `postgresql-15-pg-html5-email-address` | `postgresql-14-pg-html5-email-address` | `postgresql-13-pg-html5-email-address` |
| `u24` | `postgresql-17-pg-html5-email-address` | `postgresql-16-pg-html5-email-address` | `postgresql-15-pg-html5-email-address` | `postgresql-14-pg-html5-email-address` | `postgresql-13-pg-html5-email-address` |






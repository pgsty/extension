# ddl_historization


> [ddl_historization](https://github.com/rodo/pg_ddl_historization): Historize the ddl changes inside PostgreSQL database
>
> https://github.com/rodo/pg_ddl_historization





[UTIL](/util) extensions: [`gzip`](/gzip), [`bzip`](/bzip), [`zstd`](/zstd), [`http`](/http), [`pg_net`](/pg_net), [`pg_curl`](/pg_curl), [`pgjq`](/pgjq), [`pgjwt`](/pgjwt), [`pg_smtp_client`](/pg_smtp_client), [`pg_html5_email_address`](/pg_html5_email_address), [`url_encode`](/url_encode), [`pgsql_tweaks`](/pgsql_tweaks), [`pg_extra_time`](/pg_extra_time), [`pgpcre`](/pgpcre), [`icu_ext`](/icu_ext), [`pgqr`](/pgqr), [`pg_protobuf`](/pg_protobuf), [`envvar`](/envvar), [`floatfile`](/floatfile), [`pg_render`](/pg_render), [`pg_readme`](/pg_readme), [`pg_readme_test_extension`](/pg_readme_test_extension), [`ddl_historization`](/ddl_historization), [`data_historization`](/data_historization), [`schedoc`](/schedoc), [`hashlib`](/hashlib), [`xxhash`](/xxhash), [`shacrypt`](/shacrypt), [`cryptint`](/cryptint), [`pguecc`](/pguecc), [`sparql`](/sparql)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [ddl_historization](https://github.com/rodo/pg_ddl_historization) | 0.0.7 | **<span class="tcwarn">GPLv2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [ddl_historization](/ddl_historization) |  |  | [`plpgsql`](plpgsql) | [`schedoc`](/schedoc) |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION ddl_historization CASCADE;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.0.7 | **<span class="tcwarn">GPLv2</span>** | **<span class="tcwarn">PIGSTY</span>** | `ddl_historization_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 0.0.7 | **<span class="tcwarn">GPLv2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-ddl-historization` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `ddl_historization` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add ddl_historization
```


Install `ddl_historization` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["ddl_historization"]}'
```


Install `ddl_historization` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install ddl_historization_17;
dnf install ddl_historization_16;
dnf install ddl_historization_15;
dnf install ddl_historization_14;
dnf install ddl_historization_13;
```


Install `ddl_historization` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-ddl-historization;
apt install postgresql-16-ddl-historization;
apt install postgresql-15-ddl-historization;
apt install postgresql-14-ddl-historization;
apt install postgresql-13-ddl-historization;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `ddl_historization_17` | `ddl_historization_16` | `ddl_historization_15` | `ddl_historization_14` | `ddl_historization_13` |
| `el9` | `ddl_historization_17` | `ddl_historization_16` | `ddl_historization_15` | `ddl_historization_14` | `ddl_historization_13` |
| `d12` | `postgresql-17-ddl-historization` | `postgresql-16-ddl-historization` | `postgresql-15-ddl-historization` | `postgresql-14-ddl-historization` | `postgresql-13-ddl-historization` |
| `u22` | `postgresql-17-ddl-historization` | `postgresql-16-ddl-historization` | `postgresql-15-ddl-historization` | `postgresql-14-ddl-historization` | `postgresql-13-ddl-historization` |
| `u24` | `postgresql-17-ddl-historization` | `postgresql-16-ddl-historization` | `postgresql-15-ddl-historization` | `postgresql-14-ddl-historization` | `postgresql-13-ddl-historization` |






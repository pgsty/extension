# schedoc


> [pg_schedoc](https://github.com/ZeroGachis/pg_schedoc): Cross documentation between Django and DBT projects
>
> https://github.com/ZeroGachis/pg_schedoc





[UTIL](/util) extensions: [`zstd`](/zstd), [`gzip`](/gzip), [`http`](/http), [`pg_net`](/pg_net), [`pg_curl`](/pg_curl), [`pgjq`](/pgjq), [`pgjwt`](/pgjwt), [`pg_smtp_client`](/pg_smtp_client), [`pg_html5_email_address`](/pg_html5_email_address), [`url_encode`](/url_encode), [`pgsql_tweaks`](/pgsql_tweaks), [`pg_extra_time`](/pg_extra_time), [`pgpcre`](/pgpcre), [`icu_ext`](/icu_ext), [`pgqr`](/pgqr), [`pg_protobuf`](/pg_protobuf), [`envvar`](/envvar), [`floatfile`](/floatfile), [`pg_readme`](/pg_readme), [`ddl_historization`](/ddl_historization), [`data_historization`](/data_historization), [`schedoc`](/schedoc), [`hashlib`](/hashlib), [`xxhash`](/xxhash), [`shacrypt`](/shacrypt), [`cryptint`](/cryptint), [`pguecc`](/pguecc), [`sparql`](/sparql)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [schedoc](https://github.com/ZeroGachis/pg_schedoc) | 0.0.2 | **<span class="tcwarn">GPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_schedoc](/schedoc) |  |  | [`ddl_historization`](ddl_historization) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION schedoc CASCADE;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.0.2 | **<span class="tcwarn">GPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_schedoc_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | `ddl_historization_$v` |
| [DEB](/deb) | 0.0.2 | **<span class="tcwarn">GPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-schedoc` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | `postgresql-$v-ddl-historization` |



Install `schedoc` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add schedoc
```


Install `pg_schedoc` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_schedoc"]}'
```


Install `pg_schedoc` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_schedoc_17;
dnf install pg_schedoc_16;
dnf install pg_schedoc_15;
dnf install pg_schedoc_14;
dnf install pg_schedoc_13;
```


Install `pg_schedoc` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-schedoc;
apt install postgresql-16-pg-schedoc;
apt install postgresql-15-pg-schedoc;
apt install postgresql-14-pg-schedoc;
apt install postgresql-13-pg-schedoc;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_schedoc_17` | `pg_schedoc_16` | `pg_schedoc_15` | `pg_schedoc_14` | `pg_schedoc_13` |
| `el9` | `pg_schedoc_17` | `pg_schedoc_16` | `pg_schedoc_15` | `pg_schedoc_14` | `pg_schedoc_13` |
| `d12` | `postgresql-17-pg-schedoc` | `postgresql-16-pg-schedoc` | `postgresql-15-pg-schedoc` | `postgresql-14-pg-schedoc` | `postgresql-13-pg-schedoc` |
| `u22` | `postgresql-17-pg-schedoc` | `postgresql-16-pg-schedoc` | `postgresql-15-pg-schedoc` | `postgresql-14-pg-schedoc` | `postgresql-13-pg-schedoc` |
| `u24` | `postgresql-17-pg-schedoc` | `postgresql-16-pg-schedoc` | `postgresql-15-pg-schedoc` | `postgresql-14-pg-schedoc` | `postgresql-13-pg-schedoc` |






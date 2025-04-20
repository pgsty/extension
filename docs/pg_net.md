# pg_net


> [pg_net](https://github.com/supabase/pg_net): Async HTTP Requests
>
> https://github.com/supabase/pg_net





[UTIL](/util) extensions: [`gzip`](/gzip), [`bzip`](/bzip), [`zstd`](/zstd), [`http`](/http), [`pg_net`](/pg_net), [`pg_curl`](/pg_curl), [`pgjq`](/pgjq), [`pgjwt`](/pgjwt), [`pg_smtp_client`](/pg_smtp_client), [`pg_html5_email_address`](/pg_html5_email_address), [`url_encode`](/url_encode), [`pgsql_tweaks`](/pgsql_tweaks), [`pg_extra_time`](/pg_extra_time), [`pgpcre`](/pgpcre), [`icu_ext`](/icu_ext), [`pgqr`](/pgqr), [`pg_protobuf`](/pg_protobuf), [`envvar`](/envvar), [`floatfile`](/floatfile), [`pg_readme`](/pg_readme), [`pg_readme_test_extension`](/pg_readme_test_extension), [`ddl_historization`](/ddl_historization), [`data_historization`](/data_historization), [`schedoc`](/schedoc), [`hashlib`](/hashlib), [`xxhash`](/xxhash), [`shacrypt`](/shacrypt), [`cryptint`](/cryptint), [`pguecc`](/pguecc), [`sparql`](/sparql)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_net](https://github.com/supabase/pg_net) | 0.9.2 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_net](/pg_net) | `supabase` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'pg_net'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION pg_net;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.9.2 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_net_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 0.9.2 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-net` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pg_net` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_net
```


Install `pg_net` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_net"]}'
```


Install `pg_net` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_net_17*;
dnf install pg_net_16*;
dnf install pg_net_15*;
dnf install pg_net_14*;
dnf install pg_net_13*;
```


Install `pg_net` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-net;
apt install postgresql-16-pg-net;
apt install postgresql-15-pg-net;
apt install postgresql-14-pg-net;
apt install postgresql-13-pg-net;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_net_17*` | `pg_net_16*` | `pg_net_15*` | `pg_net_14*` | `pg_net_13*` |
| `el9` | `pg_net_17*` | `pg_net_16*` | `pg_net_15*` | `pg_net_14*` | `pg_net_13*` |
| `d12` | `postgresql-17-pg-net` | `postgresql-16-pg-net` | `postgresql-15-pg-net` | `postgresql-14-pg-net` | `postgresql-13-pg-net` |
| `u22` | `postgresql-17-pg-net` | `postgresql-16-pg-net` | `postgresql-15-pg-net` | `postgresql-14-pg-net` | `postgresql-13-pg-net` |
| `u24` | `postgresql-17-pg-net` | `postgresql-16-pg-net` | `postgresql-15-pg-net` | `postgresql-14-pg-net` | `postgresql-13-pg-net` |






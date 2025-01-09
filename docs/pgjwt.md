# pgjwt


> [pgjwt](https://github.com/michelp/pgjwt): JSON Web Token API for Postgresql
>
> https://github.com/michelp/pgjwt





[FUNC](/func) extensions: [`topn`](/topn), [`gzip`](/gzip), [`zstd`](/zstd), [`http`](/http), [`pg_net`](/pg_net), [`pg_smtp_client`](/pg_smtp_client), [`pg_html5_email_address`](/pg_html5_email_address), [`pgsql_tweaks`](/pgsql_tweaks), [`pg_extra_time`](/pg_extra_time), [`count_distinct`](/count_distinct), [`extra_window_functions`](/extra_window_functions), [`first_last_agg`](/first_last_agg), [`tdigest`](/tdigest), [`aggs_for_vecs`](/aggs_for_vecs), [`aggs_for_arrays`](/aggs_for_arrays), [`arraymath`](/arraymath), [`quantile`](/quantile), [`lower_quantile`](/lower_quantile), [`pg_idkit`](/pg_idkit), [`pg_uuidv7`](/pg_uuidv7), [`permuteseq`](/permuteseq), [`pg_hashids`](/pg_hashids), [`sequential_uuids`](/sequential_uuids), [`pg_math`](/pg_math), [`random`](/random), [`base36`](/base36), [`base62`](/base62), [`pg_base58`](/pg_base58), [`floatvec`](/floatvec), [`financial`](/financial), [`pgjwt`](/pgjwt), [`hashlib`](/hashlib), [`shacrypt`](/shacrypt), [`cryptint`](/cryptint), [`pguecc`](/pguecc), [`pgpcre`](/pgpcre), [`icu_ext`](/icu_ext), [`pgqr`](/pgqr), [`envvar`](/envvar), [`pg_protobuf`](/pg_protobuf), [`url_encode`](/url_encode), [`pg_readme`](/pg_readme), [`refint`](/refint), [`autoinc`](/autoinc), [`insert_username`](/insert_username), [`moddatetime`](/moddatetime), [`tsm_system_time`](/tsm_system_time), [`dict_xsyn`](/dict_xsyn), [`tsm_system_rows`](/tsm_system_rows), [`tcn`](/tcn), [`uuid-ossp`](/uuid-ossp), [`btree_gist`](/btree_gist), [`btree_gin`](/btree_gin), [`intarray`](/intarray), [`intagg`](/intagg), [`dict_int`](/dict_int), [`unaccent`](/unaccent)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgjwt](https://github.com/michelp/pgjwt) | 0.2.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgjwt](/pgjwt) | `supabase` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pgjwt;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.2.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `pgjwt_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 0.2.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pgjwt` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pgjwt` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pgjwt
```


Install `pgjwt` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgjwt"]}'
```


Install `pgjwt` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pgjwt_17*;
dnf install pgjwt_16*;
dnf install pgjwt_15*;
dnf install pgjwt_14*;
dnf install pgjwt_13*;
```


Install `pgjwt` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pgjwt;
apt install postgresql-16-pgjwt;
apt install postgresql-15-pgjwt;
apt install postgresql-14-pgjwt;
apt install postgresql-13-pgjwt;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgjwt_17*` | `pgjwt_16*` | `pgjwt_15*` | `pgjwt_14*` | `pgjwt_13*` |
| `el9` | `pgjwt_17*` | `pgjwt_16*` | `pgjwt_15*` | `pgjwt_14*` | `pgjwt_13*` |
| `d12` | `postgresql-17-pgjwt` | `postgresql-16-pgjwt` | `postgresql-15-pgjwt` | `postgresql-14-pgjwt` | `postgresql-13-pgjwt` |
| `u22` | `postgresql-17-pgjwt` | `postgresql-16-pgjwt` | `postgresql-15-pgjwt` | `postgresql-14-pgjwt` | `postgresql-13-pgjwt` |
| `u24` | `postgresql-17-pgjwt` | `postgresql-16-pgjwt` | `postgresql-15-pgjwt` | `postgresql-14-pgjwt` | `postgresql-13-pgjwt` |






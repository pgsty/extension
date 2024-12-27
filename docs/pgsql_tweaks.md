# pgsql_tweaks


> [pgsql_tweaks](https://github.com/sjstoelting/pgsql-tweaks): Some functions and views for daily usage
>
> https://github.com/sjstoelting/pgsql-tweaks





[FUNC](/func) extensions: [`topn`](/topn), [`gzip`](/gzip), [`zstd`](/zstd), [`http`](/http), [`pg_net`](/pg_net), [`pg_smtp_client`](/pg_smtp_client), [`pg_html5_email_address`](/pg_html5_email_address), [`pgsql_tweaks`](/pgsql_tweaks), [`pg_extra_time`](/pg_extra_time), [`count_distinct`](/count_distinct), [`extra_window_functions`](/extra_window_functions), [`first_last_agg`](/first_last_agg), [`tdigest`](/tdigest), [`aggs_for_vecs`](/aggs_for_vecs), [`aggs_for_arrays`](/aggs_for_arrays), [`arraymath`](/arraymath), [`quantile`](/quantile), [`lower_quantile`](/lower_quantile), [`pg_idkit`](/pg_idkit), [`pg_uuidv7`](/pg_uuidv7), [`permuteseq`](/permuteseq), [`pg_hashids`](/pg_hashids), [`sequential_uuids`](/sequential_uuids), [`pg_math`](/pg_math), [`random`](/random), [`base36`](/base36), [`base62`](/base62), [`pg_base58`](/pg_base58), [`floatvec`](/floatvec), [`financial`](/financial), [`pgjwt`](/pgjwt), [`hashlib`](/hashlib), [`shacrypt`](/shacrypt), [`cryptint`](/cryptint), [`pguecc`](/pguecc), [`pgpcre`](/pgpcre), [`icu_ext`](/icu_ext), [`pgqr`](/pgqr), [`envvar`](/envvar), [`pg_protobuf`](/pg_protobuf), [`url_encode`](/url_encode), [`refint`](/refint), [`autoinc`](/autoinc), [`insert_username`](/insert_username), [`moddatetime`](/moddatetime), [`tsm_system_time`](/tsm_system_time), [`dict_xsyn`](/dict_xsyn), [`tsm_system_rows`](/tsm_system_rows), [`tcn`](/tcn), [`uuid-ossp`](/uuid-ossp), [`btree_gist`](/btree_gist), [`btree_gin`](/btree_gin), [`intarray`](/intarray), [`intagg`](/intagg), [`dict_int`](/dict_int), [`unaccent`](/unaccent)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgsql_tweaks](https://github.com/sjstoelting/pgsql-tweaks) | 0.10.7 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgsql_tweaks](/pgsql_tweaks) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pgsql_tweaks;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.10.7 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pgsql_tweaks_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 0.10.4 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pgsql-tweaks` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pgsql_tweaks` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pgsql_tweaks
```


Install `pgsql_tweaks` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgsql_tweaks"]}'
```


Install `pgsql_tweaks` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pgsql_tweaks_17*;
dnf install pgsql_tweaks_16*;
dnf install pgsql_tweaks_15*;
dnf install pgsql_tweaks_14*;
dnf install pgsql_tweaks_13*;
```


Install `pgsql_tweaks` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pgsql-tweaks;
apt install postgresql-16-pgsql-tweaks;
apt install postgresql-15-pgsql-tweaks;
apt install postgresql-14-pgsql-tweaks;
apt install postgresql-13-pgsql-tweaks;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgsql_tweaks_17*` | `pgsql_tweaks_16*` | `pgsql_tweaks_15*` | `pgsql_tweaks_14*` | `pgsql_tweaks_13*` |
| `el9` | `pgsql_tweaks_17*` | `pgsql_tweaks_16*` | `pgsql_tweaks_15*` | `pgsql_tweaks_14*` | `pgsql_tweaks_13*` |
| `d12` | `postgresql-17-pgsql-tweaks` | `postgresql-16-pgsql-tweaks` | `postgresql-15-pgsql-tweaks` | `postgresql-14-pgsql-tweaks` | `postgresql-13-pgsql-tweaks` |
| `u22` | `postgresql-17-pgsql-tweaks` | `postgresql-16-pgsql-tweaks` | `postgresql-15-pgsql-tweaks` | `postgresql-14-pgsql-tweaks` | `postgresql-13-pgsql-tweaks` |
| `u24` | `postgresql-17-pgsql-tweaks` | `postgresql-16-pgsql-tweaks` | `postgresql-15-pgsql-tweaks` | `postgresql-14-pgsql-tweaks` | `postgresql-13-pgsql-tweaks` |






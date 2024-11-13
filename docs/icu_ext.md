# icu_ext


> [icu_ext](https://github.com/dverite/icu_ext): Access ICU functions
>
> https://github.com/dverite/icu_ext





[FUNC](/func) extensions: [`topn`](/topn), [`gzip`](/gzip), [`zstd`](/zstd), [`http`](/http), [`pg_net`](/pg_net), [`pg_smtp_client`](/pg_smtp_client), [`pg_html5_email_address`](/pg_html5_email_address), [`pgsql_tweaks`](/pgsql_tweaks), [`pg_extra_time`](/pg_extra_time), [`timeit`](/timeit), [`count_distinct`](/count_distinct), [`extra_window_functions`](/extra_window_functions), [`first_last_agg`](/first_last_agg), [`tdigest`](/tdigest), [`aggs_for_vecs`](/aggs_for_vecs), [`aggs_for_arrays`](/aggs_for_arrays), [`arraymath`](/arraymath), [`quantile`](/quantile), [`lower_quantile`](/lower_quantile), [`pg_idkit`](/pg_idkit), [`pg_uuidv7`](/pg_uuidv7), [`permuteseq`](/permuteseq), [`pg_hashids`](/pg_hashids), [`sequential_uuids`](/sequential_uuids), [`pg_math`](/pg_math), [`random`](/random), [`base36`](/base36), [`base62`](/base62), [`pg_base58`](/pg_base58), [`floatvec`](/floatvec), [`financial`](/financial), [`pgjwt`](/pgjwt), [`pg_hashlib`](/pg_hashlib), [`shacrypt`](/shacrypt), [`cryptint`](/cryptint), [`pguecc`](/pguecc), [`pgpcre`](/pgpcre), [`icu_ext`](/icu_ext), [`pgqr`](/pgqr), [`envvar`](/envvar), [`pg_protobuf`](/pg_protobuf), [`url_encode`](/url_encode), [`refint`](/refint), [`autoinc`](/autoinc), [`insert_username`](/insert_username), [`moddatetime`](/moddatetime), [`tsm_system_time`](/tsm_system_time), [`dict_xsyn`](/dict_xsyn), [`tsm_system_rows`](/tsm_system_rows), [`tcn`](/tcn), [`uuid-ossp`](/uuid-ossp), [`btree_gist`](/btree_gist), [`btree_gin`](/btree_gin), [`intarray`](/intarray), [`intagg`](/intagg), [`dict_int`](/dict_int), [`unaccent`](/unaccent)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [icu_ext](https://github.com/dverite/icu_ext) | 1.9 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [icu_ext](/icu_ext) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION icu_ext;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `icu_ext_17*` | `icu_ext_16*` | `icu_ext_15*` | `icu_ext_14*` | `icu_ext_13*` | `icu_ext_12*` |
| `el9` | `icu_ext_17*` | `icu_ext_16*` | `icu_ext_15*` | `icu_ext_14*` | `icu_ext_13*` | `icu_ext_12*` |
| `d12` | `postgresql-17-icu-ext` | `postgresql-16-icu-ext` | `postgresql-15-icu-ext` | `postgresql-14-icu-ext` | `postgresql-13-icu-ext` | `postgresql-12-icu-ext` |
| `u22` | `postgresql-17-icu-ext` | `postgresql-16-icu-ext` | `postgresql-15-icu-ext` | `postgresql-14-icu-ext` | `postgresql-13-icu-ext` | `postgresql-12-icu-ext` |
| `u24` | `postgresql-17-icu-ext` | `postgresql-16-icu-ext` | `postgresql-15-icu-ext` | `postgresql-14-icu-ext` | `postgresql-13-icu-ext` | `postgresql-12-icu-ext` |



Install `icu_ext` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["icu_ext"]}'
```


Install `icu_ext` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install icu_ext_17*;
yum install icu_ext_16*;
yum install icu_ext_15*;
yum install icu_ext_14*;
yum install icu_ext_13*;
yum install icu_ext_12*;
```


Install `icu_ext` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-icu-ext;
apt install postgresql-16-icu-ext;
apt install postgresql-15-icu-ext;
apt install postgresql-14-icu-ext;
apt install postgresql-13-icu-ext;
apt install postgresql-12-icu-ext;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `icu_ext_17*` | `icu_ext_16*` | `icu_ext_15*` | `icu_ext_14*` | `icu_ext_13*` | `icu_ext_12*` |
| `el9` | `icu_ext_17*` | `icu_ext_16*` | `icu_ext_15*` | `icu_ext_14*` | `icu_ext_13*` | `icu_ext_12*` |
| `d12` | `postgresql-17-icu-ext` | `postgresql-16-icu-ext` | `postgresql-15-icu-ext` | `postgresql-14-icu-ext` | `postgresql-13-icu-ext` | `postgresql-12-icu-ext` |
| `u22` | `postgresql-17-icu-ext` | `postgresql-16-icu-ext` | `postgresql-15-icu-ext` | `postgresql-14-icu-ext` | `postgresql-13-icu-ext` | `postgresql-12-icu-ext` |
| `u24` | `postgresql-17-icu-ext` | `postgresql-16-icu-ext` | `postgresql-15-icu-ext` | `postgresql-14-icu-ext` | `postgresql-13-icu-ext` | `postgresql-12-icu-ext` |






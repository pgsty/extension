# cryptint


> [cryptint](https://github.com/dverite/cryptint): Encryption functions for int and bigint values
>
> https://github.com/dverite/cryptint





[FUNC](/func) extensions: [`topn`](/topn), [`gzip`](/gzip), [`zstd`](/zstd), [`http`](/http), [`pg_net`](/pg_net), [`pg_smtp_client`](/pg_smtp_client), [`pg_html5_email_address`](/pg_html5_email_address), [`pgsql_tweaks`](/pgsql_tweaks), [`pg_extra_time`](/pg_extra_time), [`timeit`](/timeit), [`count_distinct`](/count_distinct), [`extra_window_functions`](/extra_window_functions), [`first_last_agg`](/first_last_agg), [`tdigest`](/tdigest), [`aggs_for_vecs`](/aggs_for_vecs), [`aggs_for_arrays`](/aggs_for_arrays), [`arraymath`](/arraymath), [`quantile`](/quantile), [`lower_quantile`](/lower_quantile), [`pg_idkit`](/pg_idkit), [`pg_uuidv7`](/pg_uuidv7), [`permuteseq`](/permuteseq), [`pg_hashids`](/pg_hashids), [`sequential_uuids`](/sequential_uuids), [`pg_math`](/pg_math), [`random`](/random), [`base36`](/base36), [`base62`](/base62), [`pg_base58`](/pg_base58), [`floatvec`](/floatvec), [`financial`](/financial), [`pgjwt`](/pgjwt), [`pg_hashlib`](/pg_hashlib), [`shacrypt`](/shacrypt), [`cryptint`](/cryptint), [`pguecc`](/pguecc), [`pgpcre`](/pgpcre), [`icu_ext`](/icu_ext), [`pgqr`](/pgqr), [`envvar`](/envvar), [`pg_protobuf`](/pg_protobuf), [`url_encode`](/url_encode), [`refint`](/refint), [`autoinc`](/autoinc), [`insert_username`](/insert_username), [`moddatetime`](/moddatetime), [`tsm_system_time`](/tsm_system_time), [`dict_xsyn`](/dict_xsyn), [`tsm_system_rows`](/tsm_system_rows), [`tcn`](/tcn), [`uuid-ossp`](/uuid-ossp), [`btree_gist`](/btree_gist), [`btree_gin`](/btree_gin), [`intarray`](/intarray), [`intagg`](/intagg), [`dict_int`](/dict_int), [`unaccent`](/unaccent)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [cryptint](https://github.com/dverite/cryptint) | 1.0.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [cryptint](/cryptint) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION cryptint;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `cryptint_17*` | `cryptint_16*` | `cryptint_15*` | `cryptint_14*` | `cryptint_13*` | `cryptint_12*` |
| `el9` | `cryptint_17*` | `cryptint_16*` | `cryptint_15*` | `cryptint_14*` | `cryptint_13*` | `cryptint_12*` |
| `d12` | `postgresql-17-cryptint` | `postgresql-16-cryptint` | `postgresql-15-cryptint` | `postgresql-14-cryptint` | `postgresql-13-cryptint` | `postgresql-12-cryptint` |
| `u22` | `postgresql-17-cryptint` | `postgresql-16-cryptint` | `postgresql-15-cryptint` | `postgresql-14-cryptint` | `postgresql-13-cryptint` | `postgresql-12-cryptint` |
| `u24` | `postgresql-17-cryptint` | `postgresql-16-cryptint` | `postgresql-15-cryptint` | `postgresql-14-cryptint` | `postgresql-13-cryptint` | `postgresql-12-cryptint` |



Install `cryptint` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["cryptint"]}'
```


Install `cryptint` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install cryptint_17*;
yum install cryptint_16*;
yum install cryptint_15*;
yum install cryptint_14*;
yum install cryptint_13*;
yum install cryptint_12*;
```


Install `cryptint` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-cryptint;
apt install postgresql-16-cryptint;
apt install postgresql-15-cryptint;
apt install postgresql-14-cryptint;
apt install postgresql-13-cryptint;
apt install postgresql-12-cryptint;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `cryptint_17*` | `cryptint_16*` | `cryptint_15*` | `cryptint_14*` | `cryptint_13*` | `cryptint_12*` |
| `el9` | `cryptint_17*` | `cryptint_16*` | `cryptint_15*` | `cryptint_14*` | `cryptint_13*` | `cryptint_12*` |
| `d12` | `postgresql-17-cryptint` | `postgresql-16-cryptint` | `postgresql-15-cryptint` | `postgresql-14-cryptint` | `postgresql-13-cryptint` | `postgresql-12-cryptint` |
| `u22` | `postgresql-17-cryptint` | `postgresql-16-cryptint` | `postgresql-15-cryptint` | `postgresql-14-cryptint` | `postgresql-13-cryptint` | `postgresql-12-cryptint` |
| `u24` | `postgresql-17-cryptint` | `postgresql-16-cryptint` | `postgresql-15-cryptint` | `postgresql-14-cryptint` | `postgresql-13-cryptint` | `postgresql-12-cryptint` |






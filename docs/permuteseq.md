# permuteseq


> [permuteseq](https://github.com/dverite/permuteseq): Pseudo-randomly permute sequences with a format-preserving encryption on elements
>
> https://github.com/dverite/permuteseq





[FUNC](/func) extensions: [`topn`](/topn), [`gzip`](/gzip), [`zstd`](/zstd), [`http`](/http), [`pg_net`](/pg_net), [`pg_smtp_client`](/pg_smtp_client), [`pg_html5_email_address`](/pg_html5_email_address), [`pgsql_tweaks`](/pgsql_tweaks), [`pg_extra_time`](/pg_extra_time), [`count_distinct`](/count_distinct), [`extra_window_functions`](/extra_window_functions), [`first_last_agg`](/first_last_agg), [`tdigest`](/tdigest), [`aggs_for_vecs`](/aggs_for_vecs), [`aggs_for_arrays`](/aggs_for_arrays), [`arraymath`](/arraymath), [`quantile`](/quantile), [`lower_quantile`](/lower_quantile), [`pg_idkit`](/pg_idkit), [`pg_uuidv7`](/pg_uuidv7), [`permuteseq`](/permuteseq), [`pg_hashids`](/pg_hashids), [`sequential_uuids`](/sequential_uuids), [`pg_math`](/pg_math), [`random`](/random), [`base36`](/base36), [`base62`](/base62), [`pg_base58`](/pg_base58), [`floatvec`](/floatvec), [`financial`](/financial), [`pgjwt`](/pgjwt), [`pg_hashlib`](/pg_hashlib), [`shacrypt`](/shacrypt), [`cryptint`](/cryptint), [`pguecc`](/pguecc), [`pgpcre`](/pgpcre), [`icu_ext`](/icu_ext), [`pgqr`](/pgqr), [`envvar`](/envvar), [`pg_protobuf`](/pg_protobuf), [`url_encode`](/url_encode), [`refint`](/refint), [`autoinc`](/autoinc), [`insert_username`](/insert_username), [`moddatetime`](/moddatetime), [`tsm_system_time`](/tsm_system_time), [`dict_xsyn`](/dict_xsyn), [`tsm_system_rows`](/tsm_system_rows), [`tcn`](/tcn), [`uuid-ossp`](/uuid-ossp), [`btree_gist`](/btree_gist), [`btree_gin`](/btree_gin), [`intarray`](/intarray), [`intagg`](/intagg), [`dict_int`](/dict_int), [`unaccent`](/unaccent)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [permuteseq](https://github.com/dverite/permuteseq) | 1.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [permuteseq](/permuteseq) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION permuteseq;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `permuteseq_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-permuteseq` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `permuteseq` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["permuteseq"]}'
```


Install `permuteseq` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install permuteseq_17*;
dnf install permuteseq_16*;
dnf install permuteseq_15*;
dnf install permuteseq_14*;
dnf install permuteseq_13*;
dnf install permuteseq_12*;
```


Install `permuteseq` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-permuteseq;
apt install postgresql-16-permuteseq;
apt install postgresql-15-permuteseq;
apt install postgresql-14-permuteseq;
apt install postgresql-13-permuteseq;
apt install postgresql-12-permuteseq;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `permuteseq_17*` | `permuteseq_16*` | `permuteseq_15*` | `permuteseq_14*` | `permuteseq_13*` | `permuteseq_12*` |
| `el9` | `permuteseq_17*` | `permuteseq_16*` | `permuteseq_15*` | `permuteseq_14*` | `permuteseq_13*` | `permuteseq_12*` |
| `d12` | `postgresql-17-permuteseq` | `postgresql-16-permuteseq` | `postgresql-15-permuteseq` | `postgresql-14-permuteseq` | `postgresql-13-permuteseq` | `postgresql-12-permuteseq` |
| `u22` | `postgresql-17-permuteseq` | `postgresql-16-permuteseq` | `postgresql-15-permuteseq` | `postgresql-14-permuteseq` | `postgresql-13-permuteseq` | `postgresql-12-permuteseq` |
| `u24` | `postgresql-17-permuteseq` | `postgresql-16-permuteseq` | `postgresql-15-permuteseq` | `postgresql-14-permuteseq` | `postgresql-13-permuteseq` | `postgresql-12-permuteseq` |






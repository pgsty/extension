# aggs_for_arrays


> [aggs_for_arrays](https://github.com/pjungwir/aggs_for_arrays): Various functions for computing statistics on arrays of numbers
>
> https://github.com/pjungwir/aggs_for_arrays





[FUNC](/func) extensions: [`pg_idkit`](/pg_idkit), [`pg_uuidv7`](/pg_uuidv7), [`permuteseq`](/permuteseq), [`pg_hashids`](/pg_hashids), [`sequential_uuids`](/sequential_uuids), [`topn`](/topn), [`quantile`](/quantile), [`lower_quantile`](/lower_quantile), [`count_distinct`](/count_distinct), [`omnisketch`](/omnisketch), [`ddsketch`](/ddsketch), [`vasco`](/vasco), [`tdigest`](/tdigest), [`first_last_agg`](/first_last_agg), [`extra_window_functions`](/extra_window_functions), [`floatvec`](/floatvec), [`aggs_for_vecs`](/aggs_for_vecs), [`aggs_for_arrays`](/aggs_for_arrays), [`arraymath`](/arraymath), [`pg_math`](/pg_math), [`random`](/random), [`base36`](/base36), [`base62`](/base62), [`pg_base58`](/pg_base58), [`financial`](/financial), [`refint`](/refint), [`autoinc`](/autoinc), [`insert_username`](/insert_username), [`moddatetime`](/moddatetime), [`tsm_system_time`](/tsm_system_time), [`dict_xsyn`](/dict_xsyn), [`tsm_system_rows`](/tsm_system_rows), [`tcn`](/tcn), [`uuid-ossp`](/uuid-ossp), [`btree_gist`](/btree_gist), [`btree_gin`](/btree_gin), [`intarray`](/intarray), [`intagg`](/intagg), [`dict_int`](/dict_int), [`unaccent`](/unaccent)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [aggs_for_arrays](https://github.com/pjungwir/aggs_for_arrays) | 1.3.3 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [aggs_for_arrays](/aggs_for_arrays) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION aggs_for_arrays;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.3.3 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `aggs_for_arrays_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.3.3 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-aggs-for-arrays` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `aggs_for_arrays` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add aggs_for_arrays
```


Install `aggs_for_arrays` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["aggs_for_arrays"]}'
```


Install `aggs_for_arrays` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install aggs_for_arrays_17*;
dnf install aggs_for_arrays_16*;
dnf install aggs_for_arrays_15*;
dnf install aggs_for_arrays_14*;
dnf install aggs_for_arrays_13*;
```


Install `aggs_for_arrays` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-aggs-for-arrays;
apt install postgresql-16-aggs-for-arrays;
apt install postgresql-15-aggs-for-arrays;
apt install postgresql-14-aggs-for-arrays;
apt install postgresql-13-aggs-for-arrays;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `aggs_for_arrays_17*` | `aggs_for_arrays_16*` | `aggs_for_arrays_15*` | `aggs_for_arrays_14*` | `aggs_for_arrays_13*` |
| `el9` | `aggs_for_arrays_17*` | `aggs_for_arrays_16*` | `aggs_for_arrays_15*` | `aggs_for_arrays_14*` | `aggs_for_arrays_13*` |
| `d12` | `postgresql-17-aggs-for-arrays` | `postgresql-16-aggs-for-arrays` | `postgresql-15-aggs-for-arrays` | `postgresql-14-aggs-for-arrays` | `postgresql-13-aggs-for-arrays` |
| `u22` | `postgresql-17-aggs-for-arrays` | `postgresql-16-aggs-for-arrays` | `postgresql-15-aggs-for-arrays` | `postgresql-14-aggs-for-arrays` | `postgresql-13-aggs-for-arrays` |
| `u24` | `postgresql-17-aggs-for-arrays` | `postgresql-16-aggs-for-arrays` | `postgresql-15-aggs-for-arrays` | `postgresql-14-aggs-for-arrays` | `postgresql-13-aggs-for-arrays` |






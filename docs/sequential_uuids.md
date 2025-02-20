# sequential_uuids


> [sequential_uuids](https://github.com/tvondra/sequential-uuids): generator of sequential UUIDs
>
> https://github.com/tvondra/sequential-uuids





[FUNC](/func) extensions: [`pg_idkit`](/pg_idkit), [`pg_uuidv7`](/pg_uuidv7), [`permuteseq`](/permuteseq), [`pg_hashids`](/pg_hashids), [`sequential_uuids`](/sequential_uuids), [`topn`](/topn), [`quantile`](/quantile), [`lower_quantile`](/lower_quantile), [`count_distinct`](/count_distinct), [`omnisketch`](/omnisketch), [`ddsketch`](/ddsketch), [`vasco`](/vasco), [`xicor`](/xicor), [`tdigest`](/tdigest), [`first_last_agg`](/first_last_agg), [`extra_window_functions`](/extra_window_functions), [`floatvec`](/floatvec), [`aggs_for_vecs`](/aggs_for_vecs), [`aggs_for_arrays`](/aggs_for_arrays), [`arraymath`](/arraymath), [`pg_math`](/pg_math), [`random`](/random), [`base36`](/base36), [`base62`](/base62), [`pg_base58`](/pg_base58), [`financial`](/financial), [`refint`](/refint), [`autoinc`](/autoinc), [`insert_username`](/insert_username), [`moddatetime`](/moddatetime), [`tsm_system_time`](/tsm_system_time), [`dict_xsyn`](/dict_xsyn), [`tsm_system_rows`](/tsm_system_rows), [`tcn`](/tcn), [`uuid-ossp`](/uuid-ossp), [`btree_gist`](/btree_gist), [`btree_gin`](/btree_gin), [`intarray`](/intarray), [`intagg`](/intagg), [`dict_int`](/dict_int), [`unaccent`](/unaccent)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [sequential_uuids](https://github.com/tvondra/sequential-uuids) | 1.0.3 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [sequential_uuids](/sequential_uuids) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION sequential_uuids;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0.3 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `sequential_uuids_$v` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 1.0.3 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-sequential-uuids` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `sequential_uuids` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add sequential_uuids
```


Install `sequential_uuids` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["sequential_uuids"]}'
```


Install `sequential_uuids` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install sequential_uuids_17;
dnf install sequential_uuids_16;
dnf install sequential_uuids_15;
dnf install sequential_uuids_14;
dnf install sequential_uuids_13;
```


Install `sequential_uuids` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-sequential-uuids;
apt install postgresql-16-sequential-uuids;
apt install postgresql-15-sequential-uuids;
apt install postgresql-14-sequential-uuids;
apt install postgresql-13-sequential-uuids;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `sequential_uuids_17` | `sequential_uuids_16` | `sequential_uuids_15` | `sequential_uuids_14` | `sequential_uuids_13` |
| `el9` | `sequential_uuids_17` | `sequential_uuids_16` | `sequential_uuids_15` | `sequential_uuids_14` | `sequential_uuids_13` |
| `d12` | `postgresql-17-sequential-uuids` | `postgresql-16-sequential-uuids` | `postgresql-15-sequential-uuids` | `postgresql-14-sequential-uuids` | `postgresql-13-sequential-uuids` |
| `u22` | `postgresql-17-sequential-uuids` | `postgresql-16-sequential-uuids` | `postgresql-15-sequential-uuids` | `postgresql-14-sequential-uuids` | `postgresql-13-sequential-uuids` |
| `u24` | `postgresql-17-sequential-uuids` | `postgresql-16-sequential-uuids` | `postgresql-15-sequential-uuids` | `postgresql-14-sequential-uuids` | `postgresql-13-sequential-uuids` |






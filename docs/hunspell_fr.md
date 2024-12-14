# hunspell_fr


> [hunspell_fr](https://github.com/postgrespro/hunspell_dicts): French Hunspell Dictionary
>
> https://github.com/postgrespro/hunspell_dicts





[FTS](/fts) extensions: [`pg_search`](/pg_search), [`pgroonga`](/pgroonga), [`pg_bigm`](/pg_bigm), [`zhparser`](/zhparser), [`pg_bestmatch`](/pg_bestmatch), [`hunspell_cs_cz`](/hunspell_cs_cz), [`hunspell_de_de`](/hunspell_de_de), [`hunspell_en_us`](/hunspell_en_us), [`hunspell_fr`](/hunspell_fr), [`hunspell_ne_np`](/hunspell_ne_np), [`hunspell_nl_nl`](/hunspell_nl_nl), [`hunspell_nn_no`](/hunspell_nn_no), [`hunspell_pt_pt`](/hunspell_pt_pt), [`hunspell_ru_ru`](/hunspell_ru_ru), [`hunspell_ru_ru_aot`](/hunspell_ru_ru_aot), [`fuzzystrmatch`](/fuzzystrmatch), [`pg_trgm`](/pg_trgm)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [hunspell_fr](https://github.com/postgrespro/hunspell_dicts) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Data` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [hunspell_fr](/hunspell_fr) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION hunspell_fr;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `hunspell_fr_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-hunspell-fr` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `hunspell_fr` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["hunspell_fr"]}'
```


Install `hunspell_fr` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install hunspell_fr_17;
dnf install hunspell_fr_16;
dnf install hunspell_fr_15;
dnf install hunspell_fr_14;
dnf install hunspell_fr_13;
dnf install hunspell_fr_12;
```


Install `hunspell_fr` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-hunspell-fr;
apt install postgresql-16-hunspell-fr;
apt install postgresql-15-hunspell-fr;
apt install postgresql-14-hunspell-fr;
apt install postgresql-13-hunspell-fr;
apt install postgresql-12-hunspell-fr;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `hunspell_fr_17` | `hunspell_fr_16` | `hunspell_fr_15` | `hunspell_fr_14` | `hunspell_fr_13` | `hunspell_fr_12` |
| `el9` | `hunspell_fr_17` | `hunspell_fr_16` | `hunspell_fr_15` | `hunspell_fr_14` | `hunspell_fr_13` | `hunspell_fr_12` |
| `d12` | `postgresql-17-hunspell-fr` | `postgresql-16-hunspell-fr` | `postgresql-15-hunspell-fr` | `postgresql-14-hunspell-fr` | `postgresql-13-hunspell-fr` | `postgresql-12-hunspell-fr` |
| `u22` | `postgresql-17-hunspell-fr` | `postgresql-16-hunspell-fr` | `postgresql-15-hunspell-fr` | `postgresql-14-hunspell-fr` | `postgresql-13-hunspell-fr` | `postgresql-12-hunspell-fr` |
| `u24` | `postgresql-17-hunspell-fr` | `postgresql-16-hunspell-fr` | `postgresql-15-hunspell-fr` | `postgresql-14-hunspell-fr` | `postgresql-13-hunspell-fr` | `postgresql-12-hunspell-fr` |






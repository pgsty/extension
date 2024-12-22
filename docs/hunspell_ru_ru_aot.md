# hunspell_ru_ru_aot


> [hunspell_ru_ru_aot](https://github.com/postgrespro/hunspell_dicts): Russian Hunspell Dictionary (from AOT.ru group)
>
> https://github.com/postgrespro/hunspell_dicts





[FTS](/fts) extensions: [`pg_search`](/pg_search), [`pgroonga`](/pgroonga), [`pgroonga_database`](/pgroonga_database), [`pg_bigm`](/pg_bigm), [`zhparser`](/zhparser), [`pg_bestmatch`](/pg_bestmatch), [`hunspell_cs_cz`](/hunspell_cs_cz), [`hunspell_de_de`](/hunspell_de_de), [`hunspell_en_us`](/hunspell_en_us), [`hunspell_fr`](/hunspell_fr), [`hunspell_ne_np`](/hunspell_ne_np), [`hunspell_nl_nl`](/hunspell_nl_nl), [`hunspell_nn_no`](/hunspell_nn_no), [`hunspell_pt_pt`](/hunspell_pt_pt), [`hunspell_ru_ru`](/hunspell_ru_ru), [`hunspell_ru_ru_aot`](/hunspell_ru_ru_aot), [`fuzzystrmatch`](/fuzzystrmatch), [`pg_trgm`](/pg_trgm)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [hunspell_ru_ru_aot](https://github.com/postgrespro/hunspell_dicts) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Data` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [hunspell_ru_ru_aot](/hunspell_ru_ru_aot) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION hunspell_ru_ru_aot;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `hunspell_ru_ru_aot_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-hunspell-ru-ru-aot` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `hunspell_ru_ru_aot` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["hunspell_ru_ru_aot"]}'
```


Install `hunspell_ru_ru_aot` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install hunspell_ru_ru_aot_17;
dnf install hunspell_ru_ru_aot_16;
dnf install hunspell_ru_ru_aot_15;
dnf install hunspell_ru_ru_aot_14;
dnf install hunspell_ru_ru_aot_13;
dnf install hunspell_ru_ru_aot_12;
```


Install `hunspell_ru_ru_aot` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-hunspell-ru-ru-aot;
apt install postgresql-16-hunspell-ru-ru-aot;
apt install postgresql-15-hunspell-ru-ru-aot;
apt install postgresql-14-hunspell-ru-ru-aot;
apt install postgresql-13-hunspell-ru-ru-aot;
apt install postgresql-12-hunspell-ru-ru-aot;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `hunspell_ru_ru_aot_17` | `hunspell_ru_ru_aot_16` | `hunspell_ru_ru_aot_15` | `hunspell_ru_ru_aot_14` | `hunspell_ru_ru_aot_13` | `hunspell_ru_ru_aot_12` |
| `el9` | `hunspell_ru_ru_aot_17` | `hunspell_ru_ru_aot_16` | `hunspell_ru_ru_aot_15` | `hunspell_ru_ru_aot_14` | `hunspell_ru_ru_aot_13` | `hunspell_ru_ru_aot_12` |
| `d12` | `postgresql-17-hunspell-ru-ru-aot` | `postgresql-16-hunspell-ru-ru-aot` | `postgresql-15-hunspell-ru-ru-aot` | `postgresql-14-hunspell-ru-ru-aot` | `postgresql-13-hunspell-ru-ru-aot` | `postgresql-12-hunspell-ru-ru-aot` |
| `u22` | `postgresql-17-hunspell-ru-ru-aot` | `postgresql-16-hunspell-ru-ru-aot` | `postgresql-15-hunspell-ru-ru-aot` | `postgresql-14-hunspell-ru-ru-aot` | `postgresql-13-hunspell-ru-ru-aot` | `postgresql-12-hunspell-ru-ru-aot` |
| `u24` | `postgresql-17-hunspell-ru-ru-aot` | `postgresql-16-hunspell-ru-ru-aot` | `postgresql-15-hunspell-ru-ru-aot` | `postgresql-14-hunspell-ru-ru-aot` | `postgresql-13-hunspell-ru-ru-aot` | `postgresql-12-hunspell-ru-ru-aot` |






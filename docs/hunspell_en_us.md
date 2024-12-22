# hunspell_en_us


> [hunspell_en_us](https://github.com/postgrespro/hunspell_dicts): en_US Hunspell Dictionary
>
> https://github.com/postgrespro/hunspell_dicts





[FTS](/fts) extensions: [`pg_search`](/pg_search), [`pgroonga`](/pgroonga), [`pgroonga_database`](/pgroonga_database), [`pg_bigm`](/pg_bigm), [`zhparser`](/zhparser), [`pg_bestmatch`](/pg_bestmatch), [`hunspell_cs_cz`](/hunspell_cs_cz), [`hunspell_de_de`](/hunspell_de_de), [`hunspell_en_us`](/hunspell_en_us), [`hunspell_fr`](/hunspell_fr), [`hunspell_ne_np`](/hunspell_ne_np), [`hunspell_nl_nl`](/hunspell_nl_nl), [`hunspell_nn_no`](/hunspell_nn_no), [`hunspell_pt_pt`](/hunspell_pt_pt), [`hunspell_ru_ru`](/hunspell_ru_ru), [`hunspell_ru_ru_aot`](/hunspell_ru_ru_aot), [`fuzzystrmatch`](/fuzzystrmatch), [`pg_trgm`](/pg_trgm)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [hunspell_en_us](https://github.com/postgrespro/hunspell_dicts) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Data` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [hunspell_en_us](/hunspell_en_us) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION hunspell_en_us;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `hunspell_en_us_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-hunspell-en-us` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `hunspell_en_us` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["hunspell_en_us"]}'
```


Install `hunspell_en_us` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install hunspell_en_us_17;
dnf install hunspell_en_us_16;
dnf install hunspell_en_us_15;
dnf install hunspell_en_us_14;
dnf install hunspell_en_us_13;
dnf install hunspell_en_us_12;
```


Install `hunspell_en_us` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-hunspell-en-us;
apt install postgresql-16-hunspell-en-us;
apt install postgresql-15-hunspell-en-us;
apt install postgresql-14-hunspell-en-us;
apt install postgresql-13-hunspell-en-us;
apt install postgresql-12-hunspell-en-us;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `hunspell_en_us_17` | `hunspell_en_us_16` | `hunspell_en_us_15` | `hunspell_en_us_14` | `hunspell_en_us_13` | `hunspell_en_us_12` |
| `el9` | `hunspell_en_us_17` | `hunspell_en_us_16` | `hunspell_en_us_15` | `hunspell_en_us_14` | `hunspell_en_us_13` | `hunspell_en_us_12` |
| `d12` | `postgresql-17-hunspell-en-us` | `postgresql-16-hunspell-en-us` | `postgresql-15-hunspell-en-us` | `postgresql-14-hunspell-en-us` | `postgresql-13-hunspell-en-us` | `postgresql-12-hunspell-en-us` |
| `u22` | `postgresql-17-hunspell-en-us` | `postgresql-16-hunspell-en-us` | `postgresql-15-hunspell-en-us` | `postgresql-14-hunspell-en-us` | `postgresql-13-hunspell-en-us` | `postgresql-12-hunspell-en-us` |
| `u24` | `postgresql-17-hunspell-en-us` | `postgresql-16-hunspell-en-us` | `postgresql-15-hunspell-en-us` | `postgresql-14-hunspell-en-us` | `postgresql-13-hunspell-en-us` | `postgresql-12-hunspell-en-us` |






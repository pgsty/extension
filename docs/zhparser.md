# zhparser


> [zhparser](https://github.com/amutu/zhparser): a parser for full-text search of Chinese
>
> https://github.com/amutu/zhparser





[FTS](/fts) extensions: [`pg_search`](/pg_search), [`pgroonga`](/pgroonga), [`pgroonga_database`](/pgroonga_database), [`pg_bigm`](/pg_bigm), [`zhparser`](/zhparser), [`pg_bestmatch`](/pg_bestmatch), [`vchord_bm25`](/vchord_bm25), [`pg_tokenizer`](/pg_tokenizer), [`hunspell_cs_cz`](/hunspell_cs_cz), [`hunspell_de_de`](/hunspell_de_de), [`hunspell_en_us`](/hunspell_en_us), [`hunspell_fr`](/hunspell_fr), [`hunspell_ne_np`](/hunspell_ne_np), [`hunspell_nl_nl`](/hunspell_nl_nl), [`hunspell_nn_no`](/hunspell_nn_no), [`hunspell_pt_pt`](/hunspell_pt_pt), [`hunspell_ru_ru`](/hunspell_ru_ru), [`hunspell_ru_ru_aot`](/hunspell_ru_ru_aot), [`fuzzystrmatch`](/fuzzystrmatch), [`pg_trgm`](/pg_trgm)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [zhparser](https://github.com/amutu/zhparser) | 2.3 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [zhparser](/zhparser) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION zhparser;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 2.3 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `zhparser_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 2.3 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-zhparser` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `zhparser` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add zhparser
```


Install `zhparser` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["zhparser"]}'
```


Install `zhparser` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install zhparser_17*;
dnf install zhparser_16*;
dnf install zhparser_15*;
dnf install zhparser_14*;
dnf install zhparser_13*;
```


Install `zhparser` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-zhparser;
apt install postgresql-16-zhparser;
apt install postgresql-15-zhparser;
apt install postgresql-14-zhparser;
apt install postgresql-13-zhparser;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `zhparser_17*` | `zhparser_16*` | `zhparser_15*` | `zhparser_14*` | `zhparser_13*` |
| `el9` | `zhparser_17*` | `zhparser_16*` | `zhparser_15*` | `zhparser_14*` | `zhparser_13*` |
| `d12` | `postgresql-17-zhparser` | `postgresql-16-zhparser` | `postgresql-15-zhparser` | `postgresql-14-zhparser` | `postgresql-13-zhparser` |
| `u22` | `postgresql-17-zhparser` | `postgresql-16-zhparser` | `postgresql-15-zhparser` | `postgresql-14-zhparser` | `postgresql-13-zhparser` |
| `u24` | `postgresql-17-zhparser` | `postgresql-16-zhparser` | `postgresql-15-zhparser` | `postgresql-14-zhparser` | `postgresql-13-zhparser` |






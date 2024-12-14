# pgroonga


> [pgroonga](https://github.com/pgroonga/pgroonga): Use Groonga as index, fast full text search platform for all languages!
>
> https://github.com/pgroonga/pgroonga





[FTS](/fts) extensions: [`pg_search`](/pg_search), [`pgroonga`](/pgroonga), [`pg_bigm`](/pg_bigm), [`zhparser`](/zhparser), [`pg_bestmatch`](/pg_bestmatch), [`hunspell_cs_cz`](/hunspell_cs_cz), [`hunspell_de_de`](/hunspell_de_de), [`hunspell_en_us`](/hunspell_en_us), [`hunspell_fr`](/hunspell_fr), [`hunspell_ne_np`](/hunspell_ne_np), [`hunspell_nl_nl`](/hunspell_nl_nl), [`hunspell_nn_no`](/hunspell_nn_no), [`hunspell_pt_pt`](/hunspell_pt_pt), [`hunspell_ru_ru`](/hunspell_ru_ru), [`hunspell_ru_ru_aot`](/hunspell_ru_ru_aot), [`fuzzystrmatch`](/fuzzystrmatch), [`pg_trgm`](/pg_trgm)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgroonga](https://github.com/pgroonga/pgroonga) | 3.2.5 | BSD-3 | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgroonga](/pgroonga) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pgroonga;
```
> **Comment**: missing 12-14 support on el, missing aarch64 on el
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 3.2.5 | BSD-3 | **<span class="tcwarn">PIGSTY</span>** | `postgresql$v-pgdg-pgroonga` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  |  | `groonga-libs` |
| [DEB](/deb) | 3.2.5 | BSD-3 | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pgdg-pgroonga` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  |  | `libgroonga0` |



Install `pgroonga` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgroonga"]}'
```


Install `pgroonga` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install postgresql17-pgdg-pgroonga;
yum install postgresql16-pgdg-pgroonga;
yum install postgresql15-pgdg-pgroonga;
yum install postgresql14-pgdg-pgroonga;
yum install postgresql13-pgdg-pgroonga;
yum install postgresql12-pgdg-pgroonga;
```


Install `pgroonga` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pgdg-pgroonga;
apt install postgresql-16-pgdg-pgroonga;
apt install postgresql-15-pgdg-pgroonga;
apt install postgresql-14-pgdg-pgroonga;
apt install postgresql-13-pgdg-pgroonga;
apt install postgresql-12-pgdg-pgroonga;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `postgresql17-pgdg-pgroonga` | `postgresql16-pgdg-pgroonga` | `postgresql15-pgdg-pgroonga` | `postgresql14-pgdg-pgroonga` | `postgresql13-pgdg-pgroonga` | `postgresql12-pgdg-pgroonga` |
| `el9` | `postgresql17-pgdg-pgroonga` | `postgresql16-pgdg-pgroonga` | `postgresql15-pgdg-pgroonga` | `postgresql14-pgdg-pgroonga` | `postgresql13-pgdg-pgroonga` | `postgresql12-pgdg-pgroonga` |
| `d12` | `postgresql-17-pgdg-pgroonga` | `postgresql-16-pgdg-pgroonga` | `postgresql-15-pgdg-pgroonga` | `postgresql-14-pgdg-pgroonga` | `postgresql-13-pgdg-pgroonga` | `postgresql-12-pgdg-pgroonga` |
| `u22` | `postgresql-17-pgdg-pgroonga` | `postgresql-16-pgdg-pgroonga` | `postgresql-15-pgdg-pgroonga` | `postgresql-14-pgdg-pgroonga` | `postgresql-13-pgdg-pgroonga` | `postgresql-12-pgdg-pgroonga` |
| `u24` | `postgresql-17-pgdg-pgroonga` | `postgresql-16-pgdg-pgroonga` | `postgresql-15-pgdg-pgroonga` | `postgresql-14-pgdg-pgroonga` | `postgresql-13-pgdg-pgroonga` | `postgresql-12-pgdg-pgroonga` |






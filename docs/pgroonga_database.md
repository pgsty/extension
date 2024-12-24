# pgroonga_database


> [pgroonga](https://github.com/pgroonga/pgroonga): PGroonga database management module
>
> https://github.com/pgroonga/pgroonga





[FTS](/fts) extensions: [`pg_search`](/pg_search), [`pgroonga`](/pgroonga), [`pgroonga_database`](/pgroonga_database), [`pg_bigm`](/pg_bigm), [`zhparser`](/zhparser), [`pg_bestmatch`](/pg_bestmatch), [`hunspell_cs_cz`](/hunspell_cs_cz), [`hunspell_de_de`](/hunspell_de_de), [`hunspell_en_us`](/hunspell_en_us), [`hunspell_fr`](/hunspell_fr), [`hunspell_ne_np`](/hunspell_ne_np), [`hunspell_nl_nl`](/hunspell_nl_nl), [`hunspell_nn_no`](/hunspell_nn_no), [`hunspell_pt_pt`](/hunspell_pt_pt), [`hunspell_ru_ru`](/hunspell_ru_ru), [`hunspell_ru_ru_aot`](/hunspell_ru_ru_aot), [`fuzzystrmatch`](/fuzzystrmatch), [`pg_trgm`](/pg_trgm)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgroonga_database](https://github.com/pgroonga/pgroonga) | 3.2.5 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgroonga](/pgroonga_database) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pgroonga_database;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| Distro-pgroonga | 3.2.5 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pgroonga_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | `groonga-libs` |
| Distro-pgroonga | 3.2.5 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pgdg-pgroonga` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | `libgroonga0` |



Install `pgroonga_database` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pgroonga_database
```


Install `pgroonga` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgroonga"]}'
```


Install `pgroonga` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pgroonga_17*;
dnf install pgroonga_16*;
dnf install pgroonga_15*;
dnf install pgroonga_14*;
dnf install pgroonga_13*;
```


Install `pgroonga` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pgdg-pgroonga;
apt install postgresql-16-pgdg-pgroonga;
apt install postgresql-15-pgdg-pgroonga;
apt install postgresql-14-pgdg-pgroonga;
apt install postgresql-13-pgdg-pgroonga;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgroonga_17*` | `pgroonga_16*` | `pgroonga_15*` | `pgroonga_14*` | `pgroonga_13*` |
| `el9` | `pgroonga_17*` | `pgroonga_16*` | `pgroonga_15*` | `pgroonga_14*` | `pgroonga_13*` |
| `d12` | `postgresql-17-pgdg-pgroonga` | `postgresql-16-pgdg-pgroonga` | `postgresql-15-pgdg-pgroonga` | `postgresql-14-pgdg-pgroonga` | `postgresql-13-pgdg-pgroonga` |
| `u22` | `postgresql-17-pgdg-pgroonga` | `postgresql-16-pgdg-pgroonga` | `postgresql-15-pgdg-pgroonga` | `postgresql-14-pgdg-pgroonga` | `postgresql-13-pgdg-pgroonga` |
| `u24` | `postgresql-17-pgdg-pgroonga` | `postgresql-16-pgdg-pgroonga` | `postgresql-15-pgdg-pgroonga` | `postgresql-14-pgdg-pgroonga` | `postgresql-13-pgdg-pgroonga` |






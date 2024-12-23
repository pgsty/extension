# pgroonga


> [pgroonga](https://github.com/pgroonga/pgroonga): Use Groonga as index, fast full text search platform for all languages!
>
> https://github.com/pgroonga/pgroonga





[FTS](/fts) extensions: [`pg_search`](/pg_search), [`pgroonga`](/pgroonga), [`pgroonga_database`](/pgroonga_database), [`pg_bigm`](/pg_bigm), [`zhparser`](/zhparser), [`pg_bestmatch`](/pg_bestmatch), [`hunspell_cs_cz`](/hunspell_cs_cz), [`hunspell_de_de`](/hunspell_de_de), [`hunspell_en_us`](/hunspell_en_us), [`hunspell_fr`](/hunspell_fr), [`hunspell_ne_np`](/hunspell_ne_np), [`hunspell_nl_nl`](/hunspell_nl_nl), [`hunspell_nn_no`](/hunspell_nn_no), [`hunspell_pt_pt`](/hunspell_pt_pt), [`hunspell_ru_ru`](/hunspell_ru_ru), [`hunspell_ru_ru_aot`](/hunspell_ru_ru_aot), [`fuzzystrmatch`](/fuzzystrmatch), [`pg_trgm`](/pg_trgm)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgroonga](https://github.com/pgroonga/pgroonga) | 3.2.5 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgroonga](/pgroonga) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pgroonga;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 3.2.5 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pgroonga_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | `groonga-libs` |
| [DEB](/deb) | 3.2.5 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pgdg-pgroonga` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | `libgroonga0` |



Install `pgroonga` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pgroonga
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
apt install postgresql-12-pgdg-pgroonga;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgroonga_17*` | `pgroonga_16*` | `pgroonga_15*` | `pgroonga_14*` | `pgroonga_13*` |
| `el9` | `pgroonga_17*` | `pgroonga_16*` | `pgroonga_15*` | `pgroonga_14*` | `pgroonga_13*` |
| `d12` | `postgresql-17-pgdg-pgroonga` | `postgresql-16-pgdg-pgroonga` | `postgresql-15-pgdg-pgroonga` | `postgresql-14-pgdg-pgroonga` | `postgresql-13-pgdg-pgroonga` |
| `u22` | `postgresql-17-pgdg-pgroonga` | `postgresql-16-pgdg-pgroonga` | `postgresql-15-pgdg-pgroonga` | `postgresql-14-pgdg-pgroonga` | `postgresql-13-pgdg-pgroonga` |
| `u24` | `postgresql-17-pgdg-pgroonga` | `postgresql-16-pgdg-pgroonga` | `postgresql-15-pgdg-pgroonga` | `postgresql-14-pgdg-pgroonga` | `postgresql-13-pgdg-pgroonga` |






--------

## Usage

- https://pgroonga.github.io/
- [News](https://pgroonga.github.io/news/): It lists release information.
- [Overview](https://pgroonga.github.io/overview/): It describes about PGroonga.
- [Install](https://pgroonga.github.io/install/): It describes how to install PGroonga.
- [Upgrade](https://pgroonga.github.io/upgrade/): It describes how to upgrade PGroonga.
- [Uninstall](https://pgroonga.github.io/uninstall/): It describes how to uninstall PGroonga.
- [Tutorial](https://pgroonga.github.io/tutorial/): It describes how to use PGroonga step by step.
- [FAQ](https://pgroonga.github.io/faq/): Frequently asked questions.
- [How to](https://pgroonga.github.io/how-to/): It describes about useful information for specific situations.
- [Reference](https://pgroonga.github.io/reference/): It describes details for each features such as options, functions and operators.
- [Troubleshooting](https://pgroonga.github.io/troubleshooting/): It describes how to fix troubles.
- [Community](https://pgroonga.github.io/community/): It introduces about PGroonga community.
- [Users](https://pgroonga.github.io/users/): It lists PGroonga users.
- [Development](https://pgroonga.github.io/development/): It describes how to develop PGroonga.

Here's a quick [tutorial](https://pgroonga.github.io/tutorial/) about how to use PGroonga:

```sql
CREATE EXTENSION IF NOT EXISTS pgroonga;

CREATE TABLE memos
(
    id      integer,
    content text
);

CREATE INDEX pgroonga_content_index ON memos USING pgroonga (content);

INSERT INTO memos VALUES (1, 'PostgreSQL is a relational database management system.');
INSERT INTO memos VALUES (2, 'Groonga is a fast full text search engine that supports all languages.');
INSERT INTO memos VALUES (3, 'PGroonga is a PostgreSQL extension that uses Groonga as index.');
INSERT INTO memos VALUES (4, 'There is groonga command.');

SET enable_seqscan = off;

-- now let's query pgroonga

SELECT * FROM memos WHERE content &@ 'engine';
--  id |                                content                                 
-- ----+------------------------------------------------------------------------
--   2 | Groonga is a fast full text search engine that supports all languages.
-- (1 row)

SELECT * FROM memos WHERE content &@~ 'PGroonga OR PostgreSQL';
--  id |                            content                             
-- ----+----------------------------------------------------------------
--   3 | PGroonga is a PostgreSQL extension that uses Groonga as index.
--   1 | PostgreSQL is a relational database management system.
-- (2 rows)

SELECT * FROM memos WHERE content LIKE '%engine%';
--  id |                                content                                 
-- ----+------------------------------------------------------------------------
--   2 | Groonga is a fast full text search engine that supports all languages.
-- (1 row)
```

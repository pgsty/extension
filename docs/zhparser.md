# zhparser


> [zhparser](https://github.com/amutu/zhparser): a parser for full-text search of Chinese
>
> https://github.com/amutu/zhparser





[FTS](/fts) extensions: [`pg_search`](/pg_search), [`pg_bigm`](/pg_bigm), [`zhparser`](/zhparser), [`hunspell_cs_cz`](/hunspell_cs_cz), [`hunspell_de_de`](/hunspell_de_de), [`hunspell_en_us`](/hunspell_en_us), [`hunspell_fr`](/hunspell_fr), [`hunspell_ne_np`](/hunspell_ne_np), [`hunspell_nl_nl`](/hunspell_nl_nl), [`hunspell_nn_no`](/hunspell_nn_no), [`hunspell_pt_pt`](/hunspell_pt_pt), [`hunspell_ru_ru`](/hunspell_ru_ru), [`hunspell_ru_ru_aot`](/hunspell_ru_ru_aot), [`fuzzystrmatch`](/fuzzystrmatch), [`pg_trgm`](/pg_trgm)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [zhparser](https://github.com/amutu/zhparser) | 2.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [zhparser](/zhparser) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION zhparser;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `zhparser_17*` | `zhparser_16*` | `zhparser_15*` | `zhparser_14*` | `zhparser_13*` | `zhparser_12*` |
| `el9` | `zhparser_17*` | `zhparser_16*` | `zhparser_15*` | `zhparser_14*` | `zhparser_13*` | `zhparser_12*` |
| `d12` | `postgresql-17-zhparser` | `postgresql-16-zhparser` | `postgresql-15-zhparser` | `postgresql-14-zhparser` | `postgresql-13-zhparser` | `postgresql-12-zhparser` |
| `u22` | `postgresql-17-zhparser` | `postgresql-16-zhparser` | `postgresql-15-zhparser` | `postgresql-14-zhparser` | `postgresql-13-zhparser` | `postgresql-12-zhparser` |
| `u24` | `postgresql-17-zhparser` | `postgresql-16-zhparser` | `postgresql-15-zhparser` | `postgresql-14-zhparser` | `postgresql-13-zhparser` | `postgresql-12-zhparser` |



Install `zhparser` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["zhparser"]}'
```


Install `zhparser` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install zhparser_17*;
yum install zhparser_16*;
yum install zhparser_15*;
yum install zhparser_14*;
yum install zhparser_13*;
yum install zhparser_12*;
```


Install `zhparser` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-zhparser;
apt install postgresql-16-zhparser;
apt install postgresql-15-zhparser;
apt install postgresql-14-zhparser;
apt install postgresql-13-zhparser;
apt install postgresql-12-zhparser;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `zhparser_17*` | `zhparser_16*` | `zhparser_15*` | `zhparser_14*` | `zhparser_13*` | `zhparser_12*` |
| `el9` | `zhparser_17*` | `zhparser_16*` | `zhparser_15*` | `zhparser_14*` | `zhparser_13*` | `zhparser_12*` |
| `d12` | `postgresql-17-zhparser` | `postgresql-16-zhparser` | `postgresql-15-zhparser` | `postgresql-14-zhparser` | `postgresql-13-zhparser` | `postgresql-12-zhparser` |
| `u22` | `postgresql-17-zhparser` | `postgresql-16-zhparser` | `postgresql-15-zhparser` | `postgresql-14-zhparser` | `postgresql-13-zhparser` | `postgresql-12-zhparser` |
| `u24` | `postgresql-17-zhparser` | `postgresql-16-zhparser` | `postgresql-15-zhparser` | `postgresql-14-zhparser` | `postgresql-13-zhparser` | `postgresql-12-zhparser` |






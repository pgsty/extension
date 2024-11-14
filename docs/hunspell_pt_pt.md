# hunspell_pt_pt


> [hunspell_pt_pt](https://github.com/postgrespro/hunspell_dicts): Portuguese Hunspell Dictionary
>
> https://github.com/postgrespro/hunspell_dicts





[FTS](/fts) extensions: [`pg_search`](/pg_search), [`pg_bigm`](/pg_bigm), [`zhparser`](/zhparser), [`hunspell_cs_cz`](/hunspell_cs_cz), [`hunspell_de_de`](/hunspell_de_de), [`hunspell_en_us`](/hunspell_en_us), [`hunspell_fr`](/hunspell_fr), [`hunspell_ne_np`](/hunspell_ne_np), [`hunspell_nl_nl`](/hunspell_nl_nl), [`hunspell_nn_no`](/hunspell_nn_no), [`hunspell_pt_pt`](/hunspell_pt_pt), [`hunspell_ru_ru`](/hunspell_ru_ru), [`hunspell_ru_ru_aot`](/hunspell_ru_ru_aot), [`fuzzystrmatch`](/fuzzystrmatch), [`pg_trgm`](/pg_trgm)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [hunspell_pt_pt](https://github.com/postgrespro/hunspell_dicts) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Data` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [hunspell_pt_pt](/hunspell_pt_pt) | `broken` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION hunspell_pt_pt;
```
> **Comment**: WARNING, conflict with pg built-in dict file, not recommended
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `hunspell_pt_pt_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-hunspell-pt-pt` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `hunspell_pt_pt` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["hunspell_pt_pt"]}'
```


Install `hunspell_pt_pt` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install hunspell_pt_pt_17;
yum install hunspell_pt_pt_16;
yum install hunspell_pt_pt_15;
yum install hunspell_pt_pt_14;
yum install hunspell_pt_pt_13;
yum install hunspell_pt_pt_12;
```


Install `hunspell_pt_pt` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-hunspell-pt-pt;
apt install postgresql-16-hunspell-pt-pt;
apt install postgresql-15-hunspell-pt-pt;
apt install postgresql-14-hunspell-pt-pt;
apt install postgresql-13-hunspell-pt-pt;
apt install postgresql-12-hunspell-pt-pt;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `hunspell_pt_pt_17` | `hunspell_pt_pt_16` | `hunspell_pt_pt_15` | `hunspell_pt_pt_14` | `hunspell_pt_pt_13` | `hunspell_pt_pt_12` |
| `el9` | `hunspell_pt_pt_17` | `hunspell_pt_pt_16` | `hunspell_pt_pt_15` | `hunspell_pt_pt_14` | `hunspell_pt_pt_13` | `hunspell_pt_pt_12` |
| `d12` | `postgresql-17-hunspell-pt-pt` | `postgresql-16-hunspell-pt-pt` | `postgresql-15-hunspell-pt-pt` | `postgresql-14-hunspell-pt-pt` | `postgresql-13-hunspell-pt-pt` | `postgresql-12-hunspell-pt-pt` |
| `u22` | `postgresql-17-hunspell-pt-pt` | `postgresql-16-hunspell-pt-pt` | `postgresql-15-hunspell-pt-pt` | `postgresql-14-hunspell-pt-pt` | `postgresql-13-hunspell-pt-pt` | `postgresql-12-hunspell-pt-pt` |
| `u24` | `postgresql-17-hunspell-pt-pt` | `postgresql-16-hunspell-pt-pt` | `postgresql-15-hunspell-pt-pt` | `postgresql-14-hunspell-pt-pt` | `postgresql-13-hunspell-pt-pt` | `postgresql-12-hunspell-pt-pt` |






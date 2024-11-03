# hunspell_ru_ru_aot


> [hunspell_ru_ru_aot](https://github.com/postgrespro/hunspell_dicts): Russian Hunspell Dictionary (from AOT.ru group)
>
> https://github.com/postgrespro/hunspell_dicts





[FTS](/fts) extensions: [`pg_search`](/pg_search), [`pg_bigm`](/pg_bigm), [`zhparser`](/zhparser), [`hunspell_cs_cz`](/hunspell_cs_cz), [`hunspell_de_de`](/hunspell_de_de), [`hunspell_en_us`](/hunspell_en_us), [`hunspell_fr`](/hunspell_fr), [`hunspell_ne_np`](/hunspell_ne_np), [`hunspell_nl_nl`](/hunspell_nl_nl), [`hunspell_nn_no`](/hunspell_nn_no), [`hunspell_pt_pt`](/hunspell_pt_pt), [`hunspell_ru_ru`](/hunspell_ru_ru), [`hunspell_ru_ru_aot`](/hunspell_ru_ru_aot), [`fuzzystrmatch`](/fuzzystrmatch), [`pg_trgm`](/pg_trgm)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [hunspell_ru_ru_aot](https://github.com/postgrespro/hunspell_dicts) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Data` |  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Package | Tags | Schemas | Requires | Required by |
|---------|------|---------|----------|-------------|
| [hunspell_ru_ru_aot](/hunspell_ru_ru_aot) |  |  |  |  |





```sql
CREATE EXTENSION hunspell_ru_ru_aot;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `hunspell_ru_ru_aot_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-hunspell-ru-ru-aot` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `hunspell_ru_ru_aot` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

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








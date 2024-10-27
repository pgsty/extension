# FTS


> FTS: ElasticSearch Alternative with BM25, 2-gram/3-gram Fuzzy Search, Zhparser & Hunspell Segregation Dicts, etc...
## Extensions


There are 15 available extensions in this category:

[`pg_search`](/pg_search) [`pg_bigm`](/pg_bigm) [`zhparser`](/zhparser) [`hunspell_cs_cz`](/hunspell_cs_cz) [`hunspell_de_de`](/hunspell_de_de) [`hunspell_en_us`](/hunspell_en_us) [`hunspell_fr`](/hunspell_fr) [`hunspell_ne_np`](/hunspell_ne_np) [`hunspell_nl_nl`](/hunspell_nl_nl) [`hunspell_nn_no`](/hunspell_nn_no) [`hunspell_pt_pt`](/hunspell_pt_pt) [`hunspell_ru_ru`](/hunspell_ru_ru) [`hunspell_ru_ru_aot`](/hunspell_ru_ru_aot) [`fuzzystrmatch`](/fuzzystrmatch) [`pg_trgm`](/pg_trgm)


| ID | Extension | Version | Package | License | RPM | DEB | Website | `LOAD` | `DYLIB` | `DDL` | Description |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:-------:|:------:|:-------:|:-----:|-------------|
| 1300 | [pg_search](/pg_search) | 0.11.1 | [pg_search](/pg_search) | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/paradedb/paradedb/tree/dev/pg_search) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | pg_search: Full text search for PostgreSQL using BM25 |
| 1310 | [pg_bigm](/pg_bigm) | 1.2 | [pg_bigm](/pg_bigm) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/pgbigm/pg_bigm) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | create 2-gram (bigram) index for faster full text search. |
| 1320 | [zhparser](/zhparser) | 2.2 | [zhparser](/zhparser) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/amutu/zhparser) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | a parser for full-text search of Chinese |
| 1330 | [hunspell_cs_cz](/hunspell_cs_cz) | 1.0 | [hunspell_cs_cz](/hunspell_cs_cz) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/postgrespro/hunspell_dicts) |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | Czech Hunspell Dictionary |
| 1331 | [hunspell_de_de](/hunspell_de_de) | 1.0 | [hunspell_de_de](/hunspell_de_de) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/postgrespro/hunspell_dicts) |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | German Hunspell Dictionary |
| 1332 | [hunspell_en_us](/hunspell_en_us) | 1.0 | [hunspell_en_us](/hunspell_en_us) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/postgrespro/hunspell_dicts) |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | en_US Hunspell Dictionary |
| 1333 | [hunspell_fr](/hunspell_fr) | 1.0 | [hunspell_fr](/hunspell_fr) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/postgrespro/hunspell_dicts) |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | French Hunspell Dictionary |
| 1334 | [hunspell_ne_np](/hunspell_ne_np) | 1.0 | [hunspell_ne_np](/hunspell_ne_np) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/postgrespro/hunspell_dicts) |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | Nepali Hunspell Dictionary |
| 1335 | [hunspell_nl_nl](/hunspell_nl_nl) | 1.0 | [hunspell_nl_nl](/hunspell_nl_nl) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/postgrespro/hunspell_dicts) |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | Dutch Hunspell Dictionary |
| 1336 | [hunspell_nn_no](/hunspell_nn_no) | 1.0 | [hunspell_nn_no](/hunspell_nn_no) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/postgrespro/hunspell_dicts) |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | Norwegian (norsk) Hunspell Dictionary |
| 1337 | [hunspell_pt_pt](/hunspell_pt_pt) | 1.0 | [hunspell_pt_pt](/hunspell_pt_pt) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/postgrespro/hunspell_dicts) |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | Portuguese Hunspell Dictionary |
| 1338 | [hunspell_ru_ru](/hunspell_ru_ru) | 1.0 | [hunspell_ru_ru](/hunspell_ru_ru) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/postgrespro/hunspell_dicts) |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | Russian Hunspell Dictionary |
| 1339 | [hunspell_ru_ru_aot](/hunspell_ru_ru_aot) | 1.0 | [hunspell_ru_ru_aot](/hunspell_ru_ru_aot) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/postgrespro/hunspell_dicts) |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | Russian Hunspell Dictionary (from AOT.ru group) |
| 1380 | [fuzzystrmatch](/fuzzystrmatch) | 1.2 | [fuzzystrmatch](/fuzzystrmatch) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | **<span class="tcblue">CONTRIB</span>** | [LINK](https://www.postgresql.org/docs/current/fuzzystrmatch.html) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | determine similarities and distance between strings |
| 1390 | [pg_trgm](/pg_trgm) | 1.6 | [pg_trgm](/pg_trgm) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | **<span class="tcblue">CONTRIB</span>** | [LINK](https://www.postgresql.org/docs/current/pgtrgm.html) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | text similarity measurement and index searching based on trigrams |



```yaml
pg17: pg_search pg_bigm zhparser hunspell_cs_cz hunspell_de_de hunspell_en_us hunspell_fr hunspell_ne_np hunspell_nl_nl hunspell_nn_no hunspell_pt_pt hunspell_ru_ru hunspell_ru_ru_aot 
pg16: pg_search pg_bigm zhparser hunspell_cs_cz hunspell_de_de hunspell_en_us hunspell_fr hunspell_ne_np hunspell_nl_nl hunspell_nn_no hunspell_pt_pt hunspell_ru_ru hunspell_ru_ru_aot 
pg15: pg_search pg_bigm zhparser hunspell_cs_cz hunspell_de_de hunspell_en_us hunspell_fr hunspell_ne_np hunspell_nl_nl hunspell_nn_no hunspell_pt_pt hunspell_ru_ru hunspell_ru_ru_aot 
pg14: pg_search pg_bigm zhparser hunspell_cs_cz hunspell_de_de hunspell_en_us hunspell_fr hunspell_ne_np hunspell_nl_nl hunspell_nn_no hunspell_pt_pt hunspell_ru_ru hunspell_ru_ru_aot 
pg13: pg_bigm zhparser hunspell_cs_cz hunspell_de_de hunspell_en_us hunspell_fr hunspell_ne_np hunspell_nl_nl hunspell_nn_no hunspell_pt_pt hunspell_ru_ru hunspell_ru_ru_aot #pg_search
pg12: pg_bigm zhparser hunspell_cs_cz hunspell_de_de hunspell_en_us hunspell_fr hunspell_ne_np hunspell_nl_nl hunspell_nn_no hunspell_pt_pt hunspell_ru_ru hunspell_ru_ru_aot #pg_search
```



--------

## RPM Packages


| Package | Version | License | RPM | RPM Package | 17 | 16 | 15 | 14 | 13 | 12 | Description |
|---------|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|:--:|-------------|
| [pg_search](/pg_search) | 0.11.1 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_search_$v` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |  | pg_search: Full text search for PostgreSQL using BM25 |
| [pg_bigm](/pg_bigm) | 1.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pg_bigm_$v*` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | create 2-gram (bigram) index for faster full text search. |
| [zhparser](/zhparser) | 2.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `zhparser_$v*` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | a parser for full-text search of Chinese |
| [hunspell_cs_cz](/hunspell_cs_cz) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `hunspell_cs_cz_$v` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Czech Hunspell Dictionary |
| [hunspell_de_de](/hunspell_de_de) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `hunspell_de_de_$v` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | German Hunspell Dictionary |
| [hunspell_en_us](/hunspell_en_us) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `hunspell_en_us_$v` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | en_US Hunspell Dictionary |
| [hunspell_fr](/hunspell_fr) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `hunspell_fr_$v` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | French Hunspell Dictionary |
| [hunspell_ne_np](/hunspell_ne_np) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `hunspell_ne_np_$v` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Nepali Hunspell Dictionary |
| [hunspell_nl_nl](/hunspell_nl_nl) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `hunspell_nl_nl_$v` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Dutch Hunspell Dictionary |
| [hunspell_nn_no](/hunspell_nn_no) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `hunspell_nn_no_$v` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Norwegian (norsk) Hunspell Dictionary |
| [hunspell_pt_pt](/hunspell_pt_pt) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `hunspell_pt_pt_$v` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Portuguese Hunspell Dictionary |
| [hunspell_ru_ru](/hunspell_ru_ru) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `hunspell_ru_ru_$v` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Russian Hunspell Dictionary |
| [hunspell_ru_ru_aot](/hunspell_ru_ru_aot) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `hunspell_ru_ru_aot_$v` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Russian Hunspell Dictionary (from AOT.ru group) |
| [fuzzystrmatch](/fuzzystrmatch) | 1.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql$v-contrib` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | determine similarities and distance between strings |
| [pg_trgm](/pg_trgm) | 1.6 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql$v-contrib` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | text similarity measurement and index searching based on trigrams |



```yaml
pg17: pg_search_17 pg_bigm_17* zhparser_17* hunspell_cs_cz_17 hunspell_de_de_17 hunspell_en_us_17 hunspell_fr_17 hunspell_ne_np_17 hunspell_nl_nl_17 hunspell_nn_no_17 hunspell_pt_pt_17 hunspell_ru_ru_17 hunspell_ru_ru_aot_17 
pg16: pg_search_16 pg_bigm_16* zhparser_16* hunspell_cs_cz_16 hunspell_de_de_16 hunspell_en_us_16 hunspell_fr_16 hunspell_ne_np_16 hunspell_nl_nl_16 hunspell_nn_no_16 hunspell_pt_pt_16 hunspell_ru_ru_16 hunspell_ru_ru_aot_16 
pg15: pg_search_15 pg_bigm_15* zhparser_15* hunspell_cs_cz_15 hunspell_de_de_15 hunspell_en_us_15 hunspell_fr_15 hunspell_ne_np_15 hunspell_nl_nl_15 hunspell_nn_no_15 hunspell_pt_pt_15 hunspell_ru_ru_15 hunspell_ru_ru_aot_15 
pg14: pg_search_14 pg_bigm_14* zhparser_14* hunspell_cs_cz_14 hunspell_de_de_14 hunspell_en_us_14 hunspell_fr_14 hunspell_ne_np_14 hunspell_nl_nl_14 hunspell_nn_no_14 hunspell_pt_pt_14 hunspell_ru_ru_14 hunspell_ru_ru_aot_14 
pg13: pg_bigm_13* zhparser_13* hunspell_cs_cz_13 hunspell_de_de_13 hunspell_en_us_13 hunspell_fr_13 hunspell_ne_np_13 hunspell_nl_nl_13 hunspell_nn_no_13 hunspell_pt_pt_13 hunspell_ru_ru_13 hunspell_ru_ru_aot_13 #pg_search_13
pg12: pg_bigm_12* zhparser_12* hunspell_cs_cz_12 hunspell_de_de_12 hunspell_en_us_12 hunspell_fr_12 hunspell_ne_np_12 hunspell_nl_nl_12 hunspell_nn_no_12 hunspell_pt_pt_12 hunspell_ru_ru_12 hunspell_ru_ru_aot_12 #pg_search_12
```



--------

## DEB Packages


| Package | Version | License | DEB | DEB Package | 17 | 16 | 15 | 14 | 13 | 12 | Description |
|---------|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|:--:|-------------|
| [pg_search](/pg_search) | 0.11.1 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-search` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |  | pg_search: Full text search for PostgreSQL using BM25 |
| [pg_bigm](/pg_bigm) | 1.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-bigm` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | create 2-gram (bigram) index for faster full text search. |
| [zhparser](/zhparser) | 2.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-zhparser` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | a parser for full-text search of Chinese |
| [hunspell_cs_cz](/hunspell_cs_cz) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-hunspell-cs-cz` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Czech Hunspell Dictionary |
| [hunspell_de_de](/hunspell_de_de) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-hunspell-de-de` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | German Hunspell Dictionary |
| [hunspell_en_us](/hunspell_en_us) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-hunspell-en-us` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | en_US Hunspell Dictionary |
| [hunspell_fr](/hunspell_fr) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-hunspell-fr` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | French Hunspell Dictionary |
| [hunspell_ne_np](/hunspell_ne_np) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-hunspell-ne-np` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Nepali Hunspell Dictionary |
| [hunspell_nl_nl](/hunspell_nl_nl) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-hunspell-nl-nl` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Dutch Hunspell Dictionary |
| [hunspell_nn_no](/hunspell_nn_no) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-hunspell-nn-no` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Norwegian (norsk) Hunspell Dictionary |
| [hunspell_pt_pt](/hunspell_pt_pt) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-hunspell-pt-pt` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Portuguese Hunspell Dictionary |
| [hunspell_ru_ru](/hunspell_ru_ru) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-hunspell-ru-ru` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Russian Hunspell Dictionary |
| [hunspell_ru_ru_aot](/hunspell_ru_ru_aot) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-hunspell-ru-ru-aot` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Russian Hunspell Dictionary (from AOT.ru group) |
| [fuzzystrmatch](/fuzzystrmatch) | 1.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql-$v` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | determine similarities and distance between strings |
| [pg_trgm](/pg_trgm) | 1.6 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql-$v` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | text similarity measurement and index searching based on trigrams |



```yaml
pg17: pg_search_17 pg_bigm_17* zhparser_17* hunspell_cs_cz_17 hunspell_de_de_17 hunspell_en_us_17 hunspell_fr_17 hunspell_ne_np_17 hunspell_nl_nl_17 hunspell_nn_no_17 hunspell_pt_pt_17 hunspell_ru_ru_17 hunspell_ru_ru_aot_17 
pg16: pg_search_16 pg_bigm_16* zhparser_16* hunspell_cs_cz_16 hunspell_de_de_16 hunspell_en_us_16 hunspell_fr_16 hunspell_ne_np_16 hunspell_nl_nl_16 hunspell_nn_no_16 hunspell_pt_pt_16 hunspell_ru_ru_16 hunspell_ru_ru_aot_16 
pg15: pg_search_15 pg_bigm_15* zhparser_15* hunspell_cs_cz_15 hunspell_de_de_15 hunspell_en_us_15 hunspell_fr_15 hunspell_ne_np_15 hunspell_nl_nl_15 hunspell_nn_no_15 hunspell_pt_pt_15 hunspell_ru_ru_15 hunspell_ru_ru_aot_15 
pg14: pg_search_14 pg_bigm_14* zhparser_14* hunspell_cs_cz_14 hunspell_de_de_14 hunspell_en_us_14 hunspell_fr_14 hunspell_ne_np_14 hunspell_nl_nl_14 hunspell_nn_no_14 hunspell_pt_pt_14 hunspell_ru_ru_14 hunspell_ru_ru_aot_14 
pg13: pg_bigm_13* zhparser_13* hunspell_cs_cz_13 hunspell_de_de_13 hunspell_en_us_13 hunspell_fr_13 hunspell_ne_np_13 hunspell_nl_nl_13 hunspell_nn_no_13 hunspell_pt_pt_13 hunspell_ru_ru_13 hunspell_ru_ru_aot_13 #pg_search_13
pg12: pg_bigm_12* zhparser_12* hunspell_cs_cz_12 hunspell_de_de_12 hunspell_en_us_12 hunspell_fr_12 hunspell_ne_np_12 hunspell_nl_nl_12 hunspell_nn_no_12 hunspell_pt_pt_12 hunspell_ru_ru_12 hunspell_ru_ru_aot_12 #pg_search_12
```



--------

## pg_search

[`pg_search`](/pg_search): pg_search: Full text search for PostgreSQL using BM25

## pg_bigm

[`pg_bigm`](/pg_bigm): create 2-gram (bigram) index for faster full text search.

## zhparser

[`zhparser`](/zhparser): a parser for full-text search of Chinese

## hunspell_cs_cz

[`hunspell_cs_cz`](/hunspell_cs_cz): Czech Hunspell Dictionary

## hunspell_de_de

[`hunspell_de_de`](/hunspell_de_de): German Hunspell Dictionary

## hunspell_en_us

[`hunspell_en_us`](/hunspell_en_us): en_US Hunspell Dictionary

## hunspell_fr

[`hunspell_fr`](/hunspell_fr): French Hunspell Dictionary

## hunspell_ne_np

[`hunspell_ne_np`](/hunspell_ne_np): Nepali Hunspell Dictionary

## hunspell_nl_nl

[`hunspell_nl_nl`](/hunspell_nl_nl): Dutch Hunspell Dictionary

## hunspell_nn_no

[`hunspell_nn_no`](/hunspell_nn_no): Norwegian (norsk) Hunspell Dictionary

## hunspell_pt_pt

[`hunspell_pt_pt`](/hunspell_pt_pt): Portuguese Hunspell Dictionary

## hunspell_ru_ru

[`hunspell_ru_ru`](/hunspell_ru_ru): Russian Hunspell Dictionary

## hunspell_ru_ru_aot

[`hunspell_ru_ru_aot`](/hunspell_ru_ru_aot): Russian Hunspell Dictionary (from AOT.ru group)

## fuzzystrmatch

[`fuzzystrmatch`](/fuzzystrmatch): determine similarities and distance between strings

## pg_trgm

[`pg_trgm`](/pg_trgm): text similarity measurement and index searching based on trigrams

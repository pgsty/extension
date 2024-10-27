# pg_vectorize


> [pg_vectorize](/https://github.com/tembo-io/pg_vectorize): The simplest way to do vector search on Postgres


-------

## Extension


| ID | Extension | Version | License | RPM | DEB | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:--:|-----------|:-------:|:-------:|:---:|:---:|:------:|:-------:|:-----:|:-------:|:-------:|
| 1220 | [vectorize](https://github.com/tembo-io/pg_vectorize) | 0.18.3 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |





```sql
CREATE EXTENSION vectorize CASCADE;
```

- **Requires**: [`pg_cron`](pg_cron), [`pgmq`](pgmq), [`vector`](vector)

-----------


## Packages


| OS | Version | License | RPM | RPM Package | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.18.3 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_vectorize_$v` |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |  |  |
| [DEB](/deb) | 0.18.3 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-vectorize` |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |  |  |



Install `pg_vectorize` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_vectorize"]}'
```


Install `pg_vectorize` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_vectorize_16;
dnf install pg_vectorize_15;
dnf install pg_vectorize_14;
```


Install `pg_vectorize` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-16-pg-vectorize;
apt install postgresql-15-pg-vectorize;
apt install postgresql-14-pg-vectorize;
```


-----------


## Category: RAG


| ID | Extension | Version | Package | License | RPM | DEB | PL | Tags | Schemas | Requires | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:--:|------|---------|----------|:------:|:-------:|:-----:|:-------:|:-------:|
| 1200 | [vector](/vector) | 0.7.4 | [pgvector](/vector) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1210 | [vectorscale](/vectorscale) | 0.4.0 | [pgvectorscale](/vectorscale) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` | `pgrx` |  | [`vector`](vector) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1220 | [vectorize](/vectorize) | 0.18.3 | [pg_vectorize](/vectorize) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` | `pgrx` | `vectorize` | [`pg_cron`](pg_cron), [`pgmq`](pgmq), [`vector`](vector) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1230 | [pg_similarity](/pg_similarity) | 1.0 | [pg_similarity](/pg_similarity) | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1240 | [smlar](/smlar) | 1.0 | [smlar](/smlar) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` | `nil-lic` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |
| 1250 | [pg_summarize](/pg_summarize) | 0.0.0 | [pg_summarize](/pg_summarize) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` | `pgrx` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1260 | [pg_tiktoken](/pg_tiktoken) | 0.0.1 | [pg_tiktoken](/pg_tiktoken) | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` | `pgrx` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1270 | [pgml](/pgml) | 2.9.3 | [pgml](/pgml) | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` | `pgrx` | `pgml` |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1280 | [pg4ml](/pg4ml) | 2.0 | [pg4ml](/pg4ml) | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` |  |  | [`plpgsql`](plpgsql), [`tablefunc`](tablefunc), [`cube`](cube), [`plpython3u`](plpython3u) |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |




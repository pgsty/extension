# pgvectorscale


> [pgvectorscale](/https://github.com/timescale/pgvectorscale): pgvectorscale:  Advanced indexing for vector data


-------

## Extension


| ID | Extension | Version | License | RPM | DEB | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` | Requires |
|:--:|-----------|:-------:|:-------:|:---:|:---:|:------:|:-------:|:-----:|:-------:|:-------:|----------|
| 1210 | [vectorscale](https://github.com/timescale/pgvectorscale) | 0.4.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> | [`vector`](/rag/vector) |





```sql
CREATE EXTENSION vectorscaleCASCADE;
```


-----------


## Packages


| OS | Version | License | RPM | RPM Package | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.4.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pgvectorscale_$v` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |  |
| [DEB](/deb) | 0.4.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pgvectorscale` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |  |



Install `pgvectorscale` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pgvectorscale_17;
dnf install pgvectorscale_16;
dnf install pgvectorscale_15;
dnf install pgvectorscale_14;
dnf install pgvectorscale_13;
```


Install `pgvectorscale` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pgvectorscale;
apt install postgresql-16-pgvectorscale;
apt install postgresql-15-pgvectorscale;
apt install postgresql-14-pgvectorscale;
apt install postgresql-13-pgvectorscale;
```


-----------


## Category: RAG


| ID | Extension | Version | Package | License | RPM | DEB | lang | Tags | Schemas | Requires | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:----:|------|---------|----------|:------:|:-------:|:-----:|:-------:|:-------:|
| 1200 | [vector](/rag/vector) | 0.7.4 | [pgvector](/rag/vector) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1210 | [vectorscale](/rag/vectorscale) | 0.4.0 | [pgvectorscale](/rag/vectorscale) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | Rust | `pgrx` |  | [`vector`](/rag/vector) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1220 | [vectorize](/rag/vectorize) | 0.18.3 | [pg_vectorize](/rag/vectorize) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | Rust | `pgrx` | `vectorize` | [`pg_cron`](/time/pg_cron), [`pgmq`](/feat/pgmq), [`vector`](/rag/vector) |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1230 | [pg_similarity](/rag/pg_similarity) | 1.0 | [pg_similarity](/rag/pg_similarity) | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1240 | [smlar](/rag/smlar) | 1.0 | [smlar](/rag/smlar) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | C | `nil-lic` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |
| 1250 | [pg_summarize](/rag/pg_summarize) | 0.0.0 | [pg_summarize](/rag/pg_summarize) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | Rust | `pgrx` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1260 | [pg_tiktoken](/rag/pg_tiktoken) | 0.0.1 | [pg_tiktoken](/rag/pg_tiktoken) | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | Rust | `pgrx` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1270 | [pgml](/rag/pgml) | 2.9.3 | [pgml](/rag/pgml) | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | Rust | `pgrx` | `pgml` |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1280 | [pg4ml](/rag/pg4ml) | 2.0 | [pg4ml](/rag/pg4ml) | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | SQL |  |  | [`plpgsql`](/lang/plpgsql), [`tablefunc`](/olap/tablefunc), [`cube`](/type/cube), [`plpython3u`](/lang/plpython3u) |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |




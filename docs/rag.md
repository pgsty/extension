# RAG


> RAG: Vector Database with IVFFLAT, HNSW, DiskANN Indexes, AI & ML in SQL interface, Similarity Funcs, etc... 
## Extensions


There are 10 available extensions in this category:

[`vector`](/vector) [`vchord`](/vchord) [`vectorscale`](/vectorscale) [`vectorize`](/vectorize) [`pg_similarity`](/pg_similarity) [`smlar`](/smlar) [`pg_summarize`](/pg_summarize) [`pg_tiktoken`](/pg_tiktoken) [`pg4ml`](/pg4ml) [`pgml`](/pgml)


| ID | Extension | Version | Package | License | RPM | DEB | Website | `Bin` | `LOAD` | `DYLIB` | `DDL` | Description |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:-------:|:-----:|:------:|:-------:|:-----:|-------------|
| 1200 | [vector](/vector) | 0.8.0 | [pgvector](/vector) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/pgvector/pgvector) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | vector data type and ivfflat and hnsw access methods |
| 1210 | [vchord](/vchord) | 0.1.0 | [vchord](/vchord) | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/tensorchord/VectorChord) |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Vector database plugin for Postgres, written in Rust |
| 1220 | [vectorscale](/vectorscale) | 0.5.1 | [pgvectorscale](/vectorscale) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/timescale/pgvectorscale) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | pgvectorscale:  Advanced indexing for vector data |
| 1230 | [vectorize](/vectorize) | 0.20.0 | [pg_vectorize](/vectorize) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/tembo-io/pg_vectorize) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | The simplest way to do vector search on Postgres |
| 1240 | [pg_similarity](/pg_similarity) | 1.0 | [pg_similarity](/pg_similarity) | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/eulerto/pg_similarity) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | support similarity queries |
| 1250 | [smlar](/smlar) | 1.0 | [smlar](/smlar) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/jirutka/smlar) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Effective similarity search |
| 1260 | [pg_summarize](/pg_summarize) | 0.0.0 | [pg_summarize](/pg_summarize) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/HexaCluster/pg_summarize) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Text Summarization using LLMs. Built using pgrx |
| 1270 | [pg_tiktoken](/pg_tiktoken) | 0.0.1 | [pg_tiktoken](/pg_tiktoken) | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/kelvich/pg_tiktoken) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | pg_tictoken: tiktoken tokenizer for use with OpenAI models in postgres |
| 1280 | [pg4ml](/pg4ml) | 2.0 | [pg4ml](/pg4ml) | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://gitee.com/guotiecheng/plpgsql_pg4ml) |  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | Machine learning framework for PostgreSQL |
| 1290 | [pgml](/pgml) | 2.9.3 | [pgml](/pgml) | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/postgresml/postgresml) |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | PostgresML: Run AL/ML workloads with SQL interface |



### RHEL 8 Compatible (el8)

```yaml
pg17: pgvector vchord pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pg4ml #pgml
pg16: pgvector vchord pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pg4ml pgml
pg15: pgvector vchord pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pg4ml pgml
pg14: pgvector vchord pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pg4ml pgml
pg13: pgvector pgvectorscale pg_similarity smlar pg_summarize pg_tiktoken pg4ml #vchord #pg_vectorize #pgml
```


### RHEL 9 Compatible (el9)

```yaml
pg17: pgvector vchord pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pg4ml #pgml
pg16: pgvector vchord pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pg4ml pgml
pg15: pgvector vchord pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pg4ml pgml
pg14: pgvector vchord pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pg4ml pgml
pg13: pgvector pgvectorscale pg_similarity smlar pg_summarize pg_tiktoken pg4ml #vchord #pg_vectorize #pgml
```


### Debian 12 bookworm Compatible (d12)

```yaml
pg17: pgvector vchord pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pg4ml #pgml
pg16: pgvector vchord pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pg4ml pgml
pg15: pgvector vchord pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pg4ml pgml
pg14: pgvector vchord pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pg4ml pgml
pg13: pgvector pgvectorscale pg_similarity smlar pg_summarize pg_tiktoken pg4ml #vchord #pg_vectorize #pgml
```


### Ubuntu 24.04 jammy Compatible (u22)

```yaml
pg17: pgvector vchord pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pg4ml #pgml
pg16: pgvector vchord pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pg4ml pgml
pg15: pgvector vchord pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pg4ml pgml
pg14: pgvector vchord pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pg4ml pgml
pg13: pgvector pgvectorscale pg_similarity smlar pg_summarize pg_tiktoken pg4ml #vchord #pg_vectorize #pgml
```


### Ubuntu 24.04 noble Compatible (u24)

```yaml
pg17: pgvector vchord pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pg4ml #pgml
pg16: pgvector vchord pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pg4ml #pgml
pg15: pgvector vchord pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pg4ml #pgml
pg14: pgvector vchord pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pg4ml #pgml
pg13: pgvector pgvectorscale pg_similarity smlar pg_summarize pg_tiktoken pg4ml #vchord #pg_vectorize #pgml
```



--------

## RPM Packages


| Package | Version | License | RPM | RPM Package | 17 | 16 | 15 | 14 | 13 | Description |
|---------|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|-------------|
| [pgvector](/vector) | 0.8.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pgvector_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | vector data type and ivfflat and hnsw access methods |
| [vchord](/vchord) | 0.1.0 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `vchord_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | Vector database plugin for Postgres, written in Rust |
| [pgvectorscale](/vectorscale) | 0.5.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pgvectorscale_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | pgvectorscale:  Advanced indexing for vector data |
| [pg_vectorize](/vectorize) | 0.20.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_vectorize_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | The simplest way to do vector search on Postgres |
| [pg_similarity](/pg_similarity) | 1.0 | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_similarity_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | support similarity queries |
| [smlar](/smlar) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `smlar_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Effective similarity search |
| [pg_summarize](/pg_summarize) | 0.0.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_summarize_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Text Summarization using LLMs. Built using pgrx |
| [pg_tiktoken](/pg_tiktoken) | 0.0.1 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_tiktoken_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | pg_tictoken: tiktoken tokenizer for use with OpenAI models in postgres |
| [pg4ml](/pg4ml) | 2.0 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg4ml_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Machine learning framework for PostgreSQL |
| [pgml](/pgml) | 2.9.3 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `pgml_$v` |  | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | PostgresML: Run AL/ML workloads with SQL interface |



### RHEL 8 Compatible (el8)

```yaml
pg17: pgvector_17* vchord_17 pgvectorscale_17 pg_vectorize_17 pg_similarity_17* smlar_17* pg_summarize_17 pg_tiktoken_17 pg4ml_17 #pgml_17
pg16: pgvector_16* vchord_16 pgvectorscale_16 pg_vectorize_16 pg_similarity_16* smlar_16* pg_summarize_16 pg_tiktoken_16 pg4ml_16 pgml_16
pg15: pgvector_15* vchord_15 pgvectorscale_15 pg_vectorize_15 pg_similarity_15* smlar_15* pg_summarize_15 pg_tiktoken_15 pg4ml_15 pgml_15
pg14: pgvector_14* vchord_14 pgvectorscale_14 pg_vectorize_14 pg_similarity_14* smlar_14* pg_summarize_14 pg_tiktoken_14 pg4ml_14 pgml_14
pg13: pgvector_13* pgvectorscale_13 pg_similarity_13* smlar_13* pg_summarize_13 pg_tiktoken_13 pg4ml_13 #vchord_13 #pg_vectorize_13 #pgml_13
```


### RHEL 9 Compatible (el9)

```yaml
pg17: pgvector_17* vchord_17 pgvectorscale_17 pg_vectorize_17 pg_similarity_17* smlar_17* pg_summarize_17 pg_tiktoken_17 pg4ml_17 #pgml_17
pg16: pgvector_16* vchord_16 pgvectorscale_16 pg_vectorize_16 pg_similarity_16* smlar_16* pg_summarize_16 pg_tiktoken_16 pg4ml_16 pgml_16
pg15: pgvector_15* vchord_15 pgvectorscale_15 pg_vectorize_15 pg_similarity_15* smlar_15* pg_summarize_15 pg_tiktoken_15 pg4ml_15 pgml_15
pg14: pgvector_14* vchord_14 pgvectorscale_14 pg_vectorize_14 pg_similarity_14* smlar_14* pg_summarize_14 pg_tiktoken_14 pg4ml_14 pgml_14
pg13: pgvector_13* pgvectorscale_13 pg_similarity_13* smlar_13* pg_summarize_13 pg_tiktoken_13 pg4ml_13 #vchord_13 #pg_vectorize_13 #pgml_13
```



--------

## DEB Packages


| Package | Version | License | DEB | DEB Package | 17 | 16 | 15 | 14 | 13 | Description |
|---------|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|-------------|
| [pgvector](/vector) | 0.8.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pgvector` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | vector data type and ivfflat and hnsw access methods |
| [vchord](/vchord) | 0.1.0 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-vchord` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | Vector database plugin for Postgres, written in Rust |
| [pgvectorscale](/vectorscale) | 0.5.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pgvectorscale` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | pgvectorscale:  Advanced indexing for vector data |
| [pg_vectorize](/vectorize) | 0.20.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-vectorize` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | The simplest way to do vector search on Postgres |
| [pg_similarity](/pg_similarity) | 1.0 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-similarity` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | support similarity queries |
| [smlar](/smlar) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-smlar` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Effective similarity search |
| [pg_summarize](/pg_summarize) | 0.0.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-summarize` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Text Summarization using LLMs. Built using pgrx |
| [pg_tiktoken](/pg_tiktoken) | 0.0.1 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-tiktoken` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | pg_tictoken: tiktoken tokenizer for use with OpenAI models in postgres |
| [pg4ml](/pg4ml) | 2.0 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg4ml` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Machine learning framework for PostgreSQL |
| [pgml](/pgml) | 2.9.2 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pgml` |  | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | PostgresML: Run AL/ML workloads with SQL interface |



### Debian 12 bookworm Compatible (d12)

```yaml
pg17: postgresql-17-pgvector postgresql-17-vchord postgresql-17-pgvectorscale postgresql-17-pg-vectorize postgresql-17-similarity postgresql-17-smlar postgresql-17-pg-summarize postgresql-17-pg-tiktoken postgresql-17-pg4ml #postgresql-17-pgml
pg16: postgresql-16-pgvector postgresql-16-vchord postgresql-16-pgvectorscale postgresql-16-pg-vectorize postgresql-16-similarity postgresql-16-smlar postgresql-16-pg-summarize postgresql-16-pg-tiktoken postgresql-16-pg4ml postgresql-16-pgml
pg15: postgresql-15-pgvector postgresql-15-vchord postgresql-15-pgvectorscale postgresql-15-pg-vectorize postgresql-15-similarity postgresql-15-smlar postgresql-15-pg-summarize postgresql-15-pg-tiktoken postgresql-15-pg4ml postgresql-15-pgml
pg14: postgresql-14-pgvector postgresql-14-vchord postgresql-14-pgvectorscale postgresql-14-pg-vectorize postgresql-14-similarity postgresql-14-smlar postgresql-14-pg-summarize postgresql-14-pg-tiktoken postgresql-14-pg4ml postgresql-14-pgml
pg13: postgresql-13-pgvector postgresql-13-pgvectorscale postgresql-13-similarity postgresql-13-smlar postgresql-13-pg-summarize postgresql-13-pg-tiktoken postgresql-13-pg4ml #postgresql-13-vchord #postgresql-13-pg-vectorize #postgresql-13-pgml
```


### Ubuntu 24.04 jammy Compatible (u22)

```yaml
pg17: postgresql-17-pgvector postgresql-17-vchord postgresql-17-pgvectorscale postgresql-17-pg-vectorize postgresql-17-similarity postgresql-17-smlar postgresql-17-pg-summarize postgresql-17-pg-tiktoken postgresql-17-pg4ml #postgresql-17-pgml
pg16: postgresql-16-pgvector postgresql-16-vchord postgresql-16-pgvectorscale postgresql-16-pg-vectorize postgresql-16-similarity postgresql-16-smlar postgresql-16-pg-summarize postgresql-16-pg-tiktoken postgresql-16-pg4ml postgresql-16-pgml
pg15: postgresql-15-pgvector postgresql-15-vchord postgresql-15-pgvectorscale postgresql-15-pg-vectorize postgresql-15-similarity postgresql-15-smlar postgresql-15-pg-summarize postgresql-15-pg-tiktoken postgresql-15-pg4ml postgresql-15-pgml
pg14: postgresql-14-pgvector postgresql-14-vchord postgresql-14-pgvectorscale postgresql-14-pg-vectorize postgresql-14-similarity postgresql-14-smlar postgresql-14-pg-summarize postgresql-14-pg-tiktoken postgresql-14-pg4ml postgresql-14-pgml
pg13: postgresql-13-pgvector postgresql-13-pgvectorscale postgresql-13-similarity postgresql-13-smlar postgresql-13-pg-summarize postgresql-13-pg-tiktoken postgresql-13-pg4ml #postgresql-13-vchord #postgresql-13-pg-vectorize #postgresql-13-pgml
```


### Ubuntu 24.04 noble Compatible (u24)

```yaml
pg17: postgresql-17-pgvector postgresql-17-vchord postgresql-17-pgvectorscale postgresql-17-pg-vectorize postgresql-17-similarity postgresql-17-smlar postgresql-17-pg-summarize postgresql-17-pg-tiktoken postgresql-17-pg4ml #postgresql-17-pgml
pg16: postgresql-16-pgvector postgresql-16-vchord postgresql-16-pgvectorscale postgresql-16-pg-vectorize postgresql-16-similarity postgresql-16-smlar postgresql-16-pg-summarize postgresql-16-pg-tiktoken postgresql-16-pg4ml #postgresql-16-pgml
pg15: postgresql-15-pgvector postgresql-15-vchord postgresql-15-pgvectorscale postgresql-15-pg-vectorize postgresql-15-similarity postgresql-15-smlar postgresql-15-pg-summarize postgresql-15-pg-tiktoken postgresql-15-pg4ml #postgresql-15-pgml
pg14: postgresql-14-pgvector postgresql-14-vchord postgresql-14-pgvectorscale postgresql-14-pg-vectorize postgresql-14-similarity postgresql-14-smlar postgresql-14-pg-summarize postgresql-14-pg-tiktoken postgresql-14-pg4ml #postgresql-14-pgml
pg13: postgresql-13-pgvector postgresql-13-pgvectorscale postgresql-13-similarity postgresql-13-smlar postgresql-13-pg-summarize postgresql-13-pg-tiktoken postgresql-13-pg4ml #postgresql-13-vchord #postgresql-13-pg-vectorize #postgresql-13-pgml
```



--------

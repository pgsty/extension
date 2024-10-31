# RAG


> RAG: Vector Database with IVFFLAT, HNSW, DiskANN Indexes, AI & ML in SQL interface, Similarity Funcs, etc... 
## Extensions


There are 9 available extensions in this category:

[`vector`](/vector) [`vectorscale`](/vectorscale) [`vectorize`](/vectorize) [`pg_similarity`](/pg_similarity) [`smlar`](/smlar) [`pg_summarize`](/pg_summarize) [`pg_tiktoken`](/pg_tiktoken) [`pgml`](/pgml) [`pg4ml`](/pg4ml)


| ID | Extension | Version | Package | License | RPM | DEB | Website | `Bin` | `LOAD` | `DYLIB` | `DDL` | Description |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:-------:|:-----:|:------:|:-------:|:-----:|-------------|
| 1200 | [vector](/vector) | 0.7.4 | [pgvector](/vector) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/pgvector/pgvector) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | vector data type and ivfflat and hnsw access methods |
| 1210 | [vectorscale](/vectorscale) | 0.4.0 | [pgvectorscale](/vectorscale) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/timescale/pgvectorscale) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | pgvectorscale:  Advanced indexing for vector data |
| 1220 | [vectorize](/vectorize) | 0.20.0 | [pg_vectorize](/vectorize) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | 14} | [LINK](https://github.com/tembo-io/pg_vectorize) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | The simplest way to do vector search on Postgres |
| 1230 | [pg_similarity](/pg_similarity) | 1.0 | [pg_similarity](/pg_similarity) | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/eulerto/pg_similarity) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | support similarity queries |
| 1240 | [smlar](/smlar) | 1.0 | [smlar](/smlar) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/jirutka/smlar) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Effective similarity search |
| 1250 | [pg_summarize](/pg_summarize) | 0.0.0 | [pg_summarize](/pg_summarize) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/HexaCluster/pg_summarize) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Text Summarization using LLMs. Built using pgrx |
| 1260 | [pg_tiktoken](/pg_tiktoken) | 0.0.1 | [pg_tiktoken](/pg_tiktoken) | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/kelvich/pg_tiktoken) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | pg_tictoken: tiktoken tokenizer for use with OpenAI models in postgres |
| 1270 | [pgml](/pgml) | 2.9.3 | [pgml](/pgml) | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/postgresml/postgresml) |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | PostgresML: Run AL/ML workloads with SQL interface |
| 1280 | [pg4ml](/pg4ml) | 2.0 | [pg4ml](/pg4ml) | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://gitee.com/guotiecheng/plpgsql_pg4ml) |  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | Machine learning framework for PostgreSQL |



```yaml
pg17: pgvector pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pg4ml #pgml
pg16: pgvector pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pgml pg4ml 
pg15: pgvector pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pgml pg4ml 
pg14: pgvector pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pgml pg4ml 
pg13: pgvector pgvectorscale pg_similarity smlar pg_summarize pg_tiktoken pg4ml #pg_vectorize #pgml
pg12: pgvector pg_similarity pg_summarize pg_tiktoken pg4ml #pgvectorscale #pg_vectorize #smlar #pgml
```



--------

## RPM Packages


| Package | Version | License | RPM | RPM Package | 17 | 16 | 15 | 14 | 13 | 12 | Description |
|---------|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|:--:|-------------|
| [pgvector](/vector) | 0.7.4 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pgvector_$v*` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | vector data type and ivfflat and hnsw access methods |
| [pgvectorscale](/vectorscale) | 0.4.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pgvectorscale_$v` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | pgvectorscale:  Advanced indexing for vector data |
| [pg_vectorize](/vectorize) | 0.20.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_vectorize_$v` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |  | The simplest way to do vector search on Postgres |
| [pg_similarity](/pg_similarity) | 1.0 | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_similarity_$v*` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | support similarity queries |
| [smlar](/smlar) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `smlar_$v*` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | Effective similarity search |
| [pg_summarize](/pg_summarize) | 0.0.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_summarize_$v` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Text Summarization using LLMs. Built using pgrx |
| [pg_tiktoken](/pg_tiktoken) | 0.0.1 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_tiktoken_$v` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | pg_tictoken: tiktoken tokenizer for use with OpenAI models in postgres |
| [pgml](/pgml) | 2.9.3 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `pgml_$v` |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |  | PostgresML: Run AL/ML workloads with SQL interface |
| [pg4ml](/pg4ml) | 2.0 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg4ml_$v` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Machine learning framework for PostgreSQL |



```yaml
pg17: pgvector_17* pgvectorscale_17 pg_vectorize_17 pg_similarity_17* smlar_17* pg_summarize_17 pg_tiktoken_17 pg4ml_17 #pgml_17
pg16: pgvector_16* pgvectorscale_16 pg_vectorize_16 pg_similarity_16* smlar_16* pg_summarize_16 pg_tiktoken_16 pgml_16 pg4ml_16 
pg15: pgvector_15* pgvectorscale_15 pg_vectorize_15 pg_similarity_15* smlar_15* pg_summarize_15 pg_tiktoken_15 pgml_15 pg4ml_15 
pg14: pgvector_14* pgvectorscale_14 pg_vectorize_14 pg_similarity_14* smlar_14* pg_summarize_14 pg_tiktoken_14 pgml_14 pg4ml_14 
pg13: pgvector_13* pgvectorscale_13 pg_similarity_13* smlar_13* pg_summarize_13 pg_tiktoken_13 pg4ml_13 #pg_vectorize_13 #pgml_13
pg12: pgvector_12* pg_similarity_12* pg_summarize_12 pg_tiktoken_12 pg4ml_12 #pgvectorscale_12 #pg_vectorize_12 #smlar_12* #pgml_12
```



--------

## DEB Packages


| Package | Version | License | DEB | DEB Package | 17 | 16 | 15 | 14 | 13 | 12 | Description |
|---------|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|:--:|-------------|
| [pgvector](/vector) | 0.7.4 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pgvector` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | vector data type and ivfflat and hnsw access methods |
| [pgvectorscale](/vectorscale) | 0.4.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pgvectorscale` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | pgvectorscale:  Advanced indexing for vector data |
| [pg_vectorize](/vectorize) | 15 | **<span class="tcblue">PostgreSQL</span>** | 14} | `postgresql-$v-pg-vectorize` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |  | The simplest way to do vector search on Postgres |
| [pg_similarity](/pg_similarity) | 1.0 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-similarity` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | support similarity queries |
| [smlar](/smlar) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-smlar` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | Effective similarity search |
| [pg_summarize](/pg_summarize) | 0.0.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-summarize` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Text Summarization using LLMs. Built using pgrx |
| [pg_tiktoken](/pg_tiktoken) | 0.0.1 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-tiktoken` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | pg_tictoken: tiktoken tokenizer for use with OpenAI models in postgres |
| [pgml](/pgml) | 2.9.2 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pgml` |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |  | PostgresML: Run AL/ML workloads with SQL interface |
| [pg4ml](/pg4ml) | 2.0 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg4ml` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Machine learning framework for PostgreSQL |



```yaml
pg17: pgvector_17* pgvectorscale_17 pg_vectorize_17 pg_similarity_17* smlar_17* pg_summarize_17 pg_tiktoken_17 pg4ml_17 #pgml_17
pg16: pgvector_16* pgvectorscale_16 pg_vectorize_16 pg_similarity_16* smlar_16* pg_summarize_16 pg_tiktoken_16 pgml_16 pg4ml_16 
pg15: pgvector_15* pgvectorscale_15 pg_vectorize_15 pg_similarity_15* smlar_15* pg_summarize_15 pg_tiktoken_15 pgml_15 pg4ml_15 
pg14: pgvector_14* pgvectorscale_14 pg_vectorize_14 pg_similarity_14* smlar_14* pg_summarize_14 pg_tiktoken_14 pgml_14 pg4ml_14 
pg13: pgvector_13* pgvectorscale_13 pg_similarity_13* smlar_13* pg_summarize_13 pg_tiktoken_13 pg4ml_13 #pg_vectorize_13 #pgml_13
pg12: pgvector_12* pg_similarity_12* pg_summarize_12 pg_tiktoken_12 pg4ml_12 #pgvectorscale_12 #pg_vectorize_12 #smlar_12* #pgml_12
```



--------


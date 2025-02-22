# pg_bestmatch


> [pg_bestmatch](https://github.com/tensorchord/pg_bestmatch.rs): Generate BM25 sparse vector inside PostgreSQL
>
> https://github.com/tensorchord/pg_bestmatch.rs





[FTS](/fts) extensions: [`pg_search`](/pg_search), [`pgroonga`](/pgroonga), [`pgroonga_database`](/pgroonga_database), [`pg_bigm`](/pg_bigm), [`zhparser`](/zhparser), [`pg_bestmatch`](/pg_bestmatch), [`vchord_bm25`](/vchord_bm25), [`hunspell_cs_cz`](/hunspell_cs_cz), [`hunspell_de_de`](/hunspell_de_de), [`hunspell_en_us`](/hunspell_en_us), [`hunspell_fr`](/hunspell_fr), [`hunspell_ne_np`](/hunspell_ne_np), [`hunspell_nl_nl`](/hunspell_nl_nl), [`hunspell_nn_no`](/hunspell_nn_no), [`hunspell_pt_pt`](/hunspell_pt_pt), [`hunspell_ru_ru`](/hunspell_ru_ru), [`hunspell_ru_ru_aot`](/hunspell_ru_ru_aot), [`fuzzystrmatch`](/fuzzystrmatch), [`pg_trgm`](/pg_trgm)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_bestmatch](https://github.com/tensorchord/pg_bestmatch.rs) | 0.0.1 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_bestmatch](/pg_bestmatch) | `pgrx` | `bm_catalog` |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'pg_bestmatch'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION pg_bestmatch;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.0.1 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_bestmatch_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 0.0.1 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-bestmatch` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pg_bestmatch` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_bestmatch
```


Install `pg_bestmatch` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_bestmatch"]}'
```


Install `pg_bestmatch` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_bestmatch_17;
dnf install pg_bestmatch_16;
dnf install pg_bestmatch_15;
dnf install pg_bestmatch_14;
dnf install pg_bestmatch_13;
```


Install `pg_bestmatch` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-bestmatch;
apt install postgresql-16-pg-bestmatch;
apt install postgresql-15-pg-bestmatch;
apt install postgresql-14-pg-bestmatch;
apt install postgresql-13-pg-bestmatch;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_bestmatch_17` | `pg_bestmatch_16` | `pg_bestmatch_15` | `pg_bestmatch_14` | `pg_bestmatch_13` |
| `el9` | `pg_bestmatch_17` | `pg_bestmatch_16` | `pg_bestmatch_15` | `pg_bestmatch_14` | `pg_bestmatch_13` |
| `d12` | `postgresql-17-pg-bestmatch` | `postgresql-16-pg-bestmatch` | `postgresql-15-pg-bestmatch` | `postgresql-14-pg-bestmatch` | `postgresql-13-pg-bestmatch` |
| `u22` | `postgresql-17-pg-bestmatch` | `postgresql-16-pg-bestmatch` | `postgresql-15-pg-bestmatch` | `postgresql-14-pg-bestmatch` | `postgresql-13-pg-bestmatch` |
| `u24` | `postgresql-17-pg-bestmatch` | `postgresql-16-pg-bestmatch` | `postgresql-15-pg-bestmatch` | `postgresql-14-pg-bestmatch` | `postgresql-13-pg-bestmatch` |





--------

## Usage

- repo: https://github.com/tensorchord/pg_bestmatch.rs
- benchmark: https://hazyresearch.stanford.edu/blog/2024-05-20-m2-bert-retrieval


### How does it work?

- Create an BM25 statistics based on your document set by `bm25_create(table_name, column_name, statistic_name);`. It will create a materilized view to record the stats.
- Generate document sparse vector by `bm25_document_to_svector(statistic_name, passage)`
- For query, generate query sparse vector `bm25_query_to_svector(statistic_name, query)`
- Calculate the score by dot product between the query sparse vector and the document sparse vector
- Currently we use huggingface tokenizer with `bert-base-uncased` vocabulary set to tokenize words. Might support more configuration on tokenizer in the future.


### Install

```sql
CREATE EXTENSION pg_bestmatch;
SET search_path TO public, bm_catalog;
```



--------

## Example

Here is an example workflow demonstrating the usage of this extension with the example of [Stanford LoCo benchmark](https://hazyresearch.stanford.edu/blog/2024-05-20-m2-bert-retrieval).

0. Load the dataset. Here is a script for you if you want to experience `pg_bestmatch` with the dataset.

```sh
wget https://huggingface.co/api/datasets/hazyresearch/LoCoV1-Documents/parquet/default/test/0.parquet -O documents.parquet
wget https://huggingface.co/api/datasets/hazyresearch/LoCoV1-Queries/parquet/default/test/0.parquet -O queries.parquet
```

```python
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
from psycopg2.extensions import register_adapter, AsIs

def adapter_numpy_float64(numpy_float64):
    return AsIs(numpy_float64)

def adapter_numpy_int64(numpy_int64):
    return AsIs(numpy_int64)

def adapter_numpy_float32(numpy_float32):
    return AsIs(numpy_float32)

def adapter_numpy_int32(numpy_int32):
    return AsIs(numpy_int32)

def adapter_numpy_array(numpy_array):
    return AsIs(tuple(numpy_array))

register_adapter(np.float64, adapter_numpy_float64)
register_adapter(np.int64, adapter_numpy_int64)
register_adapter(np.float32, adapter_numpy_float32)
register_adapter(np.int32, adapter_numpy_int32)
register_adapter(np.ndarray, adapter_numpy_array)

db_url = "postgresql://localhost:5432/pg_bestmatch_test"
engine = create_engine(db_url)

def load_documents():
    df = pd.read_parquet("documents.parquet")
    df.to_sql("documents", engine, if_exists='replace', index=False)

def load_queries():
    df = pd.read_parquet("queries.parquet")
    df['answer_pids'] = df['answer_pids'].apply(lambda x: str(x[0]))    
    df.to_sql("queries", engine, if_exists='replace', index=False)

load_documents()
load_queries()
```

1. Create BM25 statistics for the `documents` table.

```sql
SELECT bm25_create('documents', 'passage', 'documents_passage_bm25', 0.75, 1.2);
```

2. Add an embedding column to the `documents` and `queries` tables and update the embeddings for documents and queries.

```sql
ALTER TABLE documents ADD COLUMN embedding svector; -- for pgvecto.rs users
ALTER TABLE documents ADD COLUMN embedding sparsevec; -- for pgvector users

UPDATE documents SET embedding = bm25_document_to_svector('documents_passage_bm25', passage)::svector; -- for pgvecto.rs users
UPDATE documents SET embedding = bm25_document_to_svector('documents_passage_bm25', passage, 'pgvector')::sparsevec; -- for pgvector users
```

3. (Optional) Create a vector index on the sparse vector column.

```sql
CREATE INDEX ON documents USING vectors (embedding svector_dot_ops); -- for pgvecto.rs users
CREATE INDEX ON documents USING ivfflat (embedding sparsevec_ip_ops); -- for pgvector users
```

4. Perform a vector search to find the most relevant documents for each query.

```sql
ALTER TABLE queries ADD COLUMN embedding svector; -- for pgvecto.rs users
ALTER TABLE queries ADD COLUMN embedding sparsevec; -- for pgvector users

UPDATE queries SET embedding = bm25_query_to_svector('documents_passage_bm25', query)::svector; -- for pgvecto.rs users
UPDATE queries SET embedding = bm25_query_to_svector('documents_passage_bm25', query, 'pgvector')::sparsevec; -- for pgvector users

SELECT sum((array[answer_pids] = array(SELECT pid FROM documents WHERE queries.dataset = documents.dataset ORDER BY queries.embedding <#> documents.embedding LIMIT 1))::int) FROM queries;
```

This workflow showcases how to leverage BM25 text queries and vector search in PostgreSQL using this extension. The Top 1 recall of BM25 on this dataset is `0.77`. If you reproduce the result, your operations are correct.


--------

## Comparison with pg_search

- `pg_bestmatch.rs` only provides methods for generating sparse vectors and does not support index-based search (which can be achieved by pgvecto.rs or pgvector).
- `pg_search` performs BM25 retrieval via the external `tantivy` engine, which may have limitations when combined with transactions, filters, or JOIN operations. Since `pg_bestmatch.rs` is entirely native to Postgres, it offers full compatibility with these operations inside postgres.


--------

## Reference

- `tokenize`
    - Description: Tokenizes an input string into individual tokens.
    - Example:
      ```sql
      SELECT tokenize('i have an apple'); -- result: {i,have,an,apple}
      ```
- `bm25_create`
    - Description: Creates BM25 statistics for a specified table and column.
    - Usage:
      ```sql
      SELECT bm25_create('documents', 'passage', 'documents_passage_bm25');
      ```
    - Parameters:
        - `table_name`: Name of the table.
        - `column_name`: Name of the column.
        - `stat_name`: Name of the BM25 statistics.
        - `b`: BM25 parameter (default 0.75).
        - `k`: BM25 parameter (default 1.2).
- `bm25_refresh`
    - Description: Updates the BM25 statistics to reflect any changes in the underlying data.
    - Usage:
      ```sql
      SELECT bm25_refresh('documents_passage_bm25');
      ```
    - Parameters:
        - `stat_name`: Name of the BM25 statistics to update.
- `bm25_drop`
    - Description: Deletes the BM25 statistics for a specified table and column.
    - Usage:
      ```sql
      SELECT bm25_drop('documents_passage_bm25');
      ```
    - Parameters:
        - `stat_name`: Name of the BM25 statistics to delete.
- `bm25_document_to_svector`
    - Description: Converts document text into a sparse vector representation.
    - Usage:
      ```sql
      SELECT bm25_document_to_svector('documents_passage_bm25', 'document_text');
      ```
    - Parameters:
        - `stat_name`: Name of the BM25 statistics.
        - `document_text`: The text of the document.
        - `style`: Emits `pgvecto.rs`-style sparse vector or `pgvector`-style sparse vector.
- `bm25_query_to_svector`
    - Description: Converts query text into a sparse vector representation.
    - Usage:
      ```sql
      SELECT bm25_query_to_svector('documents_passage_bm25', 'We begin, as always, with the text.');
      ```
    - Parameters:
        - `stat_name`: Name of the BM25 statistics.
        - `query_text`: The text of the query.
        - `style`: Emits `pgvecto.rs`-style sparse vector or `pgvector`-style sparse vector.

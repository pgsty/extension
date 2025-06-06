# vectorize


> [pg_vectorize](https://github.com/ChuckHend/pg_vectorize): The simplest way to do vector search on Postgres
>
> https://github.com/ChuckHend/pg_vectorize





[RAG](/rag) extensions: [`vector`](/vector), [`vchord`](/vchord), [`vectorscale`](/vectorscale), [`vectorize`](/vectorize), [`pg_similarity`](/pg_similarity), [`smlar`](/smlar), [`pg_summarize`](/pg_summarize), [`pg_tiktoken`](/pg_tiktoken), [`pg4ml`](/pg4ml), [`pgml`](/pgml)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [vectorize](https://github.com/ChuckHend/pg_vectorize) | 0.22.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_vectorize](/vectorize) | `pgrx` | `vectorize` | [`pg_cron`](pg_cron), [`pgmq`](pgmq), [`vector`](vector) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |





```sql
CREATE EXTENSION vectorize CASCADE;
```
> **Comment**: pgrx=0.13.1
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.22.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_vectorize_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | `pgmq_$v`, `pg_cron_$v`, `pgvector_$v` |
| [DEB](/deb) | 0.22.2 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-vectorize` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | `postgresql-$v-pgmq`, `postgresql-$v-pg-cron`, `postgresql-$v-pgvector` |



Install `vectorize` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add vectorize
```


Install `pg_vectorize` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_vectorize"]}'
```


Install `pg_vectorize` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_vectorize_17;
dnf install pg_vectorize_16;
dnf install pg_vectorize_15;
dnf install pg_vectorize_14;
```


Install `pg_vectorize` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-vectorize;
apt install postgresql-16-pg-vectorize;
apt install postgresql-15-pg-vectorize;
apt install postgresql-14-pg-vectorize;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_vectorize_17` | `pg_vectorize_16` | `pg_vectorize_15` | `pg_vectorize_14` | <span class="tcred">✘</span> |
| `el9` | `pg_vectorize_17` | `pg_vectorize_16` | `pg_vectorize_15` | `pg_vectorize_14` | <span class="tcred">✘</span> |
| `d12` | `postgresql-17-pg-vectorize` | `postgresql-16-pg-vectorize` | `postgresql-15-pg-vectorize` | `postgresql-14-pg-vectorize` | <span class="tcred">✘</span> |
| `u22` | `postgresql-17-pg-vectorize` | `postgresql-16-pg-vectorize` | `postgresql-15-pg-vectorize` | `postgresql-14-pg-vectorize` | <span class="tcred">✘</span> |
| `u24` | `postgresql-17-pg-vectorize` | `postgresql-16-pg-vectorize` | `postgresql-15-pg-vectorize` | `postgresql-14-pg-vectorize` | <span class="tcred">✘</span> |






# pg_vectorize


> [pg_vectorize](https://github.com/tembo-io/pg_vectorize): The simplest way to do vector search on Postgres
>
> https://github.com/tembo-io/pg_vectorize





[RAG](/rag) extensions: [`vector`](/vector), [`vectorscale`](/vectorscale), [`vectorize`](/vectorize), [`pg_similarity`](/pg_similarity), [`smlar`](/smlar), [`pg_summarize`](/pg_summarize), [`pg_tiktoken`](/pg_tiktoken), [`pgml`](/pgml), [`pg4ml`](/pg4ml)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [vectorize](https://github.com/tembo-io/pg_vectorize) | 0.20.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_vectorize](/vectorize) | `pgrx` | `vectorize` | [`pg_cron`](pg_cron), [`pgmq`](pgmq), [`vector`](vector) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION vectorize CASCADE;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.20.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_vectorize_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  | `pgmq_$v`, `pg_cron_$v`, `pgvector_$v` |
| [DEB](/deb) | 0.20.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-vectorize` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  | `postgresql-$v-pgmq`, `postgresql-$v-pg-cron`, `postgresql-$v-pgvector` |



Install `pg_vectorize` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_vectorize"]}'
```


Install `pg_vectorize` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install pg_vectorize_17;
yum install pg_vectorize_16;
yum install pg_vectorize_15;
yum install pg_vectorize_14;
yum install pg_vectorize_13;
yum install pg_vectorize_12;
```


Install `pg_vectorize` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-vectorize;
apt install postgresql-16-pg-vectorize;
apt install postgresql-15-pg-vectorize;
apt install postgresql-14-pg-vectorize;
apt install postgresql-13-pg-vectorize;
apt install postgresql-12-pg-vectorize;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_vectorize_17` | `pg_vectorize_16` | `pg_vectorize_15` | `pg_vectorize_14` | `pg_vectorize_13` | `pg_vectorize_12` |
| `el9` | `pg_vectorize_17` | `pg_vectorize_16` | `pg_vectorize_15` | `pg_vectorize_14` | `pg_vectorize_13` | `pg_vectorize_12` |
| `d12` | `postgresql-17-pg-vectorize` | `postgresql-16-pg-vectorize` | `postgresql-15-pg-vectorize` | `postgresql-14-pg-vectorize` | `postgresql-13-pg-vectorize` | `postgresql-12-pg-vectorize` |
| `u22` | `postgresql-17-pg-vectorize` | `postgresql-16-pg-vectorize` | `postgresql-15-pg-vectorize` | `postgresql-14-pg-vectorize` | `postgresql-13-pg-vectorize` | `postgresql-12-pg-vectorize` |
| `u24` | `postgresql-17-pg-vectorize` | `postgresql-16-pg-vectorize` | `postgresql-15-pg-vectorize` | `postgresql-14-pg-vectorize` | `postgresql-13-pg-vectorize` | `postgresql-12-pg-vectorize` |






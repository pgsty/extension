# pg_summarize


> [pg_summarize](https://github.com/HexaCluster/pg_summarize): Text Summarization using LLMs. Built using pgrx
>
> https://github.com/HexaCluster/pg_summarize





[RAG](/rag) extensions: [`vector`](/vector), [`vectorscale`](/vectorscale), [`vectorize`](/vectorize), [`pg_similarity`](/pg_similarity), [`smlar`](/smlar), [`pg_summarize`](/pg_summarize), [`pg_tiktoken`](/pg_tiktoken), [`pgml`](/pgml), [`pg4ml`](/pg4ml)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_summarize](https://github.com/HexaCluster/pg_summarize) | 0.0.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_summarize](/pg_summarize) | `pgrx` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_summarize;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_summarize_17` | `pg_summarize_16` | `pg_summarize_15` | `pg_summarize_14` | `pg_summarize_13` | `pg_summarize_12` |
| `el9` | `pg_summarize_17` | `pg_summarize_16` | `pg_summarize_15` | `pg_summarize_14` | `pg_summarize_13` | `pg_summarize_12` |
| `d12` | `postgresql-17-pg-summarize` | `postgresql-16-pg-summarize` | `postgresql-15-pg-summarize` | `postgresql-14-pg-summarize` | `postgresql-13-pg-summarize` | `postgresql-12-pg-summarize` |
| `u22` | `postgresql-17-pg-summarize` | `postgresql-16-pg-summarize` | `postgresql-15-pg-summarize` | `postgresql-14-pg-summarize` | `postgresql-13-pg-summarize` | `postgresql-12-pg-summarize` |
| `u24` | `postgresql-17-pg-summarize` | `postgresql-16-pg-summarize` | `postgresql-15-pg-summarize` | `postgresql-14-pg-summarize` | `postgresql-13-pg-summarize` | `postgresql-12-pg-summarize` |



Install `pg_summarize` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_summarize"]}'
```


Install `pg_summarize` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install pg_summarize_17;
yum install pg_summarize_16;
yum install pg_summarize_15;
yum install pg_summarize_14;
yum install pg_summarize_13;
yum install pg_summarize_12;
```


Install `pg_summarize` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-summarize;
apt install postgresql-16-pg-summarize;
apt install postgresql-15-pg-summarize;
apt install postgresql-14-pg-summarize;
apt install postgresql-13-pg-summarize;
apt install postgresql-12-pg-summarize;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_summarize_17` | `pg_summarize_16` | `pg_summarize_15` | `pg_summarize_14` | `pg_summarize_13` | `pg_summarize_12` |
| `el9` | `pg_summarize_17` | `pg_summarize_16` | `pg_summarize_15` | `pg_summarize_14` | `pg_summarize_13` | `pg_summarize_12` |
| `d12` | `postgresql-17-pg-summarize` | `postgresql-16-pg-summarize` | `postgresql-15-pg-summarize` | `postgresql-14-pg-summarize` | `postgresql-13-pg-summarize` | `postgresql-12-pg-summarize` |
| `u22` | `postgresql-17-pg-summarize` | `postgresql-16-pg-summarize` | `postgresql-15-pg-summarize` | `postgresql-14-pg-summarize` | `postgresql-13-pg-summarize` | `postgresql-12-pg-summarize` |
| `u24` | `postgresql-17-pg-summarize` | `postgresql-16-pg-summarize` | `postgresql-15-pg-summarize` | `postgresql-14-pg-summarize` | `postgresql-13-pg-summarize` | `postgresql-12-pg-summarize` |






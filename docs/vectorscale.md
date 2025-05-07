# vectorscale


> [pgvectorscale](https://github.com/timescale/pgvectorscale): pgvectorscale:  Advanced indexing for vector data
>
> https://github.com/timescale/pgvectorscale





[RAG](/rag) extensions: [`vector`](/vector), [`vchord`](/vchord), [`vectorscale`](/vectorscale), [`vectorize`](/vectorize), [`pg_similarity`](/pg_similarity), [`smlar`](/smlar), [`pg_summarize`](/pg_summarize), [`pg_tiktoken`](/pg_tiktoken), [`pg4ml`](/pg4ml), [`pgml`](/pgml)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [vectorscale](https://github.com/timescale/pgvectorscale) | 0.7.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgvectorscale](/vectorscale) | `pgrx` |  | [`vector`](vector) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION vectorscale CASCADE;
```
> **Comment**: pgrx=v0.12.5
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.7.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pgvectorscale_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 0.7.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pgvectorscale` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `vectorscale` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add vectorscale
```


Install `pgvectorscale` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgvectorscale"]}'
```


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




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgvectorscale_17` | `pgvectorscale_16` | `pgvectorscale_15` | `pgvectorscale_14` | `pgvectorscale_13` |
| `el9` | `pgvectorscale_17` | `pgvectorscale_16` | `pgvectorscale_15` | `pgvectorscale_14` | `pgvectorscale_13` |
| `d12` | `postgresql-17-pgvectorscale` | `postgresql-16-pgvectorscale` | `postgresql-15-pgvectorscale` | `postgresql-14-pgvectorscale` | `postgresql-13-pgvectorscale` |
| `u22` | `postgresql-17-pgvectorscale` | `postgresql-16-pgvectorscale` | `postgresql-15-pgvectorscale` | `postgresql-14-pgvectorscale` | `postgresql-13-pgvectorscale` |
| `u24` | `postgresql-17-pgvectorscale` | `postgresql-16-pgvectorscale` | `postgresql-15-pgvectorscale` | `postgresql-14-pgvectorscale` | `postgresql-13-pgvectorscale` |






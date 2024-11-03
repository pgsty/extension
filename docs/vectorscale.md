# pgvectorscale


> [pgvectorscale](https://github.com/timescale/pgvectorscale): pgvectorscale:  Advanced indexing for vector data
>
> https://github.com/timescale/pgvectorscale





[RAG](/rag) extensions: [`vector`](/vector), [`vectorscale`](/vectorscale), [`vectorize`](/vectorize), [`pg_similarity`](/pg_similarity), [`smlar`](/smlar), [`pg_summarize`](/pg_summarize), [`pg_tiktoken`](/pg_tiktoken), [`pgml`](/pgml), [`pg4ml`](/pg4ml)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [vectorscale](https://github.com/timescale/pgvectorscale) | 0.4.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Package | Tags | Schemas | Requires | Required by |
|---------|------|---------|----------|-------------|
| [pgvectorscale](/vectorscale) | `pgrx` |  | [`vector`](vector) |  |





```sql
CREATE EXTENSION vectorscale CASCADE;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.4.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pgvectorscale_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  |
| [DEB](/deb) | 0.4.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pgvectorscale` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  |



Install `pgvectorscale` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

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








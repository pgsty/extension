# pgvector


> [pgvector](https://github.com/pgvector/pgvector): vector data type and ivfflat and hnsw access methods
>
> https://github.com/pgvector/pgvector





[RAG](/rag) extensions: [`vector`](/vector), [`vectorscale`](/vectorscale), [`vectorize`](/vectorize), [`pg_similarity`](/pg_similarity), [`smlar`](/smlar), [`pg_summarize`](/pg_summarize), [`pg_tiktoken`](/pg_tiktoken), [`pgml`](/pgml), [`pg4ml`](/pg4ml)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [vector](https://github.com/pgvector/pgvector) | 0.8.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Package | Tags | Schemas | Requires | Required by |
|---------|------|---------|----------|-------------|
| [pgvector](/vector) |  |  |  | [`vectorscale`](/vectorscale), [`vectorize`](/vectorize) |





```sql
CREATE EXTENSION vector;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.8.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pgvector_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 0.8.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pgvector` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pgvector` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgvector"]}'
```


Install `pgvector` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pgvector_17*;
dnf install pgvector_16*;
dnf install pgvector_15*;
dnf install pgvector_14*;
dnf install pgvector_13*;
dnf install pgvector_12*;
```


Install `pgvector` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pgvector;
apt install postgresql-16-pgvector;
apt install postgresql-15-pgvector;
apt install postgresql-14-pgvector;
apt install postgresql-13-pgvector;
apt install postgresql-12-pgvector;
```








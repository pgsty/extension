# pg_tiktoken


> [pg_tiktoken](https://github.com/kelvich/pg_tiktoken): pg_tictoken: tiktoken tokenizer for use with OpenAI models in postgres
>
> https://github.com/kelvich/pg_tiktoken





[RAG](/rag) extensions: [`vector`](/vector), [`vectorscale`](/vectorscale), [`vectorize`](/vectorize), [`pg_similarity`](/pg_similarity), [`smlar`](/smlar), [`pg_summarize`](/pg_summarize), [`pg_tiktoken`](/pg_tiktoken), [`pgml`](/pgml), [`pg4ml`](/pg4ml)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_tiktoken](https://github.com/kelvich/pg_tiktoken) | 0.0.1 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_tiktoken](/pg_tiktoken) | `pgrx` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_tiktoken;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.0.1 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_tiktoken_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 0.0.1 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-tiktoken` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pg_tiktoken` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_tiktoken"]}'
```


Install `pg_tiktoken` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install pg_tiktoken_17;
yum install pg_tiktoken_16;
yum install pg_tiktoken_15;
yum install pg_tiktoken_14;
yum install pg_tiktoken_13;
yum install pg_tiktoken_12;
```


Install `pg_tiktoken` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-tiktoken;
apt install postgresql-16-pg-tiktoken;
apt install postgresql-15-pg-tiktoken;
apt install postgresql-14-pg-tiktoken;
apt install postgresql-13-pg-tiktoken;
apt install postgresql-12-pg-tiktoken;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_tiktoken_17` | `pg_tiktoken_16` | `pg_tiktoken_15` | `pg_tiktoken_14` | `pg_tiktoken_13` | `pg_tiktoken_12` |
| `el9` | `pg_tiktoken_17` | `pg_tiktoken_16` | `pg_tiktoken_15` | `pg_tiktoken_14` | `pg_tiktoken_13` | `pg_tiktoken_12` |
| `d12` | `postgresql-17-pg-tiktoken` | `postgresql-16-pg-tiktoken` | `postgresql-15-pg-tiktoken` | `postgresql-14-pg-tiktoken` | `postgresql-13-pg-tiktoken` | `postgresql-12-pg-tiktoken` |
| `u22` | `postgresql-17-pg-tiktoken` | `postgresql-16-pg-tiktoken` | `postgresql-15-pg-tiktoken` | `postgresql-14-pg-tiktoken` | `postgresql-13-pg-tiktoken` | `postgresql-12-pg-tiktoken` |
| `u24` | `postgresql-17-pg-tiktoken` | `postgresql-16-pg-tiktoken` | `postgresql-15-pg-tiktoken` | `postgresql-14-pg-tiktoken` | `postgresql-13-pg-tiktoken` | `postgresql-12-pg-tiktoken` |






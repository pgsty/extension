# pg_tiktoken


> [pg_tiktoken](https://github.com/kelvich/pg_tiktoken): pg_tictoken: tiktoken tokenizer for use with OpenAI models in postgres
>
> https://github.com/kelvich/pg_tiktoken





[RAG](/rag) extensions: [`vector`](/vector), [`vectorscale`](/vectorscale), [`vectorize`](/vectorize), [`pg_similarity`](/pg_similarity), [`smlar`](/smlar), [`pg_summarize`](/pg_summarize), [`pg_tiktoken`](/pg_tiktoken), [`pgml`](/pgml), [`pg4ml`](/pg4ml)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [pg_tiktoken](https://github.com/kelvich/pg_tiktoken) | 0.0.1 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Package | Tags | Schemas | Requires | Required by |
|---------|------|---------|----------|-------------|
| [pg_tiktoken](/pg_tiktoken) | `pgrx` |  |  |  |





```sql
CREATE EXTENSION pg_tiktoken;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.0.1 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_tiktoken_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 0.0.1 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-tiktoken` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pg_tiktoken` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_tiktoken"]}'
```


Install `pg_tiktoken` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_tiktoken_17;
dnf install pg_tiktoken_16;
dnf install pg_tiktoken_15;
dnf install pg_tiktoken_14;
dnf install pg_tiktoken_13;
dnf install pg_tiktoken_12;
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








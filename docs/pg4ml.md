# pg4ml


> [pg4ml](https://gitee.com/guotiecheng/plpgsql_pg4ml): Machine learning framework for PostgreSQL
>
> https://gitee.com/guotiecheng/plpgsql_pg4ml





[RAG](/rag) extensions: [`vector`](/vector), [`vectorscale`](/vectorscale), [`vectorize`](/vectorize), [`pg_similarity`](/pg_similarity), [`smlar`](/smlar), [`pg_summarize`](/pg_summarize), [`pg_tiktoken`](/pg_tiktoken), [`pgml`](/pgml), [`pg4ml`](/pg4ml)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg4ml](https://gitee.com/guotiecheng/plpgsql_pg4ml) | 2.0 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg4ml](/pg4ml) |  |  | [`plpgsql`](plpgsql), [`tablefunc`](tablefunc), [`cube`](cube), [`plpython3u`](plpython3u) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg4ml CASCADE;
```
> **Comment**: require python3
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 2.0 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg4ml_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 2.0 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg4ml` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pg4ml` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg4ml"]}'
```


Install `pg4ml` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install pg4ml_17;
yum install pg4ml_16;
yum install pg4ml_15;
yum install pg4ml_14;
yum install pg4ml_13;
yum install pg4ml_12;
```


Install `pg4ml` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg4ml;
apt install postgresql-16-pg4ml;
apt install postgresql-15-pg4ml;
apt install postgresql-14-pg4ml;
apt install postgresql-13-pg4ml;
apt install postgresql-12-pg4ml;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg4ml_17` | `pg4ml_16` | `pg4ml_15` | `pg4ml_14` | `pg4ml_13` | `pg4ml_12` |
| `el9` | `pg4ml_17` | `pg4ml_16` | `pg4ml_15` | `pg4ml_14` | `pg4ml_13` | `pg4ml_12` |
| `d12` | `postgresql-17-pg4ml` | `postgresql-16-pg4ml` | `postgresql-15-pg4ml` | `postgresql-14-pg4ml` | `postgresql-13-pg4ml` | `postgresql-12-pg4ml` |
| `u22` | `postgresql-17-pg4ml` | `postgresql-16-pg4ml` | `postgresql-15-pg4ml` | `postgresql-14-pg4ml` | `postgresql-13-pg4ml` | `postgresql-12-pg4ml` |
| `u24` | `postgresql-17-pg4ml` | `postgresql-16-pg4ml` | `postgresql-15-pg4ml` | `postgresql-14-pg4ml` | `postgresql-13-pg4ml` | `postgresql-12-pg4ml` |






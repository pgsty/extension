# smlar


> [smlar](https://github.com/jirutka/smlar): Effective similarity search
>
> https://github.com/jirutka/smlar





[RAG](/rag) extensions: [`vector`](/vector), [`vchord`](/vchord), [`vectorscale`](/vectorscale), [`vectorize`](/vectorize), [`pg_similarity`](/pg_similarity), [`smlar`](/smlar), [`pg_summarize`](/pg_summarize), [`pg_tiktoken`](/pg_tiktoken), [`pg4ml`](/pg4ml), [`pgml`](/pgml)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [smlar](https://github.com/jirutka/smlar) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [smlar](/smlar) | `nil-lic` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION smlar;
```
> **Comment**: fix math.abs, gist pointer problem
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `smlar_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-smlar` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `smlar` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add smlar
```


Install `smlar` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["smlar"]}'
```


Install `smlar` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install smlar_17*;
dnf install smlar_16*;
dnf install smlar_15*;
dnf install smlar_14*;
dnf install smlar_13*;
```


Install `smlar` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-smlar;
apt install postgresql-16-smlar;
apt install postgresql-15-smlar;
apt install postgresql-14-smlar;
apt install postgresql-13-smlar;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `smlar_17*` | `smlar_16*` | `smlar_15*` | `smlar_14*` | `smlar_13*` |
| `el9` | `smlar_17*` | `smlar_16*` | `smlar_15*` | `smlar_14*` | `smlar_13*` |
| `d12` | `postgresql-17-smlar` | `postgresql-16-smlar` | `postgresql-15-smlar` | `postgresql-14-smlar` | `postgresql-13-smlar` |
| `u22` | `postgresql-17-smlar` | `postgresql-16-smlar` | `postgresql-15-smlar` | `postgresql-14-smlar` | `postgresql-13-smlar` |
| `u24` | `postgresql-17-smlar` | `postgresql-16-smlar` | `postgresql-15-smlar` | `postgresql-14-smlar` | `postgresql-13-smlar` |






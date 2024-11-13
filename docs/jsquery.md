# jsquery


> [jsquery](https://github.com/postgrespro/jsquery): data type for jsonb inspection
>
> https://github.com/postgrespro/jsquery





[FEAT](/feat) extensions: [`age`](/age), [`hll`](/hll), [`rum`](/rum), [`pg_graphql`](/pg_graphql), [`pg_jsonschema`](/pg_jsonschema), [`jsquery`](/jsquery), [`pg_hint_plan`](/pg_hint_plan), [`hypopg`](/hypopg), [`index_advisor`](/index_advisor), [`plan_filter`](/plan_filter), [`imgsmlr`](/imgsmlr), [`pg_ivm`](/pg_ivm), [`pgmq`](/pgmq), [`pgq`](/pgq), [`pg_cardano`](/pg_cardano), [`rdkit`](/rdkit), [`bloom`](/bloom)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [jsquery](https://github.com/postgrespro/jsquery) | 1.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [jsquery](/jsquery) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION jsquery;
```
> **Comment**: no pg13,12 on el9
-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `jsquery_17*` | `jsquery_16*` | `jsquery_15*` | `jsquery_14*` | `jsquery_13*` | `jsquery_12*` |
| `el9` | `jsquery_17*` | `jsquery_16*` | `jsquery_15*` | `jsquery_14*` | `jsquery_13*` | `jsquery_12*` |
| `d12` | `postgresql-17-jsquery` | `postgresql-16-jsquery` | `postgresql-15-jsquery` | `postgresql-14-jsquery` | `postgresql-13-jsquery` | `postgresql-12-jsquery` |
| `u22` | `postgresql-17-jsquery` | `postgresql-16-jsquery` | `postgresql-15-jsquery` | `postgresql-14-jsquery` | `postgresql-13-jsquery` | `postgresql-12-jsquery` |
| `u24` | `postgresql-17-jsquery` | `postgresql-16-jsquery` | `postgresql-15-jsquery` | `postgresql-14-jsquery` | `postgresql-13-jsquery` | `postgresql-12-jsquery` |



Install `jsquery` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["jsquery"]}'
```


Install `jsquery` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install jsquery_17*;
yum install jsquery_16*;
yum install jsquery_15*;
yum install jsquery_14*;
yum install jsquery_13*;
yum install jsquery_12*;
```


Install `jsquery` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-jsquery;
apt install postgresql-16-jsquery;
apt install postgresql-15-jsquery;
apt install postgresql-14-jsquery;
apt install postgresql-13-jsquery;
apt install postgresql-12-jsquery;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `jsquery_17*` | `jsquery_16*` | `jsquery_15*` | `jsquery_14*` | `jsquery_13*` | `jsquery_12*` |
| `el9` | `jsquery_17*` | `jsquery_16*` | `jsquery_15*` | `jsquery_14*` | `jsquery_13*` | `jsquery_12*` |
| `d12` | `postgresql-17-jsquery` | `postgresql-16-jsquery` | `postgresql-15-jsquery` | `postgresql-14-jsquery` | `postgresql-13-jsquery` | `postgresql-12-jsquery` |
| `u22` | `postgresql-17-jsquery` | `postgresql-16-jsquery` | `postgresql-15-jsquery` | `postgresql-14-jsquery` | `postgresql-13-jsquery` | `postgresql-12-jsquery` |
| `u24` | `postgresql-17-jsquery` | `postgresql-16-jsquery` | `postgresql-15-jsquery` | `postgresql-14-jsquery` | `postgresql-13-jsquery` | `postgresql-12-jsquery` |






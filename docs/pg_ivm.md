# pg_ivm


> [pg_ivm](https://github.com/sraoss/pg_ivm): incremental view maintenance on PostgreSQL
>
> https://github.com/sraoss/pg_ivm





[FEAT](/feat) extensions: [`age`](/age), [`hll`](/hll), [`rum`](/rum), [`pg_graphql`](/pg_graphql), [`pg_jsonschema`](/pg_jsonschema), [`jsquery`](/jsquery), [`pg_hint_plan`](/pg_hint_plan), [`hypopg`](/hypopg), [`index_advisor`](/index_advisor), [`plan_filter`](/plan_filter), [`imgsmlr`](/imgsmlr), [`pg_ivm`](/pg_ivm), [`pgmq`](/pgmq), [`pgq`](/pgq), [`pg_cardano`](/pg_cardano), [`rdkit`](/rdkit), [`bloom`](/bloom)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_ivm](https://github.com/sraoss/pg_ivm) | 1.8 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_ivm](/pg_ivm) |  | `pg_catalog` |  | [`timeseries`](/timeseries) |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_ivm;
```
> **Comment**: no pg12 on el8/9 pgdg repo
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.8 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pg_ivm_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |  |
| [DEB](/deb) | 1.9 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-ivm` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |  |



Install `pg_ivm` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_ivm"]}'
```


Install `pg_ivm` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install pg_ivm_17*;
yum install pg_ivm_16*;
yum install pg_ivm_15*;
yum install pg_ivm_14*;
yum install pg_ivm_13*;
yum install pg_ivm_12*;
```


Install `pg_ivm` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pg-ivm;
apt install postgresql-16-pg-ivm;
apt install postgresql-15-pg-ivm;
apt install postgresql-14-pg-ivm;
apt install postgresql-13-pg-ivm;
apt install postgresql-12-pg-ivm;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_ivm_17*` | `pg_ivm_16*` | `pg_ivm_15*` | `pg_ivm_14*` | `pg_ivm_13*` | `pg_ivm_12*` |
| `el9` | `pg_ivm_17*` | `pg_ivm_16*` | `pg_ivm_15*` | `pg_ivm_14*` | `pg_ivm_13*` | `pg_ivm_12*` |
| `d12` | `postgresql-17-pg-ivm` | `postgresql-16-pg-ivm` | `postgresql-15-pg-ivm` | `postgresql-14-pg-ivm` | `postgresql-13-pg-ivm` | `postgresql-12-pg-ivm` |
| `u22` | `postgresql-17-pg-ivm` | `postgresql-16-pg-ivm` | `postgresql-15-pg-ivm` | `postgresql-14-pg-ivm` | `postgresql-13-pg-ivm` | `postgresql-12-pg-ivm` |
| `u24` | `postgresql-17-pg-ivm` | `postgresql-16-pg-ivm` | `postgresql-15-pg-ivm` | `postgresql-14-pg-ivm` | `postgresql-13-pg-ivm` | `postgresql-12-pg-ivm` |






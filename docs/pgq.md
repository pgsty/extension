# pgq


> [pgq](https://github.com/pgq/pgq): Generic queue for PostgreSQL
>
> https://github.com/pgq/pgq





[FEAT](/feat) extensions: [`age`](/age), [`hll`](/hll), [`rum`](/rum), [`pg_graphql`](/pg_graphql), [`pg_jsonschema`](/pg_jsonschema), [`jsquery`](/jsquery), [`pg_hint_plan`](/pg_hint_plan), [`hypopg`](/hypopg), [`index_advisor`](/index_advisor), [`plan_filter`](/plan_filter), [`imgsmlr`](/imgsmlr), [`pg_ivm`](/pg_ivm), [`pgmq`](/pgmq), [`pgq`](/pgq), [`pg_cardano`](/pg_cardano), [`rdkit`](/rdkit), [`bloom`](/bloom)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgq](https://github.com/pgq/pgq) | 3.5.1 | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgq](/pgq) |  | `pg_catalog` |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pgq;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 3.5.1 | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | `pgq_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 3.5 | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pgq3` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pgq` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgq"]}'
```


Install `pgq` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pgq_17*;
dnf install pgq_16*;
dnf install pgq_15*;
dnf install pgq_14*;
dnf install pgq_13*;
dnf install pgq_12*;
```


Install `pgq` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pgq3;
apt install postgresql-16-pgq3;
apt install postgresql-15-pgq3;
apt install postgresql-14-pgq3;
apt install postgresql-13-pgq3;
apt install postgresql-12-pgq3;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgq_17*` | `pgq_16*` | `pgq_15*` | `pgq_14*` | `pgq_13*` | `pgq_12*` |
| `el9` | `pgq_17*` | `pgq_16*` | `pgq_15*` | `pgq_14*` | `pgq_13*` | `pgq_12*` |
| `d12` | `postgresql-17-pgq3` | `postgresql-16-pgq3` | `postgresql-15-pgq3` | `postgresql-14-pgq3` | `postgresql-13-pgq3` | `postgresql-12-pgq3` |
| `u22` | `postgresql-17-pgq3` | `postgresql-16-pgq3` | `postgresql-15-pgq3` | `postgresql-14-pgq3` | `postgresql-13-pgq3` | `postgresql-12-pgq3` |
| `u24` | `postgresql-17-pgq3` | `postgresql-16-pgq3` | `postgresql-15-pgq3` | `postgresql-14-pgq3` | `postgresql-13-pgq3` | `postgresql-12-pgq3` |






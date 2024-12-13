# pg_hint_plan


> [pg_hint_plan](https://github.com/ossc-db/pg_hint_plan): Give PostgreSQL ability to manually force some decisions in execution plans.
>
> https://github.com/ossc-db/pg_hint_plan





[FEAT](/feat) extensions: [`age`](/age), [`hll`](/hll), [`rum`](/rum), [`pg_graphql`](/pg_graphql), [`pg_jsonschema`](/pg_jsonschema), [`jsquery`](/jsquery), [`pg_hint_plan`](/pg_hint_plan), [`hypopg`](/hypopg), [`index_advisor`](/index_advisor), [`plan_filter`](/plan_filter), [`imgsmlr`](/imgsmlr), [`pg_ivm`](/pg_ivm), [`pgmq`](/pgmq), [`pgq`](/pgq), [`pg_cardano`](/pg_cardano), [`rdkit`](/rdkit), [`bloom`](/bloom)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_hint_plan](https://github.com/ossc-db/pg_hint_plan) | 1.7.0 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_hint_plan](/pg_hint_plan) |  | `hint_plan` |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_hint_plan;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.7.0 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `pg_hint_plan_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 1.7.0 | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pg-hint-plan` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pg_hint_plan` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_hint_plan"]}'
```


Install `pg_hint_plan` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install pg_hint_plan_17*;
yum install pg_hint_plan_16*;
yum install pg_hint_plan_15*;
yum install pg_hint_plan_14*;
yum install pg_hint_plan_13*;
yum install pg_hint_plan_12*;
```


Install `pg_hint_plan` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pg-hint-plan;
apt install postgresql-16-pg-hint-plan;
apt install postgresql-15-pg-hint-plan;
apt install postgresql-14-pg-hint-plan;
apt install postgresql-13-pg-hint-plan;
apt install postgresql-12-pg-hint-plan;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_hint_plan_17*` | `pg_hint_plan_16*` | `pg_hint_plan_15*` | `pg_hint_plan_14*` | `pg_hint_plan_13*` | `pg_hint_plan_12*` |
| `el9` | `pg_hint_plan_17*` | `pg_hint_plan_16*` | `pg_hint_plan_15*` | `pg_hint_plan_14*` | `pg_hint_plan_13*` | `pg_hint_plan_12*` |
| `d12` | `postgresql-17-pg-hint-plan` | `postgresql-16-pg-hint-plan` | `postgresql-15-pg-hint-plan` | `postgresql-14-pg-hint-plan` | `postgresql-13-pg-hint-plan` | `postgresql-12-pg-hint-plan` |
| `u22` | `postgresql-17-pg-hint-plan` | `postgresql-16-pg-hint-plan` | `postgresql-15-pg-hint-plan` | `postgresql-14-pg-hint-plan` | `postgresql-13-pg-hint-plan` | `postgresql-12-pg-hint-plan` |
| `u24` | `postgresql-17-pg-hint-plan` | `postgresql-16-pg-hint-plan` | `postgresql-15-pg-hint-plan` | `postgresql-14-pg-hint-plan` | `postgresql-13-pg-hint-plan` | `postgresql-12-pg-hint-plan` |






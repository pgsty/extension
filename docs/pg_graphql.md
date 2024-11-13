# pg_graphql


> [pg_graphql](https://github.com/supabase/pg_graphql): pg_graphql: GraphQL support
>
> https://github.com/supabase/pg_graphql





[FEAT](/feat) extensions: [`age`](/age), [`hll`](/hll), [`rum`](/rum), [`pg_graphql`](/pg_graphql), [`pg_jsonschema`](/pg_jsonschema), [`jsquery`](/jsquery), [`pg_hint_plan`](/pg_hint_plan), [`hypopg`](/hypopg), [`index_advisor`](/index_advisor), [`plan_filter`](/plan_filter), [`imgsmlr`](/imgsmlr), [`pg_ivm`](/pg_ivm), [`pgmq`](/pgmq), [`pgq`](/pgq), [`pg_cardano`](/pg_cardano), [`rdkit`](/rdkit), [`bloom`](/bloom)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_graphql](https://github.com/supabase/pg_graphql) | 1.5.9 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_graphql](/pg_graphql) | `pgrx`, `supabase` | `graphql` |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_graphql;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_graphql_17` | `pg_graphql_16` | `pg_graphql_15` | `pg_graphql_14` | `pg_graphql_13` | `pg_graphql_12` |
| `el9` | `pg_graphql_17` | `pg_graphql_16` | `pg_graphql_15` | `pg_graphql_14` | `pg_graphql_13` | `pg_graphql_12` |
| `d12` | `postgresql-17-pg-graphql` | `postgresql-16-pg-graphql` | `postgresql-15-pg-graphql` | `postgresql-14-pg-graphql` | `postgresql-13-pg-graphql` | `postgresql-12-pg-graphql` |
| `u22` | `postgresql-17-pg-graphql` | `postgresql-16-pg-graphql` | `postgresql-15-pg-graphql` | `postgresql-14-pg-graphql` | `postgresql-13-pg-graphql` | `postgresql-12-pg-graphql` |
| `u24` | `postgresql-17-pg-graphql` | `postgresql-16-pg-graphql` | `postgresql-15-pg-graphql` | `postgresql-14-pg-graphql` | `postgresql-13-pg-graphql` | `postgresql-12-pg-graphql` |



Install `pg_graphql` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_graphql"]}'
```


Install `pg_graphql` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install pg_graphql_17;
yum install pg_graphql_16;
yum install pg_graphql_15;
yum install pg_graphql_14;
yum install pg_graphql_13;
yum install pg_graphql_12;
```


Install `pg_graphql` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-graphql;
apt install postgresql-16-pg-graphql;
apt install postgresql-15-pg-graphql;
apt install postgresql-14-pg-graphql;
apt install postgresql-13-pg-graphql;
apt install postgresql-12-pg-graphql;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_graphql_17` | `pg_graphql_16` | `pg_graphql_15` | `pg_graphql_14` | `pg_graphql_13` | `pg_graphql_12` |
| `el9` | `pg_graphql_17` | `pg_graphql_16` | `pg_graphql_15` | `pg_graphql_14` | `pg_graphql_13` | `pg_graphql_12` |
| `d12` | `postgresql-17-pg-graphql` | `postgresql-16-pg-graphql` | `postgresql-15-pg-graphql` | `postgresql-14-pg-graphql` | `postgresql-13-pg-graphql` | `postgresql-12-pg-graphql` |
| `u22` | `postgresql-17-pg-graphql` | `postgresql-16-pg-graphql` | `postgresql-15-pg-graphql` | `postgresql-14-pg-graphql` | `postgresql-13-pg-graphql` | `postgresql-12-pg-graphql` |
| `u24` | `postgresql-17-pg-graphql` | `postgresql-16-pg-graphql` | `postgresql-15-pg-graphql` | `postgresql-14-pg-graphql` | `postgresql-13-pg-graphql` | `postgresql-12-pg-graphql` |






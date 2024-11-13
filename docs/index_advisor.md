# index_advisor


> [index_advisor](https://github.com/supabase/index_advisor): Query index advisor
>
> https://github.com/supabase/index_advisor





[FEAT](/feat) extensions: [`age`](/age), [`hll`](/hll), [`rum`](/rum), [`pg_graphql`](/pg_graphql), [`pg_jsonschema`](/pg_jsonschema), [`jsquery`](/jsquery), [`pg_hint_plan`](/pg_hint_plan), [`hypopg`](/hypopg), [`index_advisor`](/index_advisor), [`plan_filter`](/plan_filter), [`imgsmlr`](/imgsmlr), [`pg_ivm`](/pg_ivm), [`pgmq`](/pgmq), [`pgq`](/pgq), [`pg_cardano`](/pg_cardano), [`rdkit`](/rdkit), [`bloom`](/bloom)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [index_advisor](https://github.com/supabase/index_advisor) | 0.2.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [index_advisor](/index_advisor) | `supabase` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION index_advisor;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `index_advisor_17` | `index_advisor_16` | `index_advisor_15` | `index_advisor_14` | `index_advisor_13` | `index_advisor_12` |
| `el9` | `index_advisor_17` | `index_advisor_16` | `index_advisor_15` | `index_advisor_14` | `index_advisor_13` | `index_advisor_12` |
| `d12` | `postgresql-17-index-advisor` | `postgresql-16-index-advisor` | `postgresql-15-index-advisor` | `postgresql-14-index-advisor` | `postgresql-13-index-advisor` | `postgresql-12-index-advisor` |
| `u22` | `postgresql-17-index-advisor` | `postgresql-16-index-advisor` | `postgresql-15-index-advisor` | `postgresql-14-index-advisor` | `postgresql-13-index-advisor` | `postgresql-12-index-advisor` |
| `u24` | `postgresql-17-index-advisor` | `postgresql-16-index-advisor` | `postgresql-15-index-advisor` | `postgresql-14-index-advisor` | `postgresql-13-index-advisor` | `postgresql-12-index-advisor` |



Install `index_advisor` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["index_advisor"]}'
```


Install `index_advisor` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install index_advisor_17;
yum install index_advisor_16;
yum install index_advisor_15;
yum install index_advisor_14;
yum install index_advisor_13;
yum install index_advisor_12;
```


Install `index_advisor` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-index-advisor;
apt install postgresql-16-index-advisor;
apt install postgresql-15-index-advisor;
apt install postgresql-14-index-advisor;
apt install postgresql-13-index-advisor;
apt install postgresql-12-index-advisor;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `index_advisor_17` | `index_advisor_16` | `index_advisor_15` | `index_advisor_14` | `index_advisor_13` | `index_advisor_12` |
| `el9` | `index_advisor_17` | `index_advisor_16` | `index_advisor_15` | `index_advisor_14` | `index_advisor_13` | `index_advisor_12` |
| `d12` | `postgresql-17-index-advisor` | `postgresql-16-index-advisor` | `postgresql-15-index-advisor` | `postgresql-14-index-advisor` | `postgresql-13-index-advisor` | `postgresql-12-index-advisor` |
| `u22` | `postgresql-17-index-advisor` | `postgresql-16-index-advisor` | `postgresql-15-index-advisor` | `postgresql-14-index-advisor` | `postgresql-13-index-advisor` | `postgresql-12-index-advisor` |
| `u24` | `postgresql-17-index-advisor` | `postgresql-16-index-advisor` | `postgresql-15-index-advisor` | `postgresql-14-index-advisor` | `postgresql-13-index-advisor` | `postgresql-12-index-advisor` |






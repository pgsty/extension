# hypopg


> [hypopg](https://github.com/HypoPG/hypopg): Hypothetical indexes for PostgreSQL
>
> https://github.com/HypoPG/hypopg





[FEAT](/feat) extensions: [`age`](/age), [`hll`](/hll), [`rum`](/rum), [`pg_graphql`](/pg_graphql), [`pg_jsonschema`](/pg_jsonschema), [`jsquery`](/jsquery), [`pg_hint_plan`](/pg_hint_plan), [`hypopg`](/hypopg), [`index_advisor`](/index_advisor), [`plan_filter`](/plan_filter), [`imgsmlr`](/imgsmlr), [`pg_ivm`](/pg_ivm), [`pgmq`](/pgmq), [`pgq`](/pgq), [`pg_cardano`](/pg_cardano), [`rdkit`](/rdkit), [`bloom`](/bloom)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [hypopg](https://github.com/HypoPG/hypopg) | 1.4.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [hypopg](/hypopg) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION hypopg;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `hypopg_17*` | `hypopg_16*` | `hypopg_15*` | `hypopg_14*` | `hypopg_13*` | `hypopg_12*` |
| `el9` | `hypopg_17*` | `hypopg_16*` | `hypopg_15*` | `hypopg_14*` | `hypopg_13*` | `hypopg_12*` |
| `d12` | `postgresql-17-hypopg` | `postgresql-16-hypopg` | `postgresql-15-hypopg` | `postgresql-14-hypopg` | `postgresql-13-hypopg` | `postgresql-12-hypopg` |
| `u22` | `postgresql-17-hypopg` | `postgresql-16-hypopg` | `postgresql-15-hypopg` | `postgresql-14-hypopg` | `postgresql-13-hypopg` | `postgresql-12-hypopg` |
| `u24` | `postgresql-17-hypopg` | `postgresql-16-hypopg` | `postgresql-15-hypopg` | `postgresql-14-hypopg` | `postgresql-13-hypopg` | `postgresql-12-hypopg` |



Install `hypopg` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["hypopg"]}'
```


Install `hypopg` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install hypopg_17*;
yum install hypopg_16*;
yum install hypopg_15*;
yum install hypopg_14*;
yum install hypopg_13*;
yum install hypopg_12*;
```


Install `hypopg` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-hypopg;
apt install postgresql-16-hypopg;
apt install postgresql-15-hypopg;
apt install postgresql-14-hypopg;
apt install postgresql-13-hypopg;
apt install postgresql-12-hypopg;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `hypopg_17*` | `hypopg_16*` | `hypopg_15*` | `hypopg_14*` | `hypopg_13*` | `hypopg_12*` |
| `el9` | `hypopg_17*` | `hypopg_16*` | `hypopg_15*` | `hypopg_14*` | `hypopg_13*` | `hypopg_12*` |
| `d12` | `postgresql-17-hypopg` | `postgresql-16-hypopg` | `postgresql-15-hypopg` | `postgresql-14-hypopg` | `postgresql-13-hypopg` | `postgresql-12-hypopg` |
| `u22` | `postgresql-17-hypopg` | `postgresql-16-hypopg` | `postgresql-15-hypopg` | `postgresql-14-hypopg` | `postgresql-13-hypopg` | `postgresql-12-hypopg` |
| `u24` | `postgresql-17-hypopg` | `postgresql-16-hypopg` | `postgresql-15-hypopg` | `postgresql-14-hypopg` | `postgresql-13-hypopg` | `postgresql-12-hypopg` |






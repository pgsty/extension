# imgsmlr


> [imgsmlr](https://github.com/postgrespro/imgsmlr): Image similarity with haar
>
> https://github.com/postgrespro/imgsmlr





[FEAT](/feat) extensions: [`age`](/age), [`hll`](/hll), [`rum`](/rum), [`pg_graphql`](/pg_graphql), [`pg_jsonschema`](/pg_jsonschema), [`jsquery`](/jsquery), [`pg_hint_plan`](/pg_hint_plan), [`hypopg`](/hypopg), [`index_advisor`](/index_advisor), [`plan_filter`](/plan_filter), [`imgsmlr`](/imgsmlr), [`pg_ivm`](/pg_ivm), [`pgmq`](/pgmq), [`pgq`](/pgq), [`pg_cardano`](/pg_cardano), [`rdkit`](/rdkit), [`bloom`](/bloom)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [imgsmlr](https://github.com/postgrespro/imgsmlr) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [imgsmlr](/imgsmlr) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION imgsmlr;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `imgsmlr_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-imgsmlr` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `imgsmlr` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["imgsmlr"]}'
```


Install `imgsmlr` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install imgsmlr_17*;
dnf install imgsmlr_16*;
dnf install imgsmlr_15*;
dnf install imgsmlr_14*;
dnf install imgsmlr_13*;
dnf install imgsmlr_12*;
```


Install `imgsmlr` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-imgsmlr;
apt install postgresql-16-imgsmlr;
apt install postgresql-15-imgsmlr;
apt install postgresql-14-imgsmlr;
apt install postgresql-13-imgsmlr;
apt install postgresql-12-imgsmlr;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `imgsmlr_17*` | `imgsmlr_16*` | `imgsmlr_15*` | `imgsmlr_14*` | `imgsmlr_13*` | `imgsmlr_12*` |
| `el9` | `imgsmlr_17*` | `imgsmlr_16*` | `imgsmlr_15*` | `imgsmlr_14*` | `imgsmlr_13*` | `imgsmlr_12*` |
| `d12` | `postgresql-17-imgsmlr` | `postgresql-16-imgsmlr` | `postgresql-15-imgsmlr` | `postgresql-14-imgsmlr` | `postgresql-13-imgsmlr` | `postgresql-12-imgsmlr` |
| `u22` | `postgresql-17-imgsmlr` | `postgresql-16-imgsmlr` | `postgresql-15-imgsmlr` | `postgresql-14-imgsmlr` | `postgresql-13-imgsmlr` | `postgresql-12-imgsmlr` |
| `u24` | `postgresql-17-imgsmlr` | `postgresql-16-imgsmlr` | `postgresql-15-imgsmlr` | `postgresql-14-imgsmlr` | `postgresql-13-imgsmlr` | `postgresql-12-imgsmlr` |






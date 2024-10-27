# pg_cardano


> [pg_cardano](/https://github.com/Fell-x27/pg_cardano): A suite of Cardano-related tools


-------

## Extension


| ID | Extension | Version | License | RPM | DEB | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:--:|-----------|:-------:|:-------:|:---:|:---:|:------:|:-------:|:-----:|:-------:|:-------:|
| 1840 | [pg_cardano](https://github.com/Fell-x27/pg_cardano) | 1.0.2 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |





```sql
CREATE EXTENSION pg_cardano;
```



-----------


## Packages


| OS | Version | License | RPM | RPM Package | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0.2 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_cardano_$v` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |
| [DEB](/deb) | 1.0.2 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-cardano` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |



Install `pg_cardano` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_cardano"]}'
```


Install `pg_cardano` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_cardano_17;
dnf install pg_cardano_16;
dnf install pg_cardano_15;
dnf install pg_cardano_14;
dnf install pg_cardano_13;
dnf install pg_cardano_12;
```


Install `pg_cardano` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-cardano;
apt install postgresql-16-pg-cardano;
apt install postgresql-15-pg-cardano;
apt install postgresql-14-pg-cardano;
apt install postgresql-13-pg-cardano;
apt install postgresql-12-pg-cardano;
```


-----------


## Category: FEAT


| ID | Extension | Version | Package | License | RPM | DEB | PL | Tags | Schemas | Requires | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:--:|------|---------|----------|:------:|:-------:|:-----:|:-------:|:-------:|
| 1700 | [age](/age) | 1.5.0 | [age](/age) | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** |  |  | `ag_catalog` |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1710 | [hll](/hll) | 2.18 | [hll](/hll) | **<span class="tccyan">Apache-2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1720 | [rum](/rum) | 1.3 | [rum](/rum) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1730 | [pg_graphql](/pg_graphql) | 1.5.9 | [pg_graphql](/pg_graphql) | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` | `pgrx`, `supabase` | `graphql` |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1750 | [pg_jsonschema](/pg_jsonschema) | 0.3.3 | [pg_jsonschema](/pg_jsonschema) | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` | `pgrx`, `supabase` |  |  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1760 | [jsquery](/jsquery) | 1.1 | [jsquery](/jsquery) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1770 | [pg_hint_plan](/pg_hint_plan) | 1.6.1 | [pg_hint_plan](/pg_hint_plan) | **<span class="tcblue">BSD-3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  | `hint_plan` |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1780 | [hypopg](/hypopg) | 1.4.1 | [hypopg](/hypopg) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1790 | [index_advisor](/index_advisor) | 0.2.0 | [index_advisor](/index_advisor) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` | `supabase` |  |  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |
| 1791 | [plan_filter](/plan_filter) | 0.0.1 | [pg_plan_filter](/plan_filter) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |  |  |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1800 | [imgsmlr](/imgsmlr) | 1.0 | [imgsmlr](/imgsmlr) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1810 | [pg_ivm](/pg_ivm) | 1.8 | [pg_ivm](/pg_ivm) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** |  |  | `pg_catalog` |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1820 | [pgmq](/pgmq) | 1.4.4 | [pgmq](/pgmq) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` |  | `pgmq` |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |
| 1830 | [pgq](/pgq) | 3.5.1 | [pgq](/pgq) | **<span class="tcblue">ISC</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |  | `pg_catalog` |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1840 | [pg_cardano](/pg_cardano) | 1.0.2 | [pg_cardano](/pg_cardano) | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` | `pgrx` |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |
| 1850 | [rdkit](/rdkit) | 4.3.0 | [rdkit](/rdkit) | **<span class="tcblue">BSD-3</span>** |  | **<span class="tccyan">PGDG</span>** |  |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |
| 1990 | [bloom](/bloom) | 1.0 | [bloom](/bloom) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | **<span class="tcblue">CONTRIB</span>** | `C` |  |  |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |




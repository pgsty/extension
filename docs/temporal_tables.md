# temporal_tables


> [temporal_tables](https://pgxn.org/dist/temporal_tables/): temporal tables
>
> https://pgxn.org/dist/temporal_tables/





[TIME](/time) extensions: [`timescaledb`](/timescaledb), [`timescaledb_toolkit`](/timescaledb_toolkit), [`timeseries`](/timeseries), [`periods`](/periods), [`temporal_tables`](/temporal_tables), [`emaj`](/emaj), [`table_version`](/table_version), [`pg_cron`](/pg_cron), [`pg_later`](/pg_later), [`pg_background`](/pg_background)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [temporal_tables](https://pgxn.org/dist/temporal_tables/) | 1.2.2 | **<span class="tcblue">BSD-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [temporal_tables](/temporal_tables) | `pgdg-flaw` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION temporal_tables;
```
> **Comment**: no pg17 on el8/9 pgdg repo
-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `temporal_tables_17*` | `temporal_tables_16*` | `temporal_tables_15*` | `temporal_tables_14*` | `temporal_tables_13*` | `temporal_tables_12*` |
| `el9` | `temporal_tables_17*` | `temporal_tables_16*` | `temporal_tables_15*` | `temporal_tables_14*` | `temporal_tables_13*` | `temporal_tables_12*` |
| `d12` | `postgresql-17-temporal-tables` | `postgresql-16-temporal-tables` | `postgresql-15-temporal-tables` | `postgresql-14-temporal-tables` | `postgresql-13-temporal-tables` | `postgresql-12-temporal-tables` |
| `u22` | `postgresql-17-temporal-tables` | `postgresql-16-temporal-tables` | `postgresql-15-temporal-tables` | `postgresql-14-temporal-tables` | `postgresql-13-temporal-tables` | `postgresql-12-temporal-tables` |
| `u24` | `postgresql-17-temporal-tables` | `postgresql-16-temporal-tables` | `postgresql-15-temporal-tables` | `postgresql-14-temporal-tables` | `postgresql-13-temporal-tables` | `postgresql-12-temporal-tables` |



Install `temporal_tables` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["temporal_tables"]}'
```


Install `temporal_tables` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install temporal_tables_17*;
yum install temporal_tables_16*;
yum install temporal_tables_15*;
yum install temporal_tables_14*;
yum install temporal_tables_13*;
yum install temporal_tables_12*;
```


Install `temporal_tables` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-temporal-tables;
apt install postgresql-16-temporal-tables;
apt install postgresql-15-temporal-tables;
apt install postgresql-14-temporal-tables;
apt install postgresql-13-temporal-tables;
apt install postgresql-12-temporal-tables;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `temporal_tables_17*` | `temporal_tables_16*` | `temporal_tables_15*` | `temporal_tables_14*` | `temporal_tables_13*` | `temporal_tables_12*` |
| `el9` | `temporal_tables_17*` | `temporal_tables_16*` | `temporal_tables_15*` | `temporal_tables_14*` | `temporal_tables_13*` | `temporal_tables_12*` |
| `d12` | `postgresql-17-temporal-tables` | `postgresql-16-temporal-tables` | `postgresql-15-temporal-tables` | `postgresql-14-temporal-tables` | `postgresql-13-temporal-tables` | `postgresql-12-temporal-tables` |
| `u22` | `postgresql-17-temporal-tables` | `postgresql-16-temporal-tables` | `postgresql-15-temporal-tables` | `postgresql-14-temporal-tables` | `postgresql-13-temporal-tables` | `postgresql-12-temporal-tables` |
| `u24` | `postgresql-17-temporal-tables` | `postgresql-16-temporal-tables` | `postgresql-15-temporal-tables` | `postgresql-14-temporal-tables` | `postgresql-13-temporal-tables` | `postgresql-12-temporal-tables` |






# pg_background


> [pg_background](https://github.com/vibhorkum/pg_background): Run SQL queries in the background
>
> https://github.com/vibhorkum/pg_background





[TIME](/time) extensions: [`timescaledb`](/timescaledb), [`timescaledb_toolkit`](/timescaledb_toolkit), [`timeseries`](/timeseries), [`periods`](/periods), [`temporal_tables`](/temporal_tables), [`emaj`](/emaj), [`table_version`](/table_version), [`pg_cron`](/pg_cron), [`pg_later`](/pg_later), [`pg_background`](/pg_background)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_background](https://github.com/vibhorkum/pg_background) | 1.3 | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_background](/pg_background) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_background;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_background_17*` | `pg_background_16*` | `pg_background_15*` | `pg_background_14*` | `pg_background_13*` | `pg_background_12*` |
| `el9` | `pg_background_17*` | `pg_background_16*` | `pg_background_15*` | `pg_background_14*` | `pg_background_13*` | `pg_background_12*` |
| `d12` | `postgresql-17-pg-background` | `postgresql-16-pg-background` | `postgresql-15-pg-background` | `postgresql-14-pg-background` | `postgresql-13-pg-background` | `postgresql-12-pg-background` |
| `u22` | `postgresql-17-pg-background` | `postgresql-16-pg-background` | `postgresql-15-pg-background` | `postgresql-14-pg-background` | `postgresql-13-pg-background` | `postgresql-12-pg-background` |
| `u24` | `postgresql-17-pg-background` | `postgresql-16-pg-background` | `postgresql-15-pg-background` | `postgresql-14-pg-background` | `postgresql-13-pg-background` | `postgresql-12-pg-background` |



Install `pg_background` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_background"]}'
```


Install `pg_background` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install pg_background_17*;
yum install pg_background_16*;
yum install pg_background_15*;
yum install pg_background_14*;
yum install pg_background_13*;
yum install pg_background_12*;
```


Install `pg_background` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pg-background;
apt install postgresql-16-pg-background;
apt install postgresql-15-pg-background;
apt install postgresql-14-pg-background;
apt install postgresql-13-pg-background;
apt install postgresql-12-pg-background;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_background_17*` | `pg_background_16*` | `pg_background_15*` | `pg_background_14*` | `pg_background_13*` | `pg_background_12*` |
| `el9` | `pg_background_17*` | `pg_background_16*` | `pg_background_15*` | `pg_background_14*` | `pg_background_13*` | `pg_background_12*` |
| `d12` | `postgresql-17-pg-background` | `postgresql-16-pg-background` | `postgresql-15-pg-background` | `postgresql-14-pg-background` | `postgresql-13-pg-background` | `postgresql-12-pg-background` |
| `u22` | `postgresql-17-pg-background` | `postgresql-16-pg-background` | `postgresql-15-pg-background` | `postgresql-14-pg-background` | `postgresql-13-pg-background` | `postgresql-12-pg-background` |
| `u24` | `postgresql-17-pg-background` | `postgresql-16-pg-background` | `postgresql-15-pg-background` | `postgresql-14-pg-background` | `postgresql-13-pg-background` | `postgresql-12-pg-background` |






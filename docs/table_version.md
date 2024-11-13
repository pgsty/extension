# table_version


> [table_version](https://github.com/linz/postgresql-tableversion): PostgreSQL table versioning extension
>
> https://github.com/linz/postgresql-tableversion





[TIME](/time) extensions: [`timescaledb`](/timescaledb), [`timescaledb_toolkit`](/timescaledb_toolkit), [`timeseries`](/timeseries), [`periods`](/periods), [`temporal_tables`](/temporal_tables), [`emaj`](/emaj), [`table_version`](/table_version), [`pg_cron`](/pg_cron), [`pg_later`](/pg_later), [`pg_background`](/pg_background)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [table_version](https://github.com/linz/postgresql-tableversion) | 1.10.3 | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [table_version](/table_version) | `pgdg-flaw` | `table_version` | [`plpgsql`](plpgsql) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION table_version CASCADE;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `table_version_17*` | `table_version_16*` | `table_version_15*` | `table_version_14*` | `table_version_13*` | `table_version_12*` |
| `el9` | `table_version_17*` | `table_version_16*` | `table_version_15*` | `table_version_14*` | `table_version_13*` | `table_version_12*` |
| `d12` | `postgresql-17-tableversion` | `postgresql-16-tableversion` | `postgresql-15-tableversion` | `postgresql-14-tableversion` | `postgresql-13-tableversion` | `postgresql-12-tableversion` |
| `u22` | `postgresql-17-tableversion` | `postgresql-16-tableversion` | `postgresql-15-tableversion` | `postgresql-14-tableversion` | `postgresql-13-tableversion` | `postgresql-12-tableversion` |
| `u24` | `postgresql-17-tableversion` | `postgresql-16-tableversion` | `postgresql-15-tableversion` | `postgresql-14-tableversion` | `postgresql-13-tableversion` | `postgresql-12-tableversion` |



Install `table_version` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["table_version"]}'
```


Install `table_version` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install table_version_17*;
yum install table_version_16*;
yum install table_version_15*;
yum install table_version_14*;
yum install table_version_13*;
yum install table_version_12*;
```


Install `table_version` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-tableversion;
apt install postgresql-16-tableversion;
apt install postgresql-15-tableversion;
apt install postgresql-14-tableversion;
apt install postgresql-13-tableversion;
apt install postgresql-12-tableversion;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `table_version_17*` | `table_version_16*` | `table_version_15*` | `table_version_14*` | `table_version_13*` | `table_version_12*` |
| `el9` | `table_version_17*` | `table_version_16*` | `table_version_15*` | `table_version_14*` | `table_version_13*` | `table_version_12*` |
| `d12` | `postgresql-17-tableversion` | `postgresql-16-tableversion` | `postgresql-15-tableversion` | `postgresql-14-tableversion` | `postgresql-13-tableversion` | `postgresql-12-tableversion` |
| `u22` | `postgresql-17-tableversion` | `postgresql-16-tableversion` | `postgresql-15-tableversion` | `postgresql-14-tableversion` | `postgresql-13-tableversion` | `postgresql-12-tableversion` |
| `u24` | `postgresql-17-tableversion` | `postgresql-16-tableversion` | `postgresql-15-tableversion` | `postgresql-14-tableversion` | `postgresql-13-tableversion` | `postgresql-12-tableversion` |






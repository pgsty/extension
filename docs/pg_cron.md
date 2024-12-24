# pg_cron


> [pg_cron](https://github.com/citusdata/pg_cron): Job scheduler for PostgreSQL
>
> https://github.com/citusdata/pg_cron





[TIME](/time) extensions: [`timescaledb`](/timescaledb), [`timeseries`](/timeseries), [`periods`](/periods), [`temporal_tables`](/temporal_tables), [`emaj`](/emaj), [`table_version`](/table_version), [`pg_cron`](/pg_cron), [`pg_later`](/pg_later), [`pg_background`](/pg_background)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_cron](https://github.com/citusdata/pg_cron) | 1.6 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_cron](/pg_cron) |  | `pg_catalog` |  | [`timeseries`](/timeseries), [`vectorize`](/vectorize) |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'pg_cron'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION pg_cron;
```
> **Comment**: require cron.database_name
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.6 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pg_cron_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 1.6 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-cron` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pg_cron` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_cron
```


Install `pg_cron` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_cron"]}'
```


Install `pg_cron` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pg_cron_17*;
dnf install pg_cron_16*;
dnf install pg_cron_15*;
dnf install pg_cron_14*;
dnf install pg_cron_13*;
```


Install `pg_cron` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-cron;
apt install postgresql-16-cron;
apt install postgresql-15-cron;
apt install postgresql-14-cron;
apt install postgresql-13-cron;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_cron_17*` | `pg_cron_16*` | `pg_cron_15*` | `pg_cron_14*` | `pg_cron_13*` |
| `el9` | `pg_cron_17*` | `pg_cron_16*` | `pg_cron_15*` | `pg_cron_14*` | `pg_cron_13*` |
| `d12` | `postgresql-17-cron` | `postgresql-16-cron` | `postgresql-15-cron` | `postgresql-14-cron` | `postgresql-13-cron` |
| `u22` | `postgresql-17-cron` | `postgresql-16-cron` | `postgresql-15-cron` | `postgresql-14-cron` | `postgresql-13-cron` |
| `u24` | `postgresql-17-cron` | `postgresql-16-cron` | `postgresql-15-cron` | `postgresql-14-cron` | `postgresql-13-cron` |






--------

## Usage

beware that `cron.database` has to be set before adding to `shared_preload_libraries`

```bash

```

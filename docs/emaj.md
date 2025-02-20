# emaj


> [emaj](https://github.com/dalibo/emaj): Enables fine-grained write logging and time travel on subsets of the database.
>
> https://github.com/dalibo/emaj





[TIME](/time) extensions: [`timescaledb`](/timescaledb), [`timescaledb_toolkit`](/timescaledb_toolkit), [`timeseries`](/timeseries), [`periods`](/periods), [`temporal_tables`](/temporal_tables), [`emaj`](/emaj), [`table_version`](/table_version), [`pg_cron`](/pg_cron), [`pg_task`](/pg_task), [`pg_later`](/pg_later), [`pg_background`](/pg_background)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [emaj](https://github.com/dalibo/emaj) | 4.5.0 | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [emaj](/emaj) |  | `emaj` | [`dblink`](dblink), [`btree_gist`](btree_gist) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION emaj CASCADE;
```
> **Comment**: max_prepared_transactions
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 4.5.0 | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | `e-maj_$v` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 4.4.0 | **<span class="tcwarn">GPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-emaj` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `emaj` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add emaj
```


Install `emaj` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["emaj"]}'
```


Install `emaj` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install e-maj_17;
dnf install e-maj_16;
dnf install e-maj_15;
dnf install e-maj_14;
dnf install e-maj_13;
```


Install `emaj` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-emaj;
apt install postgresql-16-emaj;
apt install postgresql-15-emaj;
apt install postgresql-14-emaj;
apt install postgresql-13-emaj;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `e-maj_17` | `e-maj_16` | `e-maj_15` | `e-maj_14` | `e-maj_13` |
| `el9` | `e-maj_17` | `e-maj_16` | `e-maj_15` | `e-maj_14` | `e-maj_13` |
| `d12` | `postgresql-17-emaj` | `postgresql-16-emaj` | `postgresql-15-emaj` | `postgresql-14-emaj` | `postgresql-13-emaj` |
| `u22` | `postgresql-17-emaj` | `postgresql-16-emaj` | `postgresql-15-emaj` | `postgresql-14-emaj` | `postgresql-13-emaj` |
| `u24` | `postgresql-17-emaj` | `postgresql-16-emaj` | `postgresql-15-emaj` | `postgresql-14-emaj` | `postgresql-13-emaj` |






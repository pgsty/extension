# pg_task


> [pg_task](https://github.com/RekGRpth/pg_task): execute any sql command at any specific time at background
>
> https://github.com/RekGRpth/pg_task





[TIME](/time) extensions: [`timescaledb`](/timescaledb), [`timescaledb_toolkit`](/timescaledb_toolkit), [`timeseries`](/timeseries), [`periods`](/periods), [`temporal_tables`](/temporal_tables), [`emaj`](/emaj), [`table_version`](/table_version), [`pg_cron`](/pg_cron), [`pg_task`](/pg_task), [`pg_later`](/pg_later), [`pg_background`](/pg_background)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_task](https://github.com/RekGRpth/pg_task) | 1.0.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_task](/pg_task) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'pg_task'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION pg_task;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `pg_task_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 1.0.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-task` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pg_task` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_task
```


Install `pg_task` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_task"]}'
```


Install `pg_task` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pg_task_17*;
dnf install pg_task_16*;
dnf install pg_task_15*;
dnf install pg_task_14*;
dnf install pg_task_13*;
```


Install `pg_task` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pg-task;
apt install postgresql-16-pg-task;
apt install postgresql-15-pg-task;
apt install postgresql-14-pg-task;
apt install postgresql-13-pg-task;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_task_17*` | `pg_task_16*` | `pg_task_15*` | `pg_task_14*` | `pg_task_13*` |
| `el9` | `pg_task_17*` | `pg_task_16*` | `pg_task_15*` | `pg_task_14*` | `pg_task_13*` |
| `d12` | `postgresql-17-pg-task` | `postgresql-16-pg-task` | `postgresql-15-pg-task` | `postgresql-14-pg-task` | `postgresql-13-pg-task` |
| `u22` | `postgresql-17-pg-task` | `postgresql-16-pg-task` | `postgresql-15-pg-task` | `postgresql-14-pg-task` | `postgresql-13-pg-task` |
| `u24` | `postgresql-17-pg-task` | `postgresql-16-pg-task` | `postgresql-15-pg-task` | `postgresql-14-pg-task` | `postgresql-13-pg-task` |






# timeseries


> [pg_timeseries](https://github.com/tembo-io/pg_timeseries): Convenience API for Tembo time series stack
>
> https://github.com/tembo-io/pg_timeseries





[TIME](/time) extensions: [`timescaledb`](/timescaledb), [`timeseries`](/timeseries), [`periods`](/periods), [`temporal_tables`](/temporal_tables), [`emaj`](/emaj), [`table_version`](/table_version), [`pg_cron`](/pg_cron), [`pg_task`](/pg_task), [`pg_later`](/pg_later), [`pg_background`](/pg_background)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [timeseries](https://github.com/tembo-io/pg_timeseries) | 0.1.6 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_timeseries](/timeseries) |  |  | [`columnar`](columnar), [`pg_cron`](pg_cron), [`pg_ivm`](pg_ivm), [`pg_partman`](pg_partman) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcred">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcred">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcred">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcred">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcred">✘</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcred">✘</span> |





```sql
CREATE EXTENSION timeseries CASCADE;
```
> **Comment**: unmet deps: hydra17 not ready, pg_partman17/pg_ivm12 on el not ready
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.1.6 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_timeseries_$v` |  | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | `hydra_$v`, `pg_cron_$v`, `pg_ivm_$v`, `pg_partman_$v` |
| [DEB](/deb) | 0.1.6 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-timeseries` |  | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `timeseries` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add timeseries
```


Install `pg_timeseries` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_timeseries"]}'
```


Install `pg_timeseries` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_timeseries_16;
dnf install pg_timeseries_15;
dnf install pg_timeseries_14;
dnf install pg_timeseries_13;
```


Install `pg_timeseries` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-16-pg-timeseries;
apt install postgresql-15-pg-timeseries;
apt install postgresql-14-pg-timeseries;
apt install postgresql-13-pg-timeseries;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcred">✘</span> | `pg_timeseries_16` | `pg_timeseries_15` | `pg_timeseries_14` | `pg_timeseries_13` |
| `el9` | <span class="tcred">✘</span> | `pg_timeseries_16` | `pg_timeseries_15` | `pg_timeseries_14` | `pg_timeseries_13` |
| `d12` | <span class="tcred">✘</span> | `postgresql-16-pg-timeseries` | `postgresql-15-pg-timeseries` | `postgresql-14-pg-timeseries` | `postgresql-13-pg-timeseries` |
| `u22` | <span class="tcred">✘</span> | `postgresql-16-pg-timeseries` | `postgresql-15-pg-timeseries` | `postgresql-14-pg-timeseries` | `postgresql-13-pg-timeseries` |
| `u24` | <span class="tcred">✘</span> | `postgresql-16-pg-timeseries` | `postgresql-15-pg-timeseries` | `postgresql-14-pg-timeseries` | <span class="tcred">✘</span> |






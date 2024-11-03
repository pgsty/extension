# pg_timeseries


> [pg_timeseries](https://github.com/tembo-io/pg_timeseries): Convenience API for Tembo time series stack
>
> https://github.com/tembo-io/pg_timeseries





[TIME](/time) extensions: [`timescaledb`](/timescaledb), [`timescaledb_toolkit`](/timescaledb_toolkit), [`timeseries`](/timeseries), [`periods`](/periods), [`temporal_tables`](/temporal_tables), [`emaj`](/emaj), [`table_version`](/table_version), [`pg_cron`](/pg_cron), [`pg_later`](/pg_later), [`pg_background`](/pg_background)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [timeseries](https://github.com/tembo-io/pg_timeseries) | 0.1.6 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` |  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Package | Tags | Schemas | Requires | Required by |
|---------|------|---------|----------|-------------|
| [pg_timeseries](/timeseries) |  |  | [`columnar`](columnar), [`pg_cron`](pg_cron), [`pg_ivm`](pg_ivm), [`pg_partman`](pg_partman) |  |





```sql
CREATE EXTENSION timeseries CASCADE;
```
> **Comment**: unmet deps: hydra17 not ready, pg_partman17/pg_ivm12 on el not ready
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.1.6 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_timeseries_$v` |  | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | `hydra_$v`, `pg_cron_$v`, `pg_ivm_$v`, `pg_partman_$v` |
| [DEB](/deb) | 0.1.6 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-timeseries` |  | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |  |



Install `pg_timeseries` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

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
apt install postgresql-12-pg-timeseries;
```








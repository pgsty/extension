# timescaledb_toolkit


> [timescaledb_toolkit](https://github.com/timescale/timescaledb-toolkit): Library of analytical hyperfunctions, time-series pipelining, and other SQL utilities
>
> https://github.com/timescale/timescaledb-toolkit





[TIME](/time) extensions: [`timescaledb`](/timescaledb), [`timescaledb_toolkit`](/timescaledb_toolkit), [`timeseries`](/timeseries), [`periods`](/periods), [`temporal_tables`](/temporal_tables), [`emaj`](/emaj), [`table_version`](/table_version), [`pg_cron`](/pg_cron), [`pg_later`](/pg_later), [`pg_background`](/pg_background)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL | `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|-----------|:-------:|:-------:|:---:|:---:|:--:|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
| [timescaledb_toolkit](https://github.com/timescale/timescaledb-toolkit) | 1.18.0 | **<span class="tcwarn">Timescale</span>** | **<span class="tcwarn">TIMESCALE</span>** | **<span class="tcwarn">TIMESCALE</span>** | `Rust` |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |



| Package | Tags | Schemas | Requires | Required by |
|---------|------|---------|----------|-------------|
| [timescaledb_toolkit](/timescaledb_toolkit) |  |  |  |  |





```sql
CREATE EXTENSION timescaledb_toolkit;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.18.0 | **<span class="tcwarn">Timescale</span>** | **<span class="tcwarn">TIMESCALE</span>** | `timescaledb-toolkit-postgresql-$v` |  | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.18.0 | **<span class="tcwarn">Timescale</span>** | **<span class="tcwarn">TIMESCALE</span>** | `timescaledb-toolkit-postgresql-$v` |  | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `timescaledb_toolkit` via [Pigsty](https://pigsty.cc/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["timescaledb_toolkit"]}'
```


Install `timescaledb_toolkit` [RPM](/rpm) from the **<span class="tcwarn">TIMESCALE</span>** **YUM** repo:

```bash
dnf install timescaledb-toolkit-postgresql-16;
dnf install timescaledb-toolkit-postgresql-15;
dnf install timescaledb-toolkit-postgresql-14;
dnf install timescaledb-toolkit-postgresql-13;
dnf install timescaledb-toolkit-postgresql-12;
```


Install `timescaledb_toolkit` [DEB](/deb) from the **<span class="tcwarn">TIMESCALE</span>** **APT** repo:

```bash
apt install timescaledb-toolkit-postgresql-16;
apt install timescaledb-toolkit-postgresql-15;
apt install timescaledb-toolkit-postgresql-14;
apt install timescaledb-toolkit-postgresql-13;
apt install timescaledb-toolkit-postgresql-12;
```








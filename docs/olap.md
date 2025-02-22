# OLAP


> OLAP: DuckDB Integration with FDW & PG Lakehouse, Access Parquet from File/S3, Sharding with Citus/Partman/PlProxy, ...
## Extensions


There are 13 available extensions in this category:

[`citus`](/citus) [`citus_columnar`](/citus_columnar) [`columnar`](/columnar) [`pg_analytics`](/pg_analytics) [`pg_duckdb`](/pg_duckdb) [`pg_mooncake`](/pg_mooncake) [`duckdb_fdw`](/duckdb_fdw) [`pg_parquet`](/pg_parquet) [`pg_fkpart`](/pg_fkpart) [`pg_partman`](/pg_partman) [`plproxy`](/plproxy) [`pg_strom`](/pg_strom) [`tablefunc`](/tablefunc)


| ID | Extension | Version | Package | License | RPM | DEB | Website | `Bin` | `LOAD` | `DYLIB` | `DDL` | Description |
|:--:|-----------|:-------:|---------|:-------:|:---:|:---:|:-------:|:-----:|:------:|:-------:|:-----:|-------------|
| 2400 | [citus](/citus) | 13.0.1 | [citus](/citus) | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/citusdata/citus) |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Distributed PostgreSQL as an extension |
| 2401 | [citus_columnar](/citus_columnar) | 11.3-1 | [citus](/citus_columnar) | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/citusdata/citus) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Citus columnar storage engine |
| 2410 | [columnar](/columnar) | 11.1-11 | [hydra](/columnar) | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/hydradatabase/hydra) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Hydra Columnar extension |
| 2420 | [pg_analytics](/pg_analytics) | 0.3.4 | [pg_analytics](/pg_analytics) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/paradedb/pg_analytics) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Postgres for analytics, powered by DuckDB |
| 2430 | [pg_duckdb](/pg_duckdb) | 0.2.0 | [pg_duckdb](/pg_duckdb) | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/duckdb/pg_duckdb) |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | DuckDB Embedded in Postgres |
| 2440 | [pg_mooncake](/pg_mooncake) | 0.1.2 | [pg_mooncake](/pg_mooncake) | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/Mooncake-Labs/pg_mooncake) |  |  | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> | Columnstore Table in Postgres |
| 2450 | [duckdb_fdw](/duckdb_fdw) | 1.1.2 | [duckdb_fdw](/duckdb_fdw) | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/alitrack/duckdb_fdw) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | DuckDB Foreign Data Wrapper |
| 2460 | [pg_parquet](/pg_parquet) | 0.2.0 | [pg_parquet](/pg_parquet) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/CrunchyData/pg_parquet/) |  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | copy data between Postgres and Parquet |
| 2500 | [pg_fkpart](/pg_fkpart) | 1.7 | [pg_fkpart](/pg_fkpart) | **<span class="tcwarn">GPLv2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | [LINK](https://github.com/lemoineat/pg_fkpart) |  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | Table partitioning by foreign key utility |
| 2510 | [pg_partman](/pg_partman) | 5.2.4 | [pg_partman](/pg_partman) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/pgpartman/pg_partman) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Extension to manage partitioned tables by time or ID |
| 2520 | [plproxy](/plproxy) | 2.11.0 | [plproxy](/plproxy) | **<span class="tcblue">BSD-0</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** | [LINK](https://github.com/plproxy/plproxy) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | Database partitioning implemented as procedural language |
| 2530 | [pg_strom](/pg_strom) | 5.1 | [pg_strom](/pg_strom) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** |  | [LINK](https://github.com/heterodb/pg-strom) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | PG-Strom - big-data processing acceleration using GPU and NVME |
| 2590 | [tablefunc](/tablefunc) | 1.0 | [tablefunc](/tablefunc) | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | **<span class="tcblue">CONTRIB</span>** | [LINK](https://www.postgresql.org/docs/current/tablefunc.html) |  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | functions that manipulate whole tables, including crosstab |



### RHEL 8 Compatible (el8)

```yaml
pg17: citus pg_analytics pg_mooncake duckdb_fdw pg_parquet pg_fkpart pg_partman plproxy #hydra #pg_duckdb #pg_strom
pg16: citus hydra pg_analytics pg_mooncake duckdb_fdw pg_parquet pg_fkpart pg_partman plproxy #pg_duckdb #pg_strom
pg15: citus hydra pg_analytics pg_mooncake duckdb_fdw pg_parquet pg_fkpart pg_partman plproxy #pg_duckdb #pg_strom
pg14: citus hydra pg_analytics pg_mooncake duckdb_fdw pg_parquet pg_fkpart pg_partman plproxy #pg_duckdb #pg_strom
pg13: hydra duckdb_fdw pg_fkpart pg_partman plproxy #citus #pg_analytics #pg_duckdb #pg_mooncake #pg_parquet #pg_strom
```


### RHEL 9 Compatible (el9)

```yaml
pg17: citus pg_analytics pg_duckdb pg_mooncake duckdb_fdw pg_parquet pg_fkpart pg_partman plproxy #hydra #pg_strom
pg16: citus hydra pg_analytics pg_duckdb pg_mooncake duckdb_fdw pg_parquet pg_fkpart pg_partman plproxy #pg_strom
pg15: citus hydra pg_analytics pg_duckdb pg_mooncake duckdb_fdw pg_parquet pg_fkpart pg_partman plproxy #pg_strom
pg14: citus hydra pg_analytics pg_duckdb pg_mooncake duckdb_fdw pg_parquet pg_fkpart pg_partman plproxy #pg_strom
pg13: hydra duckdb_fdw pg_fkpart pg_partman plproxy #citus #pg_analytics #pg_duckdb #pg_mooncake #pg_parquet #pg_strom
```


### Debian 12 bookworm Compatible (d12)

```yaml
pg17: citus pg_analytics pg_duckdb pg_mooncake duckdb_fdw pg_parquet pg_fkpart pg_partman plproxy #hydra #pg_strom
pg16: citus hydra pg_analytics pg_duckdb pg_mooncake duckdb_fdw pg_parquet pg_fkpart pg_partman plproxy #pg_strom
pg15: citus hydra pg_analytics pg_duckdb pg_mooncake duckdb_fdw pg_parquet pg_fkpart pg_partman plproxy #pg_strom
pg14: citus hydra pg_analytics pg_duckdb pg_mooncake duckdb_fdw pg_parquet pg_fkpart pg_partman plproxy #pg_strom
pg13: hydra duckdb_fdw pg_fkpart pg_partman plproxy #citus #pg_analytics #pg_duckdb #pg_mooncake #pg_parquet #pg_strom
```


### Ubuntu 24.04 jammy Compatible (u22)

```yaml
pg17: citus pg_analytics pg_duckdb pg_mooncake duckdb_fdw pg_parquet pg_fkpart pg_partman plproxy #hydra #pg_strom
pg16: citus hydra pg_analytics pg_duckdb pg_mooncake duckdb_fdw pg_parquet pg_fkpart pg_partman plproxy #pg_strom
pg15: citus hydra pg_analytics pg_duckdb pg_mooncake duckdb_fdw pg_parquet pg_fkpart pg_partman plproxy #pg_strom
pg14: citus hydra pg_analytics pg_duckdb pg_mooncake duckdb_fdw pg_parquet pg_fkpart pg_partman plproxy #pg_strom
pg13: hydra duckdb_fdw pg_fkpart pg_partman plproxy #citus #pg_analytics #pg_duckdb #pg_mooncake #pg_parquet #pg_strom
```


### Ubuntu 24.04 noble Compatible (u24)

```yaml
pg17: citus pg_analytics pg_duckdb pg_mooncake duckdb_fdw pg_parquet pg_fkpart pg_partman plproxy #hydra #pg_strom
pg16: citus hydra pg_analytics pg_duckdb pg_mooncake duckdb_fdw pg_parquet pg_fkpart pg_partman plproxy #pg_strom
pg15: citus hydra pg_analytics pg_duckdb pg_mooncake duckdb_fdw pg_parquet pg_fkpart pg_partman plproxy #pg_strom
pg14: citus hydra pg_analytics pg_duckdb pg_mooncake duckdb_fdw pg_parquet pg_fkpart pg_partman plproxy #pg_strom
pg13: hydra duckdb_fdw pg_fkpart plproxy #citus #pg_analytics #pg_duckdb #pg_mooncake #pg_parquet #pg_partman #pg_strom
```



--------

## RPM Packages


| Package | Version | License | RPM | RPM Package | 17 | 16 | 15 | 14 | 13 | Description |
|---------|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|-------------|
| [citus](/citus) | 13.0-1 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `citus_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | Distributed PostgreSQL as an extension |
| [hydra](/columnar) | 11.1-11 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `hydra_$v*` |  | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Hydra Columnar extension |
| [pg_analytics](/pg_analytics) | 0.3.4 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_analytics_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | Postgres for analytics, powered by DuckDB |
| [pg_duckdb](/pg_duckdb) | 0.2.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_duckdb_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | DuckDB Embedded in Postgres |
| [pg_mooncake](/pg_mooncake) | 0.1.2 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_mooncake_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | Columnstore Table in Postgres |
| [duckdb_fdw](/duckdb_fdw) | 1.1.2 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `duckdb_fdw_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | DuckDB Foreign Data Wrapper |
| [pg_parquet](/pg_parquet) | 0.2.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_parquet_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | copy data between Postgres and Parquet |
| [pg_fkpart](/pg_fkpart) | 1.7 | **<span class="tcwarn">GPLv2</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_fkpart_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Table partitioning by foreign key utility |
| [pg_partman](/pg_partman) | 5.2.4 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pg_partman_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Extension to manage partitioned tables by time or ID |
| [plproxy](/plproxy) | 2.11.0 | **<span class="tcblue">BSD-0</span>** | **<span class="tcwarn">PIGSTY</span>** | `plproxy_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Database partitioning implemented as procedural language |
| [pg_strom](/pg_strom) | 5.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pg_strom_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | PG-Strom - big-data processing acceleration using GPU and NVME |
| [tablefunc](/tablefunc) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql$v-contrib` | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | functions that manipulate whole tables, including crosstab |



### RHEL 8 Compatible (el8)

```yaml
pg17: citus_17* pg_analytics_17 pg_mooncake_17* duckdb_fdw_17* pg_parquet_17 pg_fkpart_17 pg_partman_17* plproxy_17* #hydra_17* #pg_duckdb_17* #pg_strom_17*
pg16: citus_16* hydra_16* pg_analytics_16 pg_mooncake_16* duckdb_fdw_16* pg_parquet_16 pg_fkpart_16 pg_partman_16* plproxy_16* #pg_duckdb_16* #pg_strom_16*
pg15: citus_15* hydra_15* pg_analytics_15 pg_mooncake_15* duckdb_fdw_15* pg_parquet_15 pg_fkpart_15 pg_partman_15* plproxy_15* #pg_duckdb_15* #pg_strom_15*
pg14: citus_14* hydra_14* pg_analytics_14 pg_mooncake_14* duckdb_fdw_14* pg_parquet_14 pg_fkpart_14 pg_partman_14* plproxy_14* #pg_duckdb_14* #pg_strom_14*
pg13: hydra_13* duckdb_fdw_13* pg_fkpart_13 pg_partman_13* plproxy_13* #citus_13* #pg_analytics_13 #pg_duckdb_13* #pg_mooncake_13* #pg_parquet_13 #pg_strom_13*
```


### RHEL 9 Compatible (el9)

```yaml
pg17: citus_17* pg_analytics_17 pg_duckdb_17* pg_mooncake_17* duckdb_fdw_17* pg_parquet_17 pg_fkpart_17 pg_partman_17* plproxy_17* #hydra_17* #pg_strom_17*
pg16: citus_16* hydra_16* pg_analytics_16 pg_duckdb_16* pg_mooncake_16* duckdb_fdw_16* pg_parquet_16 pg_fkpart_16 pg_partman_16* plproxy_16* #pg_strom_16*
pg15: citus_15* hydra_15* pg_analytics_15 pg_duckdb_15* pg_mooncake_15* duckdb_fdw_15* pg_parquet_15 pg_fkpart_15 pg_partman_15* plproxy_15* #pg_strom_15*
pg14: citus_14* hydra_14* pg_analytics_14 pg_duckdb_14* pg_mooncake_14* duckdb_fdw_14* pg_parquet_14 pg_fkpart_14 pg_partman_14* plproxy_14* #pg_strom_14*
pg13: hydra_13* duckdb_fdw_13* pg_fkpart_13 pg_partman_13* plproxy_13* #citus_13* #pg_analytics_13 #pg_duckdb_13* #pg_mooncake_13* #pg_parquet_13 #pg_strom_13*
```



--------

## DEB Packages


| Package | Version | License | DEB | DEB Package | 17 | 16 | 15 | 14 | 13 | Description |
|---------|---------|:-------:|:---:|-------------|:--:|:--:|:--:|:--:|:--:|-------------|
| [citus](/citus) | 13.0-1 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-citus` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | Distributed PostgreSQL as an extension |
| [hydra](/columnar) | 11.1-11 | **<span class="tcwarn">AGPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-hydra` |  | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Hydra Columnar extension |
| [pg_analytics](/pg_analytics) | 0.3.4 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-analytics` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | Postgres for analytics, powered by DuckDB |
| [pg_duckdb](/pg_duckdb) | 0.2.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-duckdb` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | DuckDB Embedded in Postgres |
| [pg_mooncake](/pg_mooncake) | 0.1.2 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-mooncake` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | Columnstore Table in Postgres |
| [duckdb_fdw](/duckdb_fdw) | 1.1.2 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-duckdb-fdw` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | DuckDB Foreign Data Wrapper |
| [pg_parquet](/pg_parquet) | 0.2.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-parquet` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  | copy data between Postgres and Parquet |
| [pg_fkpart](/pg_fkpart) | 1.7 | **<span class="tcwarn">GPLv2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-fkpart` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | Table partitioning by foreign key utility |
| [pg_partman](/pg_partman) | 5.2.4 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-partman` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Extension to manage partitioned tables by time or ID |
| [plproxy](/plproxy) | 2.11.0 | **<span class="tcblue">BSD-0</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-plproxy` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | Database partitioning implemented as procedural language |
| [tablefunc](/tablefunc) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql-$v` | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | functions that manipulate whole tables, including crosstab |



### Debian 12 bookworm Compatible (d12)

```yaml
pg17: postgresql-17-citus postgresql-17-pg-analytics postgresql-17-pg-duckdb postgresql-17-pg-mooncake postgresql-17-duckdb-fdw postgresql-17-pg-parquet postgresql-17-pg-fkpart postgresql-17-partman postgresql-17-plproxy #postgresql-17-hydra
pg16: postgresql-16-citus postgresql-16-hydra postgresql-16-pg-analytics postgresql-16-pg-duckdb postgresql-16-pg-mooncake postgresql-16-duckdb-fdw postgresql-16-pg-parquet postgresql-16-pg-fkpart postgresql-16-partman postgresql-16-plproxy
pg15: postgresql-15-citus postgresql-15-hydra postgresql-15-pg-analytics postgresql-15-pg-duckdb postgresql-15-pg-mooncake postgresql-15-duckdb-fdw postgresql-15-pg-parquet postgresql-15-pg-fkpart postgresql-15-partman postgresql-15-plproxy
pg14: postgresql-14-citus postgresql-14-hydra postgresql-14-pg-analytics postgresql-14-pg-duckdb postgresql-14-pg-mooncake postgresql-14-duckdb-fdw postgresql-14-pg-parquet postgresql-14-pg-fkpart postgresql-14-partman postgresql-14-plproxy
pg13: postgresql-13-hydra postgresql-13-duckdb-fdw postgresql-13-pg-fkpart postgresql-13-partman postgresql-13-plproxy #postgresql-13-citus #postgresql-13-pg-analytics #postgresql-13-pg-duckdb #postgresql-13-pg-mooncake #postgresql-13-pg-parquet
```


### Ubuntu 24.04 jammy Compatible (u22)

```yaml
pg17: postgresql-17-citus postgresql-17-pg-analytics postgresql-17-pg-duckdb postgresql-17-pg-mooncake postgresql-17-duckdb-fdw postgresql-17-pg-parquet postgresql-17-pg-fkpart postgresql-17-partman postgresql-17-plproxy #postgresql-17-hydra
pg16: postgresql-16-citus postgresql-16-hydra postgresql-16-pg-analytics postgresql-16-pg-duckdb postgresql-16-pg-mooncake postgresql-16-duckdb-fdw postgresql-16-pg-parquet postgresql-16-pg-fkpart postgresql-16-partman postgresql-16-plproxy
pg15: postgresql-15-citus postgresql-15-hydra postgresql-15-pg-analytics postgresql-15-pg-duckdb postgresql-15-pg-mooncake postgresql-15-duckdb-fdw postgresql-15-pg-parquet postgresql-15-pg-fkpart postgresql-15-partman postgresql-15-plproxy
pg14: postgresql-14-citus postgresql-14-hydra postgresql-14-pg-analytics postgresql-14-pg-duckdb postgresql-14-pg-mooncake postgresql-14-duckdb-fdw postgresql-14-pg-parquet postgresql-14-pg-fkpart postgresql-14-partman postgresql-14-plproxy
pg13: postgresql-13-hydra postgresql-13-duckdb-fdw postgresql-13-pg-fkpart postgresql-13-partman postgresql-13-plproxy #postgresql-13-citus #postgresql-13-pg-analytics #postgresql-13-pg-duckdb #postgresql-13-pg-mooncake #postgresql-13-pg-parquet
```


### Ubuntu 24.04 noble Compatible (u24)

```yaml
pg17: postgresql-17-citus postgresql-17-pg-analytics postgresql-17-pg-duckdb postgresql-17-pg-mooncake postgresql-17-duckdb-fdw postgresql-17-pg-parquet postgresql-17-pg-fkpart postgresql-17-partman postgresql-17-plproxy #postgresql-17-hydra
pg16: postgresql-16-citus postgresql-16-hydra postgresql-16-pg-analytics postgresql-16-pg-duckdb postgresql-16-pg-mooncake postgresql-16-duckdb-fdw postgresql-16-pg-parquet postgresql-16-pg-fkpart postgresql-16-partman postgresql-16-plproxy
pg15: postgresql-15-citus postgresql-15-hydra postgresql-15-pg-analytics postgresql-15-pg-duckdb postgresql-15-pg-mooncake postgresql-15-duckdb-fdw postgresql-15-pg-parquet postgresql-15-pg-fkpart postgresql-15-partman postgresql-15-plproxy
pg14: postgresql-14-citus postgresql-14-hydra postgresql-14-pg-analytics postgresql-14-pg-duckdb postgresql-14-pg-mooncake postgresql-14-duckdb-fdw postgresql-14-pg-parquet postgresql-14-pg-fkpart postgresql-14-partman postgresql-14-plproxy
pg13: postgresql-13-hydra postgresql-13-duckdb-fdw postgresql-13-pg-fkpart postgresql-13-plproxy #postgresql-13-citus #postgresql-13-pg-analytics #postgresql-13-pg-duckdb #postgresql-13-pg-mooncake #postgresql-13-pg-parquet #postgresql-13-partman
```



--------

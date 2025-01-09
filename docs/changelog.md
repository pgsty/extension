# Changelog

**2025-01-09**

- lower_quantile 1.0.3
- quantile 1.1.8
- sequential_uuids 1.0.3
- pgmq 1.5.0 (subdir)
- floatvec 1.1.1
- rename postgresql-$v-timescaledb to postgresql-$v-timescaledb-tsl

New extensions:

- add omnisketch 1.0.2
- add ddsketch 1.0.1
- add pg_duration 1.0.1
- add ddl_historization 0.0.7
- add data_historization 1.1.0
- add schedoc 0.0.1
- add floatfile 1.3.1 https://pgxn.org/dist/floatfile/1.3.1/
- add pg_upless https://pgxn.org/dist/pg_upless/0.0.3/
- add pg_task 1.0.0
- add pg_readme 0.7.0

```bash
make lower_quantile quantile ddsketch omnisketch sequential_uuids pgmq floatvec pg_timeseries timescaledb
make floatfile pg_upless pg_task pg_readme vasco pg_xxhash pg_duration ddl_historization data_historization pg_schedoc
```

**2025-01-08**

- pg_anon 2.0.0 
- pg_parquet 0.2.0 
- wrappers 0.4.4 
- pg_later 0.3.0 
- topn fix for deb.arm64
- add age 17 on debian
- powa + pg17, 5.0.1
- h3 + pg17
- ogr_fdw + pg17
- age + pg17 1.5 on debian
- rdkit + pg17 on u24 (TBD)
- pgtap + pg17 1.3.3
- repmgr
- topn + pg17
- add synchdb for ubuntu (TBD)


**2025-01-07**

- pg_partman 5.2.4
- credcheck 3.0
- ogr_fdw 1.1.5
- ddlx 0.29
- postgis 3.5.1
- tdigest 1.4.3
- pg_repack 1.5.2


**2024-12-30**

- Build citus on all deb distros (amd/arm)
- Build pgroonga on all deb distros (amd/arm)
- Build timescaledb on all deb distros (amd/arm)
- Add synchdb v1.0 for pg16 on ubuntu distros ()

**2024-12-24**

- Build citus for el aarch64 distros

**2024-12-23**

- Add `pig` 0.0.1, the Pigsty CLI tool

**2024-12-21**

- Build pg_timescaledb for EL distros
- Build pgroonga for all distros
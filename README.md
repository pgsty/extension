# PostgreSQL Extension Repo

[![Webite: ext.pigsty.io](https://img.shields.io/badge/website-ext.pigsty.io-slategray?style=flat&logo=cilium&logoColor=white)](https://ext.pigsty.io)
[![Extensions: 345](https://img.shields.io/badge/extensions-345-%233E668F?style=flat&logo=postgresql&logoColor=white&labelColor=3E668F)](https://pigsty.io/docs/pgext/list)
[![Postgres: 12-17](https://img.shields.io/badge/PostgreSQL-12~17-%233E668F?style=flat&logo=postgresql&labelColor=3E668F&logoColor=white)](https://pigsty.io/docs/pgsql)

The supplementary [APT](#apt-repo) and [YUM](#yum-repo) repo for PostgreSQL extensions, maintained and used by [Pigsty](https://pigsty.io)

Contains 150+ PG extensions for PostgreSQL 12 - 17 in addition to the official PGDG apt/yum repo.

Why extension matters to PostgreSQL? check the post: "[***PostgreSQL is eating the database world!***](https://medium.com/@fengruohang/postgres-is-eating-the-database-world-157c204dcfc4)"

-------

## Get Started

All rpm/deb packages are signed with GPG key `B9BD8B20` (`9592A7BC7A682E7333376E09E7935D8DB9BD8B20` ).

### YUM Repo

[![Linux](https://img.shields.io/badge/Linux-x86_64-%23FCC624?style=flat&logo=linux&labelColor=FCC624&logoColor=black)](https://pigsty.io/docs/node)
[![RHEL Support: 8/9](https://img.shields.io/badge/EL-7/8/9-red?style=flat&logo=redhat&logoColor=red)](https://pigsty.io/docs/pgext/list/rpm/)
[![RHEL](https://img.shields.io/badge/RHEL-slategray?style=flat&logo=redhat&logoColor=red)](https://pigsty.io/docs/pgext/list/rpm/)
[![CentOS](https://img.shields.io/badge/CentOS-slategray?style=flat&logo=centos&logoColor=%23262577)](https://almalinux.org/)
[![RockyLinux](https://img.shields.io/badge/RockyLinux-slategray?style=flat&logo=rockylinux&logoColor=%2310B981)](https://almalinux.org/)
[![AlmaLinux](https://img.shields.io/badge/AlmaLinux-slategray?style=flat&logo=almalinux&logoColor=black)](https://almalinux.org/)
[![OracleLinux](https://img.shields.io/badge/OracleLinux-slategray?style=flat&logo=oracle&logoColor=%23F80000)](https://almalinux.org/)

For EL 8/9 and compatible platforms, use the following commands to add the yum repo:

```bash
curl -fsSL https://repo.pigsty.io/key      | sudo tee /etc/pki/rpm-gpg/RPM-GPG-KEY-pigsty >/dev/null  # add gpg key
curl -fsSL https://repo.pigsty.io/yum/repo | sudo tee /etc/yum.repos.d/pigsty.repo        >/dev/null  # add repo file
sudo yum makecache
```

### APT Repo

[![Linux](https://img.shields.io/badge/Linux-x86_64-%23FCC624?style=flat&logo=linux&labelColor=FCC624&logoColor=black)](https://pigsty.io/docs/node)
[![Ubuntu Support: 22](https://img.shields.io/badge/Ubuntu-22-%23E95420?style=flat&logo=ubuntu&logoColor=%23E95420)](https://pigsty.io/docs/pgext/list/deb/)
[![Debian Support: 12](https://img.shields.io/badge/Debian-12-%23A81D33?style=flat&logo=debian&logoColor=%23A81D33)](https://pigsty.io/docs/reference/compatibility/)

For Ubuntu 22.04 & Debian 12 or any compatible platforms, use the following commands to add the APT repo:

```bash
curl -fsSL https://repo.pigsty.io/key | sudo gpg --dearmor -o /etc/apt/keyrings/pigsty.gpg
sudo tee /etc/apt/sources.list.d/pigsty-io.list > /dev/null <<EOF
deb [signed-by=/etc/apt/keyrings/pigsty.gpg] https://repo.pigsty.io/apt/infra generic main 
deb [signed-by=/etc/apt/keyrings/pigsty.gpg] https://repo.pigsty.io/apt/pgsql/$(lsb_release -cs) $(lsb_release -cs) main
EOF
sudo apt update
```

-------

## What's Inside

Linux x86_64/amd64 Extension packages for PostgreSQL 12 - 17, on El8, EL9, Ubuntu 22.04 and Debian 12.

|  Statistics   | All | PGDG | PIGSTY | MISC | MISS | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:-------------:|:---:|:----:|:------:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| EL Extension  | 338 | 134  |  130   |  4   |  7   | 298  | 334  | 336  | 328  | 319  | 310  |
| Deb Extension | 326 | 109  |  143   |  74  |  19  | 290  | 322  | 324  | 316  | 307  | 300  |
|  RPM Package  | 313 | 122  |  129   |  4   |  6   | 275  | 309  | 311  | 303  | 294  | 285  |
|  DEB Package  | 298 |  93  |  142   |  64  |  19  | 264  | 294  | 296  | 288  | 279  | 272  |

> Note: One single rpm/deb package may contain more than one extension

```
timescaledb pg_timeseries periods temporal_tables emaj table_version pg_cron pg_later pg_background pg_timetable postgis pgrouting pointcloud pg_h3 q3c ogr_fdw pg_polyline geoip pg_geohash #mobilitydb
pgvector pgvectorscale pg_vectorize pg_similarity smlar pg_summarize pg_tiktoken pgml pg4ml pg_search pg_bigm zhparser hunspell hydra pg_analytics pg_parquet pg_duckdb duckdb_fdw pg_fkpart pg_partman plproxy pg_strom citus
pg_hint_plan age hll rum pg_graphql pg_jsonschema jsquery index_advisor pg_plan_filter hypopg imgsmlr pg_ivm pgmq pgq pg_cardano rdkit pg_tle plv8 pllua plprql pldebugger plpgsql_check plprofiler plsh #plr pgtap faker dbt2
prefix semver pgunit md5hash asn1oid roaringbitmap pgfaceting pgsphere pg_country pg_currency pgmp numeral pg_rational pguint pg_uint128 ip4r pg_uri pgemailaddr acl timestamp9 chkpass debversion pg_rrule pgpool pgagent
topn pg_gzip pg_zstd pg_http pg_net pg_html5_email_address pgsql_tweaks pg_extra_time pg_timeit count_distinct extra_window_functions first_last_agg tdigest aggs_for_arrays aggs_for_vecs pg_arraymath quantile lower_quantile
pg_idkit pg_uuidv7 permuteseq pg_hashids sequential_uuids pg_math pg_random pg_base36 pg_base62 pg_base58 floatvec pg_financial pgjwt pg_hashlib shacrypt cryptint pg_ecdsa pgpcre icu_ext pgqr envvar pg_protobuf url_encode
pg_repack pg_squeeze pg_dirtyread pgfincore pgdd ddlx pg_prioritize pg_checksums pg_readonly safeupdate pg_permissions pgautofailover pg_catcheck preprepare pgcozy pg_orphaned pg_crash pg_cheat_funcs pg_savior table_log pg_fio
pg_profile pg_show_plans pg_stat_kcache pg_stat_monitor pg_qualstats pg_store_plans pg_track_settings pg_wait_sampling system_stats pg_meta pgnodemx pg_sqlog bgw_replstatus pgmeminfo toastinfo pg_explain_ui pg_relusage 
passwordcheck supautils pgsodium pg_vault anonymizer pg_tde pgsmcrypto pgaudit pgauditlogtofile pg_auth_mon credcheck pgcryptokey pg_jobmon logerrors login_hook set_user pgextwlist pg_snakeoil pg_auditor sslutils noset
wrappers multicorn jdbc_fdw odbc_fdw mysql_fdw tds_fdw sqlite_fdw pgbouncer_fdw mongo_fdw redis_fdw pg_redis_pubsub kafka_fdw hdfs_fdw firebird_fdw aws_s3 log_fdw oracle_fdw db2_fdw pgexporter_ext pg_top pagevis powa pg_mon
pglogical pgl_ddl_deploy pg_failover_slots wal2json wal2mongo decoderbufs decoder_raw mimeo pgcopydb pgloader pg_fact_loader pg_bulkload pg_comparator pgimportdoc pgexportdoc repmgr slony
orafce pgtt session_variable pg_statement_rollback pg_dbms_metadata pg_dbms_lock pgmemcache pg_dbms_job wiltondb gis-stack rag-stack fdw-stack fts-stack etl-stack feat-stack olap-stack supa-stack stat-stack json-stack
........ 
```


-------

## Update Extension Version

```bash
psql postgres://10.10.10.9/postgres -c 'COPY (SELECT * FROM pg_available_extensions) TO stdout CSV HEADER' > /tmp/rpm_new.csv
psql postgres://10.10.10.22/postgres -c 'COPY (SELECT * FROM pg_available_extensions) TO stdout CSV HEADER' > /tmp/deb_new.csv

scp sv:/tmp/*_new.csv data/

psql -c 'TRUNCATE ext.rpm_new,ext.deb_new;'
cat data/rpm_new.csv | psql -c 'COPY ext.rpm_new FROM stdin CSV HEADER;'
cat data/deb_new.csv | psql -c 'COPY ext.deb_new FROM stdin CSV HEADER;'
```

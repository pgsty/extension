# PostgreSQL 扩展软件仓库

[![Webite: ext.pigsty.io](https://img.shields.io/badge/website-ext.pigsty.io-slategray?style=flat&logo=cilium&logoColor=white)](https://ext.pigsty.io)
[![Extensions: 345](https://img.shields.io/badge/extensions-345-%233E668F?style=flat&logo=postgresql&logoColor=white&labelColor=3E668F)](https://pigsty.io/docs/pgext/list)
[![Postgres: 12-17](https://img.shields.io/badge/PostgreSQL-12~17-%233E668F?style=flat&logo=postgresql&labelColor=3E668F&logoColor=white)](https://pigsty.io/docs/pgsql)

由 [Pigsty](https://pigsty.io) 所维护与使用的PostgreSQL软件补充源：[apt](#apt-repo) 与 [yum](#yum-repo) 仓库。

在 PGDG 官方仓库的基础上提供了 **143** 个额外的 EL 扩展包，与 **130** 个额外的 DEB 扩展包，针对 PostgreSQL 12 - 17 与四大操作系统发行版大版本提供。


-------

## 快速上手


### YUM仓库

[![Linux](https://img.shields.io/badge/Linux-x86_64-%23FCC624?style=flat&logo=linux&labelColor=FCC624&logoColor=black)](https://pigsty.io/docs/node)
[![RHEL Support: 8/9](https://img.shields.io/badge/EL-7/8/9-red?style=flat&logo=redhat&logoColor=red)](https://pigsty.io/docs/pgext/list/rpm/)
[![RHEL](https://img.shields.io/badge/RHEL-slategray?style=flat&logo=redhat&logoColor=red)](https://pigsty.io/docs/pgext/list/rpm/)
[![CentOS](https://img.shields.io/badge/CentOS-slategray?style=flat&logo=centos&logoColor=%23262577)](https://almalinux.org/)
[![RockyLinux](https://img.shields.io/badge/RockyLinux-slategray?style=flat&logo=rockylinux&logoColor=%2310B981)](https://almalinux.org/)
[![AlmaLinux](https://img.shields.io/badge/AlmaLinux-slategray?style=flat&logo=almalinux&logoColor=black)](https://almalinux.org/)
[![OracleLinux](https://img.shields.io/badge/OracleLinux-slategray?style=flat&logo=oracle&logoColor=%23F80000)](https://almalinux.org/)

对于 EL 8/9 以及兼容的操作系统发行版，使用以下命令将 GPG 密钥与 Repo 文件添加到系统中并启用仓库：

```bash
curl -fsSL https://repo.pigsty.io/key      | sudo tee /etc/pki/rpm-gpg/RPM-GPG-KEY-pigsty >/dev/null  # 添加 gpg 密钥
curl -fsSL https://repo.pigsty.io/yum/repo | sudo tee /etc/yum.repos.d/pigsty.repo        >/dev/null  # 添加 repo 文件
sudo yum makecache
```

### APT仓库

[![Linux](https://img.shields.io/badge/Linux-x86_64-%23FCC624?style=flat&logo=linux&labelColor=FCC624&logoColor=black)](https://pigsty.io/docs/node)
[![Ubuntu Support: 22](https://img.shields.io/badge/Ubuntu-22-%23E95420?style=flat&logo=ubuntu&logoColor=%23E95420)](https://pigsty.io/docs/pgext/list/deb/)
[![Debian Support: 12](https://img.shields.io/badge/Debian-12-%23A81D33?style=flat&logo=debian&logoColor=%23A81D33)](https://pigsty.io/docs/reference/compatibility/)

对于 Ubuntu 22.04 与 Debian 12 以及其他兼容系统，使用以下命令将 GPG 密钥与 Repo 文件添加到系统中并启用仓库：

```bash
curl -fsSL https://repo.pigsty.io/key | sudo gpg --dearmor -o /etc/apt/keyrings/pigsty.gpg  # 添加 gpg 密钥
sudo tee /etc/apt/sources.list.d/pigsty-io.list > /dev/null <<EOF
deb [signed-by=/etc/apt/keyrings/pigsty.gpg] https://repo.pigsty.io/apt/infra generic main 
deb [signed-by=/etc/apt/keyrings/pigsty.gpg] https://repo.pigsty.io/apt/pgsql/$(lsb_release -cs) $(lsb_release -cs) main
EOF
sudo apt update
```


-------

## 仓库内容

针对 Linux x86_64 内核架构，PostgreSQL 12 - 17 预编译打包的扩展 RPM / DEB 包。

|  Statistics   | All | PGDG | PIGSTY | MISC | MISS | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:-------------:|:---:|:----:|:------:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| EL Extension  | 338 | 134  |  130   |  4   |  7   | 298  | 334  | 336  | 328  | 319  | 310  |
| Deb Extension | 326 | 109  |  143   |  74  |  19  | 290  | 322  | 324  | 316  | 307  | 300  |
|  RPM Package  | 313 | 122  |  129   |  4   |  6   | 275  | 309  | 311  | 303  | 294  | 285  |
|  DEB Package  | 298 |  93  |  142   |  64  |  19  | 264  | 294  | 296  | 288  | 279  | 272  |

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

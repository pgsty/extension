# PostgreSQL 扩展软件仓库

[![Webite: pigsty.io](https://img.shields.io/badge/website-ext.pigsty.io-slategray?style=flat&logo=cilium&logoColor=white)](https://pigsty.io/ext)
[![Extensions: 421](https://img.shields.io/badge/extensions-414-%233E668F?style=flat&logo=postgresql&logoColor=white&labelColor=3E668F)](https://pigsty.io/ext/list)
[![Postgres: 13-17](https://img.shields.io/badge/PostgreSQL-12~17-%233E668F?style=flat&logo=postgresql&labelColor=3E668F&logoColor=white)](https://pigsty.io/docs/pgsql)

由 [Pigsty](https://pigsty.io) 所维护与使用的PostgreSQL软件补充源：[apt](#apt-repo) 与 [yum](#yum-repo) 仓库。

在 PGDG 官方仓库的基础上提供了 **215** 个额外的 EL 扩展包，与 **223** 个额外的 DEB 扩展包，针对 PostgreSQL 12 - 17 与五大操作系统发行版大版本提供。

为什么插件与扩展对 PostgreSQL 非常重要？请看《[*PostgreSQL 正在吞噬数据库世界*](https://pigsty.cc/zh/blog/pg/pg-eat-db-world/)》

[![PostgreSQL扩展生态](https://pigsty.cc/img/pigsty/ecosystem.jpg)](https://pigsty.cc/zh/blog/pg/pg-eat-db-world/)


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

| Entry / Filter | All | PGDG | PIGSTY | CONTRIB | MISC | MISS | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:--------------:|:---:|:----:|:------:|:-------:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| RPM Extension  | 407 | 117  |  215   |   71    |  4   |  7   | 388  | 400  | 402  | 386  | 363  |
|  RPM Package   | 282 | 105  |  173   |    1    |  4   |  1   | 267  | 277  | 279  | 268  | 248  |
| DEB Extension  | 401 | 103  |  223   |   71    |  4   |  13  | 386  | 394  | 396  | 384  | 359  |
|  DEB Package   | 274 |  89  |  180   |    1    |  4   |  1   | 263  | 269  | 271  | 264  | 242  |

[**TIME**](/time): [`timescaledb`](/timescaledb) [`timescaledb_toolkit`](/timescaledb_toolkit) [`timeseries`](/timeseries) [`periods`](/periods) [`temporal_tables`](/temporal_tables) [`emaj`](/emaj) [`table_version`](/table_version) [`pg_cron`](/pg_cron) [`pg_task`](/pg_task) [`pg_later`](/pg_later) [`pg_background`](/pg_background)
[**GIS**](/gis): [`postgis`](/postgis) [`postgis_topology`](/postgis_topology) [`postgis_raster`](/postgis_raster) [`postgis_sfcgal`](/postgis_sfcgal) [`postgis_tiger_geocoder`](/postgis_tiger_geocoder) [`address_standardizer`](/address_standardizer) [`address_standardizer_data_us`](/address_standardizer_data_us) [`pgrouting`](/pgrouting) [`pointcloud`](/pointcloud) [`pointcloud_postgis`](/pointcloud_postgis) [`h3`](/h3) [`h3_postgis`](/h3_postgis) [`q3c`](/q3c) [`ogr_fdw`](/ogr_fdw) [`geoip`](/geoip) [`pg_polyline`](/pg_polyline) [`pg_geohash`](/pg_geohash) [`mobilitydb`](/mobilitydb) [`tzf`](/tzf) [`earthdistance`](/earthdistance)
[**RAG**](/rag): [`vector`](/vector) [`vchord`](/vchord) [`vectorscale`](/vectorscale) [`vectorize`](/vectorize) [`pg_similarity`](/pg_similarity) [`smlar`](/smlar) [`pg_summarize`](/pg_summarize) [`pg_tiktoken`](/pg_tiktoken) [`pg4ml`](/pg4ml) [`pgml`](/pgml)
[**FTS**](/fts): [`pg_search`](/pg_search) [`pgroonga`](/pgroonga) [`pgroonga_database`](/pgroonga_database) [`pg_bigm`](/pg_bigm) [`zhparser`](/zhparser) [`pg_bestmatch`](/pg_bestmatch) [`vchord_bm25`](/vchord_bm25) [`hunspell_cs_cz`](/hunspell_cs_cz) [`hunspell_de_de`](/hunspell_de_de) [`hunspell_en_us`](/hunspell_en_us) [`hunspell_fr`](/hunspell_fr) [`hunspell_ne_np`](/hunspell_ne_np) [`hunspell_nl_nl`](/hunspell_nl_nl) [`hunspell_nn_no`](/hunspell_nn_no) [`hunspell_pt_pt`](/hunspell_pt_pt) [`hunspell_ru_ru`](/hunspell_ru_ru) [`hunspell_ru_ru_aot`](/hunspell_ru_ru_aot) [`fuzzystrmatch`](/fuzzystrmatch) [`pg_trgm`](/pg_trgm)
[**OLAP**](/olap): [`citus`](/citus) [`citus_columnar`](/citus_columnar) [`columnar`](/columnar) [`pg_analytics`](/pg_analytics) [`pg_duckdb`](/pg_duckdb) [`pg_mooncake`](/pg_mooncake) [`duckdb_fdw`](/duckdb_fdw) [`pg_parquet`](/pg_parquet) [`pg_fkpart`](/pg_fkpart) [`pg_partman`](/pg_partman) [`plproxy`](/plproxy) [`pg_strom`](/pg_strom) [`tablefunc`](/tablefunc)
[**FEAT**](/feat): [`age`](/age) [`hll`](/hll) [`rum`](/rum) [`pg_graphql`](/pg_graphql) [`pg_jsonschema`](/pg_jsonschema) [`jsquery`](/jsquery) [`pg_hint_plan`](/pg_hint_plan) [`hypopg`](/hypopg) [`index_advisor`](/index_advisor) [`plan_filter`](/plan_filter) [`imgsmlr`](/imgsmlr) [`pg_ivm`](/pg_ivm) [`pg_incremental`](/pg_incremental) [`pgmq`](/pgmq) [`pgq`](/pgq) [`pg_cardano`](/pg_cardano) [`rdkit`](/rdkit) [`omni`](/omni) [`omni_auth`](/omni_auth) [`omni_aws`](/omni_aws) [`omni_cloudevents`](/omni_cloudevents) [`omni_containers`](/omni_containers) [`omni_credentials`](/omni_credentials) [`omni_email`](/omni_email) [`omni_http`](/omni_http) [`omni_httpc`](/omni_httpc) [`omni_httpd`](/omni_httpd) [`omni_id`](/omni_id) [`omni_json`](/omni_json) [`omni_kube`](/omni_kube) [`omni_ledger`](/omni_ledger) [`omni_manifest`](/omni_manifest) [`omni_mimetypes`](/omni_mimetypes) [`omni_os`](/omni_os) [`omni_polyfill`](/omni_polyfill) [`omni_python`](/omni_python) [`omni_regex`](/omni_regex) [`omni_rest`](/omni_rest) [`omni_schema`](/omni_schema) [`omni_seq`](/omni_seq) [`omni_service`](/omni_service) [`omni_session`](/omni_session) [`omni_sql`](/omni_sql) [`omni_sqlite`](/omni_sqlite) [`omni_test`](/omni_test) [`omni_txn`](/omni_txn) [`omni_types`](/omni_types) [`omni_var`](/omni_var) [`omni_vfs`](/omni_vfs) [`omni_vfs_types_v1`](/omni_vfs_types_v1) [`omni_web`](/omni_web) [`omni_worker`](/omni_worker) [`omni_xml`](/omni_xml) [`omni_yaml`](/omni_yaml) [`bloom`](/bloom)
[**LANG**](/lang): [`pg_tle`](/pg_tle) [`plv8`](/plv8) [`pllua`](/pllua) [`hstore_pllua`](/hstore_pllua) [`plluau`](/plluau) [`hstore_plluau`](/hstore_plluau) [`plprql`](/plprql) [`pldbgapi`](/pldbgapi) [`plpgsql_check`](/plpgsql_check) [`plprofiler`](/plprofiler) [`plsh`](/plsh) [`pljava`](/pljava) [`plr`](/plr) [`pgtap`](/pgtap) [`faker`](/faker) [`dbt2`](/dbt2) [`pltcl`](/pltcl) [`pltclu`](/pltclu) [`plperl`](/plperl) [`bool_plperl`](/bool_plperl) [`hstore_plperl`](/hstore_plperl) [`jsonb_plperl`](/jsonb_plperl) [`plperlu`](/plperlu) [`bool_plperlu`](/bool_plperlu) [`jsonb_plperlu`](/jsonb_plperlu) [`hstore_plperlu`](/hstore_plperlu) [`plpgsql`](/plpgsql) [`plpython3u`](/plpython3u) [`jsonb_plpython3u`](/jsonb_plpython3u) [`ltree_plpython3u`](/ltree_plpython3u) [`hstore_plpython3u`](/hstore_plpython3u)
[**TYPE**](/type): [`prefix`](/prefix) [`semver`](/semver) [`unit`](/unit) [`pgpdf`](/pgpdf) [`pglite_fusion`](/pglite_fusion) [`md5hash`](/md5hash) [`asn1oid`](/asn1oid) [`roaringbitmap`](/roaringbitmap) [`pgfaceting`](/pgfaceting) [`pg_sphere`](/pg_sphere) [`country`](/country) [`pg_xenophile`](/pg_xenophile) [`l10n_table_dependent_extension`](/l10n_table_dependent_extension) [`currency`](/currency) [`collection`](/collection) [`pgmp`](/pgmp) [`numeral`](/numeral) [`pg_rational`](/pg_rational) [`uint`](/uint) [`uint128`](/uint128) [`hashtypes`](/hashtypes) [`ip4r`](/ip4r) [`pg_duration`](/pg_duration) [`uri`](/uri) [`emailaddr`](/emailaddr) [`acl`](/acl) [`debversion`](/debversion) [`pg_rrule`](/pg_rrule) [`timestamp9`](/timestamp9) [`chkpass`](/chkpass) [`isn`](/isn) [`seg`](/seg) [`cube`](/cube) [`ltree`](/ltree) [`hstore`](/hstore) [`citext`](/citext) [`xml2`](/xml2)
[**UTIL**](/util): [`gzip`](/gzip) [`bzip`](/bzip) [`zstd`](/zstd) [`http`](/http) [`pg_net`](/pg_net) [`pg_curl`](/pg_curl) [`pgjq`](/pgjq) [`pgjwt`](/pgjwt) [`pg_smtp_client`](/pg_smtp_client) [`pg_html5_email_address`](/pg_html5_email_address) [`url_encode`](/url_encode) [`pgsql_tweaks`](/pgsql_tweaks) [`pg_extra_time`](/pg_extra_time) [`pgpcre`](/pgpcre) [`icu_ext`](/icu_ext) [`pgqr`](/pgqr) [`pg_protobuf`](/pg_protobuf) [`envvar`](/envvar) [`floatfile`](/floatfile) [`pg_readme`](/pg_readme) [`pg_readme_test_extension`](/pg_readme_test_extension) [`ddl_historization`](/ddl_historization) [`data_historization`](/data_historization) [`schedoc`](/schedoc) [`hashlib`](/hashlib) [`xxhash`](/xxhash) [`shacrypt`](/shacrypt) [`cryptint`](/cryptint) [`pguecc`](/pguecc) [`sparql`](/sparql)
[**FUNC**](/func): [`pg_idkit`](/pg_idkit) [`pg_uuidv7`](/pg_uuidv7) [`permuteseq`](/permuteseq) [`pg_hashids`](/pg_hashids) [`sequential_uuids`](/sequential_uuids) [`topn`](/topn) [`quantile`](/quantile) [`lower_quantile`](/lower_quantile) [`count_distinct`](/count_distinct) [`omnisketch`](/omnisketch) [`ddsketch`](/ddsketch) [`vasco`](/vasco) [`xicor`](/xicor) [`tdigest`](/tdigest) [`first_last_agg`](/first_last_agg) [`extra_window_functions`](/extra_window_functions) [`floatvec`](/floatvec) [`aggs_for_vecs`](/aggs_for_vecs) [`aggs_for_arrays`](/aggs_for_arrays) [`arraymath`](/arraymath) [`pg_math`](/pg_math) [`random`](/random) [`base36`](/base36) [`base62`](/base62) [`pg_base58`](/pg_base58) [`financial`](/financial) [`refint`](/refint) [`autoinc`](/autoinc) [`insert_username`](/insert_username) [`moddatetime`](/moddatetime) [`tsm_system_time`](/tsm_system_time) [`dict_xsyn`](/dict_xsyn) [`tsm_system_rows`](/tsm_system_rows) [`tcn`](/tcn) [`uuid-ossp`](/uuid-ossp) [`btree_gist`](/btree_gist) [`btree_gin`](/btree_gin) [`intarray`](/intarray) [`intagg`](/intagg) [`dict_int`](/dict_int) [`unaccent`](/unaccent)
[**ADMIN**](/admin): [`pg_repack`](/pg_repack) [`pg_squeeze`](/pg_squeeze) [`pg_dirtyread`](/pg_dirtyread) [`pgfincore`](/pgfincore) [`pg_cooldown`](/pg_cooldown) [`ddlx`](/ddlx) [`prioritize`](/prioritize) [`pg_checksums`](/pg_checksums) [`pg_readonly`](/pg_readonly) [`pg_upless`](/pg_upless) [`pg_permissions`](/pg_permissions) [`pgautofailover`](/pgautofailover) [`pg_catcheck`](/pg_catcheck) [`pre_prepare`](/pre_prepare) [`pgcozy`](/pgcozy) [`pg_orphaned`](/pg_orphaned) [`pg_crash`](/pg_crash) [`pg_cheat_funcs`](/pg_cheat_funcs) [`fio`](/fio) [`pg_savior`](/pg_savior) [`safeupdate`](/safeupdate) [`pg_drop_events`](/pg_drop_events) [`table_log`](/table_log) [`pgagent`](/pgagent) [`pg_prewarm`](/pg_prewarm) [`pgpool_adm`](/pgpool_adm) [`pgpool_recovery`](/pgpool_recovery) [`pgpool_regclass`](/pgpool_regclass) [`lo`](/lo) [`basic_archive`](/basic_archive) [`basebackup_to_shell`](/basebackup_to_shell) [`old_snapshot`](/old_snapshot) [`adminpack`](/adminpack) [`amcheck`](/amcheck) [`pg_surgery`](/pg_surgery)
[**STAT**](/stat): [`pg_profile`](/pg_profile) [`pg_tracing`](/pg_tracing) [`pg_show_plans`](/pg_show_plans) [`pg_stat_kcache`](/pg_stat_kcache) [`pg_stat_monitor`](/pg_stat_monitor) [`pg_qualstats`](/pg_qualstats) [`pg_store_plans`](/pg_store_plans) [`pg_track_settings`](/pg_track_settings) [`pg_wait_sampling`](/pg_wait_sampling) [`system_stats`](/system_stats) [`meta`](/meta) [`pgnodemx`](/pgnodemx) [`pg_proctab`](/pg_proctab) [`pg_sqlog`](/pg_sqlog) [`bgw_replstatus`](/bgw_replstatus) [`pgmeminfo`](/pgmeminfo) [`toastinfo`](/toastinfo) [`explain_ui`](/explain_ui) [`pg_relusage`](/pg_relusage) [`pagevis`](/pagevis) [`powa`](/powa) [`pg_overexplain`](/pg_overexplain) [`pg_logicalinspect`](/pg_logicalinspect) [`pageinspect`](/pageinspect) [`pgrowlocks`](/pgrowlocks) [`sslinfo`](/sslinfo) [`pg_buffercache`](/pg_buffercache) [`pg_walinspect`](/pg_walinspect) [`pg_freespacemap`](/pg_freespacemap) [`pg_visibility`](/pg_visibility) [`pgstattuple`](/pgstattuple) [`auto_explain`](/auto_explain) [`pg_stat_statements`](/pg_stat_statements)
[**SEC**](/sec): [`passwordcheck_cracklib`](/passwordcheck_cracklib) [`supautils`](/supautils) [`pgsodium`](/pgsodium) [`supabase_vault`](/supabase_vault) [`pg_session_jwt`](/pg_session_jwt) [`anon`](/anon) [`pg_tde`](/pg_tde) [`pgsmcrypto`](/pgsmcrypto) [`pgaudit`](/pgaudit) [`pgauditlogtofile`](/pgauditlogtofile) [`pg_auth_mon`](/pg_auth_mon) [`credcheck`](/credcheck) [`pgcryptokey`](/pgcryptokey) [`pg_jobmon`](/pg_jobmon) [`logerrors`](/logerrors) [`login_hook`](/login_hook) [`set_user`](/set_user) [`pg_snakeoil`](/pg_snakeoil) [`pgextwlist`](/pgextwlist) [`pg_auditor`](/pg_auditor) [`sslutils`](/sslutils) [`noset`](/noset) [`sepgsql`](/sepgsql) [`auth_delay`](/auth_delay) [`pgcrypto`](/pgcrypto) [`passwordcheck`](/passwordcheck)
[**FDW**](/fdw): [`wrappers`](/wrappers) [`multicorn`](/multicorn) [`odbc_fdw`](/odbc_fdw) [`jdbc_fdw`](/jdbc_fdw) [`pgspider_ext`](/pgspider_ext) [`mysql_fdw`](/mysql_fdw) [`oracle_fdw`](/oracle_fdw) [`tds_fdw`](/tds_fdw) [`db2_fdw`](/db2_fdw) [`sqlite_fdw`](/sqlite_fdw) [`pgbouncer_fdw`](/pgbouncer_fdw) [`mongo_fdw`](/mongo_fdw) [`redis_fdw`](/redis_fdw) [`redis`](/redis) [`kafka_fdw`](/kafka_fdw) [`hdfs_fdw`](/hdfs_fdw) [`firebird_fdw`](/firebird_fdw) [`aws_s3`](/aws_s3) [`log_fdw`](/log_fdw) [`dblink`](/dblink) [`file_fdw`](/file_fdw) [`postgres_fdw`](/postgres_fdw)
[**SIM**](/sim): [`documentdb`](/documentdb) [`documentdb_core`](/documentdb_core) [`documentdb_distributed`](/documentdb_distributed) [`orafce`](/orafce) [`pgtt`](/pgtt) [`session_variable`](/session_variable) [`pg_statement_rollback`](/pg_statement_rollback) [`pg_dbms_metadata`](/pg_dbms_metadata) [`pg_dbms_lock`](/pg_dbms_lock) [`pg_dbms_job`](/pg_dbms_job) [`babelfishpg_common`](/babelfishpg_common) [`babelfishpg_tsql`](/babelfishpg_tsql) [`babelfishpg_tds`](/babelfishpg_tds) [`babelfishpg_money`](/babelfishpg_money) [`pgmemcache`](/pgmemcache)
[**ETL**](/etl): [`pglogical`](/pglogical) [`pglogical_origin`](/pglogical_origin) [`pglogical_ticker`](/pglogical_ticker) [`pgl_ddl_deploy`](/pgl_ddl_deploy) [`pg_failover_slots`](/pg_failover_slots) [`db_migrator`](/db_migrator) [`wal2json`](/wal2json) [`wal2mongo`](/wal2mongo) [`decoderbufs`](/decoderbufs) [`decoder_raw`](/decoder_raw) [`mimeo`](/mimeo) [`repmgr`](/repmgr) [`pg_fact_loader`](/pg_fact_loader) [`pg_bulkload`](/pg_bulkload) [`test_decoding`](/test_decoding) [`pgoutput`](/pgoutput)

```

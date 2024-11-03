# PostgreSQL Extension Repo

[![Webite: ext.pigsty.io](https://img.shields.io/badge/website-ext.pigsty.io-slategray?style=flat&logo=cilium&logoColor=white)](https://ext.pigsty.io)
[![Extensions: 340](https://img.shields.io/badge/extensions-340-%233E668F?style=flat&logo=postgresql&logoColor=white&labelColor=3E668F)](https://pigsty.io/docs/pgext/list)

The supplementary [APT](#apt-repo) and [YUM](#yum-repo) repo for PostgreSQL extensions, maintained and used by [Pigsty](https://pigsty.io)

Provide 340 available [Extensions](/list) as [RPM](/rpm) / [DEB](/deb) for PostgreSQL **12** - **17** in addition to the official PGDG repo.

**Why extension matters to PostgreSQL?** check the post: "[***PostgreSQL is eating the database world!***](https://medium.com/@fengruohang/postgres-is-eating-the-database-world-157c204dcfc4)"

[![PostgreSQL Extension Ecosystem](https://pigsty.io/img/pigsty/ecosystem.jpg)](https://medium.com/@fengruohang/postgres-is-eating-the-database-world-157c204dcfc4)


-------

## Get Started

All rpm/deb packages are signed with GPG key `B9BD8B20` (`9592A7BC7A682E7333376E09E7935D8DB9BD8B20` ).

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

### YUM Repo

[![Linux](https://img.shields.io/badge/Linux-x86_64-%23FCC624?style=flat&logo=linux&labelColor=FCC624&logoColor=black)](https://pigsty.io/docs/node)
[![RHEL Support: 8/9](https://img.shields.io/badge/EL-7/8/9-red?style=flat&logo=redhat&logoColor=red)](https://pigsty.io/docs/pgext/list/rpm/)
[![RHEL](https://img.shields.io/badge/RHEL-slategray?style=flat&logo=redhat&logoColor=red)](https://pigsty.io/docs/pgext/list/rpm/)
[![CentOS](https://img.shields.io/badge/CentOS-slategray?style=flat&logo=centos&logoColor=%23262577)](https://almalinux.org/)
[![RockyLinux](https://img.shields.io/badge/RockyLinux-slategray?style=flat&logo=rockylinux&logoColor=%2310B981)](https://almalinux.org/)
[![AlmaLinux](https://img.shields.io/badge/AlmaLinux-slategray?style=flat&logo=almalinux&logoColor=black)](https://almalinux.org/)
[![OracleLinux](https://img.shields.io/badge/OracleLinux-slategray?style=flat&logo=oracle&logoColor=%23F80000)](https://almalinux.org/)

For EL 8/9 and compatible platforms, use the following commands to add the YUM repo:

```bash
curl -fsSL https://repo.pigsty.io/key      | sudo tee /etc/pki/rpm-gpg/RPM-GPG-KEY-pigsty >/dev/null  # add gpg key
curl -fsSL https://repo.pigsty.io/yum/repo | sudo tee /etc/yum.repos.d/pigsty.repo        >/dev/null  # add repo file
sudo yum makecache
```

-------

## What's Inside

Linux x86_64/amd64 [Extension](/list) packages for PostgreSQL 12 - 17, on El8, EL9, Ubuntu 22.04 and Debian 12.

|Entry / Filter | All | PGDG | PIGSTY | CONTRIB | MISC | MISS | PG17 | PG16 | PG15 | PG14 | PG13 | PG12|
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| RPM Extension | 334 | 119 | 139 | 70 | 4 | 6 | 301 | 330 | 333 | 319 | 307 | 294 |
| DEB Extension | 326 | 104 | 143 | 70 | 5 | 14 | 302 | 322 | 325 | 316 | 303 | 293 |
| RPM Package | 251 | 107 | 138 | 1 | 4 | 1 | 220 | 247 | 250 | 239 | 229 | 216 |
| DEB Package | 241 | 90 | 142 | 1 | 5 | 1 | 218 | 237 | 240 | 234 | 223 | 213 |



> Note: One single rpm/deb package may contain more than one extension

[**TIME**](/time): [`timescaledb`](/timescaledb) [`timescaledb_toolkit`](/timescaledb_toolkit) [`timeseries`](/timeseries) [`periods`](/periods) [`temporal_tables`](/temporal_tables) [`emaj`](/emaj) [`table_version`](/table_version) [`pg_cron`](/pg_cron) [`pg_later`](/pg_later) [`pg_background`](/pg_background)
[**GIS**](/gis): [`postgis`](/postgis) [`postgis_topology`](/postgis_topology) [`postgis_raster`](/postgis_raster) [`postgis_sfcgal`](/postgis_sfcgal) [`postgis_tiger_geocoder`](/postgis_tiger_geocoder) [`address_standardizer`](/address_standardizer) [`address_standardizer_data_us`](/address_standardizer_data_us) [`pgrouting`](/pgrouting) [`pointcloud`](/pointcloud) [`pointcloud_postgis`](/pointcloud_postgis) [`h3`](/h3) [`h3_postgis`](/h3_postgis) [`q3c`](/q3c) [`ogr_fdw`](/ogr_fdw) [`geoip`](/geoip) [`pg_polyline`](/pg_polyline) [`pg_geohash`](/pg_geohash) [`mobilitydb`](/mobilitydb) [`earthdistance`](/earthdistance)
[**RAG**](/rag): [`vector`](/vector) [`vectorscale`](/vectorscale) [`vectorize`](/vectorize) [`pg_similarity`](/pg_similarity) [`smlar`](/smlar) [`pg_summarize`](/pg_summarize) [`pg_tiktoken`](/pg_tiktoken) [`pgml`](/pgml) [`pg4ml`](/pg4ml)
[**FTS**](/fts): [`pg_search`](/pg_search) [`pg_bigm`](/pg_bigm) [`zhparser`](/zhparser) [`hunspell_cs_cz`](/hunspell_cs_cz) [`hunspell_de_de`](/hunspell_de_de) [`hunspell_en_us`](/hunspell_en_us) [`hunspell_fr`](/hunspell_fr) [`hunspell_ne_np`](/hunspell_ne_np) [`hunspell_nl_nl`](/hunspell_nl_nl) [`hunspell_nn_no`](/hunspell_nn_no) [`hunspell_pt_pt`](/hunspell_pt_pt) [`hunspell_ru_ru`](/hunspell_ru_ru) [`hunspell_ru_ru_aot`](/hunspell_ru_ru_aot) [`fuzzystrmatch`](/fuzzystrmatch) [`pg_trgm`](/pg_trgm)
[**OLAP**](/olap): [`citus`](/citus) [`citus_columnar`](/citus_columnar) [`columnar`](/columnar) [`pg_analytics`](/pg_analytics) [`pg_duckdb`](/pg_duckdb) [`pg_mooncake`](/pg_mooncake) [`duckdb_fdw`](/duckdb_fdw) [`pg_parquet`](/pg_parquet) [`pg_fkpart`](/pg_fkpart) [`pg_partman`](/pg_partman) [`plproxy`](/plproxy) [`pg_strom`](/pg_strom) [`tablefunc`](/tablefunc)
[**FEAT**](/feat): [`age`](/age) [`hll`](/hll) [`rum`](/rum) [`pg_graphql`](/pg_graphql) [`pg_jsonschema`](/pg_jsonschema) [`jsquery`](/jsquery) [`pg_hint_plan`](/pg_hint_plan) [`hypopg`](/hypopg) [`index_advisor`](/index_advisor) [`plan_filter`](/plan_filter) [`imgsmlr`](/imgsmlr) [`pg_ivm`](/pg_ivm) [`pgmq`](/pgmq) [`pgq`](/pgq) [`pg_cardano`](/pg_cardano) [`rdkit`](/rdkit) [`bloom`](/bloom)
[**LANG**](/lang): [`pg_tle`](/pg_tle) [`plv8`](/plv8) [`pllua`](/pllua) [`hstore_pllua`](/hstore_pllua) [`plluau`](/plluau) [`hstore_plluau`](/hstore_plluau) [`plprql`](/plprql) [`pldbgapi`](/pldbgapi) [`plpgsql_check`](/plpgsql_check) [`plprofiler`](/plprofiler) [`plsh`](/plsh) [`pljava`](/pljava) [`plr`](/plr) [`pgtap`](/pgtap) [`faker`](/faker) [`dbt2`](/dbt2) [`pltcl`](/pltcl) [`pltclu`](/pltclu) [`plperl`](/plperl) [`bool_plperl`](/bool_plperl) [`hstore_plperl`](/hstore_plperl) [`jsonb_plperl`](/jsonb_plperl) [`plperlu`](/plperlu) [`bool_plperlu`](/bool_plperlu) [`jsonb_plperlu`](/jsonb_plperlu) [`hstore_plperlu`](/hstore_plperlu) [`plpgsql`](/plpgsql) [`plpython3u`](/plpython3u) [`jsonb_plpython3u`](/jsonb_plpython3u) [`ltree_plpython3u`](/ltree_plpython3u) [`hstore_plpython3u`](/hstore_plpython3u)
[**TYPE**](/type): [`prefix`](/prefix) [`semver`](/semver) [`unit`](/unit) [`md5hash`](/md5hash) [`asn1oid`](/asn1oid) [`roaringbitmap`](/roaringbitmap) [`pgfaceting`](/pgfaceting) [`pg_sphere`](/pg_sphere) [`country`](/country) [`currency`](/currency) [`pgmp`](/pgmp) [`numeral`](/numeral) [`pg_rational`](/pg_rational) [`uint`](/uint) [`uint128`](/uint128) [`ip4r`](/ip4r) [`uri`](/uri) [`pgemailaddr`](/pgemailaddr) [`acl`](/acl) [`debversion`](/debversion) [`pg_rrule`](/pg_rrule) [`timestamp9`](/timestamp9) [`chkpass`](/chkpass) [`isn`](/isn) [`seg`](/seg) [`cube`](/cube) [`ltree`](/ltree) [`hstore`](/hstore) [`citext`](/citext) [`xml2`](/xml2)
[**FUNC**](/func): [`topn`](/topn) [`gzip`](/gzip) [`zstd`](/zstd) [`http`](/http) [`pg_net`](/pg_net) [`pg_smtp_client`](/pg_smtp_client) [`pg_html5_email_address`](/pg_html5_email_address) [`pgsql_tweaks`](/pgsql_tweaks) [`pg_extra_time`](/pg_extra_time) [`timeit`](/timeit) [`count_distinct`](/count_distinct) [`extra_window_functions`](/extra_window_functions) [`first_last_agg`](/first_last_agg) [`tdigest`](/tdigest) [`aggs_for_vecs`](/aggs_for_vecs) [`aggs_for_arrays`](/aggs_for_arrays) [`arraymath`](/arraymath) [`quantile`](/quantile) [`lower_quantile`](/lower_quantile) [`pg_idkit`](/pg_idkit) [`pg_uuidv7`](/pg_uuidv7) [`permuteseq`](/permuteseq) [`pg_hashids`](/pg_hashids) [`sequential_uuids`](/sequential_uuids) [`pg_math`](/pg_math) [`random`](/random) [`base36`](/base36) [`base62`](/base62) [`pg_base58`](/pg_base58) [`floatvec`](/floatvec) [`financial`](/financial) [`pgjwt`](/pgjwt) [`pg_hashlib`](/pg_hashlib) [`shacrypt`](/shacrypt) [`cryptint`](/cryptint) [`pguecc`](/pguecc) [`pgpcre`](/pgpcre) [`icu_ext`](/icu_ext) [`pgqr`](/pgqr) [`envvar`](/envvar) [`pg_protobuf`](/pg_protobuf) [`url_encode`](/url_encode) [`refint`](/refint) [`autoinc`](/autoinc) [`insert_username`](/insert_username) [`moddatetime`](/moddatetime) [`tsm_system_time`](/tsm_system_time) [`dict_xsyn`](/dict_xsyn) [`tsm_system_rows`](/tsm_system_rows) [`tcn`](/tcn) [`uuid-ossp`](/uuid-ossp) [`btree_gist`](/btree_gist) [`btree_gin`](/btree_gin) [`intarray`](/intarray) [`intagg`](/intagg) [`dict_int`](/dict_int) [`unaccent`](/unaccent)
[**ADMIN**](/admin): [`pg_repack`](/pg_repack) [`pg_squeeze`](/pg_squeeze) [`pg_dirtyread`](/pg_dirtyread) [`pgfincore`](/pgfincore) [`pgdd`](/pgdd) [`ddlx`](/ddlx) [`prioritize`](/prioritize) [`pg_checksums`](/pg_checksums) [`pg_readonly`](/pg_readonly) [`safeupdate`](/safeupdate) [`pg_permissions`](/pg_permissions) [`pgautofailover`](/pgautofailover) [`pg_catcheck`](/pg_catcheck) [`pre_prepare`](/pre_prepare) [`pgcozy`](/pgcozy) [`pg_orphaned`](/pg_orphaned) [`pg_crash`](/pg_crash) [`pg_cheat_funcs`](/pg_cheat_funcs) [`pg_savior`](/pg_savior) [`table_log`](/table_log) [`pg_fio`](/pg_fio) [`pgpool_adm`](/pgpool_adm) [`pgpool_recovery`](/pgpool_recovery) [`pgpool_regclass`](/pgpool_regclass) [`pgagent`](/pgagent) [`vacuumlo`](/vacuumlo) [`pg_prewarm`](/pg_prewarm) [`oid2name`](/oid2name) [`lo`](/lo) [`basic_archive`](/basic_archive) [`basebackup_to_shell`](/basebackup_to_shell) [`old_snapshot`](/old_snapshot) [`adminpack`](/adminpack) [`amcheck`](/amcheck) [`pg_surgery`](/pg_surgery)
[**STAT**](/stat): [`pg_profile`](/pg_profile) [`pg_show_plans`](/pg_show_plans) [`pg_stat_kcache`](/pg_stat_kcache) [`pg_stat_monitor`](/pg_stat_monitor) [`pg_qualstats`](/pg_qualstats) [`pg_store_plans`](/pg_store_plans) [`pg_track_settings`](/pg_track_settings) [`pg_wait_sampling`](/pg_wait_sampling) [`system_stats`](/system_stats) [`meta`](/meta) [`pgnodemx`](/pgnodemx) [`pg_proctab`](/pg_proctab) [`pg_sqlog`](/pg_sqlog) [`bgw_replstatus`](/bgw_replstatus) [`pgmeminfo`](/pgmeminfo) [`toastinfo`](/toastinfo) [`explain_ui`](/explain_ui) [`pg_relusage`](/pg_relusage) [`pg_top`](/pg_top) [`pagevis`](/pagevis) [`powa`](/powa) [`pageinspect`](/pageinspect) [`pgrowlocks`](/pgrowlocks) [`sslinfo`](/sslinfo) [`pg_buffercache`](/pg_buffercache) [`pg_walinspect`](/pg_walinspect) [`pg_freespacemap`](/pg_freespacemap) [`pg_visibility`](/pg_visibility) [`pgstattuple`](/pgstattuple) [`auto_explain`](/auto_explain) [`pg_stat_statements`](/pg_stat_statements)
[**SEC**](/sec): [`passwordcheck_cracklib`](/passwordcheck_cracklib) [`supautils`](/supautils) [`pgsodium`](/pgsodium) [`supabase_vault`](/supabase_vault) [`pg_session_jwt`](/pg_session_jwt) [`anon`](/anon) [`pg_tde`](/pg_tde) [`pgsmcrypto`](/pgsmcrypto) [`pgaudit`](/pgaudit) [`pgauditlogtofile`](/pgauditlogtofile) [`pg_auth_mon`](/pg_auth_mon) [`credcheck`](/credcheck) [`pgcryptokey`](/pgcryptokey) [`pg_jobmon`](/pg_jobmon) [`logerrors`](/logerrors) [`login_hook`](/login_hook) [`set_user`](/set_user) [`pg_snakeoil`](/pg_snakeoil) [`pgextwlist`](/pgextwlist) [`pg_auditor`](/pg_auditor) [`sslutils`](/sslutils) [`noset`](/noset) [`sepgsql`](/sepgsql) [`auth_delay`](/auth_delay) [`pgcrypto`](/pgcrypto) [`passwordcheck`](/passwordcheck)
[**FDW**](/fdw): [`wrappers`](/wrappers) [`multicorn`](/multicorn) [`odbc_fdw`](/odbc_fdw) [`jdbc_fdw`](/jdbc_fdw) [`mysql_fdw`](/mysql_fdw) [`oracle_fdw`](/oracle_fdw) [`tds_fdw`](/tds_fdw) [`db2_fdw`](/db2_fdw) [`sqlite_fdw`](/sqlite_fdw) [`pgbouncer_fdw`](/pgbouncer_fdw) [`mongo_fdw`](/mongo_fdw) [`redis_fdw`](/redis_fdw) [`redis`](/redis) [`kafka_fdw`](/kafka_fdw) [`hdfs_fdw`](/hdfs_fdw) [`firebird_fdw`](/firebird_fdw) [`aws_s3`](/aws_s3) [`log_fdw`](/log_fdw) [`dblink`](/dblink) [`file_fdw`](/file_fdw) [`postgres_fdw`](/postgres_fdw)
[**SIM**](/sim): [`orafce`](/orafce) [`pgtt`](/pgtt) [`session_variable`](/session_variable) [`pg_statement_rollback`](/pg_statement_rollback) [`pg_dbms_metadata`](/pg_dbms_metadata) [`pg_dbms_lock`](/pg_dbms_lock) [`pg_dbms_job`](/pg_dbms_job) [`babelfishpg_common`](/babelfishpg_common) [`babelfishpg_tsql`](/babelfishpg_tsql) [`babelfishpg_tds`](/babelfishpg_tds) [`babelfishpg_money`](/babelfishpg_money) [`pgmemcache`](/pgmemcache)
[**ETL**](/etl): [`pglogical`](/pglogical) [`pglogical_origin`](/pglogical_origin) [`pglogical_ticker`](/pglogical_ticker) [`pgl_ddl_deploy`](/pgl_ddl_deploy) [`pg_failover_slots`](/pg_failover_slots) [`wal2json`](/wal2json) [`wal2mongo`](/wal2mongo) [`decoderbufs`](/decoderbufs) [`decoder_raw`](/decoder_raw) [`test_decoding`](/test_decoding) [`mimeo`](/mimeo) [`repmgr`](/repmgr) [`pg_fact_loader`](/pg_fact_loader) [`pg_bulkload`](/pg_bulkload)

----------------

## Contrib

You can edit the [`pigsty.csv`](https://github.com/pgsty/extension/blob/main/data/pigsty.csv) raw data and create a pull
request to update the metadata in case of any error.

If you have any suggestions on including new extensions or bumping to new versions, PR
or [Issue](https://github.com/pgsty/extension/issues/new) are always welcome!



----------------

## About

[![Github: pgsty/extensions](https://img.shields.io/badge/GitHub-pgsty/extensions-slategray?style=flat&logo=github&logoColor=black)](https://github.com/pgsty/extensions)
[![Author: RuohangFeng](https://img.shields.io/badge/Author-Ruohang_Feng-steelblue?style=flat)](https://vonng.com/)
[![About: @Vonng](https://img.shields.io/badge/%40Vonng-steelblue?style=flat)](https://vonng.com/en/)
[![Mail: rh@vonng.com](https://img.shields.io/badge/rh%40vonng.com-steelblue?style=flat)](mailto:rh@vonng.com)
[![Copyright: 2018-2024 rh@Vonng.com](https://img.shields.io/badge/Copyright-2018--2024_(rh%40vonng.com)-red?logo=c&color=steelblue)](https://github.com/Vonng)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-steelblue?style=flat&logo=opensourceinitiative&logoColor=green)](https://pigsty.io/docs/about/license/)

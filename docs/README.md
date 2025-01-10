# PostgreSQL Extension Repo

[![Webite: ext.pigsty.io](https://img.shields.io/badge/website-ext.pigsty.io-slategray?style=flat&logo=cilium&logoColor=white)](https://ext.pigsty.io)
[![Extensions: 351](https://img.shields.io/badge/extensions-351-%233E668F?style=flat&logo=postgresql&logoColor=white&labelColor=3E668F)](https://pigsty.io/docs/pgext/list)
[![License: Apache-2.0](https://img.shields.io/github/license/pgsty/extension?logo=opensourceinitiative&logoColor=green&color=slategray)](https://github.com/pgsty/pig/blob/main/LICENSE)

The supplementary [APT](#apt-repo) and [YUM](#yum-repo) repo for PostgreSQL extensions, maintained and used by [Pigsty](https://pigsty.io)

Provide [351](/list) available extensions as [RPM](/rpm) / [DEB](/deb) for PostgreSQL **13** - **17** in addition to the official PGDG repo.

Available on Linux: Debian 12 / Ubuntu 24.04 / 22.04 / EL8 / EL9 compatible OS distros, and `x86_64` & `ARM64` architectures. 

|Entry / Filter | All | PGDG | PIGSTY | CONTRIB | MISC | MISS | PG17 | PG16 | PG15 | PG14 | PG13|
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| RPM Extension | 345 | 116 | 156 | 69 | 4 | 6 | 321 | 340 | 343 | 331 | 313 |
| DEB Extension | 338 | 103 | 162 | 69 | 4 | 13 | 319 | 333 | 336 | 329 | 310 |



> **Why extension matters to PostgreSQL?** check the post: "[***PostgreSQL is eating the database world!***](https://medium.com/@fengruohang/postgres-is-eating-the-database-world-157c204dcfc4)"
>
> <a href="https://medium.com/@fengruohang/postgres-is-eating-the-database-world-157c204dcfc4"><img src="https://pigsty.io/img/pigsty/ecosystem.jpg" style="max-width: 1000px; max-height: 1000px; width: 100%; height: auto;"></a>


-------

## Get Started

### Pig CLI

You can use the [`pig`](/pig) cli tool (pg package manager) or just use the traditional way. It's up to you.

```bash
curl -fsSL https://repo.pigsty.io/pig | bash  # install pig rpm/deb package
$ pig repo add pigsty pgdg -u                 # add pgdg & pigsty repo, update cache      
$ pig ext install pg17                        # install PostgreSQL 17 kernels with PGDG native packages
$ pig ext install pg_duckdb                   # install the pg_duckdb extension (for current pg17)
```

### APT Repo

[![Linux AMD](https://img.shields.io/badge/Linux-AMD64-%23FCC624?style=flat&logo=linux&labelColor=FCC624&logoColor=black)](https://pigsty.io/docs/node)
[![Linux ARM](https://img.shields.io/badge/Linux-ARM64-%23FCC624?style=flat&logo=linux&labelColor=FCC624&logoColor=black)](https://pigsty.io/docs/node)
[![Ubuntu Support: 24](https://img.shields.io/badge/Ubuntu-24/noble-%23E95420?style=flat&logo=ubuntu&logoColor=%23E95420)](https://pigsty.io/docs/pgext/list/deb/)
[![Ubuntu Support: 22](https://img.shields.io/badge/Ubuntu-22/jammy-%23E95420?style=flat&logo=ubuntu&logoColor=%23E95420)](https://pigsty.io/docs/pgext/list/deb/)
[![Debian Support: 12](https://img.shields.io/badge/Debian-12/bookworm-%23A81D33?style=flat&logo=debian&logoColor=%23A81D33)](https://pigsty.io/docs/reference/compatibility/)

All rpm/deb packages are signed with GPG key `B9BD8B20` (`9592A7BC7A682E7333376E09E7935D8DB9BD8B20` ).

For Ubuntu 22.04 / 24.04 & Debian 12 or any compatible platforms, use the following commands:

```bash
curl -fsSL https://repo.pigsty.io/key | sudo gpg --dearmor -o /etc/apt/keyrings/pigsty.gpg  # add gpg key
sudo tee /etc/apt/sources.list.d/pigsty-io.list > /dev/null <<EOF
deb [signed-by=/etc/apt/keyrings/pigsty.gpg] https://repo.pigsty.io/apt/infra generic main 
deb [signed-by=/etc/apt/keyrings/pigsty.gpg] https://repo.pigsty.io/apt/pgsql/$(lsb_release -cs) $(lsb_release -cs) main
EOF
sudo apt update;  # sudo apt install pig
```

### YUM Repo

[![Linux x86_64](https://img.shields.io/badge/Linux-x86_64-%23FCC624?style=flat&logo=linux&labelColor=FCC624&logoColor=black)](https://pigsty.io/docs/node)
[![Linux AARCH64](https://img.shields.io/badge/Linux-Aarch64-%23FCC624?style=flat&logo=linux&labelColor=FCC624&logoColor=black)](https://pigsty.io/docs/node)
[![RHEL Support: 8](https://img.shields.io/badge/EL-8-red?style=flat&logo=redhat&logoColor=red)](https://pigsty.io/docs/pgext/list/rpm/)
[![RHEL Support: 9](https://img.shields.io/badge/EL-9-red?style=flat&logo=redhat&logoColor=red)](https://pigsty.io/docs/pgext/list/rpm/)
[![RHEL](https://img.shields.io/badge/RHEL-slategray?style=flat&logo=redhat&logoColor=red)](https://pigsty.io/docs/pgext/list/rpm/)
[![CentOS](https://img.shields.io/badge/CentOS-slategray?style=flat&logo=centos&logoColor=%23262577)](https://almalinux.org/)
[![RockyLinux](https://img.shields.io/badge/RockyLinux-slategray?style=flat&logo=rockylinux&logoColor=%2310B981)](https://almalinux.org/)
[![AlmaLinux](https://img.shields.io/badge/AlmaLinux-slategray?style=flat&logo=almalinux&logoColor=black)](https://almalinux.org/)
[![OracleLinux](https://img.shields.io/badge/OracleLinux-slategray?style=flat&logo=oracle&logoColor=%23F80000)](https://almalinux.org/)

For EL 8/9 and compatible platforms, use the following commands to add the YUM repo:

```bash
curl -fsSL https://repo.pigsty.io/key      | sudo tee /etc/pki/rpm-gpg/RPM-GPG-KEY-pigsty >/dev/null  # add gpg key
curl -fsSL https://repo.pigsty.io/yum/repo | sudo tee /etc/yum.repos.d/pigsty.repo        >/dev/null  # add repo file
sudo yum makecache; # sudo yum install pig 
```

-------

## What's Inside

Linux x86_64/amd64 [Extension](/list) packages for PostgreSQL 12 - 17, on El8, EL9, Ubuntu 22.04/24.04 and Debian 12.

[**TIME**](/time): [`timescaledb`](/timescaledb) [`timeseries`](/timeseries) [`periods`](/periods) [`temporal_tables`](/temporal_tables) [`emaj`](/emaj) [`table_version`](/table_version) [`pg_cron`](/pg_cron) [`pg_task`](/pg_task) [`pg_later`](/pg_later) [`pg_background`](/pg_background)
[**GIS**](/gis): [`postgis`](/postgis) [`postgis_topology`](/postgis_topology) [`postgis_raster`](/postgis_raster) [`postgis_sfcgal`](/postgis_sfcgal) [`postgis_tiger_geocoder`](/postgis_tiger_geocoder) [`address_standardizer`](/address_standardizer) [`address_standardizer_data_us`](/address_standardizer_data_us) [`pgrouting`](/pgrouting) [`pointcloud`](/pointcloud) [`pointcloud_postgis`](/pointcloud_postgis) [`h3`](/h3) [`h3_postgis`](/h3_postgis) [`q3c`](/q3c) [`ogr_fdw`](/ogr_fdw) [`geoip`](/geoip) [`pg_polyline`](/pg_polyline) [`pg_geohash`](/pg_geohash) [`mobilitydb`](/mobilitydb) [`earthdistance`](/earthdistance)
[**RAG**](/rag): [`vector`](/vector) [`vchord`](/vchord) [`vectorscale`](/vectorscale) [`vectorize`](/vectorize) [`pg_similarity`](/pg_similarity) [`smlar`](/smlar) [`pg_summarize`](/pg_summarize) [`pg_tiktoken`](/pg_tiktoken) [`pg4ml`](/pg4ml) [`pgml`](/pgml)
[**FTS**](/fts): [`pg_search`](/pg_search) [`pgroonga`](/pgroonga) [`pgroonga_database`](/pgroonga_database) [`pg_bigm`](/pg_bigm) [`zhparser`](/zhparser) [`pg_bestmatch`](/pg_bestmatch) [`hunspell_cs_cz`](/hunspell_cs_cz) [`hunspell_de_de`](/hunspell_de_de) [`hunspell_en_us`](/hunspell_en_us) [`hunspell_fr`](/hunspell_fr) [`hunspell_ne_np`](/hunspell_ne_np) [`hunspell_nl_nl`](/hunspell_nl_nl) [`hunspell_nn_no`](/hunspell_nn_no) [`hunspell_pt_pt`](/hunspell_pt_pt) [`hunspell_ru_ru`](/hunspell_ru_ru) [`hunspell_ru_ru_aot`](/hunspell_ru_ru_aot) [`fuzzystrmatch`](/fuzzystrmatch) [`pg_trgm`](/pg_trgm)
[**OLAP**](/olap): [`citus`](/citus) [`citus_columnar`](/citus_columnar) [`columnar`](/columnar) [`pg_analytics`](/pg_analytics) [`pg_duckdb`](/pg_duckdb) [`duckdb_fdw`](/duckdb_fdw) [`pg_parquet`](/pg_parquet) [`pg_fkpart`](/pg_fkpart) [`pg_partman`](/pg_partman) [`plproxy`](/plproxy) [`pg_strom`](/pg_strom) [`tablefunc`](/tablefunc)
[**FEAT**](/feat): [`age`](/age) [`hll`](/hll) [`rum`](/rum) [`pg_graphql`](/pg_graphql) [`pg_jsonschema`](/pg_jsonschema) [`jsquery`](/jsquery) [`pg_hint_plan`](/pg_hint_plan) [`hypopg`](/hypopg) [`index_advisor`](/index_advisor) [`plan_filter`](/plan_filter) [`imgsmlr`](/imgsmlr) [`pg_ivm`](/pg_ivm) [`pgmq`](/pgmq) [`pgq`](/pgq) [`pg_cardano`](/pg_cardano) [`rdkit`](/rdkit) [`bloom`](/bloom)
[**LANG**](/lang): [`pg_tle`](/pg_tle) [`plv8`](/plv8) [`pllua`](/pllua) [`hstore_pllua`](/hstore_pllua) [`plluau`](/plluau) [`hstore_plluau`](/hstore_plluau) [`plprql`](/plprql) [`pldbgapi`](/pldbgapi) [`plpgsql_check`](/plpgsql_check) [`plprofiler`](/plprofiler) [`plsh`](/plsh) [`pljava`](/pljava) [`plr`](/plr) [`pgtap`](/pgtap) [`faker`](/faker) [`dbt2`](/dbt2) [`pltcl`](/pltcl) [`pltclu`](/pltclu) [`plperl`](/plperl) [`bool_plperl`](/bool_plperl) [`hstore_plperl`](/hstore_plperl) [`jsonb_plperl`](/jsonb_plperl) [`plperlu`](/plperlu) [`bool_plperlu`](/bool_plperlu) [`jsonb_plperlu`](/jsonb_plperlu) [`hstore_plperlu`](/hstore_plperlu) [`plpgsql`](/plpgsql) [`plpython3u`](/plpython3u) [`jsonb_plpython3u`](/jsonb_plpython3u) [`ltree_plpython3u`](/ltree_plpython3u) [`hstore_plpython3u`](/hstore_plpython3u)
[**TYPE**](/type): [`prefix`](/prefix) [`semver`](/semver) [`unit`](/unit) [`pgpdf`](/pgpdf) [`pglite_fusion`](/pglite_fusion) [`md5hash`](/md5hash) [`asn1oid`](/asn1oid) [`roaringbitmap`](/roaringbitmap) [`pgfaceting`](/pgfaceting) [`pg_sphere`](/pg_sphere) [`country`](/country) [`currency`](/currency) [`pgmp`](/pgmp) [`numeral`](/numeral) [`pg_rational`](/pg_rational) [`uint`](/uint) [`uint128`](/uint128) [`ip4r`](/ip4r) [`pg_duration`](/pg_duration) [`uri`](/uri) [`emailaddr`](/emailaddr) [`acl`](/acl) [`debversion`](/debversion) [`pg_rrule`](/pg_rrule) [`timestamp9`](/timestamp9) [`chkpass`](/chkpass) [`isn`](/isn) [`seg`](/seg) [`cube`](/cube) [`ltree`](/ltree) [`hstore`](/hstore) [`citext`](/citext) [`xml2`](/xml2)
[**UTIL**](/util): [`zstd`](/zstd) [`gzip`](/gzip) [`http`](/http) [`pg_net`](/pg_net) [`pgjwt`](/pgjwt) [`pg_smtp_client`](/pg_smtp_client) [`pg_html5_email_address`](/pg_html5_email_address) [`url_encode`](/url_encode) [`pgsql_tweaks`](/pgsql_tweaks) [`pg_extra_time`](/pg_extra_time) [`pgpcre`](/pgpcre) [`icu_ext`](/icu_ext) [`pgqr`](/pgqr) [`pg_protobuf`](/pg_protobuf) [`envvar`](/envvar) [`floatfile`](/floatfile) [`pg_readme`](/pg_readme) [`ddl_historization`](/ddl_historization) [`data_historization`](/data_historization) [`schedoc`](/schedoc) [`hashlib`](/hashlib) [`shacrypt`](/shacrypt) [`cryptint`](/cryptint) [`pguecc`](/pguecc)
[**FUNC**](/func): [`pg_idkit`](/pg_idkit) [`pg_uuidv7`](/pg_uuidv7) [`permuteseq`](/permuteseq) [`pg_hashids`](/pg_hashids) [`sequential_uuids`](/sequential_uuids) [`topn`](/topn) [`quantile`](/quantile) [`lower_quantile`](/lower_quantile) [`count_distinct`](/count_distinct) [`omnisketch`](/omnisketch) [`ddsketch`](/ddsketch) [`vasco`](/vasco) [`tdigest`](/tdigest) [`first_last_agg`](/first_last_agg) [`extra_window_functions`](/extra_window_functions) [`floatvec`](/floatvec) [`aggs_for_vecs`](/aggs_for_vecs) [`aggs_for_arrays`](/aggs_for_arrays) [`arraymath`](/arraymath) [`pg_math`](/pg_math) [`random`](/random) [`base36`](/base36) [`base62`](/base62) [`pg_base58`](/pg_base58) [`financial`](/financial) [`refint`](/refint) [`autoinc`](/autoinc) [`insert_username`](/insert_username) [`moddatetime`](/moddatetime) [`tsm_system_time`](/tsm_system_time) [`dict_xsyn`](/dict_xsyn) [`tsm_system_rows`](/tsm_system_rows) [`tcn`](/tcn) [`uuid-ossp`](/uuid-ossp) [`btree_gist`](/btree_gist) [`btree_gin`](/btree_gin) [`intarray`](/intarray) [`intagg`](/intagg) [`dict_int`](/dict_int) [`unaccent`](/unaccent)
[**ADMIN**](/admin): [`pg_repack`](/pg_repack) [`pg_squeeze`](/pg_squeeze) [`pg_dirtyread`](/pg_dirtyread) [`pgfincore`](/pgfincore) [`ddlx`](/ddlx) [`prioritize`](/prioritize) [`pg_checksums`](/pg_checksums) [`pg_readonly`](/pg_readonly) [`safeupdate`](/safeupdate) [`pg_upless`](/pg_upless) [`pg_permissions`](/pg_permissions) [`pgautofailover`](/pgautofailover) [`pg_catcheck`](/pg_catcheck) [`pre_prepare`](/pre_prepare) [`pgcozy`](/pgcozy) [`pg_orphaned`](/pg_orphaned) [`pg_crash`](/pg_crash) [`pg_cheat_funcs`](/pg_cheat_funcs) [`pg_savior`](/pg_savior) [`table_log`](/table_log) [`fio`](/fio) [`pgpool_adm`](/pgpool_adm) [`pgpool_recovery`](/pgpool_recovery) [`pgpool_regclass`](/pgpool_regclass) [`pgagent`](/pgagent) [`pg_prewarm`](/pg_prewarm) [`lo`](/lo) [`basic_archive`](/basic_archive) [`basebackup_to_shell`](/basebackup_to_shell) [`old_snapshot`](/old_snapshot) [`adminpack`](/adminpack) [`amcheck`](/amcheck) [`pg_surgery`](/pg_surgery)
[**STAT**](/stat): [`pg_profile`](/pg_profile) [`pg_show_plans`](/pg_show_plans) [`pg_stat_kcache`](/pg_stat_kcache) [`pg_stat_monitor`](/pg_stat_monitor) [`pg_qualstats`](/pg_qualstats) [`pg_store_plans`](/pg_store_plans) [`pg_track_settings`](/pg_track_settings) [`pg_wait_sampling`](/pg_wait_sampling) [`system_stats`](/system_stats) [`meta`](/meta) [`pgnodemx`](/pgnodemx) [`pg_proctab`](/pg_proctab) [`pg_sqlog`](/pg_sqlog) [`bgw_replstatus`](/bgw_replstatus) [`pgmeminfo`](/pgmeminfo) [`toastinfo`](/toastinfo) [`explain_ui`](/explain_ui) [`pg_relusage`](/pg_relusage) [`pagevis`](/pagevis) [`powa`](/powa) [`pageinspect`](/pageinspect) [`pgrowlocks`](/pgrowlocks) [`sslinfo`](/sslinfo) [`pg_buffercache`](/pg_buffercache) [`pg_walinspect`](/pg_walinspect) [`pg_freespacemap`](/pg_freespacemap) [`pg_visibility`](/pg_visibility) [`pgstattuple`](/pgstattuple) [`auto_explain`](/auto_explain) [`pg_stat_statements`](/pg_stat_statements)
[**SEC**](/sec): [`passwordcheck_cracklib`](/passwordcheck_cracklib) [`supautils`](/supautils) [`pgsodium`](/pgsodium) [`supabase_vault`](/supabase_vault) [`pg_session_jwt`](/pg_session_jwt) [`anon`](/anon) [`pg_tde`](/pg_tde) [`pgsmcrypto`](/pgsmcrypto) [`pgaudit`](/pgaudit) [`pgauditlogtofile`](/pgauditlogtofile) [`pg_auth_mon`](/pg_auth_mon) [`credcheck`](/credcheck) [`pgcryptokey`](/pgcryptokey) [`pg_jobmon`](/pg_jobmon) [`logerrors`](/logerrors) [`login_hook`](/login_hook) [`set_user`](/set_user) [`pg_snakeoil`](/pg_snakeoil) [`pgextwlist`](/pgextwlist) [`pg_auditor`](/pg_auditor) [`sslutils`](/sslutils) [`noset`](/noset) [`sepgsql`](/sepgsql) [`auth_delay`](/auth_delay) [`pgcrypto`](/pgcrypto) [`passwordcheck`](/passwordcheck)
[**FDW**](/fdw): [`wrappers`](/wrappers) [`multicorn`](/multicorn) [`odbc_fdw`](/odbc_fdw) [`jdbc_fdw`](/jdbc_fdw) [`mysql_fdw`](/mysql_fdw) [`oracle_fdw`](/oracle_fdw) [`tds_fdw`](/tds_fdw) [`db2_fdw`](/db2_fdw) [`sqlite_fdw`](/sqlite_fdw) [`pgbouncer_fdw`](/pgbouncer_fdw) [`mongo_fdw`](/mongo_fdw) [`redis_fdw`](/redis_fdw) [`redis`](/redis) [`kafka_fdw`](/kafka_fdw) [`hdfs_fdw`](/hdfs_fdw) [`firebird_fdw`](/firebird_fdw) [`aws_s3`](/aws_s3) [`log_fdw`](/log_fdw) [`dblink`](/dblink) [`file_fdw`](/file_fdw) [`postgres_fdw`](/postgres_fdw)
[**SIM**](/sim): [`orafce`](/orafce) [`pgtt`](/pgtt) [`session_variable`](/session_variable) [`pg_statement_rollback`](/pg_statement_rollback) [`pg_dbms_metadata`](/pg_dbms_metadata) [`pg_dbms_lock`](/pg_dbms_lock) [`pg_dbms_job`](/pg_dbms_job) [`babelfishpg_common`](/babelfishpg_common) [`babelfishpg_tsql`](/babelfishpg_tsql) [`babelfishpg_tds`](/babelfishpg_tds) [`babelfishpg_money`](/babelfishpg_money) [`pgmemcache`](/pgmemcache)
[**ETL**](/etl): [`pglogical`](/pglogical) [`pglogical_origin`](/pglogical_origin) [`pglogical_ticker`](/pglogical_ticker) [`pgl_ddl_deploy`](/pgl_ddl_deploy) [`pg_failover_slots`](/pg_failover_slots) [`wal2json`](/wal2json) [`wal2mongo`](/wal2mongo) [`decoderbufs`](/decoderbufs) [`decoder_raw`](/decoder_raw) [`pgoutput`](/pgoutput) [`test_decoding`](/test_decoding) [`mimeo`](/mimeo) [`repmgr`](/repmgr) [`pg_fact_loader`](/pg_fact_loader) [`pg_bulkload`](/pg_bulkload)

> Note: One single rpm/deb package may contain more than one extension



----------------

## Contrib

You can edit the [`pigsty.csv`](https://github.com/pgsty/extension/blob/main/data/pigsty.csv) raw data and create a pull request to update the metadata in case of any error.

If you have any suggestions on including new extensions or bumping to new versions, PR or [Issue](https://github.com/pgsty/extension/issues/new) are always welcome!


--------

## Compatibility

`pig` runs on: RHEL 8/9, Ubuntu 22.04/24.04, and Debian 12, on both `amd64/arm64` arch

|  Code   | Distribution                   |  `x86_64`  | `aarch64`  |
|:-------:|--------------------------------|:----------:|:----------:|
| **el9** | RHEL 9 / Rocky9 / Alma9  / ... | PG 17 - 13 | PG 17 - 13 |
| **el8** | RHEL 8 / Rocky8 / Alma8 / ...  | PG 17 - 13 | PG 17 - 13 |
| **u24** | Ubuntu 24.04 (`noble`)         | PG 17 - 13 | PG 17 - 13 |
| **u22** | Ubuntu 22.04 (`jammy`)         | PG 17 - 13 | PG 17 - 13 |
| **d12** | Debian 12 (`bookworm`)         | PG 17 - 13 | PG 17 - 13 |

Here are some bad cases and limitation for above distros:

- [`pg_duckdb`](https://ext.pigsty.io/#/pg_duckdb) `el8:*:*`
- [`pljava`](https://ext.pigsty.io/#/pljava): `el8:*:*`
- [`pllua`](https://ext.pigsty.io/#/pllua): `el8:arm:13,14,15`
- [`h3`](https://ext.pigsty.io/#/h3): `el8.amd.pg17`
- [`jdbc_fdw`](https://ext.pigsty.io/#/jdbc_fdw): `el:arm:*`
- [`pg_partman`](https://ext.pigsty.io/#/pg_partman) and [`timeseries`](https://ext.pigsty.io/#/timeseries): `u24:*:13`
- [`wiltondb`](https://ext.pigsty.io/#/wiltondb): `d12:*:*`


----------------

## About

[![Github: pgsty/extension](https://img.shields.io/badge/GitHub-pgsty/extension-slategray?style=flat&logo=github&logoColor=black)](https://github.com/pgsty/extension)
[![Author: RuohangFeng](https://img.shields.io/badge/Author-Ruohang_Feng-steelblue?style=flat)](https://vonng.com/)
[![About: @Vonng](https://img.shields.io/badge/%40Vonng-steelblue?style=flat)](https://vonng.com/en/)
[![Mail: rh@vonng.com](https://img.shields.io/badge/rh%40vonng.com-steelblue?style=flat)](mailto:rh@vonng.com)
[![Copyright: 2018-2024 rh@Vonng.com](https://img.shields.io/badge/Copyright-2018--2024_(rh%40vonng.com)-red?logo=c&color=steelblue)](https://github.com/Vonng)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-steelblue?style=flat&logo=opensourceinitiative&logoColor=green)](https://pigsty.io/docs/about/license/)

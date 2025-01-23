# plan_filter


> [pg_plan_filter](https://github.com/pgexperts/pg_plan_filter): filter statements by their execution plans.
>
> https://github.com/pgexperts/pg_plan_filter





[FEAT](/feat) extensions: [`omni`](/omni), [`omni_auth`](/omni_auth), [`omni_aws`](/omni_aws), [`omni_containers`](/omni_containers), [`omni_credentials`](/omni_credentials), [`omni_http`](/omni_http), [`omni_httpc`](/omni_httpc), [`omni_httpd`](/omni_httpd), [`omni_id`](/omni_id), [`omni_json`](/omni_json), [`omni_kube`](/omni_kube), [`omni_ledger`](/omni_ledger), [`omni_manifest`](/omni_manifest), [`omni_mimetypes`](/omni_mimetypes), [`omni_os`](/omni_os), [`omni_polyfill`](/omni_polyfill), [`omni_python`](/omni_python), [`omni_regex`](/omni_regex), [`omni_rest`](/omni_rest), [`omni_schema`](/omni_schema), [`omni_seq`](/omni_seq), [`omni_service`](/omni_service), [`omni_session`](/omni_session), [`omni_sql`](/omni_sql), [`omni_test`](/omni_test), [`omni_txn`](/omni_txn), [`omni_types`](/omni_types), [`omni_var`](/omni_var), [`omni_vfs`](/omni_vfs), [`omni_vfs_types_v1`](/omni_vfs_types_v1), [`omni_web`](/omni_web), [`omni_xml`](/omni_xml), [`omni_yaml`](/omni_yaml), [`age`](/age), [`hll`](/hll), [`rum`](/rum), [`pg_graphql`](/pg_graphql), [`pg_jsonschema`](/pg_jsonschema), [`jsquery`](/jsquery), [`pg_hint_plan`](/pg_hint_plan), [`hypopg`](/hypopg), [`index_advisor`](/index_advisor), [`plan_filter`](/plan_filter), [`imgsmlr`](/imgsmlr), [`pg_ivm`](/pg_ivm), [`pg_incremental`](/pg_incremental), [`pgmq`](/pgmq), [`pgq`](/pgq), [`pg_cardano`](/pg_cardano), [`rdkit`](/rdkit), [`bloom`](/bloom)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [plan_filter](https://github.com/pgexperts/pg_plan_filter) | 0.0.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_plan_filter](/plan_filter) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'plan_filter'; # add this extension to postgresql.conf
```



-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.0.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_plan_filter_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 0.0.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-plan-filter` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `plan_filter` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add plan_filter
```


Install `pg_plan_filter` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_plan_filter"]}'
```


Install `pg_plan_filter` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_plan_filter_17*;
dnf install pg_plan_filter_16*;
dnf install pg_plan_filter_15*;
dnf install pg_plan_filter_14*;
dnf install pg_plan_filter_13*;
```


Install `pg_plan_filter` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-plan-filter;
apt install postgresql-16-pg-plan-filter;
apt install postgresql-15-pg-plan-filter;
apt install postgresql-14-pg-plan-filter;
apt install postgresql-13-pg-plan-filter;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_plan_filter_17*` | `pg_plan_filter_16*` | `pg_plan_filter_15*` | `pg_plan_filter_14*` | `pg_plan_filter_13*` |
| `el9` | `pg_plan_filter_17*` | `pg_plan_filter_16*` | `pg_plan_filter_15*` | `pg_plan_filter_14*` | `pg_plan_filter_13*` |
| `d12` | `postgresql-17-pg-plan-filter` | `postgresql-16-pg-plan-filter` | `postgresql-15-pg-plan-filter` | `postgresql-14-pg-plan-filter` | `postgresql-13-pg-plan-filter` |
| `u22` | `postgresql-17-pg-plan-filter` | `postgresql-16-pg-plan-filter` | `postgresql-15-pg-plan-filter` | `postgresql-14-pg-plan-filter` | `postgresql-13-pg-plan-filter` |
| `u24` | `postgresql-17-pg-plan-filter` | `postgresql-16-pg-plan-filter` | `postgresql-15-pg-plan-filter` | `postgresql-14-pg-plan-filter` | `postgresql-13-pg-plan-filter` |






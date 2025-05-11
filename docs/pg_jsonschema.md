# pg_jsonschema


> [pg_jsonschema](https://github.com/supabase/pg_jsonschema): PostgreSQL extension providing JSON Schema validation
>
> https://github.com/supabase/pg_jsonschema





[FEAT](/feat) extensions: [`age`](/age), [`hll`](/hll), [`rum`](/rum), [`pg_graphql`](/pg_graphql), [`pg_jsonschema`](/pg_jsonschema), [`jsquery`](/jsquery), [`pg_hint_plan`](/pg_hint_plan), [`hypopg`](/hypopg), [`index_advisor`](/index_advisor), [`plan_filter`](/plan_filter), [`imgsmlr`](/imgsmlr), [`pg_ivm`](/pg_ivm), [`pg_incremental`](/pg_incremental), [`pgmq`](/pgmq), [`pgq`](/pgq), [`pg_cardano`](/pg_cardano), [`rdkit`](/rdkit), [`omni`](/omni), [`omni_auth`](/omni_auth), [`omni_aws`](/omni_aws), [`omni_cloudevents`](/omni_cloudevents), [`omni_containers`](/omni_containers), [`omni_credentials`](/omni_credentials), [`omni_email`](/omni_email), [`omni_http`](/omni_http), [`omni_httpc`](/omni_httpc), [`omni_httpd`](/omni_httpd), [`omni_id`](/omni_id), [`omni_json`](/omni_json), [`omni_kube`](/omni_kube), [`omni_ledger`](/omni_ledger), [`omni_manifest`](/omni_manifest), [`omni_mimetypes`](/omni_mimetypes), [`omni_os`](/omni_os), [`omni_polyfill`](/omni_polyfill), [`omni_python`](/omni_python), [`omni_regex`](/omni_regex), [`omni_rest`](/omni_rest), [`omni_schema`](/omni_schema), [`omni_seq`](/omni_seq), [`omni_service`](/omni_service), [`omni_session`](/omni_session), [`omni_sql`](/omni_sql), [`omni_sqlite`](/omni_sqlite), [`omni_test`](/omni_test), [`omni_txn`](/omni_txn), [`omni_types`](/omni_types), [`omni_var`](/omni_var), [`omni_vfs`](/omni_vfs), [`omni_vfs_types_v1`](/omni_vfs_types_v1), [`omni_web`](/omni_web), [`omni_worker`](/omni_worker), [`omni_xml`](/omni_xml), [`omni_yaml`](/omni_yaml), [`bloom`](/bloom)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_jsonschema](https://github.com/supabase/pg_jsonschema) | 0.3.3 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_jsonschema](/pg_jsonschema) | `pgrx`, `supabase` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_jsonschema;
```
> **Comment**: pgrx=0.12.9
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.3.3 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_jsonschema_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 0.3.3 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-jsonschema` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pg_jsonschema` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_jsonschema
```


Install `pg_jsonschema` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_jsonschema"]}'
```


Install `pg_jsonschema` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_jsonschema_17;
dnf install pg_jsonschema_16;
dnf install pg_jsonschema_15;
dnf install pg_jsonschema_14;
dnf install pg_jsonschema_13;
```


Install `pg_jsonschema` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-jsonschema;
apt install postgresql-16-pg-jsonschema;
apt install postgresql-15-pg-jsonschema;
apt install postgresql-14-pg-jsonschema;
apt install postgresql-13-pg-jsonschema;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_jsonschema_17` | `pg_jsonschema_16` | `pg_jsonschema_15` | `pg_jsonschema_14` | `pg_jsonschema_13` |
| `el9` | `pg_jsonschema_17` | `pg_jsonschema_16` | `pg_jsonschema_15` | `pg_jsonschema_14` | `pg_jsonschema_13` |
| `d12` | `postgresql-17-pg-jsonschema` | `postgresql-16-pg-jsonschema` | `postgresql-15-pg-jsonschema` | `postgresql-14-pg-jsonschema` | `postgresql-13-pg-jsonschema` |
| `u22` | `postgresql-17-pg-jsonschema` | `postgresql-16-pg-jsonschema` | `postgresql-15-pg-jsonschema` | `postgresql-14-pg-jsonschema` | `postgresql-13-pg-jsonschema` |
| `u24` | `postgresql-17-pg-jsonschema` | `postgresql-16-pg-jsonschema` | `postgresql-15-pg-jsonschema` | `postgresql-14-pg-jsonschema` | `postgresql-13-pg-jsonschema` |






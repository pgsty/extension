# omni_auth


> [omnigres](https://docs.omnigres.org/omni_auth/basics/): Basic session management
>
> https://docs.omnigres.org/omni_auth/basics/





[FEAT](/feat) extensions: [`age`](/age), [`hll`](/hll), [`rum`](/rum), [`pg_graphql`](/pg_graphql), [`pg_jsonschema`](/pg_jsonschema), [`jsquery`](/jsquery), [`pg_hint_plan`](/pg_hint_plan), [`hypopg`](/hypopg), [`index_advisor`](/index_advisor), [`plan_filter`](/plan_filter), [`imgsmlr`](/imgsmlr), [`pg_ivm`](/pg_ivm), [`pg_incremental`](/pg_incremental), [`pgmq`](/pgmq), [`pgq`](/pgq), [`pg_cardano`](/pg_cardano), [`rdkit`](/rdkit), [`omni`](/omni), [`omni_auth`](/omni_auth), [`omni_aws`](/omni_aws), [`omni_cloudevents`](/omni_cloudevents), [`omni_containers`](/omni_containers), [`omni_credentials`](/omni_credentials), [`omni_http`](/omni_http), [`omni_httpc`](/omni_httpc), [`omni_httpd`](/omni_httpd), [`omni_id`](/omni_id), [`omni_json`](/omni_json), [`omni_kube`](/omni_kube), [`omni_ledger`](/omni_ledger), [`omni_manifest`](/omni_manifest), [`omni_mimetypes`](/omni_mimetypes), [`omni_os`](/omni_os), [`omni_polyfill`](/omni_polyfill), [`omni_python`](/omni_python), [`omni_regex`](/omni_regex), [`omni_rest`](/omni_rest), [`omni_schema`](/omni_schema), [`omni_seq`](/omni_seq), [`omni_service`](/omni_service), [`omni_session`](/omni_session), [`omni_sql`](/omni_sql), [`omni_sqlite`](/omni_sqlite), [`omni_test`](/omni_test), [`omni_txn`](/omni_txn), [`omni_types`](/omni_types), [`omni_var`](/omni_var), [`omni_vfs`](/omni_vfs), [`omni_vfs_types_v1`](/omni_vfs_types_v1), [`omni_web`](/omni_web), [`omni_worker`](/omni_worker), [`omni_xml`](/omni_xml), [`omni_yaml`](/omni_yaml), [`bloom`](/bloom)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [omni_auth](https://docs.omnigres.org/omni_auth/basics/) | 0.1.3 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [omnigres](/omni_auth) |  | `omni_auth` | [`omni_types`](omni_types), [`omni_id`](omni_id), [`pgcrypto`](pgcrypto), [`btree_gist`](btree_gist), [`omni_polyfill`](omni_polyfill) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION omni_auth CASCADE;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| Distro-omni | 0.2.9 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `omnigres_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| Distro-omni | 0.2.9 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-omnigres` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `omni_auth` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add omni_auth
```


Install `omnigres` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["omnigres"]}'
```


Install `omnigres` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install omnigres_17;
dnf install omnigres_16;
dnf install omnigres_15;
dnf install omnigres_14;
dnf install omnigres_13;
```


Install `omnigres` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-omnigres;
apt install postgresql-16-omnigres;
apt install postgresql-15-omnigres;
apt install postgresql-14-omnigres;
apt install postgresql-13-omnigres;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `omnigres_17` | `omnigres_16` | `omnigres_15` | `omnigres_14` | `omnigres_13` |
| `el9` | `omnigres_17` | `omnigres_16` | `omnigres_15` | `omnigres_14` | `omnigres_13` |
| `d12` | `postgresql-17-omnigres` | `postgresql-16-omnigres` | `postgresql-15-omnigres` | `postgresql-14-omnigres` | `postgresql-13-omnigres` |
| `u22` | `postgresql-17-omnigres` | `postgresql-16-omnigres` | `postgresql-15-omnigres` | `postgresql-14-omnigres` | `postgresql-13-omnigres` |
| `u24` | `postgresql-17-omnigres` | `postgresql-16-omnigres` | `postgresql-15-omnigres` | `postgresql-14-omnigres` | `postgresql-13-omnigres` |






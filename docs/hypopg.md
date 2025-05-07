# hypopg


> [hypopg](https://github.com/HypoPG/hypopg): Hypothetical indexes for PostgreSQL
>
> https://github.com/HypoPG/hypopg





[FEAT](/feat) extensions: [`age`](/age), [`hll`](/hll), [`rum`](/rum), [`pg_graphql`](/pg_graphql), [`pg_jsonschema`](/pg_jsonschema), [`jsquery`](/jsquery), [`pg_hint_plan`](/pg_hint_plan), [`hypopg`](/hypopg), [`index_advisor`](/index_advisor), [`plan_filter`](/plan_filter), [`imgsmlr`](/imgsmlr), [`pg_ivm`](/pg_ivm), [`pg_incremental`](/pg_incremental), [`pgmq`](/pgmq), [`pgq`](/pgq), [`pg_cardano`](/pg_cardano), [`rdkit`](/rdkit), [`omni`](/omni), [`omni_auth`](/omni_auth), [`omni_aws`](/omni_aws), [`omni_cloudevents`](/omni_cloudevents), [`omni_containers`](/omni_containers), [`omni_credentials`](/omni_credentials), [`omni_http`](/omni_http), [`omni_httpc`](/omni_httpc), [`omni_httpd`](/omni_httpd), [`omni_id`](/omni_id), [`omni_json`](/omni_json), [`omni_kube`](/omni_kube), [`omni_ledger`](/omni_ledger), [`omni_manifest`](/omni_manifest), [`omni_mimetypes`](/omni_mimetypes), [`omni_os`](/omni_os), [`omni_polyfill`](/omni_polyfill), [`omni_python`](/omni_python), [`omni_regex`](/omni_regex), [`omni_rest`](/omni_rest), [`omni_schema`](/omni_schema), [`omni_seq`](/omni_seq), [`omni_service`](/omni_service), [`omni_session`](/omni_session), [`omni_sql`](/omni_sql), [`omni_sqlite`](/omni_sqlite), [`omni_test`](/omni_test), [`omni_txn`](/omni_txn), [`omni_types`](/omni_types), [`omni_var`](/omni_var), [`omni_vfs`](/omni_vfs), [`omni_vfs_types_v1`](/omni_vfs_types_v1), [`omni_web`](/omni_web), [`omni_worker`](/omni_worker), [`omni_xml`](/omni_xml), [`omni_yaml`](/omni_yaml), [`bloom`](/bloom)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [hypopg](https://github.com/HypoPG/hypopg) | 1.4.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [hypopg](/hypopg) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION hypopg;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.4.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `hypopg_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 1.4.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-hypopg` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `hypopg` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add hypopg
```


Install `hypopg` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["hypopg"]}'
```


Install `hypopg` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install hypopg_17*;
dnf install hypopg_16*;
dnf install hypopg_15*;
dnf install hypopg_14*;
dnf install hypopg_13*;
```


Install `hypopg` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-hypopg;
apt install postgresql-16-hypopg;
apt install postgresql-15-hypopg;
apt install postgresql-14-hypopg;
apt install postgresql-13-hypopg;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `hypopg_17*` | `hypopg_16*` | `hypopg_15*` | `hypopg_14*` | `hypopg_13*` |
| `el9` | `hypopg_17*` | `hypopg_16*` | `hypopg_15*` | `hypopg_14*` | `hypopg_13*` |
| `d12` | `postgresql-17-hypopg` | `postgresql-16-hypopg` | `postgresql-15-hypopg` | `postgresql-14-hypopg` | `postgresql-13-hypopg` |
| `u22` | `postgresql-17-hypopg` | `postgresql-16-hypopg` | `postgresql-15-hypopg` | `postgresql-14-hypopg` | `postgresql-13-hypopg` |
| `u24` | `postgresql-17-hypopg` | `postgresql-16-hypopg` | `postgresql-15-hypopg` | `postgresql-14-hypopg` | `postgresql-13-hypopg` |






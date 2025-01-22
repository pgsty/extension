# bloom


> [bloom](https://www.postgresql.org/docs/current/bloom.html): bloom access method - signature file based index
>
> https://www.postgresql.org/docs/current/bloom.html





[FEAT](/feat) extensions: [`omni`](/omni), [`omni_auth`](/omni_auth), [`omni_aws`](/omni_aws), [`omni_containers`](/omni_containers), [`omni_credentials`](/omni_credentials), [`omni_http`](/omni_http), [`omni_httpc`](/omni_httpc), [`omni_httpd`](/omni_httpd), [`omni_id`](/omni_id), [`omni_json`](/omni_json), [`omni_kube`](/omni_kube), [`omni_ledger`](/omni_ledger), [`omni_manifest`](/omni_manifest), [`omni_mimetypes`](/omni_mimetypes), [`omni_os`](/omni_os), [`omni_polyfill`](/omni_polyfill), [`omni_python`](/omni_python), [`omni_regex`](/omni_regex), [`omni_rest`](/omni_rest), [`omni_schema`](/omni_schema), [`omni_seq`](/omni_seq), [`omni_service`](/omni_service), [`omni_session`](/omni_session), [`omni_sql`](/omni_sql), [`omni_test`](/omni_test), [`omni_txn`](/omni_txn), [`omni_types`](/omni_types), [`omni_var`](/omni_var), [`omni_vfs`](/omni_vfs), [`omni_vfs_types_v1`](/omni_vfs_types_v1), [`omni_web`](/omni_web), [`omni_xml`](/omni_xml), [`omni_yaml`](/omni_yaml), [`age`](/age), [`hll`](/hll), [`rum`](/rum), [`pg_graphql`](/pg_graphql), [`pg_jsonschema`](/pg_jsonschema), [`jsquery`](/jsquery), [`pg_hint_plan`](/pg_hint_plan), [`hypopg`](/hypopg), [`index_advisor`](/index_advisor), [`plan_filter`](/plan_filter), [`imgsmlr`](/imgsmlr), [`pg_ivm`](/pg_ivm), [`pgmq`](/pgmq), [`pgq`](/pgq), [`pg_cardano`](/pg_cardano), [`rdkit`](/rdkit), [`bloom`](/bloom)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [bloom](https://www.postgresql.org/docs/current/bloom.html) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | **<span class="tcblue">CONTRIB</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [bloom](/bloom) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION bloom;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql$v-contrib` | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** |  |
| [DEB](/deb) | 1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | `postgresql-$v` | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** | **<span class="tcblue">✔</span>** |  |



Install `bloom` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add bloom
```


Install `bloom` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["bloom"]}'
```


Install `bloom` [RPM](/rpm) from the **<span class="tcblue">CONTRIB</span>** **YUM** repo:

```bash
dnf install postgresql17-contrib;
dnf install postgresql16-contrib;
dnf install postgresql15-contrib;
dnf install postgresql14-contrib;
dnf install postgresql13-contrib;
```


Install `bloom` [DEB](/deb) from the **<span class="tcblue">CONTRIB</span>** **APT** repo:

```bash
apt install postgresql-17;
apt install postgresql-16;
apt install postgresql-15;
apt install postgresql-14;
apt install postgresql-13;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `postgresql17-contrib` | `postgresql16-contrib` | `postgresql15-contrib` | `postgresql14-contrib` | `postgresql13-contrib` |
| `el9` | `postgresql17-contrib` | `postgresql16-contrib` | `postgresql15-contrib` | `postgresql14-contrib` | `postgresql13-contrib` |
| `d12` | `postgresql-17` | `postgresql-16` | `postgresql-15` | `postgresql-14` | `postgresql-13` |
| `u22` | `postgresql-17` | `postgresql-16` | `postgresql-15` | `postgresql-14` | `postgresql-13` |
| `u24` | `postgresql-17` | `postgresql-16` | `postgresql-15` | `postgresql-14` | `postgresql-13` |






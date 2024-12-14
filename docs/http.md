# pg_http


> [pg_http](https://github.com/pramsey/pgsql-http): HTTP client for PostgreSQL, allows web page retrieval inside the database.
>
> https://github.com/pramsey/pgsql-http





[FUNC](/func) extensions: [`topn`](/topn), [`gzip`](/gzip), [`zstd`](/zstd), [`http`](/http), [`pg_net`](/pg_net), [`pg_smtp_client`](/pg_smtp_client), [`pg_html5_email_address`](/pg_html5_email_address), [`pgsql_tweaks`](/pgsql_tweaks), [`pg_extra_time`](/pg_extra_time), [`count_distinct`](/count_distinct), [`extra_window_functions`](/extra_window_functions), [`first_last_agg`](/first_last_agg), [`tdigest`](/tdigest), [`aggs_for_vecs`](/aggs_for_vecs), [`aggs_for_arrays`](/aggs_for_arrays), [`arraymath`](/arraymath), [`quantile`](/quantile), [`lower_quantile`](/lower_quantile), [`pg_idkit`](/pg_idkit), [`pg_uuidv7`](/pg_uuidv7), [`permuteseq`](/permuteseq), [`pg_hashids`](/pg_hashids), [`sequential_uuids`](/sequential_uuids), [`pg_math`](/pg_math), [`random`](/random), [`base36`](/base36), [`base62`](/base62), [`pg_base58`](/pg_base58), [`floatvec`](/floatvec), [`financial`](/financial), [`pgjwt`](/pgjwt), [`pg_hashlib`](/pg_hashlib), [`shacrypt`](/shacrypt), [`cryptint`](/cryptint), [`pguecc`](/pguecc), [`pgpcre`](/pgpcre), [`icu_ext`](/icu_ext), [`pgqr`](/pgqr), [`envvar`](/envvar), [`pg_protobuf`](/pg_protobuf), [`url_encode`](/url_encode), [`refint`](/refint), [`autoinc`](/autoinc), [`insert_username`](/insert_username), [`moddatetime`](/moddatetime), [`tsm_system_time`](/tsm_system_time), [`dict_xsyn`](/dict_xsyn), [`tsm_system_rows`](/tsm_system_rows), [`tcn`](/tcn), [`uuid-ossp`](/uuid-ossp), [`btree_gist`](/btree_gist), [`btree_gin`](/btree_gin), [`intarray`](/intarray), [`intagg`](/intagg), [`dict_int`](/dict_int), [`unaccent`](/unaccent)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [http](https://github.com/pramsey/pgsql-http) | 1.6 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_http](/http) | `supabase` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION http;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.6 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `pgsql_http_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 1.6 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-http` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pg_http` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_http"]}'
```


Install `pg_http` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pgsql_http_17*;
dnf install pgsql_http_16*;
dnf install pgsql_http_15*;
dnf install pgsql_http_14*;
dnf install pgsql_http_13*;
dnf install pgsql_http_12*;
```


Install `pg_http` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-http;
apt install postgresql-16-http;
apt install postgresql-15-http;
apt install postgresql-14-http;
apt install postgresql-13-http;
apt install postgresql-12-http;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgsql_http_17*` | `pgsql_http_16*` | `pgsql_http_15*` | `pgsql_http_14*` | `pgsql_http_13*` | `pgsql_http_12*` |
| `el9` | `pgsql_http_17*` | `pgsql_http_16*` | `pgsql_http_15*` | `pgsql_http_14*` | `pgsql_http_13*` | `pgsql_http_12*` |
| `d12` | `postgresql-17-http` | `postgresql-16-http` | `postgresql-15-http` | `postgresql-14-http` | `postgresql-13-http` | `postgresql-12-http` |
| `u22` | `postgresql-17-http` | `postgresql-16-http` | `postgresql-15-http` | `postgresql-14-http` | `postgresql-13-http` | `postgresql-12-http` |
| `u24` | `postgresql-17-http` | `postgresql-16-http` | `postgresql-15-http` | `postgresql-14-http` | `postgresql-13-http` | `postgresql-12-http` |






--------

## Usage

https://github.com/pramsey/pgsql-http

Request / Response Schema:

```
     Composite type "public.http_request"
    Column    |       Type        | Modifiers
--------------+-------------------+-----------
 method       | http_method       |
 uri          | character varying |
 headers      | http_header[]     |
 content_type | character varying |
 content      | character varying |

    Composite type "public.http_response"
    Column    |       Type        | Modifiers
--------------+-------------------+-----------
 status       | integer           |
 content_type | character varying |
 headers      | http_header[]     |
 content      | character varying |
```


### Examples

Sending HTTP GET requests with SQL

```sql
CREATE EXTENSION http;

-- get content
SELECT content FROM http_get('http://httpbun.com/');

-- get status and content_type
SELECT status, content_type FROM http_get('http://httpbun.com/');

--  status |       content_type
-- --------+--------------------------
--     200 | text/html; charset=utf-8

-- get headers
SELECT (unnest(headers)).* FROM http_get('http://httpbun.com/');

--             field           |                      value
--  ---------------------------+--------------------------------------------------
--  Location                  | https://httpbun.com/
--  Date                      | Mon, 04 Nov 2024 09:00:36 GMT
--  Content-Length            | 0
--  Connection                | close
--  alt-svc                   | h3=":443"; ma=2592000
--  content-security-policy   | frame-ancestors 'none'
--  content-type              | text/html
--  date                      | Mon, 04 Nov 2024 09:00:37 GMT
--  strict-transport-security | max-age=31536000; includeSubDomains; preload
--  x-content-type-options    | nosniff
--  x-powered-by              | httpbun/af040d24038613575a85f74c2283ae79f8169927
--  (11 rows)
```


```sql
SELECT status, content::json->'form' AS form FROM http_post('http://httpbun.com/post', jsonb_build_object('myvar','myval','foo','bar'));
```

Issue http put requests:

```sql
SELECT status, content_type, content::json->>'data' AS data
  FROM http_put('http://httpbun.com/put', 'some text', 'text/plain');


--  status |   content_type   |   data
-- --------+------------------+-----------
--  200 | application/json | some text
```

Issue http post request:



# zstd


> [pg_zstd](https://github.com/grahamedgecombe/pgzstd): Zstandard compression algorithm implementation in PostgreSQL
>
> https://github.com/grahamedgecombe/pgzstd





[UTIL](/util) extensions: [`gzip`](/gzip), [`bzip`](/bzip), [`zstd`](/zstd), [`http`](/http), [`pg_net`](/pg_net), [`pg_curl`](/pg_curl), [`pgjq`](/pgjq), [`pgjwt`](/pgjwt), [`pg_smtp_client`](/pg_smtp_client), [`pg_html5_email_address`](/pg_html5_email_address), [`url_encode`](/url_encode), [`pgsql_tweaks`](/pgsql_tweaks), [`pg_extra_time`](/pg_extra_time), [`pgpcre`](/pgpcre), [`icu_ext`](/icu_ext), [`pgqr`](/pgqr), [`pg_protobuf`](/pg_protobuf), [`envvar`](/envvar), [`floatfile`](/floatfile), [`pg_render`](/pg_render), [`pg_readme`](/pg_readme), [`pg_readme_test_extension`](/pg_readme_test_extension), [`ddl_historization`](/ddl_historization), [`data_historization`](/data_historization), [`schedoc`](/schedoc), [`hashlib`](/hashlib), [`xxhash`](/xxhash), [`shacrypt`](/shacrypt), [`cryptint`](/cryptint), [`pguecc`](/pguecc), [`sparql`](/sparql)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [zstd](https://github.com/grahamedgecombe/pgzstd) | 1.1.2 | **<span class="tcblue">ISC</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_zstd](/zstd) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION zstd;
```
> **Comment**: +varatt.h
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.1.2 | **<span class="tcblue">ISC</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_zstd_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.1.2 | **<span class="tcblue">ISC</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-zstd` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `zstd` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add zstd
```


Install `pg_zstd` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_zstd"]}'
```


Install `pg_zstd` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_zstd_17*;
dnf install pg_zstd_16*;
dnf install pg_zstd_15*;
dnf install pg_zstd_14*;
dnf install pg_zstd_13*;
```


Install `pg_zstd` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-zstd;
apt install postgresql-16-zstd;
apt install postgresql-15-zstd;
apt install postgresql-14-zstd;
apt install postgresql-13-zstd;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_zstd_17*` | `pg_zstd_16*` | `pg_zstd_15*` | `pg_zstd_14*` | `pg_zstd_13*` |
| `el9` | `pg_zstd_17*` | `pg_zstd_16*` | `pg_zstd_15*` | `pg_zstd_14*` | `pg_zstd_13*` |
| `d12` | `postgresql-17-zstd` | `postgresql-16-zstd` | `postgresql-15-zstd` | `postgresql-14-zstd` | `postgresql-13-zstd` |
| `u22` | `postgresql-17-zstd` | `postgresql-16-zstd` | `postgresql-15-zstd` | `postgresql-14-zstd` | `postgresql-13-zstd` |
| `u24` | `postgresql-17-zstd` | `postgresql-16-zstd` | `postgresql-15-zstd` | `postgresql-14-zstd` | `postgresql-13-zstd` |






--------

## Usage

| Function                                                                             | Return Type |
|--------------------------------------------------------------------------------------|-------------|
| <code>zstd_compress(*data* bytea [, *dictionary* bytea [, *level* integer ]])</code> | `bytea`     |
| <code>zstd_decompress(*data* bytea [, *dictionary* bytea ])</code>                   | `bytea`     |
| <code>zstd_length(*data* bytea)</code>                                               | `integer`   |

`zstd_compress` compresses the provided `data` and returns a Zstandard frame. A
preset `dictionary` may also be provided. The default compression `level` may
also be overriden, valid values range from `1` (best speed) to `22` (best
compression). The default level is `3`.

If you want to override the compression level without using a dictionary, set
`dictionary` to `NULL`.

`zstd_decompress` decompresses the provided Zstandard frame in `data` and
returns the uncompressed data. A preset `dictionary`, matching the dictionary
used to compress the data, may also be provided.

`zstd_length` returns the decompressed length of the provided Zstandard frame.
If `ZSTD_getFrameContentSize()` is available it returns `NULL` if the length is
unknown. If unavailable, it isn't possible to distinguish the error, unknown
decompressed length and zero decompressed length cases.


### Example

Basic compress/decompress example:

```sql
CREATE EXTENSION zstd;

SELECT zstd_compress('hello world');
-- zstd_compress
-- --------------------------------------------
-- \x28b52ffd200b59000068656c6c6f20776f726c64

SELECT convert_from(zstd_decompress('\x28b52ffd200b59000068656c6c6f20776f726c64'), 'utf-8');
-- convert_from
-- --------------
--  hello world
```

Compress with level (`1` for best speed, `22` for best compression, default to `3`)

```sql
CREATE EXTENSION zstd;

SELECT zstd_compress('hello world',  NULL, 10);
-- zstd_compress
-- --------------------------------------------
-- \x28b52ffd200b59000068656c6c6f20776f726c64

SELECT convert_from(zstd_decompress('\x28b52ffd200b59000068656c6c6f20776f726c64'), 'utf-8');
-- convert_from
-- --------------
--  hello world
```


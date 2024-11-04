

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

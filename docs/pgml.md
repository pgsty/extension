# pgml


> [pgml](https://github.com/postgresml/postgresml): PostgresML: Run AL/ML workloads with SQL interface
>
> https://github.com/postgresml/postgresml





[RAG](/rag) extensions: [`vector`](/vector), [`vectorscale`](/vectorscale), [`vectorize`](/vectorize), [`pg_similarity`](/pg_similarity), [`smlar`](/smlar), [`pg_summarize`](/pg_summarize), [`pg_tiktoken`](/pg_tiktoken), [`pgml`](/pgml), [`pg4ml`](/pg4ml)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgml](https://github.com/postgresml/postgresml) | 2.9.3 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgml](/pgml) | `pgrx` | `pgml` |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |



```bash
shared_preload_libraries = 'pgml'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION pgml;
```
> **Comment**: missing noble u24 packages
-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgml_17` | `pgml_16` | `pgml_15` | `pgml_14` | `pgml_13` | `pgml_12` |
| `el9` | `pgml_17` | `pgml_16` | `pgml_15` | `pgml_14` | `pgml_13` | `pgml_12` |
| `d12` | `postgresql-17-pgml` | `postgresql-16-pgml` | `postgresql-15-pgml` | `postgresql-14-pgml` | `postgresql-13-pgml` | `postgresql-12-pgml` |
| `u22` | `postgresql-17-pgml` | `postgresql-16-pgml` | `postgresql-15-pgml` | `postgresql-14-pgml` | `postgresql-13-pgml` | `postgresql-12-pgml` |
| `u24` | `postgresql-17-pgml` | `postgresql-16-pgml` | `postgresql-15-pgml` | `postgresql-14-pgml` | `postgresql-13-pgml` | `postgresql-12-pgml` |



Install `pgml` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgml"]}'
```


Install `pgml` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install pgml_17;
yum install pgml_16;
yum install pgml_15;
yum install pgml_14;
yum install pgml_13;
yum install pgml_12;
```


Install `pgml` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pgml;
apt install postgresql-16-pgml;
apt install postgresql-15-pgml;
apt install postgresql-14-pgml;
apt install postgresql-13-pgml;
apt install postgresql-12-pgml;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgml_17` | `pgml_16` | `pgml_15` | `pgml_14` | `pgml_13` | `pgml_12` |
| `el9` | `pgml_17` | `pgml_16` | `pgml_15` | `pgml_14` | `pgml_13` | `pgml_12` |
| `d12` | `postgresql-17-pgml` | `postgresql-16-pgml` | `postgresql-15-pgml` | `postgresql-14-pgml` | `postgresql-13-pgml` | `postgresql-12-pgml` |
| `u22` | `postgresql-17-pgml` | `postgresql-16-pgml` | `postgresql-15-pgml` | `postgresql-14-pgml` | `postgresql-13-pgml` | `postgresql-12-pgml` |
| `u24` | `postgresql-17-pgml` | `postgresql-16-pgml` | `postgresql-15-pgml` | `postgresql-14-pgml` | `postgresql-13-pgml` | `postgresql-12-pgml` |





--------

## Usage


After installing the `pgml` extension and python dependencies on all cluster nodes, you can enable `pgml` on the PostgreSQL cluster.

[Configure](https://pigsty.io/docs/pgsql/admin/#config-cluster) cluster with `patronictl` command and add `pgml` to `shared_preload_libraries`, and specify your `venv` dir in `pgml.venv`:

```yaml
shared_preload_libraries: pgml, timescaledb, pg_stat_statements, auto_explain
pgml.venv: '/data/pgml'
```

After that, restart database cluster, and create extension with SQL command:

```sql
CREATE EXTENSION vector;        -- nice to have pgvector installed too!
CREATE EXTENSION pgml;          -- create PostgresML in current database
SELECT pgml.version();          -- print PostgresML version string
```

If it works, you should see something like:

```bash
# create extension pgml;
INFO:  Python version: 3.11.2 (main, Oct  5 2023, 16:06:03) [GCC 8.5.0 20210514 (Red Hat 8.5.0-18)]
INFO:  Scikit-learn 1.3.0, XGBoost 2.0.0, LightGBM 4.1.0, NumPy 1.26.1
CREATE EXTENSION

# SELECT pgml.version(); -- print PostgresML version string
 version
---------
 2.7.8
```

You are all set! Check PostgresML for more details: https://postgresml.org/docs/guides/use-cases/




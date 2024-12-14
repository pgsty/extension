# pgpdf


> [pgpdf](https://github.com/Florents-Tselai/pgpdf): PDF type with meta admin & Full-Text Search
>
> https://github.com/Florents-Tselai/pgpdf





[TYPE](/type) extensions: [`prefix`](/prefix), [`semver`](/semver), [`unit`](/unit), [`pgpdf`](/pgpdf), [`pglite_fusion`](/pglite_fusion), [`md5hash`](/md5hash), [`asn1oid`](/asn1oid), [`roaringbitmap`](/roaringbitmap), [`pgfaceting`](/pgfaceting), [`pg_sphere`](/pg_sphere), [`country`](/country), [`currency`](/currency), [`pgmp`](/pgmp), [`numeral`](/numeral), [`pg_rational`](/pg_rational), [`uint`](/uint), [`uint128`](/uint128), [`ip4r`](/ip4r), [`uri`](/uri), [`pgemailaddr`](/pgemailaddr), [`acl`](/acl), [`debversion`](/debversion), [`pg_rrule`](/pg_rrule), [`timestamp9`](/timestamp9), [`chkpass`](/chkpass), [`isn`](/isn), [`seg`](/seg), [`cube`](/cube), [`ltree`](/ltree), [`hstore`](/hstore), [`citext`](/citext), [`xml2`](/xml2)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgpdf](https://github.com/Florents-Tselai/pgpdf) | 0.1.0 | **<span class="tcwarn">GPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgpdf](/pgpdf) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'pgpdf'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION pgpdf;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.1.0 | **<span class="tcwarn">GPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `pgpdf_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 0.1.0 | **<span class="tcwarn">GPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pgpdf` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pgpdf` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgpdf"]}'
```


Install `pgpdf` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pgpdf_17*;
dnf install pgpdf_16*;
dnf install pgpdf_15*;
dnf install pgpdf_14*;
dnf install pgpdf_13*;
dnf install pgpdf_12*;
```


Install `pgpdf` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pgpdf;
apt install postgresql-16-pgpdf;
apt install postgresql-15-pgpdf;
apt install postgresql-14-pgpdf;
apt install postgresql-13-pgpdf;
apt install postgresql-12-pgpdf;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgpdf_17*` | `pgpdf_16*` | `pgpdf_15*` | `pgpdf_14*` | `pgpdf_13*` | `pgpdf_12*` |
| `el9` | `pgpdf_17*` | `pgpdf_16*` | `pgpdf_15*` | `pgpdf_14*` | `pgpdf_13*` | `pgpdf_12*` |
| `d12` | `postgresql-17-pgpdf` | `postgresql-16-pgpdf` | `postgresql-15-pgpdf` | `postgresql-14-pgpdf` | `postgresql-13-pgpdf` | `postgresql-12-pgpdf` |
| `u22` | `postgresql-17-pgpdf` | `postgresql-16-pgpdf` | `postgresql-15-pgpdf` | `postgresql-14-pgpdf` | `postgresql-13-pgpdf` | `postgresql-12-pgpdf` |
| `u24` | `postgresql-17-pgpdf` | `postgresql-16-pgpdf` | `postgresql-15-pgpdf` | `postgresql-14-pgpdf` | `postgresql-13-pgpdf` | `postgresql-12-pgpdf` |





--------

## Usage

The actual PDF parsing is done by [poppler](https://poppler.freedesktop.org).

This allows you to work with PDFs in an ACID-compliant way.
The usual alternative relies on external scripts or services which can easily
make your data ingestion pipeline brittle and leave your raw data out-of-sync.

- [Full Text Search on PDFs With Postgres](https://tselai.com/full-text-search-pdf-postgres)
- [pgpdf: pdf type for Postgres](https://tselai.com/pgpdf-pdf-type-postgres)

Download some PDFs.

```sh
wget https://wiki.postgresql.org/images/e/ea/PostgreSQL_Introduction.pdf -O /tmp/pgintro.pdf
wget https://pdfobject.com/pdf/sample.pdf -O /tmp/sample.pdf
```

You can create a `pdf` type, by casting either a `text` filepath or `bytea` column.

```sql
CREATE EXTENSION pgpdf;
SELECT '/tmp/pgintro.pdf'::pdf;
```

```tsql
                                       pdf                                        
----------------------------------------------------------------------------------
 PostgreSQL Introduction                                                         +
 Digoal.Zhou                                                                     +
 7/20/2011Catalog                                                                +
  PostgreSQL Origin 
```

If you don’t have the PDF file in your filesystem, but have already stored its content in a `bytea` column, you can just cast it to `pdf`.

```tsql
SELECT pg_read_binary_file('/tmp/pgintro.pdf')::bytea::pdf;
```

--------

## Examples

Create a table with a `pdf` column:

```tsql
CREATE TABLE pdfs(name text primary key, doc pdf);

INSERT INTO pdfs VALUES ('pgintro', '/tmp/pgintro.pdf');
INSERT INTO pdfs VALUES ('pgintro', '/tmp/sample.pdf');
```

Parsing and validation should happen automatically.
The files will be read from the disk only once!

> [!NOTE]
> The filepath should be accessible by the `postgres` process / user!
> That's different than the user running psql.
> If you don't understand what this means, as your DBA!

### String Functions and Operators

Standard Postgres [String Functions and Operators](https://www.postgresql.org/docs/17/functions-string.html)
should work as usual:

```tsql
SELECT 'Below is the PDF we received ' || '/tmp/pgintro.pdf'::pdf;
```

```tsql
SELECT upper('/tmp/pgintro.pdf'::pdf::text);
```

``` tsql
SELECT name
FROM pdfs
WHERE doc::text LIKE '%Postgres%';
```

### Full-Text Search (FTS)

You can also perform full-text search (FTS), since you can work on a `pdf` file like normal text.

```tsql
SELECT '/tmp/pgintro.pdf'::pdf::text @@ to_tsquery('postgres');
```

```tsql
 ?column? 
----------
 t
(1 row)
```

```tsql
SELECT '/tmp/pgintro.pdf'::pdf::text @@ to_tsquery('oracle');
```

```tsql
 ?column? 
----------
 f
(1 row)
```

### Document similarity with `pg_trgm`

You can use [pg_trgm](https://postgresql.org/docs/17/interactive/pgtrgm.html)
to get the similarity between two documents:

```tsql
CREATE EXTENSION pg_trgm;

SELECT similarity('/tmp/pgintro.pdf'::pdf::text, '/tmp/sample.pdf'::pdf::text);
```

### Metadata

The following functions are available:

- `pdf_title(pdf) → text`
- `pdf_author(pdf) → text`
- `pdf_num_pages(pdf) → integer`

  Total number of pages in the document
- `pdf_page(pdf, integer) → text`

  Get the i-th page as text
- `pdf_creator(pdf) → text`
- `pdf_keywords(pdf) → text`
- `pdf_metadata(pdf) → text`
- `pdf_version(pdf) → text`
- `pdf_subject(pdf) → text`
- `pdf_creation(pdf) → timestamp`
- `pdf_modification(pdf) → timestamp`

```tsql
SELECT pdf_title('/tmp/pgintro.pdf');
```

```tsql
        pdf_title        
-------------------------
 PostgreSQL Introduction
(1 row)
```

```tsql
SELECT pdf_author('/tmp/pgintro.pdf');
```

```tsql
 pdf_author 
------------
 周正中
(1 row)
```

Getting a subset of pages

```tsql
SELECT pdf_num_pages('/tmp/pgintro.pdf');
```

```tsql
 pdf_num_pages 
---------------
            24
(1 row)
```

```tsql
SELECT pdf_page('/tmp/pgintro.pdf', 1);
```

```tsql
           pdf_page           
------------------------------
 Catalog                     +
  PostgreSQL Origin         +
  Layout                    +
  Features                  +
  Enterprise Class Attribute+
  Case
(1 row)
```

```tsql
SELECT pdf_subject('/tmp/pgintro.pdf');
```

```tsql
 pdf_subject 
-------------
 
(1 row)
```

```tsql
SELECT pdf_creation('/tmp/pgintro.pdf');
```

```tsql
       pdf_creation       
--------------------------
 Wed Jul 20 11:13:37 2011
(1 row)
```

```tsql
SELECT pdf_modification('/tmp/pgintro.pdf');
```

```tsql
     pdf_modification     
--------------------------
 Wed Jul 20 11:13:37 2011
(1 row)
```

```tsql
SELECT pdf_creator('/tmp/pgintro.pdf');
```

```tsql
            pdf_creator             
------------------------------------
 Microsoft® Office PowerPoint® 2007
(1 row)
```

```tsql
SELECT pdf_metadata('/tmp/pgintro.pdf');
```

```tsql
 pdf_metadata 
--------------
 
(1 row)
```

```tsql
SELECT pdf_version('/tmp/pgintro.pdf');
```

```tsql
 pdf_version 
-------------
 PDF-1.5
(1 row)
```

## Installation

Install [poppler](https://poppler.freedesktop.org) dependencies

**Linux**
```
sudo apt install -y libpoppler-glib-dev pkg-config
```

**Homebrew/MacOS**

```
brew install poppler pkgconf
```

```
cd /tmp
git clone https://github.com/Florents-Tselai/pgpdf.git
cd pgpdf
make
make install # may need sudo
```

After the installation, in a session:

```tsql
CREATE EXTENSION pgpdf;
```

### Docker

Get the [Docker image](https://hub.docker.com/r/florents/pgpdf) with:

```sh
docker pull florents/pgpdf:pg17
```

This adds pgpdf to the [Postgres image](https://hub.docker.com/_/postgres) (replace `17` with your Postgres server version, and run it the same way).

Run the image in a container.

```sh
docker run --name pgpdf -p 5432:5432 -e POSTGRES_PASSWORD=pass florents/pgpdf:pg17
```

Through another terminal, connect to the running server (container).

```sh
PGPASSWORD=pass psql -h localhost -p 5432 -U postgres
```

> [!WARNING]
> Reading arbitrary binary data (PDF) into your database can pose security risks.
> Only use this for files you trust.


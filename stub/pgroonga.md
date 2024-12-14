

--------

## Usage

- https://pgroonga.github.io/
- [News](https://pgroonga.github.io/news/): It lists release information.
- [Overview](https://pgroonga.github.io/overview/): It describes about PGroonga.
- [Install](https://pgroonga.github.io/install/): It describes how to install PGroonga.
- [Upgrade](https://pgroonga.github.io/upgrade/): It describes how to upgrade PGroonga.
- [Uninstall](https://pgroonga.github.io/uninstall/): It describes how to uninstall PGroonga.
- [Tutorial](https://pgroonga.github.io/tutorial/): It describes how to use PGroonga step by step.
- [FAQ](https://pgroonga.github.io/faq/): Frequently asked questions.
- [How to](https://pgroonga.github.io/how-to/): It describes about useful information for specific situations.
- [Reference](https://pgroonga.github.io/reference/): It describes details for each features such as options, functions and operators.
- [Troubleshooting](https://pgroonga.github.io/troubleshooting/): It describes how to fix troubles.
- [Community](https://pgroonga.github.io/community/): It introduces about PGroonga community.
- [Users](https://pgroonga.github.io/users/): It lists PGroonga users.
- [Development](https://pgroonga.github.io/development/): It describes how to develop PGroonga.

Here's a quick [tutorial](https://pgroonga.github.io/tutorial/) about how to use PGroonga:

```sql
CREATE EXTENSION IF NOT EXISTS pgroonga;

CREATE TABLE memos
(
    id      integer,
    content text
);

CREATE INDEX pgroonga_content_index ON memos USING pgroonga (content);

INSERT INTO memos VALUES (1, 'PostgreSQL is a relational database management system.');
INSERT INTO memos VALUES (2, 'Groonga is a fast full text search engine that supports all languages.');
INSERT INTO memos VALUES (3, 'PGroonga is a PostgreSQL extension that uses Groonga as index.');
INSERT INTO memos VALUES (4, 'There is groonga command.');

SET enable_seqscan = off;

-- now let's query pgroonga

SELECT * FROM memos WHERE content &@ 'engine';
--  id |                                content                                 
-- ----+------------------------------------------------------------------------
--   2 | Groonga is a fast full text search engine that supports all languages.
-- (1 row)

SELECT * FROM memos WHERE content &@~ 'PGroonga OR PostgreSQL';
--  id |                            content                             
-- ----+----------------------------------------------------------------
--   3 | PGroonga is a PostgreSQL extension that uses Groonga as index.
--   1 | PostgreSQL is a relational database management system.
-- (2 rows)

SELECT * FROM memos WHERE content LIKE '%engine%';
--  id |                                content                                 
-- ----+------------------------------------------------------------------------
--   2 | Groonga is a fast full text search engine that supports all languages.
-- (1 row)
```
# pg_rrule


> [pg_rrule](https://github.com/petropavel13/pg_rrule): RRULE field type for PostgreSQL
>
> https://github.com/petropavel13/pg_rrule





[TYPE](/type) extensions: [`prefix`](/prefix), [`semver`](/semver), [`unit`](/unit), [`pgpdf`](/pgpdf), [`pglite_fusion`](/pglite_fusion), [`md5hash`](/md5hash), [`asn1oid`](/asn1oid), [`roaringbitmap`](/roaringbitmap), [`pgfaceting`](/pgfaceting), [`pg_sphere`](/pg_sphere), [`country`](/country), [`pg_xenophile`](/pg_xenophile), [`l10n_table_dependent_extension`](/l10n_table_dependent_extension), [`currency`](/currency), [`collection`](/collection), [`pgmp`](/pgmp), [`numeral`](/numeral), [`pg_rational`](/pg_rational), [`uint`](/uint), [`uint128`](/uint128), [`hashtypes`](/hashtypes), [`ip4r`](/ip4r), [`pg_duration`](/pg_duration), [`uri`](/uri), [`emailaddr`](/emailaddr), [`acl`](/acl), [`debversion`](/debversion), [`pg_rrule`](/pg_rrule), [`timestamp9`](/timestamp9), [`chkpass`](/chkpass), [`isn`](/isn), [`seg`](/seg), [`cube`](/cube), [`ltree`](/ltree), [`hstore`](/hstore), [`citext`](/citext), [`xml2`](/xml2)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_rrule](https://github.com/petropavel13/pg_rrule) | 0.2.0 | **<span class="tcblue">MIT</span>** |  | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_rrule](/pg_rrule) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `el9` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_rrule;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [DEB](/deb) | 0.2.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pg-rrule` |  |  |  |  |  |  |



Install `pg_rrule` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_rrule
```


Install `pg_rrule` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_rrule"]}'
```


Install `pg_rrule` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-$v-pg-rrule;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `el9` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `d12` | `postgresql-17-pg-rrule` | `postgresql-16-pg-rrule` | `postgresql-15-pg-rrule` | `postgresql-14-pg-rrule` | `postgresql-13-pg-rrule` |
| `u22` | `postgresql-17-pg-rrule` | `postgresql-16-pg-rrule` | `postgresql-15-pg-rrule` | `postgresql-14-pg-rrule` | `postgresql-13-pg-rrule` |
| `u24` | `postgresql-17-pg-rrule` | `postgresql-16-pg-rrule` | `postgresql-15-pg-rrule` | `postgresql-14-pg-rrule` | `postgresql-13-pg-rrule` |






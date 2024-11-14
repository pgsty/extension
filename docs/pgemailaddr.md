# pgemailaddr


> [pgemailaddr](https://github.com/petere/pgemailaddr): Email address type for PostgreSQL
>
> https://github.com/petere/pgemailaddr





[TYPE](/type) extensions: [`prefix`](/prefix), [`semver`](/semver), [`unit`](/unit), [`md5hash`](/md5hash), [`asn1oid`](/asn1oid), [`roaringbitmap`](/roaringbitmap), [`pgfaceting`](/pgfaceting), [`pg_sphere`](/pg_sphere), [`country`](/country), [`currency`](/currency), [`pgmp`](/pgmp), [`numeral`](/numeral), [`pg_rational`](/pg_rational), [`uint`](/uint), [`uint128`](/uint128), [`ip4r`](/ip4r), [`uri`](/uri), [`pgemailaddr`](/pgemailaddr), [`acl`](/acl), [`debversion`](/debversion), [`pg_rrule`](/pg_rrule), [`timestamp9`](/timestamp9), [`chkpass`](/chkpass), [`isn`](/isn), [`seg`](/seg), [`cube`](/cube), [`ltree`](/ltree), [`hstore`](/hstore), [`citext`](/citext), [`xml2`](/xml2)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgemailaddr](https://github.com/petere/pgemailaddr) | 0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |  |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgemailaddr](/pgemailaddr) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pgemailaddr;
```
> **Comment**: +varatt.h
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_emailaddr_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-emailaddr` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pgemailaddr` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgemailaddr"]}'
```


Install `pgemailaddr` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install pg_emailaddr_17*;
yum install pg_emailaddr_16*;
yum install pg_emailaddr_15*;
yum install pg_emailaddr_14*;
yum install pg_emailaddr_13*;
yum install pg_emailaddr_12*;
```


Install `pgemailaddr` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-emailaddr;
apt install postgresql-16-pg-emailaddr;
apt install postgresql-15-pg-emailaddr;
apt install postgresql-14-pg-emailaddr;
apt install postgresql-13-pg-emailaddr;
apt install postgresql-12-pg-emailaddr;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_emailaddr_17*` | `pg_emailaddr_16*` | `pg_emailaddr_15*` | `pg_emailaddr_14*` | `pg_emailaddr_13*` | `pg_emailaddr_12*` |
| `el9` | `pg_emailaddr_17*` | `pg_emailaddr_16*` | `pg_emailaddr_15*` | `pg_emailaddr_14*` | `pg_emailaddr_13*` | `pg_emailaddr_12*` |
| `d12` | `postgresql-17-pg-emailaddr` | `postgresql-16-pg-emailaddr` | `postgresql-15-pg-emailaddr` | `postgresql-14-pg-emailaddr` | `postgresql-13-pg-emailaddr` | `postgresql-12-pg-emailaddr` |
| `u22` | `postgresql-17-pg-emailaddr` | `postgresql-16-pg-emailaddr` | `postgresql-15-pg-emailaddr` | `postgresql-14-pg-emailaddr` | `postgresql-13-pg-emailaddr` | `postgresql-12-pg-emailaddr` |
| `u24` | `postgresql-17-pg-emailaddr` | `postgresql-16-pg-emailaddr` | `postgresql-15-pg-emailaddr` | `postgresql-14-pg-emailaddr` | `postgresql-13-pg-emailaddr` | `postgresql-12-pg-emailaddr` |






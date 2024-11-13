# prefix


> [prefix](https://github.com/dimitri/prefix): Prefix Range module for PostgreSQL
>
> https://github.com/dimitri/prefix





[TYPE](/type) extensions: [`prefix`](/prefix), [`semver`](/semver), [`unit`](/unit), [`md5hash`](/md5hash), [`asn1oid`](/asn1oid), [`roaringbitmap`](/roaringbitmap), [`pgfaceting`](/pgfaceting), [`pg_sphere`](/pg_sphere), [`country`](/country), [`currency`](/currency), [`pgmp`](/pgmp), [`numeral`](/numeral), [`pg_rational`](/pg_rational), [`uint`](/uint), [`uint128`](/uint128), [`ip4r`](/ip4r), [`uri`](/uri), [`pgemailaddr`](/pgemailaddr), [`acl`](/acl), [`debversion`](/debversion), [`pg_rrule`](/pg_rrule), [`timestamp9`](/timestamp9), [`chkpass`](/chkpass), [`isn`](/isn), [`seg`](/seg), [`cube`](/cube), [`ltree`](/ltree), [`hstore`](/hstore), [`citext`](/citext), [`xml2`](/xml2)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [prefix](https://github.com/dimitri/prefix) | 1.2.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [prefix](/prefix) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION prefix;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `prefix_17*` | `prefix_16*` | `prefix_15*` | `prefix_14*` | `prefix_13*` | `prefix_12*` |
| `el9` | `prefix_17*` | `prefix_16*` | `prefix_15*` | `prefix_14*` | `prefix_13*` | `prefix_12*` |
| `d12` | `postgresql-17-prefix` | `postgresql-16-prefix` | `postgresql-15-prefix` | `postgresql-14-prefix` | `postgresql-13-prefix` | `postgresql-12-prefix` |
| `u22` | `postgresql-17-prefix` | `postgresql-16-prefix` | `postgresql-15-prefix` | `postgresql-14-prefix` | `postgresql-13-prefix` | `postgresql-12-prefix` |
| `u24` | `postgresql-17-prefix` | `postgresql-16-prefix` | `postgresql-15-prefix` | `postgresql-14-prefix` | `postgresql-13-prefix` | `postgresql-12-prefix` |



Install `prefix` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["prefix"]}'
```


Install `prefix` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install prefix_17*;
yum install prefix_16*;
yum install prefix_15*;
yum install prefix_14*;
yum install prefix_13*;
yum install prefix_12*;
```


Install `prefix` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-prefix;
apt install postgresql-16-prefix;
apt install postgresql-15-prefix;
apt install postgresql-14-prefix;
apt install postgresql-13-prefix;
apt install postgresql-12-prefix;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `prefix_17*` | `prefix_16*` | `prefix_15*` | `prefix_14*` | `prefix_13*` | `prefix_12*` |
| `el9` | `prefix_17*` | `prefix_16*` | `prefix_15*` | `prefix_14*` | `prefix_13*` | `prefix_12*` |
| `d12` | `postgresql-17-prefix` | `postgresql-16-prefix` | `postgresql-15-prefix` | `postgresql-14-prefix` | `postgresql-13-prefix` | `postgresql-12-prefix` |
| `u22` | `postgresql-17-prefix` | `postgresql-16-prefix` | `postgresql-15-prefix` | `postgresql-14-prefix` | `postgresql-13-prefix` | `postgresql-12-prefix` |
| `u24` | `postgresql-17-prefix` | `postgresql-16-prefix` | `postgresql-15-prefix` | `postgresql-14-prefix` | `postgresql-13-prefix` | `postgresql-12-prefix` |






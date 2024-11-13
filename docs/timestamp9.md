# timestamp9


> [timestamp9](https://github.com/optiver/timestamp9): timestamp nanosecond resolution
>
> https://github.com/optiver/timestamp9





[TYPE](/type) extensions: [`prefix`](/prefix), [`semver`](/semver), [`unit`](/unit), [`md5hash`](/md5hash), [`asn1oid`](/asn1oid), [`roaringbitmap`](/roaringbitmap), [`pgfaceting`](/pgfaceting), [`pg_sphere`](/pg_sphere), [`country`](/country), [`currency`](/currency), [`pgmp`](/pgmp), [`numeral`](/numeral), [`pg_rational`](/pg_rational), [`uint`](/uint), [`uint128`](/uint128), [`ip4r`](/ip4r), [`uri`](/uri), [`pgemailaddr`](/pgemailaddr), [`acl`](/acl), [`debversion`](/debversion), [`pg_rrule`](/pg_rrule), [`timestamp9`](/timestamp9), [`chkpass`](/chkpass), [`isn`](/isn), [`seg`](/seg), [`cube`](/cube), [`ltree`](/ltree), [`hstore`](/hstore), [`citext`](/citext), [`xml2`](/xml2)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [timestamp9](https://github.com/optiver/timestamp9) | 1.4.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [timestamp9](/timestamp9) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION timestamp9;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `timestamp9_17*` | `timestamp9_16*` | `timestamp9_15*` | `timestamp9_14*` | `timestamp9_13*` | `timestamp9_12*` |
| `el9` | `timestamp9_17*` | `timestamp9_16*` | `timestamp9_15*` | `timestamp9_14*` | `timestamp9_13*` | `timestamp9_12*` |
| `d12` | `postgresql-17-timestamp9` | `postgresql-16-timestamp9` | `postgresql-15-timestamp9` | `postgresql-14-timestamp9` | `postgresql-13-timestamp9` | `postgresql-12-timestamp9` |
| `u22` | `postgresql-17-timestamp9` | `postgresql-16-timestamp9` | `postgresql-15-timestamp9` | `postgresql-14-timestamp9` | `postgresql-13-timestamp9` | `postgresql-12-timestamp9` |
| `u24` | `postgresql-17-timestamp9` | `postgresql-16-timestamp9` | `postgresql-15-timestamp9` | `postgresql-14-timestamp9` | `postgresql-13-timestamp9` | `postgresql-12-timestamp9` |



Install `timestamp9` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["timestamp9"]}'
```


Install `timestamp9` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install timestamp9_17*;
yum install timestamp9_16*;
yum install timestamp9_15*;
yum install timestamp9_14*;
yum install timestamp9_13*;
yum install timestamp9_12*;
```


Install `timestamp9` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-timestamp9;
apt install postgresql-16-timestamp9;
apt install postgresql-15-timestamp9;
apt install postgresql-14-timestamp9;
apt install postgresql-13-timestamp9;
apt install postgresql-12-timestamp9;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `timestamp9_17*` | `timestamp9_16*` | `timestamp9_15*` | `timestamp9_14*` | `timestamp9_13*` | `timestamp9_12*` |
| `el9` | `timestamp9_17*` | `timestamp9_16*` | `timestamp9_15*` | `timestamp9_14*` | `timestamp9_13*` | `timestamp9_12*` |
| `d12` | `postgresql-17-timestamp9` | `postgresql-16-timestamp9` | `postgresql-15-timestamp9` | `postgresql-14-timestamp9` | `postgresql-13-timestamp9` | `postgresql-12-timestamp9` |
| `u22` | `postgresql-17-timestamp9` | `postgresql-16-timestamp9` | `postgresql-15-timestamp9` | `postgresql-14-timestamp9` | `postgresql-13-timestamp9` | `postgresql-12-timestamp9` |
| `u24` | `postgresql-17-timestamp9` | `postgresql-16-timestamp9` | `postgresql-15-timestamp9` | `postgresql-14-timestamp9` | `postgresql-13-timestamp9` | `postgresql-12-timestamp9` |






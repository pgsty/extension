# asn1oid


> [asn1oid](https://github.com/df7cb/pgsql-asn1oid): asn1oid extension
>
> https://github.com/df7cb/pgsql-asn1oid





[TYPE](/type) extensions: [`prefix`](/prefix), [`semver`](/semver), [`unit`](/unit), [`pgpdf`](/pgpdf), [`pglite_fusion`](/pglite_fusion), [`md5hash`](/md5hash), [`asn1oid`](/asn1oid), [`roaringbitmap`](/roaringbitmap), [`pgfaceting`](/pgfaceting), [`pg_sphere`](/pg_sphere), [`country`](/country), [`currency`](/currency), [`pgmp`](/pgmp), [`numeral`](/numeral), [`pg_rational`](/pg_rational), [`uint`](/uint), [`uint128`](/uint128), [`ip4r`](/ip4r), [`uri`](/uri), [`emailaddr`](/emailaddr), [`acl`](/acl), [`debversion`](/debversion), [`pg_rrule`](/pg_rrule), [`timestamp9`](/timestamp9), [`chkpass`](/chkpass), [`isn`](/isn), [`seg`](/seg), [`cube`](/cube), [`ltree`](/ltree), [`hstore`](/hstore), [`citext`](/citext), [`xml2`](/xml2)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [asn1oid](https://github.com/df7cb/pgsql-asn1oid) | 1 | **<span class="tcwarn">GPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [asn1oid](/asn1oid) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION asn1oid;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1 | **<span class="tcwarn">GPLv3</span>** | **<span class="tcwarn">PIGSTY</span>** | `asn1oid_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1 | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-asn1oid` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `asn1oid` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add asn1oid
```


Install `asn1oid` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["asn1oid"]}'
```


Install `asn1oid` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install asn1oid_17*;
dnf install asn1oid_16*;
dnf install asn1oid_15*;
dnf install asn1oid_14*;
dnf install asn1oid_13*;
```


Install `asn1oid` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-asn1oid;
apt install postgresql-16-asn1oid;
apt install postgresql-15-asn1oid;
apt install postgresql-14-asn1oid;
apt install postgresql-13-asn1oid;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `asn1oid_17*` | `asn1oid_16*` | `asn1oid_15*` | `asn1oid_14*` | `asn1oid_13*` |
| `el9` | `asn1oid_17*` | `asn1oid_16*` | `asn1oid_15*` | `asn1oid_14*` | `asn1oid_13*` |
| `d12` | `postgresql-17-asn1oid` | `postgresql-16-asn1oid` | `postgresql-15-asn1oid` | `postgresql-14-asn1oid` | `postgresql-13-asn1oid` |
| `u22` | `postgresql-17-asn1oid` | `postgresql-16-asn1oid` | `postgresql-15-asn1oid` | `postgresql-14-asn1oid` | `postgresql-13-asn1oid` |
| `u24` | `postgresql-17-asn1oid` | `postgresql-16-asn1oid` | `postgresql-15-asn1oid` | `postgresql-14-asn1oid` | `postgresql-13-asn1oid` |






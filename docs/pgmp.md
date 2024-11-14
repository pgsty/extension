# pgmp


> [pgmp](https://github.com/dvarrazzo/pgmp/): Multiple Precision Arithmetic extension
>
> https://github.com/dvarrazzo/pgmp/





[TYPE](/type) extensions: [`prefix`](/prefix), [`semver`](/semver), [`unit`](/unit), [`md5hash`](/md5hash), [`asn1oid`](/asn1oid), [`roaringbitmap`](/roaringbitmap), [`pgfaceting`](/pgfaceting), [`pg_sphere`](/pg_sphere), [`country`](/country), [`currency`](/currency), [`pgmp`](/pgmp), [`numeral`](/numeral), [`pg_rational`](/pg_rational), [`uint`](/uint), [`uint128`](/uint128), [`ip4r`](/ip4r), [`uri`](/uri), [`pgemailaddr`](/pgemailaddr), [`acl`](/acl), [`debversion`](/debversion), [`pg_rrule`](/pg_rrule), [`timestamp9`](/timestamp9), [`chkpass`](/chkpass), [`isn`](/isn), [`seg`](/seg), [`cube`](/cube), [`ltree`](/ltree), [`hstore`](/hstore), [`citext`](/citext), [`xml2`](/xml2)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgmp](https://github.com/dvarrazzo/pgmp/) | 1.1 | **<span class="tcwarn">LGPLv3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgmp](/pgmp) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pgmp;
```
> **Comment**: missing pg14,13,12 on el pgdg repo
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.1 | **<span class="tcwarn">LGPLv3</span>** | **<span class="tccyan">PGDG</span>** | `pgmp_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |  |  |  |
| [DEB](/deb) | 1.1 | **<span class="tcwarn">LGPLv3</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pgmp` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |  |  |  |



Install `pgmp` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgmp"]}'
```


Install `pgmp` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install pgmp_17*;
yum install pgmp_16*;
yum install pgmp_15*;
yum install pgmp_14*;
yum install pgmp_13*;
yum install pgmp_12*;
```


Install `pgmp` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pgmp;
apt install postgresql-16-pgmp;
apt install postgresql-15-pgmp;
apt install postgresql-14-pgmp;
apt install postgresql-13-pgmp;
apt install postgresql-12-pgmp;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgmp_17*` | `pgmp_16*` | `pgmp_15*` | `pgmp_14*` | `pgmp_13*` | `pgmp_12*` |
| `el9` | `pgmp_17*` | `pgmp_16*` | `pgmp_15*` | `pgmp_14*` | `pgmp_13*` | `pgmp_12*` |
| `d12` | `postgresql-17-pgmp` | `postgresql-16-pgmp` | `postgresql-15-pgmp` | `postgresql-14-pgmp` | `postgresql-13-pgmp` | `postgresql-12-pgmp` |
| `u22` | `postgresql-17-pgmp` | `postgresql-16-pgmp` | `postgresql-15-pgmp` | `postgresql-14-pgmp` | `postgresql-13-pgmp` | `postgresql-12-pgmp` |
| `u24` | `postgresql-17-pgmp` | `postgresql-16-pgmp` | `postgresql-15-pgmp` | `postgresql-14-pgmp` | `postgresql-13-pgmp` | `postgresql-12-pgmp` |






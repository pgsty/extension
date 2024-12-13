# ip4r


> [ip4r](https://github.com/RhodiumToad/ip4r): IPv4/v6 and IPv4/v6 range index type for PostgreSQL
>
> https://github.com/RhodiumToad/ip4r





[TYPE](/type) extensions: [`prefix`](/prefix), [`semver`](/semver), [`unit`](/unit), [`pgpdf`](/pgpdf), [`pglite_fusion`](/pglite_fusion), [`md5hash`](/md5hash), [`asn1oid`](/asn1oid), [`roaringbitmap`](/roaringbitmap), [`pgfaceting`](/pgfaceting), [`pg_sphere`](/pg_sphere), [`country`](/country), [`currency`](/currency), [`pgmp`](/pgmp), [`numeral`](/numeral), [`pg_rational`](/pg_rational), [`uint`](/uint), [`uint128`](/uint128), [`ip4r`](/ip4r), [`uri`](/uri), [`pgemailaddr`](/pgemailaddr), [`acl`](/acl), [`debversion`](/debversion), [`pg_rrule`](/pg_rrule), [`timestamp9`](/timestamp9), [`chkpass`](/chkpass), [`isn`](/isn), [`seg`](/seg), [`cube`](/cube), [`ltree`](/ltree), [`hstore`](/hstore), [`citext`](/citext), [`xml2`](/xml2)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [ip4r](https://github.com/RhodiumToad/ip4r) | 2.4 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [ip4r](/ip4r) |  |  |  | [`geoip`](/geoip) |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION ip4r;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 2.4 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `ip4r_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 2.4 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-ip4r` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `ip4r` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["ip4r"]}'
```


Install `ip4r` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install ip4r_17*;
yum install ip4r_16*;
yum install ip4r_15*;
yum install ip4r_14*;
yum install ip4r_13*;
yum install ip4r_12*;
```


Install `ip4r` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-ip4r;
apt install postgresql-16-ip4r;
apt install postgresql-15-ip4r;
apt install postgresql-14-ip4r;
apt install postgresql-13-ip4r;
apt install postgresql-12-ip4r;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `ip4r_17*` | `ip4r_16*` | `ip4r_15*` | `ip4r_14*` | `ip4r_13*` | `ip4r_12*` |
| `el9` | `ip4r_17*` | `ip4r_16*` | `ip4r_15*` | `ip4r_14*` | `ip4r_13*` | `ip4r_12*` |
| `d12` | `postgresql-17-ip4r` | `postgresql-16-ip4r` | `postgresql-15-ip4r` | `postgresql-14-ip4r` | `postgresql-13-ip4r` | `postgresql-12-ip4r` |
| `u22` | `postgresql-17-ip4r` | `postgresql-16-ip4r` | `postgresql-15-ip4r` | `postgresql-14-ip4r` | `postgresql-13-ip4r` | `postgresql-12-ip4r` |
| `u24` | `postgresql-17-ip4r` | `postgresql-16-ip4r` | `postgresql-15-ip4r` | `postgresql-14-ip4r` | `postgresql-13-ip4r` | `postgresql-12-ip4r` |






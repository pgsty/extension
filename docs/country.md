# pg_country


> [pg_country](https://github.com/adjust/pg-country): Country data type, ISO 3166-1
>
> https://github.com/adjust/pg-country





[TYPE](/type) extensions: [`prefix`](/prefix), [`semver`](/semver), [`unit`](/unit), [`md5hash`](/md5hash), [`asn1oid`](/asn1oid), [`roaringbitmap`](/roaringbitmap), [`pgfaceting`](/pgfaceting), [`pg_sphere`](/pg_sphere), [`country`](/country), [`currency`](/currency), [`pgmp`](/pgmp), [`numeral`](/numeral), [`pg_rational`](/pg_rational), [`uint`](/uint), [`uint128`](/uint128), [`ip4r`](/ip4r), [`uri`](/uri), [`pgemailaddr`](/pgemailaddr), [`acl`](/acl), [`debversion`](/debversion), [`pg_rrule`](/pg_rrule), [`timestamp9`](/timestamp9), [`chkpass`](/chkpass), [`isn`](/isn), [`seg`](/seg), [`cube`](/cube), [`ltree`](/ltree), [`hstore`](/hstore), [`citext`](/citext), [`xml2`](/xml2)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [country](https://github.com/adjust/pg-country) | 0.0.3 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_country](/country) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION country;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_country_17*` | `pg_country_16*` | `pg_country_15*` | `pg_country_14*` | `pg_country_13*` | `pg_country_12*` |
| `el9` | `pg_country_17*` | `pg_country_16*` | `pg_country_15*` | `pg_country_14*` | `pg_country_13*` | `pg_country_12*` |
| `d12` | `postgresql-17-pg-country` | `postgresql-16-pg-country` | `postgresql-15-pg-country` | `postgresql-14-pg-country` | `postgresql-13-pg-country` | `postgresql-12-pg-country` |
| `u22` | `postgresql-17-pg-country` | `postgresql-16-pg-country` | `postgresql-15-pg-country` | `postgresql-14-pg-country` | `postgresql-13-pg-country` | `postgresql-12-pg-country` |
| `u24` | `postgresql-17-pg-country` | `postgresql-16-pg-country` | `postgresql-15-pg-country` | `postgresql-14-pg-country` | `postgresql-13-pg-country` | `postgresql-12-pg-country` |



Install `pg_country` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_country"]}'
```


Install `pg_country` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install pg_country_17*;
yum install pg_country_16*;
yum install pg_country_15*;
yum install pg_country_14*;
yum install pg_country_13*;
yum install pg_country_12*;
```


Install `pg_country` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-country;
apt install postgresql-16-pg-country;
apt install postgresql-15-pg-country;
apt install postgresql-14-pg-country;
apt install postgresql-13-pg-country;
apt install postgresql-12-pg-country;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_country_17*` | `pg_country_16*` | `pg_country_15*` | `pg_country_14*` | `pg_country_13*` | `pg_country_12*` |
| `el9` | `pg_country_17*` | `pg_country_16*` | `pg_country_15*` | `pg_country_14*` | `pg_country_13*` | `pg_country_12*` |
| `d12` | `postgresql-17-pg-country` | `postgresql-16-pg-country` | `postgresql-15-pg-country` | `postgresql-14-pg-country` | `postgresql-13-pg-country` | `postgresql-12-pg-country` |
| `u22` | `postgresql-17-pg-country` | `postgresql-16-pg-country` | `postgresql-15-pg-country` | `postgresql-14-pg-country` | `postgresql-13-pg-country` | `postgresql-12-pg-country` |
| `u24` | `postgresql-17-pg-country` | `postgresql-16-pg-country` | `postgresql-15-pg-country` | `postgresql-14-pg-country` | `postgresql-13-pg-country` | `postgresql-12-pg-country` |






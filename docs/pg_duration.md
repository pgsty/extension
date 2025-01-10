# pg_duration


> [pg_duration](https://github.com/jkosh44/pg_duration): data type for representing durations
>
> https://github.com/jkosh44/pg_duration





[TYPE](/type) extensions: [`prefix`](/prefix), [`semver`](/semver), [`unit`](/unit), [`pgpdf`](/pgpdf), [`pglite_fusion`](/pglite_fusion), [`md5hash`](/md5hash), [`asn1oid`](/asn1oid), [`roaringbitmap`](/roaringbitmap), [`pgfaceting`](/pgfaceting), [`pg_sphere`](/pg_sphere), [`country`](/country), [`currency`](/currency), [`pgmp`](/pgmp), [`numeral`](/numeral), [`pg_rational`](/pg_rational), [`uint`](/uint), [`uint128`](/uint128), [`ip4r`](/ip4r), [`pg_duration`](/pg_duration), [`uri`](/uri), [`emailaddr`](/emailaddr), [`acl`](/acl), [`debversion`](/debversion), [`pg_rrule`](/pg_rrule), [`timestamp9`](/timestamp9), [`chkpass`](/chkpass), [`isn`](/isn), [`seg`](/seg), [`cube`](/cube), [`ltree`](/ltree), [`hstore`](/hstore), [`citext`](/citext), [`xml2`](/xml2)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_duration](https://github.com/jkosh44/pg_duration) | 1.0.1 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_duration](/pg_duration) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |





```sql
CREATE EXTENSION pg_duration;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0.1 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_duration_$v*` | **<span class="tcwarn">✔</span>** |  |  |  |  |  |
| [DEB](/deb) | 1.0.1 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-duration` | **<span class="tcwarn">✔</span>** |  |  |  |  |  |



Install `pg_duration` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_duration
```


Install `pg_duration` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_duration"]}'
```


Install `pg_duration` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_duration_17*;
```


Install `pg_duration` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-duration;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_duration_17*` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `el9` | `pg_duration_17*` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `d12` | `postgresql-17-pg-duration` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `u22` | `postgresql-17-pg-duration` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |
| `u24` | `postgresql-17-pg-duration` | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> | <span class="tcred">✘</span> |






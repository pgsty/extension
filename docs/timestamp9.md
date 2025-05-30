# timestamp9


> [timestamp9](https://github.com/optiver/timestamp9): timestamp nanosecond resolution
>
> https://github.com/optiver/timestamp9





[TYPE](/type) extensions: [`prefix`](/prefix), [`semver`](/semver), [`unit`](/unit), [`pgpdf`](/pgpdf), [`pglite_fusion`](/pglite_fusion), [`md5hash`](/md5hash), [`asn1oid`](/asn1oid), [`roaringbitmap`](/roaringbitmap), [`pgfaceting`](/pgfaceting), [`pg_sphere`](/pg_sphere), [`country`](/country), [`pg_xenophile`](/pg_xenophile), [`l10n_table_dependent_extension`](/l10n_table_dependent_extension), [`currency`](/currency), [`collection`](/collection), [`pgmp`](/pgmp), [`numeral`](/numeral), [`pg_rational`](/pg_rational), [`uint`](/uint), [`uint128`](/uint128), [`hashtypes`](/hashtypes), [`ip4r`](/ip4r), [`pg_duration`](/pg_duration), [`uri`](/uri), [`emailaddr`](/emailaddr), [`acl`](/acl), [`debversion`](/debversion), [`pg_rrule`](/pg_rrule), [`timestamp9`](/timestamp9), [`chkpass`](/chkpass), [`isn`](/isn), [`seg`](/seg), [`cube`](/cube), [`ltree`](/ltree), [`hstore`](/hstore), [`citext`](/citext), [`xml2`](/xml2)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [timestamp9](https://github.com/optiver/timestamp9) | 1.4.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [timestamp9](/timestamp9) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION timestamp9;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.4.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `timestamp9_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 1.4.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-timestamp9` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `timestamp9` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add timestamp9
```


Install `timestamp9` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["timestamp9"]}'
```


Install `timestamp9` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install timestamp9_17*;
dnf install timestamp9_16*;
dnf install timestamp9_15*;
dnf install timestamp9_14*;
dnf install timestamp9_13*;
```


Install `timestamp9` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-timestamp9;
apt install postgresql-16-timestamp9;
apt install postgresql-15-timestamp9;
apt install postgresql-14-timestamp9;
apt install postgresql-13-timestamp9;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `timestamp9_17*` | `timestamp9_16*` | `timestamp9_15*` | `timestamp9_14*` | `timestamp9_13*` |
| `el9` | `timestamp9_17*` | `timestamp9_16*` | `timestamp9_15*` | `timestamp9_14*` | `timestamp9_13*` |
| `d12` | `postgresql-17-timestamp9` | `postgresql-16-timestamp9` | `postgresql-15-timestamp9` | `postgresql-14-timestamp9` | `postgresql-13-timestamp9` |
| `u22` | `postgresql-17-timestamp9` | `postgresql-16-timestamp9` | `postgresql-15-timestamp9` | `postgresql-14-timestamp9` | `postgresql-13-timestamp9` |
| `u24` | `postgresql-17-timestamp9` | `postgresql-16-timestamp9` | `postgresql-15-timestamp9` | `postgresql-14-timestamp9` | `postgresql-13-timestamp9` |






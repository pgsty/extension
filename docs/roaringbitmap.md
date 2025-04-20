# roaringbitmap


> [roaringbitmap](https://github.com/ChenHuajun/pg_roaringbitmap): support for Roaring Bitmaps
>
> https://github.com/ChenHuajun/pg_roaringbitmap





[TYPE](/type) extensions: [`prefix`](/prefix), [`semver`](/semver), [`unit`](/unit), [`pgpdf`](/pgpdf), [`pglite_fusion`](/pglite_fusion), [`md5hash`](/md5hash), [`asn1oid`](/asn1oid), [`roaringbitmap`](/roaringbitmap), [`pgfaceting`](/pgfaceting), [`pg_sphere`](/pg_sphere), [`country`](/country), [`pg_xenophile`](/pg_xenophile), [`l10n_table_dependent_extension`](/l10n_table_dependent_extension), [`currency`](/currency), [`collection`](/collection), [`pgmp`](/pgmp), [`numeral`](/numeral), [`pg_rational`](/pg_rational), [`uint`](/uint), [`uint128`](/uint128), [`hashtypes`](/hashtypes), [`ip4r`](/ip4r), [`pg_duration`](/pg_duration), [`uri`](/uri), [`emailaddr`](/emailaddr), [`acl`](/acl), [`debversion`](/debversion), [`pg_rrule`](/pg_rrule), [`timestamp9`](/timestamp9), [`chkpass`](/chkpass), [`isn`](/isn), [`seg`](/seg), [`cube`](/cube), [`ltree`](/ltree), [`hstore`](/hstore), [`citext`](/citext), [`xml2`](/xml2)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [roaringbitmap](https://github.com/ChenHuajun/pg_roaringbitmap) | 0.5.4 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [roaringbitmap](/roaringbitmap) |  |  |  | [`pgfaceting`](/pgfaceting) |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION roaringbitmap;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.5 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_roaringbitmap_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 0.5 | **<span class="tccyan">Apache-2</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-roaringbitmap` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `roaringbitmap` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add roaringbitmap
```


Install `roaringbitmap` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["roaringbitmap"]}'
```


Install `roaringbitmap` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_roaringbitmap_17*;
dnf install pg_roaringbitmap_16*;
dnf install pg_roaringbitmap_15*;
dnf install pg_roaringbitmap_14*;
dnf install pg_roaringbitmap_13*;
```


Install `roaringbitmap` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-roaringbitmap;
apt install postgresql-16-roaringbitmap;
apt install postgresql-15-roaringbitmap;
apt install postgresql-14-roaringbitmap;
apt install postgresql-13-roaringbitmap;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_roaringbitmap_17*` | `pg_roaringbitmap_16*` | `pg_roaringbitmap_15*` | `pg_roaringbitmap_14*` | `pg_roaringbitmap_13*` |
| `el9` | `pg_roaringbitmap_17*` | `pg_roaringbitmap_16*` | `pg_roaringbitmap_15*` | `pg_roaringbitmap_14*` | `pg_roaringbitmap_13*` |
| `d12` | `postgresql-17-roaringbitmap` | `postgresql-16-roaringbitmap` | `postgresql-15-roaringbitmap` | `postgresql-14-roaringbitmap` | `postgresql-13-roaringbitmap` |
| `u22` | `postgresql-17-roaringbitmap` | `postgresql-16-roaringbitmap` | `postgresql-15-roaringbitmap` | `postgresql-14-roaringbitmap` | `postgresql-13-roaringbitmap` |
| `u24` | `postgresql-17-roaringbitmap` | `postgresql-16-roaringbitmap` | `postgresql-15-roaringbitmap` | `postgresql-14-roaringbitmap` | `postgresql-13-roaringbitmap` |






# pg_xenophile


> [pg_xenophile](https://github.com/bigsmoke/pg_xenophile): More than the bare necessities for PostgreSQL i18n and l10n.
>
> https://github.com/bigsmoke/pg_xenophile





[TYPE](/type) extensions: [`prefix`](/prefix), [`semver`](/semver), [`unit`](/unit), [`pgpdf`](/pgpdf), [`pglite_fusion`](/pglite_fusion), [`md5hash`](/md5hash), [`asn1oid`](/asn1oid), [`roaringbitmap`](/roaringbitmap), [`pgfaceting`](/pgfaceting), [`pg_sphere`](/pg_sphere), [`country`](/country), [`pg_xenophile`](/pg_xenophile), [`l10n_table_dependent_extension`](/l10n_table_dependent_extension), [`currency`](/currency), [`collection`](/collection), [`pgmp`](/pgmp), [`numeral`](/numeral), [`pg_rational`](/pg_rational), [`uint`](/uint), [`uint128`](/uint128), [`hashtypes`](/hashtypes), [`ip4r`](/ip4r), [`pg_duration`](/pg_duration), [`uri`](/uri), [`emailaddr`](/emailaddr), [`acl`](/acl), [`debversion`](/debversion), [`pg_rrule`](/pg_rrule), [`timestamp9`](/timestamp9), [`chkpass`](/chkpass), [`isn`](/isn), [`seg`](/seg), [`cube`](/cube), [`ltree`](/ltree), [`hstore`](/hstore), [`citext`](/citext), [`xml2`](/xml2)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_xenophile](https://github.com/bigsmoke/pg_xenophile) | 0.8.3 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_xenophile](/pg_xenophile) |  | `xeno` |  | [`l10n_table_dependent_extension`](/l10n_table_dependent_extension) |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_xenophile;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.8.3 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_xenophile_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 0.8.3 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-xenophile` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pg_xenophile` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_xenophile
```


Install `pg_xenophile` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_xenophile"]}'
```


Install `pg_xenophile` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_xenophile_17;
dnf install pg_xenophile_16;
dnf install pg_xenophile_15;
dnf install pg_xenophile_14;
dnf install pg_xenophile_13;
```


Install `pg_xenophile` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-xenophile;
apt install postgresql-16-pg-xenophile;
apt install postgresql-15-pg-xenophile;
apt install postgresql-14-pg-xenophile;
apt install postgresql-13-pg-xenophile;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_xenophile_17` | `pg_xenophile_16` | `pg_xenophile_15` | `pg_xenophile_14` | `pg_xenophile_13` |
| `el9` | `pg_xenophile_17` | `pg_xenophile_16` | `pg_xenophile_15` | `pg_xenophile_14` | `pg_xenophile_13` |
| `d12` | `postgresql-17-pg-xenophile` | `postgresql-16-pg-xenophile` | `postgresql-15-pg-xenophile` | `postgresql-14-pg-xenophile` | `postgresql-13-pg-xenophile` |
| `u22` | `postgresql-17-pg-xenophile` | `postgresql-16-pg-xenophile` | `postgresql-15-pg-xenophile` | `postgresql-14-pg-xenophile` | `postgresql-13-pg-xenophile` |
| `u24` | `postgresql-17-pg-xenophile` | `postgresql-16-pg-xenophile` | `postgresql-15-pg-xenophile` | `postgresql-14-pg-xenophile` | `postgresql-13-pg-xenophile` |






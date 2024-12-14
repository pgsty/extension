# pgextwlist


> [pgextwlist](https://github.com/dimitri/pgextwlist): PostgreSQL Extension Whitelisting
>
> https://github.com/dimitri/pgextwlist





[SEC](/sec) extensions: [`passwordcheck_cracklib`](/passwordcheck_cracklib), [`supautils`](/supautils), [`pgsodium`](/pgsodium), [`supabase_vault`](/supabase_vault), [`pg_session_jwt`](/pg_session_jwt), [`anon`](/anon), [`pg_tde`](/pg_tde), [`pgsmcrypto`](/pgsmcrypto), [`pgaudit`](/pgaudit), [`pgauditlogtofile`](/pgauditlogtofile), [`pg_auth_mon`](/pg_auth_mon), [`credcheck`](/credcheck), [`pgcryptokey`](/pgcryptokey), [`pg_jobmon`](/pg_jobmon), [`logerrors`](/logerrors), [`login_hook`](/login_hook), [`set_user`](/set_user), [`pg_snakeoil`](/pg_snakeoil), [`pgextwlist`](/pgextwlist), [`pg_auditor`](/pg_auditor), [`sslutils`](/sslutils), [`noset`](/noset), [`sepgsql`](/sepgsql), [`auth_delay`](/auth_delay), [`pgcrypto`](/pgcrypto), [`passwordcheck`](/passwordcheck)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgextwlist](https://github.com/dimitri/pgextwlist) | 1.17 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgextwlist](/pgextwlist) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'pgextwlist'; # add this extension to postgresql.conf
```



-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.17 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pgextwlist_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1.17 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pgextwlist` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pgextwlist` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgextwlist"]}'
```


Install `pgextwlist` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pgextwlist_17*;
dnf install pgextwlist_16*;
dnf install pgextwlist_15*;
dnf install pgextwlist_14*;
dnf install pgextwlist_13*;
dnf install pgextwlist_12*;
```


Install `pgextwlist` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pgextwlist;
apt install postgresql-16-pgextwlist;
apt install postgresql-15-pgextwlist;
apt install postgresql-14-pgextwlist;
apt install postgresql-13-pgextwlist;
apt install postgresql-12-pgextwlist;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgextwlist_17*` | `pgextwlist_16*` | `pgextwlist_15*` | `pgextwlist_14*` | `pgextwlist_13*` | `pgextwlist_12*` |
| `el9` | `pgextwlist_17*` | `pgextwlist_16*` | `pgextwlist_15*` | `pgextwlist_14*` | `pgextwlist_13*` | `pgextwlist_12*` |
| `d12` | `postgresql-17-pgextwlist` | `postgresql-16-pgextwlist` | `postgresql-15-pgextwlist` | `postgresql-14-pgextwlist` | `postgresql-13-pgextwlist` | `postgresql-12-pgextwlist` |
| `u22` | `postgresql-17-pgextwlist` | `postgresql-16-pgextwlist` | `postgresql-15-pgextwlist` | `postgresql-14-pgextwlist` | `postgresql-13-pgextwlist` | `postgresql-12-pgextwlist` |
| `u24` | `postgresql-17-pgextwlist` | `postgresql-16-pgextwlist` | `postgresql-15-pgextwlist` | `postgresql-14-pgextwlist` | `postgresql-13-pgextwlist` | `postgresql-12-pgextwlist` |






# passwordcheck


> [passwordcheck](https://github.com/devrimgunduz/passwordcheck_cracklib): Strengthen PostgreSQL user password checks with cracklib
>
> https://github.com/devrimgunduz/passwordcheck_cracklib





[SEC](/sec) extensions: [`passwordcheck_cracklib`](/passwordcheck_cracklib), [`supautils`](/supautils), [`pgsodium`](/pgsodium), [`supabase_vault`](/supabase_vault), [`pg_session_jwt`](/pg_session_jwt), [`anon`](/anon), [`pg_tde`](/pg_tde), [`pgsmcrypto`](/pgsmcrypto), [`pgaudit`](/pgaudit), [`pgauditlogtofile`](/pgauditlogtofile), [`pg_auth_mon`](/pg_auth_mon), [`credcheck`](/credcheck), [`pgcryptokey`](/pgcryptokey), [`pg_jobmon`](/pg_jobmon), [`logerrors`](/logerrors), [`login_hook`](/login_hook), [`set_user`](/set_user), [`pg_snakeoil`](/pg_snakeoil), [`pgextwlist`](/pgextwlist), [`pg_auditor`](/pg_auditor), [`sslutils`](/sslutils), [`noset`](/noset), [`sepgsql`](/sepgsql), [`auth_delay`](/auth_delay), [`pgcrypto`](/pgcrypto), [`passwordcheck`](/passwordcheck)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [passwordcheck_cracklib](https://github.com/devrimgunduz/passwordcheck_cracklib) | 3.0.0 | **<span class="tcwarn">LGPLv2</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [passwordcheck](/passwordcheck_cracklib) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'passwordcheck_cracklib'; # add this extension to postgresql.conf
```



-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 3.0.0 | **<span class="tcwarn">LGPLv2</span>** | **<span class="tccyan">PGDG</span>** | `passwordcheck_cracklib_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 3.0.0 | **<span class="tcwarn">LGPLv2</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-passwordcheck-cracklib` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `passwordcheck` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["passwordcheck"]}'
```


Install `passwordcheck` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install passwordcheck_cracklib_17*;
yum install passwordcheck_cracklib_16*;
yum install passwordcheck_cracklib_15*;
yum install passwordcheck_cracklib_14*;
yum install passwordcheck_cracklib_13*;
yum install passwordcheck_cracklib_12*;
```


Install `passwordcheck` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-passwordcheck-cracklib;
apt install postgresql-16-passwordcheck-cracklib;
apt install postgresql-15-passwordcheck-cracklib;
apt install postgresql-14-passwordcheck-cracklib;
apt install postgresql-13-passwordcheck-cracklib;
apt install postgresql-12-passwordcheck-cracklib;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `passwordcheck_cracklib_17*` | `passwordcheck_cracklib_16*` | `passwordcheck_cracklib_15*` | `passwordcheck_cracklib_14*` | `passwordcheck_cracklib_13*` | `passwordcheck_cracklib_12*` |
| `el9` | `passwordcheck_cracklib_17*` | `passwordcheck_cracklib_16*` | `passwordcheck_cracklib_15*` | `passwordcheck_cracklib_14*` | `passwordcheck_cracklib_13*` | `passwordcheck_cracklib_12*` |
| `d12` | `postgresql-17-passwordcheck-cracklib` | `postgresql-16-passwordcheck-cracklib` | `postgresql-15-passwordcheck-cracklib` | `postgresql-14-passwordcheck-cracklib` | `postgresql-13-passwordcheck-cracklib` | `postgresql-12-passwordcheck-cracklib` |
| `u22` | `postgresql-17-passwordcheck-cracklib` | `postgresql-16-passwordcheck-cracklib` | `postgresql-15-passwordcheck-cracklib` | `postgresql-14-passwordcheck-cracklib` | `postgresql-13-passwordcheck-cracklib` | `postgresql-12-passwordcheck-cracklib` |
| `u24` | `postgresql-17-passwordcheck-cracklib` | `postgresql-16-passwordcheck-cracklib` | `postgresql-15-passwordcheck-cracklib` | `postgresql-14-passwordcheck-cracklib` | `postgresql-13-passwordcheck-cracklib` | `postgresql-12-passwordcheck-cracklib` |






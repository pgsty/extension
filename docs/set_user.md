# set_user


> [set_user](https://github.com/pgaudit/set_user): similar to SET ROLE but with added logging
>
> https://github.com/pgaudit/set_user





[SEC](/sec) extensions: [`passwordcheck_cracklib`](/passwordcheck_cracklib), [`supautils`](/supautils), [`pgsodium`](/pgsodium), [`supabase_vault`](/supabase_vault), [`pg_session_jwt`](/pg_session_jwt), [`anon`](/anon), [`pg_tde`](/pg_tde), [`pgsmcrypto`](/pgsmcrypto), [`pgaudit`](/pgaudit), [`pgauditlogtofile`](/pgauditlogtofile), [`pg_auth_mon`](/pg_auth_mon), [`credcheck`](/credcheck), [`pgcryptokey`](/pgcryptokey), [`pg_jobmon`](/pg_jobmon), [`logerrors`](/logerrors), [`login_hook`](/login_hook), [`set_user`](/set_user), [`pg_snakeoil`](/pg_snakeoil), [`pgextwlist`](/pgextwlist), [`pg_auditor`](/pg_auditor), [`sslutils`](/sslutils), [`noset`](/noset), [`sepgsql`](/sepgsql), [`auth_delay`](/auth_delay), [`pgcrypto`](/pgcrypto), [`passwordcheck`](/passwordcheck)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [set_user](https://github.com/pgaudit/set_user) | 4.1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [set_user](/set_user) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION set_user;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 4.1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `set_user_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 4.1.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-set-user` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `set_user` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["set_user"]}'
```


Install `set_user` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install set_user_17*;
dnf install set_user_16*;
dnf install set_user_15*;
dnf install set_user_14*;
dnf install set_user_13*;
dnf install set_user_12*;
```


Install `set_user` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-set-user;
apt install postgresql-16-set-user;
apt install postgresql-15-set-user;
apt install postgresql-14-set-user;
apt install postgresql-13-set-user;
apt install postgresql-12-set-user;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `set_user_17*` | `set_user_16*` | `set_user_15*` | `set_user_14*` | `set_user_13*` | `set_user_12*` |
| `el9` | `set_user_17*` | `set_user_16*` | `set_user_15*` | `set_user_14*` | `set_user_13*` | `set_user_12*` |
| `d12` | `postgresql-17-set-user` | `postgresql-16-set-user` | `postgresql-15-set-user` | `postgresql-14-set-user` | `postgresql-13-set-user` | `postgresql-12-set-user` |
| `u22` | `postgresql-17-set-user` | `postgresql-16-set-user` | `postgresql-15-set-user` | `postgresql-14-set-user` | `postgresql-13-set-user` | `postgresql-12-set-user` |
| `u24` | `postgresql-17-set-user` | `postgresql-16-set-user` | `postgresql-15-set-user` | `postgresql-14-set-user` | `postgresql-13-set-user` | `postgresql-12-set-user` |






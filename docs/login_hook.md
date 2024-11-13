# login_hook


> [login_hook](https://github.com/splendiddata/login_hook): login_hook - hook to execute login_hook.login() at login time
>
> https://github.com/splendiddata/login_hook





[SEC](/sec) extensions: [`passwordcheck_cracklib`](/passwordcheck_cracklib), [`supautils`](/supautils), [`pgsodium`](/pgsodium), [`supabase_vault`](/supabase_vault), [`pg_session_jwt`](/pg_session_jwt), [`anon`](/anon), [`pg_tde`](/pg_tde), [`pgsmcrypto`](/pgsmcrypto), [`pgaudit`](/pgaudit), [`pgauditlogtofile`](/pgauditlogtofile), [`pg_auth_mon`](/pg_auth_mon), [`credcheck`](/credcheck), [`pgcryptokey`](/pgcryptokey), [`pg_jobmon`](/pg_jobmon), [`logerrors`](/logerrors), [`login_hook`](/login_hook), [`set_user`](/set_user), [`pg_snakeoil`](/pg_snakeoil), [`pgextwlist`](/pgextwlist), [`pg_auditor`](/pg_auditor), [`sslutils`](/sslutils), [`noset`](/noset), [`sepgsql`](/sepgsql), [`auth_delay`](/auth_delay), [`pgcrypto`](/pgcrypto), [`passwordcheck`](/passwordcheck)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [login_hook](https://github.com/splendiddata/login_hook) | 1.6 | **<span class="tcwarn">GPLv3</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [login_hook](/login_hook) |  | `login_hook` |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION login_hook;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `login_hook_17*` | `login_hook_16*` | `login_hook_15*` | `login_hook_14*` | `login_hook_13*` | `login_hook_12*` |
| `el9` | `login_hook_17*` | `login_hook_16*` | `login_hook_15*` | `login_hook_14*` | `login_hook_13*` | `login_hook_12*` |
| `d12` | `postgresql-17-login-hook` | `postgresql-16-login-hook` | `postgresql-15-login-hook` | `postgresql-14-login-hook` | `postgresql-13-login-hook` | `postgresql-12-login-hook` |
| `u22` | `postgresql-17-login-hook` | `postgresql-16-login-hook` | `postgresql-15-login-hook` | `postgresql-14-login-hook` | `postgresql-13-login-hook` | `postgresql-12-login-hook` |
| `u24` | `postgresql-17-login-hook` | `postgresql-16-login-hook` | `postgresql-15-login-hook` | `postgresql-14-login-hook` | `postgresql-13-login-hook` | `postgresql-12-login-hook` |



Install `login_hook` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["login_hook"]}'
```


Install `login_hook` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install login_hook_17*;
yum install login_hook_16*;
yum install login_hook_15*;
yum install login_hook_14*;
yum install login_hook_13*;
yum install login_hook_12*;
```


Install `login_hook` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-login-hook;
apt install postgresql-16-login-hook;
apt install postgresql-15-login-hook;
apt install postgresql-14-login-hook;
apt install postgresql-13-login-hook;
apt install postgresql-12-login-hook;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `login_hook_17*` | `login_hook_16*` | `login_hook_15*` | `login_hook_14*` | `login_hook_13*` | `login_hook_12*` |
| `el9` | `login_hook_17*` | `login_hook_16*` | `login_hook_15*` | `login_hook_14*` | `login_hook_13*` | `login_hook_12*` |
| `d12` | `postgresql-17-login-hook` | `postgresql-16-login-hook` | `postgresql-15-login-hook` | `postgresql-14-login-hook` | `postgresql-13-login-hook` | `postgresql-12-login-hook` |
| `u22` | `postgresql-17-login-hook` | `postgresql-16-login-hook` | `postgresql-15-login-hook` | `postgresql-14-login-hook` | `postgresql-13-login-hook` | `postgresql-12-login-hook` |
| `u24` | `postgresql-17-login-hook` | `postgresql-16-login-hook` | `postgresql-15-login-hook` | `postgresql-14-login-hook` | `postgresql-13-login-hook` | `postgresql-12-login-hook` |






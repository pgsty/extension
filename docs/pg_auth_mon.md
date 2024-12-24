# pg_auth_mon


> [pg_auth_mon](https://github.com/RafiaSabih/pg_auth_mon): monitor connection attempts per user
>
> https://github.com/RafiaSabih/pg_auth_mon





[SEC](/sec) extensions: [`passwordcheck_cracklib`](/passwordcheck_cracklib), [`supautils`](/supautils), [`pgsodium`](/pgsodium), [`supabase_vault`](/supabase_vault), [`pg_session_jwt`](/pg_session_jwt), [`anon`](/anon), [`pg_tde`](/pg_tde), [`pgsmcrypto`](/pgsmcrypto), [`pgaudit`](/pgaudit), [`pgauditlogtofile`](/pgauditlogtofile), [`pg_auth_mon`](/pg_auth_mon), [`credcheck`](/credcheck), [`pgcryptokey`](/pgcryptokey), [`pg_jobmon`](/pg_jobmon), [`logerrors`](/logerrors), [`login_hook`](/login_hook), [`set_user`](/set_user), [`pg_snakeoil`](/pg_snakeoil), [`pgextwlist`](/pgextwlist), [`pg_auditor`](/pg_auditor), [`sslutils`](/sslutils), [`noset`](/noset), [`sepgsql`](/sepgsql), [`auth_delay`](/auth_delay), [`pgcrypto`](/pgcrypto), [`passwordcheck`](/passwordcheck)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_auth_mon](https://github.com/RafiaSabih/pg_auth_mon) | 1.1 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_auth_mon](/pg_auth_mon) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_auth_mon;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.1 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | `pg_auth_mon_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 1.1 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-auth-mon` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pg_auth_mon` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pg_auth_mon
```


Install `pg_auth_mon` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_auth_mon"]}'
```


Install `pg_auth_mon` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pg_auth_mon_17*;
dnf install pg_auth_mon_16*;
dnf install pg_auth_mon_15*;
dnf install pg_auth_mon_14*;
dnf install pg_auth_mon_13*;
```


Install `pg_auth_mon` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pg-auth-mon;
apt install postgresql-16-pg-auth-mon;
apt install postgresql-15-pg-auth-mon;
apt install postgresql-14-pg-auth-mon;
apt install postgresql-13-pg-auth-mon;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_auth_mon_17*` | `pg_auth_mon_16*` | `pg_auth_mon_15*` | `pg_auth_mon_14*` | `pg_auth_mon_13*` |
| `el9` | `pg_auth_mon_17*` | `pg_auth_mon_16*` | `pg_auth_mon_15*` | `pg_auth_mon_14*` | `pg_auth_mon_13*` |
| `d12` | `postgresql-17-pg-auth-mon` | `postgresql-16-pg-auth-mon` | `postgresql-15-pg-auth-mon` | `postgresql-14-pg-auth-mon` | `postgresql-13-pg-auth-mon` |
| `u22` | `postgresql-17-pg-auth-mon` | `postgresql-16-pg-auth-mon` | `postgresql-15-pg-auth-mon` | `postgresql-14-pg-auth-mon` | `postgresql-13-pg-auth-mon` |
| `u24` | `postgresql-17-pg-auth-mon` | `postgresql-16-pg-auth-mon` | `postgresql-15-pg-auth-mon` | `postgresql-14-pg-auth-mon` | `postgresql-13-pg-auth-mon` |






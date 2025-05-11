# pgsmcrypto


> [pgsmcrypto](https://github.com/zhuobie/pgsmcrypto): PostgreSQL SM Algorithm Extension
>
> https://github.com/zhuobie/pgsmcrypto





[SEC](/sec) extensions: [`passwordcheck_cracklib`](/passwordcheck_cracklib), [`supautils`](/supautils), [`pgsodium`](/pgsodium), [`supabase_vault`](/supabase_vault), [`pg_session_jwt`](/pg_session_jwt), [`anon`](/anon), [`pg_tde`](/pg_tde), [`pgsmcrypto`](/pgsmcrypto), [`pgaudit`](/pgaudit), [`pgauditlogtofile`](/pgauditlogtofile), [`pg_auth_mon`](/pg_auth_mon), [`credcheck`](/credcheck), [`pgcryptokey`](/pgcryptokey), [`pg_jobmon`](/pg_jobmon), [`logerrors`](/logerrors), [`login_hook`](/login_hook), [`set_user`](/set_user), [`pg_snakeoil`](/pg_snakeoil), [`pgextwlist`](/pgextwlist), [`pg_auditor`](/pg_auditor), [`sslutils`](/sslutils), [`noset`](/noset), [`sepgsql`](/sepgsql), [`auth_delay`](/auth_delay), [`pgcrypto`](/pgcrypto), [`passwordcheck`](/passwordcheck)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgsmcrypto](https://github.com/zhuobie/pgsmcrypto) | 0.1.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `Rust` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgsmcrypto](/pgsmcrypto) | `pgrx` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pgsmcrypto;
```
> **Comment**: pgrx=0.12.6
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 0.1.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `pgsmcrypto_$v` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 0.1.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pgsmcrypto` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pgsmcrypto` via the [`pig`](https://github.com/pgsty/pig) cli tool:

```bash
pig ext add pgsmcrypto
```


Install `pgsmcrypto` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgsmcrypto"]}'
```


Install `pgsmcrypto` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pgsmcrypto_17;
dnf install pgsmcrypto_16;
dnf install pgsmcrypto_15;
dnf install pgsmcrypto_14;
dnf install pgsmcrypto_13;
```


Install `pgsmcrypto` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pgsmcrypto;
apt install postgresql-16-pgsmcrypto;
apt install postgresql-15-pgsmcrypto;
apt install postgresql-14-pgsmcrypto;
apt install postgresql-13-pgsmcrypto;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 |
|:------------:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgsmcrypto_17` | `pgsmcrypto_16` | `pgsmcrypto_15` | `pgsmcrypto_14` | `pgsmcrypto_13` |
| `el9` | `pgsmcrypto_17` | `pgsmcrypto_16` | `pgsmcrypto_15` | `pgsmcrypto_14` | `pgsmcrypto_13` |
| `d12` | `postgresql-17-pgsmcrypto` | `postgresql-16-pgsmcrypto` | `postgresql-15-pgsmcrypto` | `postgresql-14-pgsmcrypto` | `postgresql-13-pgsmcrypto` |
| `u22` | `postgresql-17-pgsmcrypto` | `postgresql-16-pgsmcrypto` | `postgresql-15-pgsmcrypto` | `postgresql-14-pgsmcrypto` | `postgresql-13-pgsmcrypto` |
| `u24` | `postgresql-17-pgsmcrypto` | `postgresql-16-pgsmcrypto` | `postgresql-15-pgsmcrypto` | `postgresql-14-pgsmcrypto` | `postgresql-13-pgsmcrypto` |






# pg_jobmon


> [pg_jobmon](https://github.com/omniti-labs/pg_jobmon): Extension for logging and monitoring functions in PostgreSQL
>
> https://github.com/omniti-labs/pg_jobmon





[SEC](/sec) extensions: [`passwordcheck_cracklib`](/passwordcheck_cracklib), [`supautils`](/supautils), [`pgsodium`](/pgsodium), [`supabase_vault`](/supabase_vault), [`pg_session_jwt`](/pg_session_jwt), [`anon`](/anon), [`pg_tde`](/pg_tde), [`pgsmcrypto`](/pgsmcrypto), [`pgaudit`](/pgaudit), [`pgauditlogtofile`](/pgauditlogtofile), [`pg_auth_mon`](/pg_auth_mon), [`credcheck`](/credcheck), [`pgcryptokey`](/pgcryptokey), [`pg_jobmon`](/pg_jobmon), [`logerrors`](/logerrors), [`login_hook`](/login_hook), [`set_user`](/set_user), [`pg_snakeoil`](/pg_snakeoil), [`pgextwlist`](/pgextwlist), [`pg_auditor`](/pg_auditor), [`sslutils`](/sslutils), [`noset`](/noset), [`sepgsql`](/sepgsql), [`auth_delay`](/auth_delay), [`pgcrypto`](/pgcrypto), [`passwordcheck`](/passwordcheck)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_jobmon](https://github.com/omniti-labs/pg_jobmon) | 1.4.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tcwarn">PIGSTY</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_jobmon](/pg_jobmon) |  |  | [`dblink`](dblink) |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_jobmon CASCADE;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.4.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pg_jobmon_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 1.4.1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-jobmon` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pg_jobmon` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_jobmon"]}'
```


Install `pg_jobmon` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pg_jobmon_17*;
dnf install pg_jobmon_16*;
dnf install pg_jobmon_15*;
dnf install pg_jobmon_14*;
dnf install pg_jobmon_13*;
dnf install pg_jobmon_12*;
```


Install `pg_jobmon` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pg-jobmon;
apt install postgresql-16-pg-jobmon;
apt install postgresql-15-pg-jobmon;
apt install postgresql-14-pg-jobmon;
apt install postgresql-13-pg-jobmon;
apt install postgresql-12-pg-jobmon;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_jobmon_17*` | `pg_jobmon_16*` | `pg_jobmon_15*` | `pg_jobmon_14*` | `pg_jobmon_13*` | `pg_jobmon_12*` |
| `el9` | `pg_jobmon_17*` | `pg_jobmon_16*` | `pg_jobmon_15*` | `pg_jobmon_14*` | `pg_jobmon_13*` | `pg_jobmon_12*` |
| `d12` | `postgresql-17-pg-jobmon` | `postgresql-16-pg-jobmon` | `postgresql-15-pg-jobmon` | `postgresql-14-pg-jobmon` | `postgresql-13-pg-jobmon` | `postgresql-12-pg-jobmon` |
| `u22` | `postgresql-17-pg-jobmon` | `postgresql-16-pg-jobmon` | `postgresql-15-pg-jobmon` | `postgresql-14-pg-jobmon` | `postgresql-13-pg-jobmon` | `postgresql-12-pg-jobmon` |
| `u24` | `postgresql-17-pg-jobmon` | `postgresql-16-pg-jobmon` | `postgresql-15-pg-jobmon` | `postgresql-14-pg-jobmon` | `postgresql-13-pg-jobmon` | `postgresql-12-pg-jobmon` |






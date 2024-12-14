# pgauditlogtofile


> [pgauditlogtofile](https://github.com/fmbiete/pgauditlogtofile): pgAudit addon to redirect audit log to an independent file
>
> https://github.com/fmbiete/pgauditlogtofile





[SEC](/sec) extensions: [`passwordcheck_cracklib`](/passwordcheck_cracklib), [`supautils`](/supautils), [`pgsodium`](/pgsodium), [`supabase_vault`](/supabase_vault), [`pg_session_jwt`](/pg_session_jwt), [`anon`](/anon), [`pg_tde`](/pg_tde), [`pgsmcrypto`](/pgsmcrypto), [`pgaudit`](/pgaudit), [`pgauditlogtofile`](/pgauditlogtofile), [`pg_auth_mon`](/pg_auth_mon), [`credcheck`](/credcheck), [`pgcryptokey`](/pgcryptokey), [`pg_jobmon`](/pg_jobmon), [`logerrors`](/logerrors), [`login_hook`](/login_hook), [`set_user`](/set_user), [`pg_snakeoil`](/pg_snakeoil), [`pgextwlist`](/pgextwlist), [`pg_auditor`](/pg_auditor), [`sslutils`](/sslutils), [`noset`](/noset), [`sepgsql`](/sepgsql), [`auth_delay`](/auth_delay), [`pgcrypto`](/pgcrypto), [`passwordcheck`](/passwordcheck)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgauditlogtofile](https://github.com/fmbiete/pgauditlogtofile) | 1.6 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgauditlogtofile](/pgauditlogtofile) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pgauditlogtofile;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.6 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `pgauditlogtofile_$v*` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |
| [DEB](/deb) | 1.6 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-pgauditlogtofile` | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** | **<span class="tccyan">✔</span>** |  |



Install `pgauditlogtofile` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgauditlogtofile"]}'
```


Install `pgauditlogtofile` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
dnf install pgauditlogtofile_17*;
dnf install pgauditlogtofile_16*;
dnf install pgauditlogtofile_15*;
dnf install pgauditlogtofile_14*;
dnf install pgauditlogtofile_13*;
dnf install pgauditlogtofile_12*;
```


Install `pgauditlogtofile` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pgauditlogtofile;
apt install postgresql-16-pgauditlogtofile;
apt install postgresql-15-pgauditlogtofile;
apt install postgresql-14-pgauditlogtofile;
apt install postgresql-13-pgauditlogtofile;
apt install postgresql-12-pgauditlogtofile;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgauditlogtofile_17*` | `pgauditlogtofile_16*` | `pgauditlogtofile_15*` | `pgauditlogtofile_14*` | `pgauditlogtofile_13*` | `pgauditlogtofile_12*` |
| `el9` | `pgauditlogtofile_17*` | `pgauditlogtofile_16*` | `pgauditlogtofile_15*` | `pgauditlogtofile_14*` | `pgauditlogtofile_13*` | `pgauditlogtofile_12*` |
| `d12` | `postgresql-17-pgauditlogtofile` | `postgresql-16-pgauditlogtofile` | `postgresql-15-pgauditlogtofile` | `postgresql-14-pgauditlogtofile` | `postgresql-13-pgauditlogtofile` | `postgresql-12-pgauditlogtofile` |
| `u22` | `postgresql-17-pgauditlogtofile` | `postgresql-16-pgauditlogtofile` | `postgresql-15-pgauditlogtofile` | `postgresql-14-pgauditlogtofile` | `postgresql-13-pgauditlogtofile` | `postgresql-12-pgauditlogtofile` |
| `u24` | `postgresql-17-pgauditlogtofile` | `postgresql-16-pgauditlogtofile` | `postgresql-15-pgauditlogtofile` | `postgresql-14-pgauditlogtofile` | `postgresql-13-pgauditlogtofile` | `postgresql-12-pgauditlogtofile` |






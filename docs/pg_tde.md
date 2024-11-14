# pg_tde


> [pg_tde](https://github.com/Percona-Lab/pg_tde): pg_tde access method
>
> https://github.com/Percona-Lab/pg_tde





[SEC](/sec) extensions: [`passwordcheck_cracklib`](/passwordcheck_cracklib), [`supautils`](/supautils), [`pgsodium`](/pgsodium), [`supabase_vault`](/supabase_vault), [`pg_session_jwt`](/pg_session_jwt), [`anon`](/anon), [`pg_tde`](/pg_tde), [`pgsmcrypto`](/pgsmcrypto), [`pgaudit`](/pgaudit), [`pgauditlogtofile`](/pgauditlogtofile), [`pg_auth_mon`](/pg_auth_mon), [`credcheck`](/credcheck), [`pgcryptokey`](/pgcryptokey), [`pg_jobmon`](/pg_jobmon), [`logerrors`](/logerrors), [`login_hook`](/login_hook), [`set_user`](/set_user), [`pg_snakeoil`](/pg_snakeoil), [`pgextwlist`](/pgextwlist), [`pg_auditor`](/pg_auditor), [`sslutils`](/sslutils), [`noset`](/noset), [`sepgsql`](/sepgsql), [`auth_delay`](/auth_delay), [`pgcrypto`](/pgcrypto), [`passwordcheck`](/passwordcheck)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_tde](https://github.com/Percona-Lab/pg_tde) | 1.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_tde](/pg_tde) | `beta` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'pg_tde'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION pg_tde;
```

-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_tde_$v*` |  | **<span class="tcwarn">✔</span>** |  |  |  |  |  |
| [DEB](/deb) | 1.0 | **<span class="tcblue">MIT</span>** | **<span class="tcwarn">PIGSTY</span>** | `postgresql-$v-pg-tde` |  | **<span class="tcwarn">✔</span>** |  |  |  |  |  |



Install `pg_tde` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_tde"]}'
```


Install `pg_tde` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install pg_tde_17*;
yum install pg_tde_16*;
yum install pg_tde_15*;
yum install pg_tde_14*;
yum install pg_tde_13*;
yum install pg_tde_12*;
```


Install `pg_tde` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-tde;
apt install postgresql-16-pg-tde;
apt install postgresql-15-pg-tde;
apt install postgresql-14-pg-tde;
apt install postgresql-13-pg-tde;
apt install postgresql-12-pg-tde;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_tde_17*` | `pg_tde_16*` | `pg_tde_15*` | `pg_tde_14*` | `pg_tde_13*` | `pg_tde_12*` |
| `el9` | `pg_tde_17*` | `pg_tde_16*` | `pg_tde_15*` | `pg_tde_14*` | `pg_tde_13*` | `pg_tde_12*` |
| `d12` | `postgresql-17-pg-tde` | `postgresql-16-pg-tde` | `postgresql-15-pg-tde` | `postgresql-14-pg-tde` | `postgresql-13-pg-tde` | `postgresql-12-pg-tde` |
| `u22` | `postgresql-17-pg-tde` | `postgresql-16-pg-tde` | `postgresql-15-pg-tde` | `postgresql-14-pg-tde` | `postgresql-13-pg-tde` | `postgresql-12-pg-tde` |
| `u24` | `postgresql-17-pg-tde` | `postgresql-16-pg-tde` | `postgresql-15-pg-tde` | `postgresql-14-pg-tde` | `postgresql-13-pg-tde` | `postgresql-12-pg-tde` |






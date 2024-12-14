# pg_snakeoil


> [pg_snakeoil](https://github.com/credativ/pg_snakeoil): The PostgreSQL Antivirus
>
> https://github.com/credativ/pg_snakeoil





[SEC](/sec) extensions: [`passwordcheck_cracklib`](/passwordcheck_cracklib), [`supautils`](/supautils), [`pgsodium`](/pgsodium), [`supabase_vault`](/supabase_vault), [`pg_session_jwt`](/pg_session_jwt), [`anon`](/anon), [`pg_tde`](/pg_tde), [`pgsmcrypto`](/pgsmcrypto), [`pgaudit`](/pgaudit), [`pgauditlogtofile`](/pgauditlogtofile), [`pg_auth_mon`](/pg_auth_mon), [`credcheck`](/credcheck), [`pgcryptokey`](/pgcryptokey), [`pg_jobmon`](/pg_jobmon), [`logerrors`](/logerrors), [`login_hook`](/login_hook), [`set_user`](/set_user), [`pg_snakeoil`](/pg_snakeoil), [`pgextwlist`](/pgextwlist), [`pg_auditor`](/pg_auditor), [`sslutils`](/sslutils), [`noset`](/noset), [`sepgsql`](/sepgsql), [`auth_delay`](/auth_delay), [`pgcrypto`](/pgcrypto), [`passwordcheck`](/passwordcheck)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_snakeoil](https://github.com/credativ/pg_snakeoil) | 1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tccyan">PGDG</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_snakeoil](/pg_snakeoil) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'pg_snakeoil'; # add this extension to postgresql.conf
```


> **Comment**: require clamV libs
-----------


## Packages


| OS | Version | License | REPO | Package Pattern | 17 | 16 | 15 | 14 | 13 | 12 | Dependency |
|:--:|---------|:-------:|:----:|-----------------|:--:|:--:|:--:|:--:|:--:|:--:|------------|
| [RPM](/rpm) | 1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcwarn">PIGSTY</span>** | `pg_snakeoil_$v*` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |
| [DEB](/deb) | 1 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | `postgresql-$v-snakeoil` | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** | **<span class="tcwarn">✔</span>** |  |



Install `pg_snakeoil` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_snakeoil"]}'
```


Install `pg_snakeoil` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
dnf install pg_snakeoil_17*;
dnf install pg_snakeoil_16*;
dnf install pg_snakeoil_15*;
dnf install pg_snakeoil_14*;
dnf install pg_snakeoil_13*;
dnf install pg_snakeoil_12*;
```


Install `pg_snakeoil` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-snakeoil;
apt install postgresql-16-snakeoil;
apt install postgresql-15-snakeoil;
apt install postgresql-14-snakeoil;
apt install postgresql-13-snakeoil;
apt install postgresql-12-snakeoil;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_snakeoil_17*` | `pg_snakeoil_16*` | `pg_snakeoil_15*` | `pg_snakeoil_14*` | `pg_snakeoil_13*` | `pg_snakeoil_12*` |
| `el9` | `pg_snakeoil_17*` | `pg_snakeoil_16*` | `pg_snakeoil_15*` | `pg_snakeoil_14*` | `pg_snakeoil_13*` | `pg_snakeoil_12*` |
| `d12` | `postgresql-17-snakeoil` | `postgresql-16-snakeoil` | `postgresql-15-snakeoil` | `postgresql-14-snakeoil` | `postgresql-13-snakeoil` | `postgresql-12-snakeoil` |
| `u22` | `postgresql-17-snakeoil` | `postgresql-16-snakeoil` | `postgresql-15-snakeoil` | `postgresql-14-snakeoil` | `postgresql-13-snakeoil` | `postgresql-12-snakeoil` |
| `u24` | `postgresql-17-snakeoil` | `postgresql-16-snakeoil` | `postgresql-15-snakeoil` | `postgresql-14-snakeoil` | `postgresql-13-snakeoil` | `postgresql-12-snakeoil` |






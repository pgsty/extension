# pgaudit


> [pgaudit](https://github.com/pgaudit/pgaudit): provides auditing functionality
>
> https://github.com/pgaudit/pgaudit





[SEC](/sec) extensions: [`passwordcheck_cracklib`](/passwordcheck_cracklib), [`supautils`](/supautils), [`pgsodium`](/pgsodium), [`supabase_vault`](/supabase_vault), [`pg_session_jwt`](/pg_session_jwt), [`anon`](/anon), [`pg_tde`](/pg_tde), [`pgsmcrypto`](/pgsmcrypto), [`pgaudit`](/pgaudit), [`pgauditlogtofile`](/pgauditlogtofile), [`pg_auth_mon`](/pg_auth_mon), [`credcheck`](/credcheck), [`pgcryptokey`](/pgcryptokey), [`pg_jobmon`](/pg_jobmon), [`logerrors`](/logerrors), [`login_hook`](/login_hook), [`set_user`](/set_user), [`pg_snakeoil`](/pg_snakeoil), [`pgextwlist`](/pgextwlist), [`pg_auditor`](/pg_auditor), [`sslutils`](/sslutils), [`noset`](/noset), [`sepgsql`](/sepgsql), [`auth_delay`](/auth_delay), [`pgcrypto`](/pgcrypto), [`passwordcheck`](/passwordcheck)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pgaudit](https://github.com/pgaudit/pgaudit) | 16.0 | **<span class="tcblue">PostgreSQL</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pgaudit](/pgaudit) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> | <span class="tcwarn">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'pgaudit'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION pgaudit;
```
> **Comment**: pg15=pgaudit17, pg14=pgaudit16 pg13=pgaudit15 pg12=pgaudit14
-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgaudit_17*` | `pgaudit_16*` | `pgaudit17_15*` | `pgaudit16_14*` | `pgaudit15_13*` | `pgaudit14_12*` |
| `el9` | `pgaudit_17*` | `pgaudit_16*` | `pgaudit17_15*` | `pgaudit16_14*` | `pgaudit15_13*` | `pgaudit14_12*` |
| `d12` | `postgresql-17-pgaudit` | `postgresql-16-pgaudit` | `postgresql-15-pgaudit` | `postgresql-14-pgaudit` | `postgresql-13-pgaudit` | `postgresql-12-pgaudit` |
| `u22` | `postgresql-17-pgaudit` | `postgresql-16-pgaudit` | `postgresql-15-pgaudit` | `postgresql-14-pgaudit` | `postgresql-13-pgaudit` | `postgresql-12-pgaudit` |
| `u24` | `postgresql-17-pgaudit` | `postgresql-16-pgaudit` | `postgresql-15-pgaudit` | `postgresql-14-pgaudit` | `postgresql-13-pgaudit` | `postgresql-12-pgaudit` |



Install `pgaudit` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgaudit"]}'   # common case
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgaudit17"]}' # pg15 @ el
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgaudit16"]}' # pg14 @ el'
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgaudit15"]}' # pg13 @ el'
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pgaudit14"]}' # pg12 @ el'
```


Install `pgaudit` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install pgaudit_17*;
yum install pgaudit_16*;
yum install pgaudit17_15*;
yum install pgaudit16_14*;
yum install pgaudit15_13*;
yum install pgaudit14_12*;
```


Install `pgaudit` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-pgaudit;
apt install postgresql-16-pgaudit;
apt install postgresql-15-pgaudit;
apt install postgresql-14-pgaudit;
apt install postgresql-13-pgaudit;
apt install postgresql-12-pgaudit;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pgaudit_17*` | `pgaudit_16*` | `pgaudit17_15*` | `pgaudit16_14*` | `pgaudit15_13*` | `pgaudit14_12*` |
| `el9` | `pgaudit_17*` | `pgaudit_16*` | `pgaudit17_15*` | `pgaudit16_14*` | `pgaudit15_13*` | `pgaudit14_12*` |
| `d12` | `postgresql-17-pgaudit` | `postgresql-16-pgaudit` | `postgresql-15-pgaudit` | `postgresql-14-pgaudit` | `postgresql-13-pgaudit` | `postgresql-12-pgaudit` |
| `u22` | `postgresql-17-pgaudit` | `postgresql-16-pgaudit` | `postgresql-15-pgaudit` | `postgresql-14-pgaudit` | `postgresql-13-pgaudit` | `postgresql-12-pgaudit` |
| `u24` | `postgresql-17-pgaudit` | `postgresql-16-pgaudit` | `postgresql-15-pgaudit` | `postgresql-14-pgaudit` | `postgresql-13-pgaudit` | `postgresql-12-pgaudit` |






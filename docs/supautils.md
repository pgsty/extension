# supautils


> [supautils](https://github.com/supabase/supautils): Extension that secures a cluster on a cloud environment
>
> https://github.com/supabase/supautils





[SEC](/sec) extensions: [`passwordcheck_cracklib`](/passwordcheck_cracklib), [`supautils`](/supautils), [`pgsodium`](/pgsodium), [`supabase_vault`](/supabase_vault), [`pg_session_jwt`](/pg_session_jwt), [`anon`](/anon), [`pg_tde`](/pg_tde), [`pgsmcrypto`](/pgsmcrypto), [`pgaudit`](/pgaudit), [`pgauditlogtofile`](/pgauditlogtofile), [`pg_auth_mon`](/pg_auth_mon), [`credcheck`](/credcheck), [`pgcryptokey`](/pgcryptokey), [`pg_jobmon`](/pg_jobmon), [`logerrors`](/logerrors), [`login_hook`](/login_hook), [`set_user`](/set_user), [`pg_snakeoil`](/pg_snakeoil), [`pgextwlist`](/pgextwlist), [`pg_auditor`](/pg_auditor), [`sslutils`](/sslutils), [`noset`](/noset), [`sepgsql`](/sepgsql), [`auth_delay`](/auth_delay), [`pgcrypto`](/pgcrypto), [`passwordcheck`](/passwordcheck)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [supautils](https://github.com/supabase/supautils) | 2.5.0 | **<span class="tccyan">Apache-2</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [supautils](/supautils) | `supabase` |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'supautils'; # add this extension to postgresql.conf
```



-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `supautils_17*` | `supautils_16*` | `supautils_15*` | `supautils_14*` | `supautils_13*` | `supautils_12*` |
| `el9` | `supautils_17*` | `supautils_16*` | `supautils_15*` | `supautils_14*` | `supautils_13*` | `supautils_12*` |
| `d12` | `postgresql-17-supautils` | `postgresql-16-supautils` | `postgresql-15-supautils` | `postgresql-14-supautils` | `postgresql-13-supautils` | `postgresql-12-supautils` |
| `u22` | `postgresql-17-supautils` | `postgresql-16-supautils` | `postgresql-15-supautils` | `postgresql-14-supautils` | `postgresql-13-supautils` | `postgresql-12-supautils` |
| `u24` | `postgresql-17-supautils` | `postgresql-16-supautils` | `postgresql-15-supautils` | `postgresql-14-supautils` | `postgresql-13-supautils` | `postgresql-12-supautils` |



Install `supautils` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["supautils"]}'
```


Install `supautils` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install supautils_17*;
yum install supautils_16*;
yum install supautils_15*;
yum install supautils_14*;
yum install supautils_13*;
yum install supautils_12*;
```


Install `supautils` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-supautils;
apt install postgresql-16-supautils;
apt install postgresql-15-supautils;
apt install postgresql-14-supautils;
apt install postgresql-13-supautils;
apt install postgresql-12-supautils;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `supautils_17*` | `supautils_16*` | `supautils_15*` | `supautils_14*` | `supautils_13*` | `supautils_12*` |
| `el9` | `supautils_17*` | `supautils_16*` | `supautils_15*` | `supautils_14*` | `supautils_13*` | `supautils_12*` |
| `d12` | `postgresql-17-supautils` | `postgresql-16-supautils` | `postgresql-15-supautils` | `postgresql-14-supautils` | `postgresql-13-supautils` | `postgresql-12-supautils` |
| `u22` | `postgresql-17-supautils` | `postgresql-16-supautils` | `postgresql-15-supautils` | `postgresql-14-supautils` | `postgresql-13-supautils` | `postgresql-12-supautils` |
| `u24` | `postgresql-17-supautils` | `postgresql-16-supautils` | `postgresql-15-supautils` | `postgresql-14-supautils` | `postgresql-13-supautils` | `postgresql-12-supautils` |






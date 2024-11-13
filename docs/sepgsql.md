# sepgsql


> [sepgsql](https://www.postgresql.org/docs/current/sepgsql.html): label-based mandatory access control (MAC) based on SELinux security policy.
>
> https://www.postgresql.org/docs/current/sepgsql.html





[SEC](/sec) extensions: [`passwordcheck_cracklib`](/passwordcheck_cracklib), [`supautils`](/supautils), [`pgsodium`](/pgsodium), [`supabase_vault`](/supabase_vault), [`pg_session_jwt`](/pg_session_jwt), [`anon`](/anon), [`pg_tde`](/pg_tde), [`pgsmcrypto`](/pgsmcrypto), [`pgaudit`](/pgaudit), [`pgauditlogtofile`](/pgauditlogtofile), [`pg_auth_mon`](/pg_auth_mon), [`credcheck`](/credcheck), [`pgcryptokey`](/pgcryptokey), [`pg_jobmon`](/pg_jobmon), [`logerrors`](/logerrors), [`login_hook`](/login_hook), [`set_user`](/set_user), [`pg_snakeoil`](/pg_snakeoil), [`pgextwlist`](/pgextwlist), [`pg_auditor`](/pg_auditor), [`sslutils`](/sslutils), [`noset`](/noset), [`sepgsql`](/sepgsql), [`auth_delay`](/auth_delay), [`pgcrypto`](/pgcrypto), [`passwordcheck`](/passwordcheck)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [sepgsql](https://www.postgresql.org/docs/current/sepgsql.html) | - | **<span class="tcblue">PostgreSQL</span>** | **<span class="tcblue">CONTRIB</span>** | **<span class="tcblue">CONTRIB</span>** | `C` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  | <span class="tcred">❗</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> |  |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [sepgsql](/sepgsql) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |



```bash
shared_preload_libraries = 'sepgsql'; # add this extension to postgresql.conf
```



```sql
CREATE EXTENSION sepgsql;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `postgresql17-contrib` | `postgresql16-contrib` | `postgresql15-contrib` | `postgresql14-contrib` | `postgresql13-contrib` | `postgresql12-contrib` |
| `el9` | `postgresql17-contrib` | `postgresql16-contrib` | `postgresql15-contrib` | `postgresql14-contrib` | `postgresql13-contrib` | `postgresql12-contrib` |
| `d12` | `postgresql-17` | `postgresql-16` | `postgresql-15` | `postgresql-14` | `postgresql-13` | `postgresql-12` |
| `u22` | `postgresql-17` | `postgresql-16` | `postgresql-15` | `postgresql-14` | `postgresql-13` | `postgresql-12` |
| `u24` | `postgresql-17` | `postgresql-16` | `postgresql-15` | `postgresql-14` | `postgresql-13` | `postgresql-12` |



Install `sepgsql` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["sepgsql"]}'
```


Install `sepgsql` [RPM](/rpm) from the **<span class="tcblue">CONTRIB</span>** **YUM** repo:

```bash
yum install postgresql17-contrib;
yum install postgresql16-contrib;
yum install postgresql15-contrib;
yum install postgresql14-contrib;
yum install postgresql13-contrib;
yum install postgresql12-contrib;
```


Install `sepgsql` [DEB](/deb) from the **<span class="tcblue">CONTRIB</span>** **APT** repo:

```bash
apt install postgresql-17;
apt install postgresql-16;
apt install postgresql-15;
apt install postgresql-14;
apt install postgresql-13;
apt install postgresql-12;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `postgresql17-contrib` | `postgresql16-contrib` | `postgresql15-contrib` | `postgresql14-contrib` | `postgresql13-contrib` | `postgresql12-contrib` |
| `el9` | `postgresql17-contrib` | `postgresql16-contrib` | `postgresql15-contrib` | `postgresql14-contrib` | `postgresql13-contrib` | `postgresql12-contrib` |
| `d12` | `postgresql-17` | `postgresql-16` | `postgresql-15` | `postgresql-14` | `postgresql-13` | `postgresql-12` |
| `u22` | `postgresql-17` | `postgresql-16` | `postgresql-15` | `postgresql-14` | `postgresql-13` | `postgresql-12` |
| `u24` | `postgresql-17` | `postgresql-16` | `postgresql-15` | `postgresql-14` | `postgresql-13` | `postgresql-12` |






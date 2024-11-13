# credcheck


> [credcheck](https://github.com/MigOpsRepos/credcheck): credcheck - postgresql plain text credential checker
>
> https://github.com/MigOpsRepos/credcheck





[SEC](/sec) extensions: [`passwordcheck_cracklib`](/passwordcheck_cracklib), [`supautils`](/supautils), [`pgsodium`](/pgsodium), [`supabase_vault`](/supabase_vault), [`pg_session_jwt`](/pg_session_jwt), [`anon`](/anon), [`pg_tde`](/pg_tde), [`pgsmcrypto`](/pgsmcrypto), [`pgaudit`](/pgaudit), [`pgauditlogtofile`](/pgauditlogtofile), [`pg_auth_mon`](/pg_auth_mon), [`credcheck`](/credcheck), [`pgcryptokey`](/pgcryptokey), [`pg_jobmon`](/pg_jobmon), [`logerrors`](/logerrors), [`login_hook`](/login_hook), [`set_user`](/set_user), [`pg_snakeoil`](/pg_snakeoil), [`pgextwlist`](/pgextwlist), [`pg_auditor`](/pg_auditor), [`sslutils`](/sslutils), [`noset`](/noset), [`sepgsql`](/sepgsql), [`auth_delay`](/auth_delay), [`pgcrypto`](/pgcrypto), [`passwordcheck`](/passwordcheck)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [credcheck](https://github.com/MigOpsRepos/credcheck) | 2.7.0 | **<span class="tcblue">MIT</span>** | **<span class="tccyan">PGDG</span>** | **<span class="tccyan">PGDG</span>** |  |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcwarn">✘</span> | <span class="tcwarn">✘</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [credcheck](/credcheck) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION credcheck;
```

-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `credcheck_17*` | `credcheck_16*` | `credcheck_15*` | `credcheck_14*` | `credcheck_13*` | `credcheck_12*` |
| `el9` | `credcheck_17*` | `credcheck_16*` | `credcheck_15*` | `credcheck_14*` | `credcheck_13*` | `credcheck_12*` |
| `d12` | `postgresql-17-credcheck` | `postgresql-16-credcheck` | `postgresql-15-credcheck` | `postgresql-14-credcheck` | `postgresql-13-credcheck` | `postgresql-12-credcheck` |
| `u22` | `postgresql-17-credcheck` | `postgresql-16-credcheck` | `postgresql-15-credcheck` | `postgresql-14-credcheck` | `postgresql-13-credcheck` | `postgresql-12-credcheck` |
| `u24` | `postgresql-17-credcheck` | `postgresql-16-credcheck` | `postgresql-15-credcheck` | `postgresql-14-credcheck` | `postgresql-13-credcheck` | `postgresql-12-credcheck` |



Install `credcheck` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["credcheck"]}'
```


Install `credcheck` [RPM](/rpm) from the **<span class="tccyan">PGDG</span>** **YUM** repo:

```bash
yum install credcheck_17*;
yum install credcheck_16*;
yum install credcheck_15*;
yum install credcheck_14*;
yum install credcheck_13*;
yum install credcheck_12*;
```


Install `credcheck` [DEB](/deb) from the **<span class="tccyan">PGDG</span>** **APT** repo:

```bash
apt install postgresql-17-credcheck;
apt install postgresql-16-credcheck;
apt install postgresql-15-credcheck;
apt install postgresql-14-credcheck;
apt install postgresql-13-credcheck;
apt install postgresql-12-credcheck;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `credcheck_17*` | `credcheck_16*` | `credcheck_15*` | `credcheck_14*` | `credcheck_13*` | `credcheck_12*` |
| `el9` | `credcheck_17*` | `credcheck_16*` | `credcheck_15*` | `credcheck_14*` | `credcheck_13*` | `credcheck_12*` |
| `d12` | `postgresql-17-credcheck` | `postgresql-16-credcheck` | `postgresql-15-credcheck` | `postgresql-14-credcheck` | `postgresql-13-credcheck` | `postgresql-12-credcheck` |
| `u22` | `postgresql-17-credcheck` | `postgresql-16-credcheck` | `postgresql-15-credcheck` | `postgresql-14-credcheck` | `postgresql-13-credcheck` | `postgresql-12-credcheck` |
| `u24` | `postgresql-17-credcheck` | `postgresql-16-credcheck` | `postgresql-15-credcheck` | `postgresql-14-credcheck` | `postgresql-13-credcheck` | `postgresql-12-credcheck` |






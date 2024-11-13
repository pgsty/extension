# pg_auditor


> [pg_auditor](https://github.com/kouber/pg_auditor): Audit data changes and provide flashback ability
>
> https://github.com/kouber/pg_auditor





[SEC](/sec) extensions: [`passwordcheck_cracklib`](/passwordcheck_cracklib), [`supautils`](/supautils), [`pgsodium`](/pgsodium), [`supabase_vault`](/supabase_vault), [`pg_session_jwt`](/pg_session_jwt), [`anon`](/anon), [`pg_tde`](/pg_tde), [`pgsmcrypto`](/pgsmcrypto), [`pgaudit`](/pgaudit), [`pgauditlogtofile`](/pgauditlogtofile), [`pg_auth_mon`](/pg_auth_mon), [`credcheck`](/credcheck), [`pgcryptokey`](/pgcryptokey), [`pg_jobmon`](/pg_jobmon), [`logerrors`](/logerrors), [`login_hook`](/login_hook), [`set_user`](/set_user), [`pg_snakeoil`](/pg_snakeoil), [`pgextwlist`](/pgextwlist), [`pg_auditor`](/pg_auditor), [`sslutils`](/sslutils), [`noset`](/noset), [`sepgsql`](/sepgsql), [`auth_delay`](/auth_delay), [`pgcrypto`](/pgcrypto), [`passwordcheck`](/passwordcheck)


-------
## Extension


| Extension | Version | License | RPM | DEB | PL |
|-----------|:-------:|:-------:|:---:|:---:|:--:|
| [pg_auditor](https://github.com/kouber/pg_auditor) | 0.2 | **<span class="tcblue">BSD-3</span>** | **<span class="tcwarn">PIGSTY</span>** | **<span class="tcwarn">PIGSTY</span>** | `SQL` |



| `Bin` | `LOAD` | `DYLIB` | `DDL` | `TRUST` | `RELOC` |
|:-----:|:------:|:-------:|:-----:|:-------:|:-------:|
|  |  | <span class="tcwarn">✘</span> | <span class="tcblue">✔</span> |  | <span class="tcblue">✔</span> |



| Alias | Tags | Schemas | Requires | Required by |
|-------|------|---------|----------|-------------|
| [pg_auditor](/pg_auditor) |  |  |  |  |



| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `el9` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `d12` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u22` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |
| `u24` | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> | <span class="tcblue">✔</span> |





```sql
CREATE EXTENSION pg_auditor;
```
> **Comment**: pg15 rpm pkg name is pgaudit17_$v*
-----------


## Packages


| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_auditor_17` | `pg_auditor_16` | `pg_auditor_15` | `pg_auditor_14` | `pg_auditor_13` | `pg_auditor_12` |
| `el9` | `pg_auditor_17` | `pg_auditor_16` | `pg_auditor_15` | `pg_auditor_14` | `pg_auditor_13` | `pg_auditor_12` |
| `d12` | `postgresql-17-pg-auditor` | `postgresql-16-pg-auditor` | `postgresql-15-pg-auditor` | `postgresql-14-pg-auditor` | `postgresql-13-pg-auditor` | `postgresql-12-pg-auditor` |
| `u22` | `postgresql-17-pg-auditor` | `postgresql-16-pg-auditor` | `postgresql-15-pg-auditor` | `postgresql-14-pg-auditor` | `postgresql-13-pg-auditor` | `postgresql-12-pg-auditor` |
| `u24` | `postgresql-17-pg-auditor` | `postgresql-16-pg-auditor` | `postgresql-15-pg-auditor` | `postgresql-14-pg-auditor` | `postgresql-13-pg-auditor` | `postgresql-12-pg-auditor` |



Install `pg_auditor` via [Pigsty](https://pigsty.io/docs/pgext/usage/install/) playbook:

```bash
./pgsql.yml -t pg_extension -e '{"pg_extensions": ["pg_auditor"]}'
```


Install `pg_auditor` [RPM](/rpm) from the **<span class="tcwarn">PIGSTY</span>** **YUM** repo:

```bash
yum install pg_auditor_17;
yum install pg_auditor_16;
yum install pg_auditor_15;
yum install pg_auditor_14;
yum install pg_auditor_13;
yum install pg_auditor_12;
```


Install `pg_auditor` [DEB](/deb) from the **<span class="tcwarn">PIGSTY</span>** **APT** repo:

```bash
apt install postgresql-17-pg-auditor;
apt install postgresql-16-pg-auditor;
apt install postgresql-15-pg-auditor;
apt install postgresql-14-pg-auditor;
apt install postgresql-13-pg-auditor;
apt install postgresql-12-pg-auditor;
```




| Distro / Ver | PG17 | PG16 | PG15 | PG14 | PG13 | PG12 |
|:------------:|:----:|:----:|:----:|:----:|:----:|:----:|
| `el8` | `pg_auditor_17` | `pg_auditor_16` | `pg_auditor_15` | `pg_auditor_14` | `pg_auditor_13` | `pg_auditor_12` |
| `el9` | `pg_auditor_17` | `pg_auditor_16` | `pg_auditor_15` | `pg_auditor_14` | `pg_auditor_13` | `pg_auditor_12` |
| `d12` | `postgresql-17-pg-auditor` | `postgresql-16-pg-auditor` | `postgresql-15-pg-auditor` | `postgresql-14-pg-auditor` | `postgresql-13-pg-auditor` | `postgresql-12-pg-auditor` |
| `u22` | `postgresql-17-pg-auditor` | `postgresql-16-pg-auditor` | `postgresql-15-pg-auditor` | `postgresql-14-pg-auditor` | `postgresql-13-pg-auditor` | `postgresql-12-pg-auditor` |
| `u24` | `postgresql-17-pg-auditor` | `postgresql-16-pg-auditor` | `postgresql-15-pg-auditor` | `postgresql-14-pg-auditor` | `postgresql-13-pg-auditor` | `postgresql-12-pg-auditor` |






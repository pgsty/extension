# Repo Usage

[![Webite: ext.pigsty.io](https://img.shields.io/badge/website-ext.pigsty.io-slategray?style=flat&logo=cilium&logoColor=white)](https://ext.pigsty.io)
[![Extensions: 339](https://img.shields.io/badge/extensions-339-%233E668F?style=flat&logo=postgresql&logoColor=white&labelColor=3E668F)](https://pigsty.io/docs/pgext/list)

The supplementary [APT](#apt-repo) and [YUM](#yum-repo) repo for PostgreSQL extensions, maintained and used by [Pigsty](https://pigsty.io)

Contains 150+ PG extensions [RPM](/rpm) / [DEB](/deb) for PostgreSQL **12** - **17** in addition to the official PGDG repo.

**Why extension matters to PostgreSQL?** check the post: "[***PostgreSQL is eating the database world!***](https://medium.com/@fengruohang/postgres-is-eating-the-database-world-157c204dcfc4)"




--------

## YUM Repo

[![Linux](https://img.shields.io/badge/Linux-x86_64-%23FCC624?style=flat&logo=linux&labelColor=FCC624&logoColor=black)](https://pigsty.io/docs/node)
[![RHEL Support: 8/9](https://img.shields.io/badge/EL-7/8/9-red?style=flat&logo=redhat&logoColor=red)](https://pigsty.io/docs/pgext/list/rpm/)
[![RHEL](https://img.shields.io/badge/RHEL-slategray?style=flat&logo=redhat&logoColor=red)](https://pigsty.io/docs/pgext/list/rpm/)
[![CentOS](https://img.shields.io/badge/CentOS-slategray?style=flat&logo=centos&logoColor=%23262577)](https://almalinux.org/)
[![RockyLinux](https://img.shields.io/badge/RockyLinux-slategray?style=flat&logo=rockylinux&logoColor=%2310B981)](https://almalinux.org/)
[![AlmaLinux](https://img.shields.io/badge/AlmaLinux-slategray?style=flat&logo=almalinux&logoColor=black)](https://almalinux.org/)
[![OracleLinux](https://img.shields.io/badge/OracleLinux-slategray?style=flat&logo=oracle&logoColor=%23F80000)](https://almalinux.org/)

Pigsty currently offers a supplementary PG extension repository for EL systems, providing **121** additional RPM plugins in addition to the official PGDG YUM repository (135).

- Pigsty YUM Repository: https://repo.pigsty.io/yum/
- PGDG YUM Repository: https://download.postgresql.org/pub/repos/yum/ ([PGDG Yum Repo Introduction](https://www.postgresql.org/download/linux/redhat/))

The Pigsty YUM repository only includes extensions **not present in the PGDG YUM repository**.
Once an extension is added to the PGDG YUM repository, Pigsty YUM repository will either remove it or align with the PGDG repository.

For EL 7/8/9 and compatible systems, use the following commands to add the GPG public key and the upstream repository file of the Pigsty repository:

```bash
curl -fsSL https://repo.pigsty.io/key      | sudo tee /etc/pki/rpm-gpg/RPM-GPG-KEY-pigsty >/dev/null  # add gpg key
curl -fsSL https://repo.pigsty.io/yum/repo | sudo tee /etc/yum.repos.d/pigsty.repo        >/dev/null  # add repo file
```

All RPMs are signed with the GPG key fingerprint `9592A7BC7A682E7333376E09E7935D8DB9BD8B20` (`B9BD8B20`).

<details><summary>Write Repo File Manually</summary><br>

```bash
sudo tee /etc/yum.repos.d/pigsty-io.repo > /dev/null <<-'EOF'
[pigsty-infra]
name=Pigsty Infra for $basearch
baseurl=https://repo.pigsty.io/yum/infra/$basearch
skip_if_unavailable = 1
enabled = 1
priority = 1
gpgcheck = 1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-pigsty
module_hotfixes=1

[pigsty-pgsql]
name=Pigsty PGSQL For el$releasever.$basearch
baseurl=https://repo.pigsty.io/yum/pgsql/el$releasever.$basearch
skip_if_unavailable = 1
enabled = 1
priority = 1
gpgcheck = 1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-pigsty
module_hotfixes=1
EOF
sudo yum makecache;
```

</details>




--------

## APT Repo


[![Linux](https://img.shields.io/badge/Linux-x86_64-%23FCC624?style=flat&logo=linux&labelColor=FCC624&logoColor=black)](https://pigsty.io/docs/node)
[![Ubuntu Support: 22](https://img.shields.io/badge/Ubuntu-22-%23E95420?style=flat&logo=ubuntu&logoColor=%23E95420)](https://pigsty.io/docs/pgext/list/deb/)
[![Debian Support: 12](https://img.shields.io/badge/Debian-12-%23A81D33?style=flat&logo=debian&logoColor=%23A81D33)](https://pigsty.io/docs/reference/compatibility/)

Pigsty currently offers a supplementary PG extension repository for Debian/Ubuntu systems, providing **133** additional DEB packages in addition to the official PGDG APT repository (109).

- Pigsty APT Repository: https://repo.pigsty.io/apt/
- PGDG APT Repository: http://apt.postgresql.org/pub/repos/apt/ ([PGDG Apt Repo Introduction](https://www.postgresql.org/download/linux/debian/))

The Pigsty APT repository only includes extensions **not present in the PGDG APT repository**.
Once an extension is added to the PGDG APT repository, Pigsty APT repository will either remove it or align with the PGDG repository.

For Debian/Ubuntu and compatible systems, use the following commands to sequentially add the GPG public key and the upstream repository file of the Pigsty repository:

```bash
# add GPG key to keyring
curl -fsSL https://repo.pigsty.io/key | sudo gpg --dearmor -o /etc/apt/keyrings/pigsty.gpg

# get debian codename, distro_codename=jammy, focal, bullseye, bookworm
sudo tee /etc/apt/sources.list.d/pigsty-io.list > /dev/null <<EOF
deb [signed-by=/etc/apt/keyrings/pigsty.gpg] https://repo.pigsty.io/apt/infra generic main 
deb [signed-by=/etc/apt/keyrings/pigsty.gpg] https://repo.pigsty.io/apt/pgsql/$(lsb_release -cs) $(lsb_release -cs) main
EOF

# refresh APT repo cache
sudo apt update
```

All DEBs are signed with the GPG key fingerprint `9592A7BC7A682E7333376E09E7935D8DB9BD8B20` (`B9BD8B20`).



--------

## Resources

GitHub Repo of this website: [github.com/pgsty/extension](https://github.com/pgsty/extension) 

The building recipes and specs, metadata are all open-sourced, related GitHub repos:

- [`pkg`](https://github.com/pgsty/pkg): The repository of RPM/DEB packages for PostgreSQL extensions
- [`infra_pkg`](https://github.com/pgsty/infra-pkg): Building observability stack & modules from tarball
- [`pgsql-rpm`](https://github.com/pgsty/pgsql-rpm): Building PostgreSQL RPM packages from source code
- [`pgsql-deb`](https://github.com/pgsty/pgsql-deb): Building PostgreSQL DEB packages from source code

**PostgreSQL Yum Repo** (el9)

- https://download.postgresql.org/pub/repos/yum/17/redhat/rhel-9-x86_64/
- https://download.postgresql.org/pub/repos/yum/16/redhat/rhel-9-x86_64/
- https://download.postgresql.org/pub/repos/yum/15/redhat/rhel-9-x86_64/
- https://download.postgresql.org/pub/repos/yum/14/redhat/rhel-9-x86_64/
- https://download.postgresql.org/pub/repos/yum/13/redhat/rhel-9-x86_64/
- https://download.postgresql.org/pub/repos/yum/12/redhat/rhel-9-x86_64/

**PostgreSQL Yum Repo** (el8)

- https://download.postgresql.org/pub/repos/yum/17/redhat/rhel-8-x86_64/
- https://download.postgresql.org/pub/repos/yum/16/redhat/rhel-8-x86_64/
- https://download.postgresql.org/pub/repos/yum/15/redhat/rhel-8-x86_64/
- https://download.postgresql.org/pub/repos/yum/14/redhat/rhel-8-x86_64/
- https://download.postgresql.org/pub/repos/yum/13/redhat/rhel-8-x86_64/
- https://download.postgresql.org/pub/repos/yum/12/redhat/rhel-8-x86_64/
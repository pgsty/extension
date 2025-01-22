#!/usr/bin/env python3

import csv
import os
import json
from datetime import datetime

##################################################
# CONSTANT                                       #
##################################################

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(SCRIPT_DIR, '..', 'data', 'pigsty.csv'))
DOCS_PATH = os.path.abspath(os.path.join(SCRIPT_DIR, '..', 'docs'))
STUB_PATH = os.path.abspath(os.path.join(SCRIPT_DIR, '..', 'stub'))
CONF_PATH = os.path.abspath(os.path.join(SCRIPT_DIR, '..', 'conf'))

PG_VERS = ['17', '16', '15', '14', '13', '12']
DISTROS = ['el8', 'el9', 'd12', 'u22', 'u24']

NOP_LIST = {
    "rpm": ["plr", "pljava","pg_dbms_job", "pgtap", "faker", "dbt2", "pgpool", "pgagent", "repmgr", "slony", "pg_strom", "oracle_fdw", "db2_fdw", "babelfishpg_common", "babelfishpg_tsql", "babelfishpg_tds", "babelfishpg_money"],
    "el7": ["plr", "pljava","pg_dbms_job", "pgtap", "faker", "dbt2", "pgpool", "pgagent", "repmgr", "slony", "pg_strom", "oracle_fdw", "db2_fdw", "babelfishpg_common", "babelfishpg_tsql", "babelfishpg_tds", "babelfishpg_money"],
    "el8": ["plr", "pljava","pg_dbms_job", "pgtap", "faker", "dbt2", "pgpool", "pgagent", "repmgr", "slony", "pg_strom", "oracle_fdw", "db2_fdw", "babelfishpg_common", "babelfishpg_tsql", "babelfishpg_tds", "babelfishpg_money"],
    "el9": ["plr", "pg_dbms_job", "pgtap", "faker", "dbt2", "pgpool", "pgagent", "repmgr", "slony", "pg_strom", "oracle_fdw", "db2_fdw", "babelfishpg_common", "babelfishpg_tsql", "babelfishpg_tds", "babelfishpg_money"],

    "deb": ["plr", "pljava", "pgtap", "pgpool", "pgagent", "repmgr", "slony", "oracle_fdw", "babelfishpg_common", "babelfishpg_tsql", "babelfishpg_tds", "babelfishpg_money"],
    "u24": ["plr",           "pgtap", "pgpool", "pgagent", "repmgr", "slony", "oracle_fdw", "babelfishpg_common", "babelfishpg_tsql", "babelfishpg_tds", "babelfishpg_money", "pgml",  "topn", "timescaledb_toolkit"],
    "u22": ["plr",           "pgtap", "pgpool", "pgagent", "repmgr", "slony", "oracle_fdw", "babelfishpg_common", "babelfishpg_tsql", "babelfishpg_tds", "babelfishpg_money"],
    "u20": ["plr", "pljava", "pgtap", "pgpool", "pgagent", "repmgr", "slony", "oracle_fdw", "babelfishpg_common", "babelfishpg_tsql", "babelfishpg_tds", "babelfishpg_money"],
    "d12": ["plr",           "pgtap", "pgpool", "pgagent", "repmgr", "slony", "oracle_fdw", "babelfishpg_common", "babelfishpg_tsql", "babelfishpg_tds", "babelfishpg_money"],
    "d11": ["plr", "pljava", "pgtap", "pgpool", "pgagent", "repmgr", "slony", "oracle_fdw", "babelfishpg_common", "babelfishpg_tsql", "babelfishpg_tds", "babelfishpg_money"],
}

EXT_NOP_LIST = []

CATES = {
    "TIME": "TIME: TimescaleDB, Versioning & Temporal Table, Crontab, Async & Background Job Scheduler, ...",
    "GIS": "GIS: GeoSpatial Data Types, Operators, and Indexes, Hexagonal Indexing, OGR Data FDW, GeoIP & MobilityDB, etc...",
    "RAG": "RAG: Vector Database with IVFFLAT, HNSW, DiskANN Indexes, AI & ML in SQL interface, Similarity Funcs, etc... ",
    "FTS": "FTS: ElasticSearch Alternative with BM25, 2-gram/3-gram Fuzzy Search, Zhparser & Hunspell Segregation Dicts, etc...",
    "OLAP": "OLAP: DuckDB Integration with FDW & PG Lakehouse, Access Parquet from File/S3, Sharding with Citus/Partman/PlProxy, ...",
    "FEAT": "FEAT: OpenCypher with AGE, GraphQL, JsonSchema, Hints & Hypo Index, HLL, Rum, IVM, ChemRDKit, and Message Queues,...",
    "LANG": "LANG: Develop, Test, Package, and Deliver Stored Procedures written in various PL/Lanaguages: Java, Js, Lua, R, Sh, PRQL, ...",
    "TYPE": "TYPE: Dedicate New Data Types Like: prefix, sember, uint, SIUnit, RoaringBitmap, Rational, Sphere, Hash, RRule, and more...",
    "UTIL": "UTIL: Utilities such as send http request, perform gzip/zstd compress, send mails, Regex, ICU, encoding, docs, Encryption,...",
    "FUNC": "FUNC: Functionality such as sync/async HTTP, GZIP, JWT, SaltedHash, Extra Window Aggs, PCRE, ICU, ID & Rand Generator, etc...",
    "OMNI": "OMNI: Omnigres extensions that turn PostgreSQL into a full-featured web application development platform...",
    "ADMIN": "ADMIN: Utilities for Bloat Control, DirtyRead, BufferInspect, DDL Generate, ChecksumVerify, Permission, Priority, Catalog,...",
    "STAT": "STAT: Observability Catalogs, Monitoring Metrics & Views, Statistics, Query Plans, WaitSampling, SlowLogs, and etc...",
    "SEC": "SEC: Auditing Logs, Enforce Passwords, Keep Secrets, TDE, SM Algorithm, Login Hooks, Log Erros, Extension White List, ...",
    "FDW": "FDW: Wrappers & Multicorn for FDW Development, Access other DBMS: MySQL, Mongo, SQLite, MSSQL, Oracle, HDFS, DB2,...",
    "SIM": "SIM: Protocol Simulation & heterogeneous DBMS Compatibility: Oracle, MSSQL, DB2, MySQL, Memcached, and Babelfish!",
    "ETL": "ETL: Logical Replication, Decoding, CDC in protobuf/JSON/Mongo format, Copy & Load & Compare Postgres Databases,...",
}

# generate
def tabulate(cols, filter_func):
    headers = "| " + " | ".join([col['header'] for col in cols]) + " |\n"
    separator = "|" + "|".join([ ':' + '-' * len(col['header'])+':' if col['center'] else '-' * (len(col['header'])+2) for col in cols]) + "|\n"
    rows = [headers, separator]
    for row in DATA:
        if not filter_func(row): continue
        row_values = [col['func'](row) for col in cols]
        row_str = "| " + " | ".join(row_values) + " |\n"
        rows.append(row_str)
    return ''.join(rows)

# open file for write
def openw(p):
    output_path = os.path.join(DOCS_PATH, p)
    return open(output_path, 'w')

# load data from pigsty extension csv, or default to ../data/ext.csv
def load_data(filepath=DATA_PATH):
    parse_array = lambda v: v[1:-1].split(',') if v.startswith('{') and v.endswith('}') else []
    data = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['id'] = int(row['id'])
            if row['tags']: row['tags'] = parse_array(row['tags'])
            if row['schemas']: row['schemas'] = parse_array(row['schemas'])
            if row['pg_ver']: row['pg_ver'] = parse_array(row['pg_ver'])
            if row['requires']: row['requires'] = parse_array(row['requires'])
            if row['rpm_deps']: row['rpm_deps'] = parse_array(row['rpm_deps'])
            if row['deb_deps']: row['deb_deps'] = parse_array(row['deb_deps'])
            if row['rpm_pg']: row['rpm_pg'] = parse_array(row['rpm_pg'])
            if row['deb_pg']: row['deb_pg'] = parse_array(row['deb_pg'])

            row['utility']     =  True if row['utility']   == 't'  else False if row['utility'] == 'f'  else None
            row['lead']        =  True if row['lead']   == 't'  else False if row['lead'] == 'f'  else None
            row['has_solib']   =  True if row['has_solib']   == 't'  else False if row['has_solib'] == 'f'  else None
            row['need_ddl']    =  True if row['need_ddl']    == 't'  else False if row['need_ddl'] == 'f'  else None
            row['need_load']   =  True if row['need_load']   == 't'  else False if row['need_load'] == 'f'  else None
            row['trusted']     =  True if row['trusted']     == 't'  else False if row['trusted'] == 'f'  else None
            row['relocatable'] =  True if row['relocatable'] == 't'  else False if row['relocatable'] == 'f'  else None

            row['has_rpm'] = True if row['rpm_repo'] else False
            row['has_deb'] = True if row['deb_repo'] else False
            row['has_both'] = True if row['deb_repo'] and row['deb_repo'] else False
            row['pg12'] = True if '12' in row['pg_ver'] else False
            row['pg13'] = True if '13' in row['pg_ver'] else False
            row['pg14'] = True if '14' in row['pg_ver'] else False
            row['pg15'] = True if '15' in row['pg_ver'] else False
            row['pg16'] = True if '16' in row['pg_ver'] else False
            row['pg17'] = True if '17' in row['pg_ver'] else False

            row['contrib'] = True if row['repo'] == 'CONTRIB' else False
            row['rpm_pgdg'] = True if row['has_rpm'] and row['rpm_repo'] == 'PGDG' else False
            row['rpm_pigsty'] = True if row['has_rpm'] and row['rpm_repo'] == 'PIGSTY' else False
            row['rpm_misc'] = True if row['has_rpm'] and (row['rpm_repo'] not in ('PGDG', 'PIGSTY', 'TIMESCALE', 'CITUS','CONTRIB','')) else False

            row['deb_pgdg'] = True if row['has_deb'] and row['deb_repo'] == 'PGDG' else False
            row['deb_pigsty'] = True if row['has_deb'] and row['deb_repo'] == 'PIGSTY' else False
            row['deb_misc'] = True if row['has_deb'] and (row['deb_repo'] not in ('PGDG', 'PIGSTY', 'TIMESCALE', 'CITUS','CONTRIB','')) else False
            data.append(row)
    return data



DATA = load_data()
CATE = list(dict.fromkeys([i['category'] for i in DATA]))

def pkg_ext_list(ver, distro):
    REPO_KEY, HAS_KEY, PG_VER_KEY, PKG_KEY = '', '', '', ''
    pg_pkg_str = ''
    filter = lambda row: True
    os_type = ''
    nop_list = NOP_LIST.get(distro.lower(), [])
    if distro.lower() in ('rpm', 'el7', 'el8', 'el9'):
        REPO_KEY, HAS_KEY, PG_VER_KEY, PKG_KEY = 'rpm_repo', 'has_rpm', 'rpm_pg', 'rpm_pkg'
        pg_pkg_str = '  - postgresql%s*\n' % ver
        os_type = "rpm"
        filter = lambda ext: ext[HAS_KEY] and ver in ext[PG_VER_KEY] and ext['alias'] not in nop_list
    elif distro.lower() in ('deb', 'u20', 'u22', 'u24', 'd12', 'd11'):
        REPO_KEY, HAS_KEY, PG_VER_KEY, PKG_KEY = 'deb_repo', 'has_deb', 'deb_pg', 'deb_pkg'
        pg_pkg_str = '  - postgresql-%s postgresql-client-%s postgresql-server-dev-%s postgresql-plpython3-%s postgresql-plperl-%s postgresql-pltcl-%s\n' % (ver,ver,ver,ver,ver,ver)
        os_type = "deb"
        filter = lambda ext: ext[HAS_KEY] and ver in ext[PG_VER_KEY] and ext['alias'] not in nop_list
    elif distro.lower() in ('both'):
        REPO_KEY, HAS_KEY, PG_VER_KEY, PKG_KEY = 'rpm_repo', 'has_rpm', 'rpm_pg', 'rpm_pkg'
        filter = lambda ext: ext["has_deb"] and ext["has_rpm"] and ver in ext["rpm_pg"] and ver in ext["deb_pg"] and ext['alias'] not in nop_list
    else:
        raise("invalid distro")

    repo_pkg, ext_list = [], []
    for cate in CATE:
        repo_pkg_add, repo_pkg_nop, ext_list_add, ext_list_nop = [], [] ,[], []
        for ext in DATA:
            #if not ext[REPO_KEY]: continue
            if ext['repo'] == 'CONTRIB': continue
            if ext['category'] == cate:
                if filter(ext):
                    # edge case: pgaudit on el8/9
                    name, pkg, alias = ext['name'], ext[PKG_KEY], ext['alias']
                    if name == 'pgaudit' and os_type == 'rpm' and ver in ['12','13','14','15']: #pg15=pgaudit17, pg14=pgaudit16 pg13=pgaudit15 pg12=pgaudit14
                        pkg = pkg.replace('$v', ver).replace('pgaudit', 'pgaudit' + str(int(ver)+2))
                        alias = alias + str(int(ver)+2)
                    elif name == 'citus_columnar':
                        continue
                    elif name == 'postgis' and os_type == 'rpm' and (ver in ['12']): #pg12=34(el8/9),33(el7)
                        if distro == 'el7': continue
                        else:
                            pkg,alias = 'postgis34_12*', 'postgis34'
                    elif name == 'postgis' and distro == 'el7' and (ver in ['12']): #pg12=34(el8/9),33(el7)
                            pkg,alias = 'postgis33_12*', 'postgis33'
                    elif name.startswith('postgis_') or name.startswith('address_standardizer'): continue
                    elif name == 'babelfish_common':
                        pkg,alias = 'wiltondb', 'wiltondb'
                    elif name == 'timescaledb' and distro == 'u24' and ver == '12':
                        pkg, alias = '#' + ext[PKG_KEY].replace('$v', ver), '#' + ext['alias']
                        repo_pkg_nop.append(pkg)
                        ext_list_nop.append(alias)
                        continue
                    elif name in ('pg_partman', 'timeseries') and distro == 'u24' and ver in ['12','13']:
                        pkg, alias = '#' + ext[PKG_KEY].replace('$v', ver), '#' + ext['alias']
                        repo_pkg_nop.append(pkg)
                        ext_list_nop.append(alias)
                        continue
                    else:
                        pkg = ext[PKG_KEY].replace('$v', ver)
                        alias = ext['alias']
                    repo_pkg_add.append(pkg)
                    if name.startswith('hunspell'):
                        if name.startswith('hunspell_cs_cz'):
                            ext_list_add.append('hunspell')
                    elif name in ['pg_mooncake', 'citus']:
                        ext_list_nop.append('#' + alias)
                    elif name == 'citus_columnar':
                        pass
                    else:
                        ext_list_add.append(alias)
                else:
                    pkg, alias = '#' + ext[PKG_KEY].replace('$v', ver), '#' + ext['alias']
                    if ext['name'].startswith('babelfish') and ext['name'] != 'babelfishpg_common': continue
                    if ext['name'] == 'babelfishpg_common':
                        pkg, alias = '#wiltondb', '#wiltondb'

                    repo_pkg_nop.append(pkg)
                    ext_list_nop.append(alias)

        repo_entry = (' '.join(list(dict.fromkeys(repo_pkg_add))) + ' ' + ' '.join(list(dict.fromkeys(repo_pkg_nop)))).rstrip('# ')
        ext_entry = (' '.join(list(dict.fromkeys(ext_list_add))) + ' ' + ' '.join(list(dict.fromkeys(ext_list_nop)))).rstrip('# ')
        repo_pkg.append(repo_entry)
        ext_list.append(ext_entry.replace('#babelfishpg_common #babelfishpg_tsql #babelfishpg_tds #babelfishpg_money', '#wiltondb'))

    return repo_pkg, ext_list


# a, b = pg_ext_list("16", "u20" )
# for i in a: print(i)
# for i in b: print(i)


RPM_COMMON_PKG = [
"ansible python3 python3-pip python3-virtualenv python3-requests python3-jmespath python3-cryptography dnf-utils modulemd-tools createrepo_c sshpass             # Distro & Boot",
"nginx dnsmasq etcd haproxy vip-manager pg_exporter pgbackrest_exporter                                                                                          # Pigsty Addons",
"grafana loki logcli promtail prometheus2 alertmanager pushgateway node_exporter blackbox_exporter nginx_exporter keepalived_exporter                            # Infra Packages",
"redis_exporter redis minio mcli ferretdb duckdb docker-ce docker-compose-plugin                                                                                 # Extra Modules",
"lz4 unzip bzip2 zlib yum pv jq git ncdu make patch bash lsof wget uuid tuned nvme-cli numactl grubby sysstat iotop htop rsync tcpdump perf flamegraph chkconfig # Node Packages 1",
"netcat socat ftp lrzsz net-tools ipvsadm bind-utils telnet audit ca-certificates readline vim-minimal keepalived chrony openssl openssh-server openssh-clients  # Node Packages 2",
"patroni patroni-etcd pgbouncer pgbackrest pgbadger pg_activity pg_filedump pgxnclient pgFormatter timescaledb-tools pgcopydb pgloader pg_timetable              # PGDG Common",
]

DEB_COMMON_PKG = [
"ansible python3 python3-pip python3-venv python3-jmespath dpkg-dev sshpass                                                                             # Distro & Boot",
"nginx dnsmasq etcd haproxy vip-manager pg-exporter pgbackrest-exporter                                                                                 # Pigsty Addons",
"grafana loki logcli promtail prometheus2 alertmanager pushgateway node-exporter blackbox-exporter nginx-exporter keepalived-exporter                   # Infra Packages",
"redis-exporter redis minio mcli ferretdb duckdb docker-ce docker-compose-plugin                                                                        # Extra Modules",
"lz4 unzip bzip2 zlib1g pv jq git ncdu make patch bash lsof wget uuid tuned nvme-cli numactl sysstat iotop htop rsync tcpdump acl chrony                # Node Tools 1",
"netcat-openbsd socat lrzsz net-tools ipvsadm dnsutils telnet ca-certificates libreadline-dev vim-tiny keepalived openssl openssh-server openssh-client # Node Tools 2",
"patroni pgbouncer pgbackrest pgbadger pg-activity postgresql-filedump pgxnclient pgformatter timescaledb-tools pgcopydb pgloader pg-timetable          # PGDG Common",
]

DISTRO_ADHOC_PKG = {
    "rpm": [],
    "deb": [],
    "el8": ["%-159s # Extra for el8" %  "python3.12-jmespath" ],
    "el9": [],
    "u24": [ "%-150s # Extra for u24"  % "ftp linux-tools-generic" ],
    "u22": [ "%-150s # Extra for u22"  % "ftp linux-tools-generic" ],
    "u20": [ "%-150s # Extra for u20"  % "ftp linux-tools-generic" ],
    "d12": [ "%-150s # Extra for d12"  % "tnftp linux-perf" ],
    "d11": [ "%-150s # Extra for d11"  % "tnftp linux-perf" ],
}

RPM_REPO = """
    # upstream repo to be downloaded from
    repo_upstream:
      - { name: pigsty-local   ,description: 'Pigsty Local'      ,module: local   ,releases: [7,8,9] ,baseurl: { default: 'http://${admin_ip}/pigsty' } } # used by intranet nodes
      - { name: pigsty-infra   ,description: 'Pigsty INFRA'      ,module: infra   ,releases: [7,8,9] ,baseurl: { default: 'http://10.10.10.1/yum/infra/$basearch' } }
      - { name: pigsty-pgsql   ,description: 'Pigsty PGSQL'      ,module: pgsql   ,releases: [7,8,9] ,baseurl: { default: 'http://10.10.10.1/yum/pgsql/el$releasever.$basearch' } }
      - { name: nginx          ,description: 'Nginx Repo'        ,module: infra   ,releases: [7,8,9] ,baseurl: { default: 'https://nginx.org/packages/centos/$releasever/$basearch/' }}
      - { name: baseos         ,description: 'EL 8+ BaseOS'      ,module: node    ,releases: [  8,9] ,baseurl: { default: 'https://dl.rockylinux.org/pub/rocky/$releasever/BaseOS/$basearch/os/'     ,china: 'https://mirrors.aliyun.com/rockylinux/$releasever/BaseOS/$basearch/os/'          ,europe: 'https://mirrors.xtom.de/rocky/$releasever/BaseOS/$basearch/os/'     }}
      - { name: appstream      ,description: 'EL 8+ AppStream'   ,module: node    ,releases: [  8,9] ,baseurl: { default: 'https://dl.rockylinux.org/pub/rocky/$releasever/AppStream/$basearch/os/'  ,china: 'https://mirrors.aliyun.com/rockylinux/$releasever/AppStream/$basearch/os/'       ,europe: 'https://mirrors.xtom.de/rocky/$releasever/AppStream/$basearch/os/'  }}
      - { name: extras         ,description: 'EL 8+ Extras'      ,module: node    ,releases: [  8,9] ,baseurl: { default: 'https://dl.rockylinux.org/pub/rocky/$releasever/extras/$basearch/os/'     ,china: 'https://mirrors.aliyun.com/rockylinux/$releasever/extras/$basearch/os/'          ,europe: 'https://mirrors.xtom.de/rocky/$releasever/extras/$basearch/os/'     }}
      - { name: powertools     ,description: 'EL 8 PowerTools'   ,module: node    ,releases: [  8  ] ,baseurl: { default: 'https://dl.rockylinux.org/pub/rocky/$releasever/PowerTools/$basearch/os/' ,china: 'https://mirrors.aliyun.com/rockylinux/$releasever/PowerTools/$basearch/os/'      ,europe: 'https://mirrors.xtom.de/rocky/$releasever/PowerTools/$basearch/os/' }}
      - { name: crb            ,description: 'EL 9 CRB'          ,module: node    ,releases: [    9] ,baseurl: { default: 'https://dl.rockylinux.org/pub/rocky/$releasever/CRB/$basearch/os/'        ,china: 'https://mirrors.aliyun.com/rockylinux/$releasever/CRB/$basearch/os/'             ,europe: 'https://mirrors.xtom.de/rocky/$releasever/CRB/$basearch/os/'        }}
      - { name: epel           ,description: 'EL 8+ EPEL'        ,module: node    ,releases: [  8,9] ,baseurl: { default: 'http://download.fedoraproject.org/pub/epel/$releasever/Everything/$basearch/' ,china: 'https://mirrors.tuna.tsinghua.edu.cn/epel/$releasever/Everything/$basearch/' ,europe: 'https://mirrors.xtom.de/epel/$releasever/Everything/$basearch/'     }}
      - { name: pgdg-common    ,description: 'PostgreSQL Common' ,module: pgsql   ,releases: [7,8,9] ,baseurl: { default: 'https://download.postgresql.org/pub/repos/yum/common/redhat/rhel-$releasever-$basearch' ,china: 'https://mirrors.tuna.tsinghua.edu.cn/postgresql/repos/yum/common/redhat/rhel-$releasever-$basearch' , europe: 'https://mirrors.xtom.de/postgresql/repos/yum/common/redhat/rhel-$releasever-$basearch' }}
      - { name: pgdg-extras    ,description: 'PostgreSQL Extra'  ,module: pgsql   ,releases: [7,8,9] ,baseurl: { default: 'https://download.postgresql.org/pub/repos/yum/common/pgdg-rhel$releasever-extras/redhat/rhel-$releasever-$basearch' ,china: 'https://mirrors.tuna.tsinghua.edu.cn/postgresql/repos/yum/common/pgdg-rhel$releasever-extras/redhat/rhel-$releasever-$basearch' , europe: 'https://mirrors.xtom.de/postgresql/repos/yum/common/pgdg-rhel$releasever-extras/redhat/rhel-$releasever-$basearch' }}
      - { name: pgdg-el8fix    ,description: 'PostgreSQL EL8FIX' ,module: pgsql   ,releases: [  8  ] ,baseurl: { default: 'https://download.postgresql.org/pub/repos/yum/common/pgdg-centos8-sysupdates/redhat/rhel-8-x86_64/' ,china: 'https://mirrors.tuna.tsinghua.edu.cn/postgresql/repos/yum/common/pgdg-centos8-sysupdates/redhat/rhel-8-x86_64/' , europe: 'https://mirrors.xtom.de/postgresql/repos/yum/common/pgdg-centos8-sysupdates/redhat/rhel-8-x86_64/' } }
      - { name: pgdg-el9fix    ,description: 'PostgreSQL EL9FIX' ,module: pgsql   ,releases: [    9] ,baseurl: { default: 'https://download.postgresql.org/pub/repos/yum/common/pgdg-rocky9-sysupdates/redhat/rhel-9-x86_64/'  ,china: 'https://mirrors.tuna.tsinghua.edu.cn/postgresql/repos/yum/common/pgdg-rocky9-sysupdates/redhat/rhel-9-x86_64/' , europe: 'https://mirrors.xtom.de/postgresql/repos/yum/common/pgdg-rocky9-sysupdates/redhat/rhel-9-x86_64/' }}
      - { name: pgdg%s         ,description: 'PostgreSQL %s'     ,module: pgsql   ,releases: [  8,9] ,baseurl: { default: 'https://download.postgresql.org/pub/repos/yum/%s/redhat/rhel-$releasever-$basearch' ,china: 'https://mirrors.tuna.tsinghua.edu.cn/postgresql/repos/yum/%s/redhat/rhel-$releasever-$basearch' ,europe: 'https://mirrors.xtom.de/postgresql/repos/yum/%s/redhat/rhel-$releasever-$basearch' }}
      - { name: pgdg%s-nonfree ,description: 'PostgreSQL %s+'    ,module: extra   ,releases: [  8,9] ,baseurl: { default: 'https://download.postgresql.org/pub/repos/yum/non-free/%s/redhat/rhel-$releasever-$basearch' ,china: 'https://mirrors.tuna.tsinghua.edu.cn/postgresql/repos/yum/non-free/%s/redhat/rhel-$releasever-$basearch' ,europe: 'https://mirrors.xtom.de/postgresql/repos/yum/non-free/%s/redhat/rhel-$releasever-$basearch' }}
      - { name: timescaledb    ,description: 'TimescaleDB'       ,module: pgsql   ,releases: [7,8,9] ,baseurl: { default: 'https://packagecloud.io/timescale/timescaledb/el/$releasever/$basearch'  }}
"""

DEB_REPO = """
    # upstream repo to be downloaded from
    repo_upstream:
      - { name: pigsty-local  ,description: 'Pigsty Local'     ,module: local     ,releases: [11,12,20,22,24] ,baseurl: { default: 'http://${admin_ip}/pigsty ./' }}
      - { name: pigsty-pgsql  ,description: 'Pigsty PgSQL'     ,module: pgsql     ,releases: [11,12,20,22,24] ,baseurl: { default: 'https://repo.pigsty.io/apt/pgsql/${distro_codename} ${distro_codename} main', china: 'https://repo.pigsty.cc/apt/pgsql/${distro_codename} ${distro_codename} main' }}
      - { name: pigsty-infra  ,description: 'Pigsty Infra'     ,module: infra     ,releases: [11,12,20,22,24] ,baseurl: { default: 'https://repo.pigsty.io/apt/infra/ generic main' ,china: 'https://repo.pigsty.cc/apt/infra/ generic main' }}
      - { name: nginx         ,description: 'Nginx'            ,module: infra     ,releases: [11,12,20,22,24] ,baseurl: { default: 'http://nginx.org/packages/mainline/${distro_name} ${distro_codename} nginx' }}
      - { name: base          ,description: 'Debian Basic'     ,module: node      ,releases: [11,12         ] ,baseurl: { default: 'http://deb.debian.org/debian/ ${distro_codename} main non-free-firmware'         ,china: 'https://mirrors.aliyun.com/debian/ ${distro_codename} main restricted universe multiverse' }}
      - { name: updates       ,description: 'Debian Updates'   ,module: node      ,releases: [11,12         ] ,baseurl: { default: 'http://deb.debian.org/debian/ ${distro_codename}-updates main non-free-firmware' ,china: 'https://mirrors.aliyun.com/debian/ ${distro_codename}-updates main restricted universe multiverse' }}
      - { name: security      ,description: 'Debian Security'  ,module: node      ,releases: [11,12         ] ,baseurl: { default: 'http://security.debian.org/debian-security ${distro_codename}-security main non-free-firmware' }}
      - { name: base          ,description: 'Ubuntu Basic'     ,module: node      ,releases: [      20,22,24] ,baseurl: { default: 'https://mirrors.edge.kernel.org/${distro_name}/ ${distro_codename}   main universe multiverse restricted' ,china: 'https://mirrors.aliyun.com/${distro_name}/ ${distro_codename}   main restricted universe multiverse' }}
      - { name: updates       ,description: 'Ubuntu Updates'   ,module: node      ,releases: [      20,22,24] ,baseurl: { default: 'https://mirrors.edge.kernel.org/ubuntu/ ${distro_codename}-backports main restricted universe multiverse' ,china: 'https://mirrors.aliyun.com/ubuntu/ ${distro_codename}-updates   main restricted universe multiverse' }}
      - { name: backports     ,description: 'Ubuntu Backports' ,module: node      ,releases: [      20,22,24] ,baseurl: { default: 'https://mirrors.edge.kernel.org/ubuntu/ ${distro_codename}-security  main restricted universe multiverse' ,china: 'https://mirrors.aliyun.com/ubuntu/ ${distro_codename}-backports main restricted universe multiverse' }}
      - { name: security      ,description: 'Ubuntu Security'  ,module: node      ,releases: [      20,22,24] ,baseurl: { default: 'https://mirrors.edge.kernel.org/ubuntu/ ${distro_codename}-updates   main restricted universe multiverse' ,china: 'https://mirrors.aliyun.com/ubuntu/ ${distro_codename}-security  main restricted universe multiverse' }}
      - { name: pgdg          ,description: 'PGDG'             ,module: pgsql     ,releases: [11,12,20,22,24] ,baseurl: { default: 'http://apt.postgresql.org/pub/repos/apt/ ${distro_codename}-pgdg main' ,china: 'https://mirrors.tuna.tsinghua.edu.cn/postgresql/repos/apt/ ${distro_codename}-pgdg main' }}
      - { name: citus         ,description: 'Citus'            ,module: pgsql     ,releases: [11,12,20,22   ] ,baseurl: { default: 'https://packagecloud.io/citusdata/community/${distro_name}/ ${distro_codename} main' } }
      - { name: timescaledb   ,description: 'Timescaledb'      ,module: pgsql     ,releases: [11,12,20,22,24] ,baseurl: { default: 'https://packagecloud.io/timescale/timescaledb/${distro_name}/ ${distro_codename} main' }}
"""

def pkg_ext_with_distro_indent(distro, ver='16', indent=3):
    distro = distro.lower()
    head_pad = '  ' * indent
    text_pad = '  ' * (indent + 1) + '- '
    if distro in ('rpm', 'el7', 'el8', 'el9'):
        os_type = "rpm"
        pg_pkg_str = '%-159s # PostgreSQL %s' % ( 'postgresql%s*'%ver, ver)
    elif distro in ('deb', 'u20', 'u22', 'u24', 'd12', 'd11'):
        os_type = "deb"
        pg_pkg_str = '%-150s # PostgreSQL %s' % ('postgresql-%s postgresql-client-%s postgresql-server-dev-%s postgresql-plpython3-%s postgresql-plperl-%s postgresql-pltcl-%s' % (ver,ver,ver,ver,ver,ver) , ver)
    else:
        raise("invalid distro")

    pkgs, exts = [], []
    pkg_list, ext_list = pkg_ext_list(ver, distro)
    if os_type == "rpm":
        pkg_all_list = [] + RPM_COMMON_PKG + DISTRO_ADHOC_PKG.get(distro, []) + [pg_pkg_str] + pkg_list
    else:
        pkg_all_list = [] + DEB_COMMON_PKG + DISTRO_ADHOC_PKG.get(distro, []) + [pg_pkg_str] + pkg_list

    pkg_str = '\n'.join([text_pad + i for i in pkg_all_list])
    ext_str = '\n'.join([text_pad + i for i in ext_list])

    # add a break between lower_quantile and idkit
    pkg_str = pkg_str.replace('-lower-quantile ', '-lower-quantile\n' + text_pad).replace(' pg_idkit_','\n' + text_pad + 'pg_idkit_')
    ext_str = ext_str.replace('lower_quantile ', 'lower_quantile\n' + text_pad)
    pkgs.append(pkg_str)
    exts.append(ext_str)

    return head_pad + 'repo_packages:\n%s' % pkg_str , head_pad + 'pg_extensions:\n%s' % ext_str


def gen_oss_conf(ver):
    pkg_ext = []
    current_date = datetime.now().strftime("%Y-%m-%d")
    for distro in DISTROS:
        pkg_str, ext_str = pkg_ext_with_distro_indent(distro,ver,4)
        entry = """%s\n%s""" % (pkg_str, ext_str)
        pkg_ext.append(entry)

    args = tuple([ver,ver,current_date,ver,ver,ver,ver,ver,ver,ver,ver,ver,ver,ver] + pkg_ext)
    output_path = os.path.join(CONF_PATH, 'oss-pg%s.yml' % ver)
    OSS_CONF_TMPL = open(os.path.join(STUB_PATH, 'conf/oss.yml')).read()
    with open(output_path, 'w') as dst:
        dst.write(OSS_CONF_TMPL % args)


def gen_distro_conf(ver, distro):
    current_date = datetime.now().strftime("%Y-%m-%d")
    pkg_str, ext_str = pkg_ext_with_distro_indent(distro,ver,0)
    ext_str, pkg_str = '\n'.join(['        #' + i for i in ext_str.split('\n')]), '\n'.join(['    ' + i for i in pkg_str.split('\n')])

    input_path = os.path.join(STUB_PATH, 'conf' ,distro + '.yml')
    TMPL = open(input_path).read()
    if distro in ['el7', 'el8', 'el9', 'rpm', 'el']:
        rpm_repo = RPM_REPO % (ver,ver,ver,ver,ver,ver,ver,ver,ver,ver)
        res = TMPL % (ver, ver, current_date, ext_str, rpm_repo, pkg_str, ver)
    else:
        res = TMPL % (ver, ver, current_date, ext_str, DEB_REPO, pkg_str, ver)
    output_path = os.path.join(CONF_PATH, '%s-pg%s.yml' % (distro, ver))
    with open(output_path, 'w') as dst:
        dst.write(res)

def gen_all():
    for ver in PG_VERS:
        gen_oss_conf(ver)
        for distro in DISTROS:
            gen_distro_conf(ver, distro)

gen_all()
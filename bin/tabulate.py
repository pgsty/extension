#!/usr/bin/env python3

import csv
import os
import json

##################################################
# CONSTANT                                       #
##################################################

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(SCRIPT_DIR, '..', 'data', 'pigsty.csv'))
DOCS_PATH = os.path.abspath(os.path.join(SCRIPT_DIR, '..', 'docs'))


LICENSE_MAP = {
    'PostgreSQL': '**<span class="tcblue">PostgreSQL</span>**',
    'BSD 0-Clause': '**<span class="tcblue">BSD-0</span>**',
    'BSD 2-Clause': '**<span class="tcblue">BSD-2</span>**',
    'BSD 3-Clause': '**<span class="tcblue">BSD-3</span>**',
    'MIT': '**<span class="tcblue">MIT</span>**',
    'ISC': '**<span class="tcblue">ISC</span>**',
    'unrestricted': '**<span class="tcblue">Public</span>**',
    'Artistic': '**<span class="tccyan">Artistic</span>**',
    'Apache-2.0': '**<span class="tccyan">Apache-2</span>**',
    'MPL-2.0': '**<span class="tccyan">MPLv2</span>**',
    'GPL-2.0': '**<span class="tcwarn">GPLv2</span>**',
    'GPL-3.0': '**<span class="tcwarn">GPLv3</span>**',
    'LGPL-2.1': '**<span class="tcwarn">LGPLv2</span>**',
    'LGPL-3.0': '**<span class="tcwarn">LGPLv3</span>**',
    'AGPL-3.0': '**<span class="tcwarn">AGPLv3</span>**',
    'Timescale': '**<span class="tcwarn">Timescale</span>**',
}

REPO_MAP = {
    "PGDG": '**<span class="tccyan">PGDG</span>**',
    "PIGSTY": '**<span class="tcwarn">PIGSTY</span>**',
    "CONTRIB": '**<span class="tcblue">CONTRIB</span>**',
    "WILTON": '**<span class="tcorange">WILTON</span>**',
}

BLUE_CHECK = '<span class="tcblue">✔</span>'
WARN_CROSS = '<span class="tcwarn">✘</span>'
RED_EXCLAM = '<span class="tcred">❗</span>'

PG_VERS = ['17', '16', '15', '14', '13', '12']

NOP_LIST = ['plr', 'pljava','pg_dbms_job', 'pgtap', 'faker', 'dbt2', 'pgpool', 'pgagent', 'pg_mon', 'oracle_fdw', 'db2_fdw', 'repmgr', 'slony', 'babelfishpg_common', 'babelfishpg_tsql', 'babelfishpg_tds', 'babelfishpg_money', '']

CATES = {
    "TIME": "TIME: TimescaleDB, Versioning & Temporal Table, Crontab, Async & Background Job Scheduler, ...",
    "GIS": "GIS: GeoSpatial Data Types, Operators, and Indexes, Hexagonal Indexing, OGR Data FDW, GeoIP & MobilityDB, etc...",
    "RAG": "RAG: Vector Database with IVFFLAT, HNSW, DiskANN Indexes, AI & ML in SQL interface, Similarity Funcs, etc... ",
    "FTS": "FTS: ElasticSearch Alternative with BM25, 2-gram/3-gram Fuzzy Search, Zhparser & Hunspell Segregation Dicts, etc...",
    "OLAP": "OLAP: DuckDB Integration with FDW & PG Lakehouse, Access Parquet from File/S3, Sharding with Citus/Partman/PlProxy, ...",
    "FEAT": "FEAT: OpenCypher with AGE, GraphQL, JsonSchema, Hints & Hypo Index, HLL, Rum, IVM, ChemRDKit, and Message Queues,...",
    "LANG": "LANG: Develop, Test, Package, and Deliver Stored Procedures written in various PL/Lanaguages: Java, Js, Lua, R, Sh, PRQL, ...",
    "TYPE": "TYPE: Dedicate New Data Types Like: prefix, sember, uint, SIUnit, RoaringBitmap, Rational, Sphere, Hash, RRule, and more...",
    "FUNC": "FUNC: Functionality such as sync/async HTTP, GZIP, JWT, SaltedHash, Extra Window Aggs, PCRE, ICU, ID & Rand Generator, etc...",
    "ADMIN": "ADMIN: Utilities for Bloat Control, DirtyRead, BufferInspect, DDL Generate, ChecksumVerify, Permission, Priority, Catalog,...",
    "STAT": "STAT: Observability Catalogs, Monitoring Metrics & Views, Statistics, Query Plans, WaitSampling, SlowLogs, and etc...",
    "SEC": "SEC: Auditing Logs, Enforce Passwords, Keep Secrets, TDE, SM Algorithm, Login Hooks, Log Erros, Extension White List, ...",
    "FDW": "FDW: Wrappers & Multicorn for FDW Development, Access other DBMS: MySQL, Mongo, SQLite, MSSQL, Oracle, HDFS, DB2,...",
    "SIM": "SIM: Protocol Simulation & heterogeneous DBMS Compatibility: Oracle, MSSQL, DB2, MySQL, Memcached, and Babelfish!",
    "ETL": "ETL: Logical Replication, Decoding, CDC in protobuf/JSON/Mongo format, Copy & Load & Compare Postgres Databases,...",
}

COLS = {
    "id":         {'header': 'ID'         ,'center': True,  'func': lambda row: str(row['id'])         },
    "name":       {'header': 'name'       ,'center': True,  'func': lambda row: str(row['name'])       },
    "alias":      {'header': 'alias'      ,'center': True,  'func': lambda row: str(row['alias'])      },
    "category":   {'header': 'category'   ,'center': True,  'func': lambda row: str(row['category'])   },
    "url":        {'header': 'url'        ,'center': True,  'func': lambda row: str(row['url'])        },
    "license":    {'header': 'license'    ,'center': True,  'func': lambda row: str(row['license'])    },
    "tags":       {'header': 'tags'       ,'center': True,  'func': lambda row: str(row['tags'])       },
    "version":    {'header': 'version'    ,'center': True,  'func': lambda row: str(row['version'])    },
    "repo":       {'header': 'repo'       ,'center': True,  'func': lambda row: str(row['repo'])       },
    "lang":       {'header': 'lang'       ,'center': True,  'func': lambda row: str(row['lang'])       },
    "has_solib":  {'header': 'has_solib'  ,'center': True,  'func': lambda row: str(row['has_solib'])  },
    "need_ddl":   {'header': 'need_ddl'   ,'center': True,  'func': lambda row: str(row['need_ddl'])   },
    "need_load":  {'header': 'need_load'  ,'center': True,  'func': lambda row: str(row['need_load'])  },
    "trusted":    {'header': 'trusted'    ,'center': True,  'func': lambda row: str(row['trusted'])    },
    "relocatable":{'header': 'relocatable','center': True,  'func': lambda row: str(row['relocatabl']) },
    "schemas":    {'header': 'schemas'    ,'center': True,  'func': lambda row: str(row['schemas'])    },
    "pg_ver":     {'header': 'pg_ver'     ,'center': True,  'func': lambda row: str(row['pg_ver'])     },
    "requires":   {'header': 'requires'   ,'center': True,  'func': lambda row: str(row['requires'])   },
    "rpm_ver":    {'header': 'rpm_ver'    ,'center': True,  'func': lambda row: str(row['rpm_ver'])    },
    "rpm_repo":   {'header': 'rpm_repo'   ,'center': True,  'func': lambda row: str(row['rpm_repo'])   },
    "rpm_pkg":    {'header': 'rpm_pkg'    ,'center': True,  'func': lambda row: str(row['rpm_pkg'])    },
    "rpm_deps":   {'header': 'rpm_deps'   ,'center': True,  'func': lambda row: str(row['rpm_deps'])   },
    "deb_ver":    {'header': 'deb_ver'    ,'center': True,  'func': lambda row: str(row['deb_ver'])    },
    "deb_repo":   {'header': 'deb_repo'   ,'center': True,  'func': lambda row: str(row['deb_repo'])   },
    "deb_pkg":    {'header': 'deb_pkg'    ,'center': True,  'func': lambda row: str(row['deb_pkg'])    },
    "deb_deps":   {'header': 'deb_deps'   ,'center': True,  'func': lambda row: str(row['deb_deps'])   },
    "en_desc":    {'header': 'Description','center': False, 'func': lambda row: str(row['en_desc'])    },
    "zh_desc":    {'header': '说明'        ,'center': False, 'func': lambda row: str(row['zh_desc'])    },
    "comment":    {'header': 'Comment'    ,'center': True,  'func': lambda row: str(row['comment'])    },

    "ext":        {'header': 'Extension'  ,'center': False, 'func': lambda row: "[%s](%s)" % (row["name"], row["url"])  },
    "ext2":       {'header': 'Extension'  ,'center': False, 'func': lambda row: row["name"] },
    "ext3":       {'header': 'Extension'  ,'center': False, 'func': lambda row: "[%s](/%s)" % (row["name"], row['name'])  },
    "link":       {'header': 'Website'    ,'center': True,  'func': lambda row: "[LINK](%s)" % row["url"]  },
    "pkg":        {'header': 'Package'    ,'center': False, 'func': lambda row: "[%s](/%s)" % (row['alias'], row['name'])  },
    "pkg2":       {'header': 'Package'    ,'center': False, 'func': lambda row: "[%s](/%s)" % (row['alias'], row['url'])  },
    "ver":        {'header': 'Version'    ,"center": True,  "func": lambda row: row['version'] },
    "rpmver":     {'header': 'Version'    ,"center": False, "func": lambda row: row['rpm_ver'] },
    "debver":     {'header': 'Version'    ,"center": False, "func": lambda row: row['deb_ver'] },
    "cat":        {'header': 'Category'   ,"center": True,  "func": lambda row: "[%s](/%s)" % (row['category'], row['category'].lower()) },
    "lic":        {'header': 'License'    ,"center": True,  "func": lambda row: LICENSE_MAP.get(row['license'], row['license']) },
    "rpmrepo":    {'header': 'RPM'        ,"center": True,  "func": lambda row: REPO_MAP.get(row['rpm_repo'], row['rpm_repo']) },
    "rpmrepo2":   {'header': 'REPO'       ,"center": True,  "func": lambda row: REPO_MAP.get(row['rpm_repo'], row['rpm_repo']) },
    "debrepo":    {'header': 'DEB'        ,"center": True,  "func": lambda row: REPO_MAP.get(row['deb_repo'], row['rpm_repo']) },
    "rpmpkg":     {'header': 'RPM Package',"center": False, "func": lambda row: '`%s`' % row['rpm_pkg'] },
    "debpkg":     {'header': 'DEB Package',"center": False, "func": lambda row: '`%s`' % row['deb_pkg'] },
    "r17":        {'header': '17'         ,"center": True,  "func": lambda row: BLUE_CHECK if '17' in row['rpm_pg'] else '' },
    "r16":        {'header': '16'         ,"center": True,  "func": lambda row: BLUE_CHECK if '16' in row['rpm_pg'] else '' },
    "r15":        {'header': '15'         ,"center": True,  "func": lambda row: BLUE_CHECK if '15' in row['rpm_pg'] else '' },
    "r14":        {'header': '14'         ,"center": True,  "func": lambda row: BLUE_CHECK if '14' in row['rpm_pg'] else '' },
    "r13":        {'header': '13'         ,"center": True,  "func": lambda row: BLUE_CHECK if '13' in row['rpm_pg'] else '' },
    "r12":        {'header': '12'         ,"center": True,  "func": lambda row: BLUE_CHECK if '12' in row['rpm_pg'] else '' },
    "d17":        {'header': '17'         ,"center": True,  "func": lambda row: BLUE_CHECK if '17' in row['deb_pg'] else '' },
    "d16":        {'header': '16'         ,"center": True,  "func": lambda row: BLUE_CHECK if '16' in row['deb_pg'] else '' },
    "d15":        {'header': '15'         ,"center": True,  "func": lambda row: BLUE_CHECK if '15' in row['deb_pg'] else '' },
    "d14":        {'header': '14'         ,"center": True,  "func": lambda row: BLUE_CHECK if '14' in row['deb_pg'] else '' },
    "d13":        {'header': '13'         ,"center": True,  "func": lambda row: BLUE_CHECK if '13' in row['deb_pg'] else '' },
    "d12":        {'header': '12'         ,"center": True,  "func": lambda row: BLUE_CHECK if '12' in row['deb_pg'] else '' },
    "load":       {'header': '`LOAD`'     ,"center": True,  "func": lambda row: '' if row['need_load'] is None else (RED_EXCLAM if row['need_load'] else '' ) },
    "ddl":        {'header': '`DDL`'      ,"center": True,  "func": lambda row: '' if row['need_ddl' ] is None else (BLUE_CHECK if row['need_ddl' ] else WARN_CROSS) },
    "trust":      {'header': '`TRUST`'    ,"center": True,  "func": lambda row: '' if row['trusted'  ] is None else (BLUE_CHECK if row['trusted'  ] else WARN_CROSS) },
    "reloc":      {'header': '`RELOC`'    ,"center": True,  "func": lambda row: '' if row['relocatable'] is None else (BLUE_CHECK if row['relocatable'] else WARN_CROSS) },
    "dylib":      {'header': '`DYLIB`'    ,"center": True,  "func": lambda row: '' if row['has_solib'  ] is None else (BLUE_CHECK if row['has_solib'  ] else WARN_CROSS) },
    "distro":     {'header': 'OS'         ,"center": True,  "func": lambda row: 'Distro-' + row['name'] },
    "req":        {'header': 'Requires'   ,'center': False, 'func': lambda row: ', '.join([ '[`%s`](%s)'%(e,e) for e in row['requires'] ])  },
    "tag":        {'header': 'Tags'       ,'center': False, 'func': lambda row: ', '.join([ '`%s`'%e for e in row['tags'] ])  },
    "schema":     {'header': 'Schemas'    ,'center': False, 'func': lambda row: ', '.join([ '`%s`'%e for e in row['schemas'] ])  },
    "rpmdep":     {'header': 'Dependency' ,'center': False, 'func': lambda row: ', '.join([ '`%s`'%e for e in row['rpm_deps'] ])  },
    "debdep":     {'header': 'Dependency' ,'center': False, 'func': lambda row: ', '.join([ '`%s`'%e for e in row['deb_deps'] ])  },
}

# generate column descriptor list
def Columns(columns):
    return [COLS.get(i) for i in columns]

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
            row['rpm_misc'] = True if row['has_rpm'] and (row['rpm_repo'] not in ('PGDG', 'PIGSTY', 'CONTRIB', '')) else False

            row['deb_pgdg'] = True if row['has_deb'] and row['deb_repo'] == 'PGDG' else False
            row['deb_pigsty'] = True if row['has_deb'] and row['deb_repo'] == 'PIGSTY' else False
            row['deb_misc'] = True if row['has_deb'] and (row['deb_repo'] != 'PGDG' and row['deb_repo'] != 'PIGSTY' and row['deb_repo'] != '') else False
            data.append(row)
    return data



def stat_data(data):
    res = {"stat": {}, "rpm_ext": {}, "deb_ext": {}, "rpm_pkg": {}, "deb_pkg": {}}
    res["stat"]["all"] = len([i for i in data ])
    res["stat"]["rpm"] = len([i for i in data if i['has_rpm'] ])
    res["stat"]["deb"] = len([i for i in data if i['has_deb'] ])
    res["stat"]["both"] = len([i for i in data if i['has_rpm'] and i['has_deb'] ])
    res["stat"]["contrib"] = len([i for i in data if i['repo'] == 'CONTRIB'])
    res["stat"]["non-contrib"] =  len([i for i in data ]) - len([i for i in data if i['contrib']])

    res["rpm_ext"]["all"] = len([i for i in data if i['has_rpm']])
    res["rpm_pkg"]["all"] = len(set([i['alias'] for i in data if i['has_rpm']]))
    res["deb_ext"]["all"] = len([i for i in data if i['has_deb']])
    res["deb_pkg"]["all"] = len(set([i['alias'] for i in data if i['has_deb']]))

    res["rpm_ext"]["pgdg"]   = len([i['name'] for i in data if i['has_rpm'] and i['rpm_pgdg'] ])
    res["rpm_ext"]["pigsty"] = len([i['name'] for i in data if i['has_rpm'] and i['rpm_pigsty']])
    res["rpm_ext"]["misc"]   = len([i['name'] for i in data if i['has_rpm'] and i['rpm_misc']])
    res["rpm_ext"]["miss"]   = len([i['name'] for i in data if not i['has_rpm']])
    res["rpm_ext"]["pg12"]   = len([i['name'] for i in data if i['has_rpm'] and '12' in i['rpm_pg'] ])
    res["rpm_ext"]["pg13"]   = len([i['name'] for i in data if i['has_rpm'] and '13' in i['rpm_pg'] ])
    res["rpm_ext"]["pg14"]   = len([i['name'] for i in data if i['has_rpm'] and '14' in i['rpm_pg'] ])
    res["rpm_ext"]["pg15"]   = len([i['name'] for i in data if i['has_rpm'] and '15' in i['rpm_pg'] ])
    res["rpm_ext"]["pg16"]   = len([i['name'] for i in data if i['has_rpm'] and '16' in i['rpm_pg'] ])
    res["rpm_ext"]["pg17"]   = len([i['name'] for i in data if i['has_rpm'] and '17' in i['rpm_pg'] ])

    res["rpm_pkg"]["pgdg"]   = len(set([i['alias'] for i in data if i['has_rpm'] and i['rpm_pgdg'] ]))
    res["rpm_pkg"]["pigsty"] = len(set([i['alias'] for i in data if i['has_rpm'] and i['rpm_pigsty']]))
    res["rpm_pkg"]["misc"]   = len(set([i['alias'] for i in data if i['has_rpm'] and i['rpm_misc']]))
    res["rpm_pkg"]["miss"]   = len(set([i['alias'] for i in data if not i['has_rpm']]))
    res["rpm_pkg"]["pg12"]   = len(set([i['alias'] for i in data if i['has_rpm'] and '12' in i['rpm_pg']]))
    res["rpm_pkg"]["pg13"]   = len(set([i['alias'] for i in data if i['has_rpm'] and '13' in i['rpm_pg']]))
    res["rpm_pkg"]["pg14"]   = len(set([i['alias'] for i in data if i['has_rpm'] and '14' in i['rpm_pg']]))
    res["rpm_pkg"]["pg15"]   = len(set([i['alias'] for i in data if i['has_rpm'] and '15' in i['rpm_pg']]))
    res["rpm_pkg"]["pg16"]   = len(set([i['alias'] for i in data if i['has_rpm'] and '16' in i['rpm_pg']]))
    res["rpm_pkg"]["pg17"]   = len(set([i['alias'] for i in data if i['has_rpm'] and '17' in i['rpm_pg']]))

    res["deb_ext"]["pgdg"]   = len([i['name'] for i in data if i['has_deb'] and i['deb_pgdg'] ])
    res["deb_ext"]["pigsty"] = len([i['name'] for i in data if i['has_deb'] and i['deb_pigsty']])
    res["deb_ext"]["misc"]   = len([i['name'] for i in data if i['has_deb'] and i['deb_misc']])
    res["deb_ext"]["miss"]   = len([i['name'] for i in data if not i['has_deb']])
    res["deb_ext"]["pg12"]   = len([i['name'] for i in data if i['has_deb'] and '12' in i['deb_pg']])
    res["deb_ext"]["pg13"]   = len([i['name'] for i in data if i['has_deb'] and '13' in i['deb_pg']])
    res["deb_ext"]["pg14"]   = len([i['name'] for i in data if i['has_deb'] and '14' in i['deb_pg']])
    res["deb_ext"]["pg15"]   = len([i['name'] for i in data if i['has_deb'] and '15' in i['deb_pg']])
    res["deb_ext"]["pg16"]   = len([i['name'] for i in data if i['has_deb'] and '16' in i['deb_pg']])
    res["deb_ext"]["pg17"]   = len([i['name'] for i in data if i['has_deb'] and '17' in i['deb_pg']])

    res["deb_pkg"]["pgdg"]   = len(set([i['alias'] for i in data if i['has_deb'] and i['deb_pgdg'] ]))
    res["deb_pkg"]["pigsty"] = len(set([i['alias'] for i in data if i['has_deb'] and i['deb_pigsty']]))
    res["deb_pkg"]["misc"]   = len(set([i['alias'] for i in data if i['has_deb'] and i['deb_misc']]))
    res["deb_pkg"]["miss"]   = len(set([i['alias'] for i in data if not i['has_deb']]))
    res["deb_pkg"]["pg12"]   = len(set([i['alias'] for i in data if i['has_deb'] and '12' in i['deb_pg'] ]))
    res["deb_pkg"]["pg13"]   = len(set([i['alias'] for i in data if i['has_deb'] and '13' in i['deb_pg'] ]))
    res["deb_pkg"]["pg14"]   = len(set([i['alias'] for i in data if i['has_deb'] and '14' in i['deb_pg'] ]))
    res["deb_pkg"]["pg15"]   = len(set([i['alias'] for i in data if i['has_deb'] and '15' in i['deb_pg'] ]))
    res["deb_pkg"]["pg16"]   = len(set([i['alias'] for i in data if i['has_deb'] and '16' in i['deb_pg'] ]))
    res["deb_pkg"]["pg17"]   = len(set([i['alias'] for i in data if i['has_deb'] and '17' in i['deb_pg'] ]))

    return res


DATA = load_data()
STAT = stat_data(DATA)
CATE = list(dict.fromkeys([i['category'] for i in DATA]))


def tabulate_stats(todolist):
    entries = {
        'rpm_ext': 'RPM Extension',
        'deb_ext': 'DEB Extension',
        'rpm_pkg': 'RPM Package',
        'deb_pkg': 'DEB Package'
    }
    filters = ['all', 'pgdg', 'pigsty', 'misc', 'miss', 'pg17', 'pg16', 'pg15', 'pg14', 'pg13', 'pg12']
    headers = ['Entry / Filter', 'All', 'PGDG', 'PIGSTY', 'MISC', 'MISS', 'PG17', 'PG16', 'PG15', 'PG14', 'PG13', 'PG12']
    markdown = '|' + ' | '.join(headers) + '|\n'
    markdown += '|' + '|'.join([':----:' for _ in headers]) + '|\n'
    for key in todolist:
        row = [entries[key]]
        for filt in filters:
            value = STAT.get(key, {}).get(filt, '')
            row.append(str(value))
        markdown += '| ' + ' | '.join(row) + ' |\n'
    return markdown



PGVER_TEMPLATE = """
----------\n
## PostgreSQL %s\n\n
```yaml
pg_version: %s
pg_extensions:
  - postgresql%s*
%s\n
repo_packages:
%s\n
```
"""

def pg_ext_list(ver, distro, category=None):
    REPO_KEY, HAS_KEY, PG_VER_KEY, PKG_KEY = '', '', '', ''
    pg_pkg_str = ''
    filter = lambda row: True
    if distro.lower() in ('el', 'rpm', 'el7', 'el8', 'el9'):
        REPO_KEY, HAS_KEY, PG_VER_KEY, PKG_KEY = 'rpm_repo', 'has_rpm', 'rpm_pg', 'rpm_pkg'
        pg_pkg_str = '  - postgresql%s*\n' % ver
        filter = lambda ext: ext[HAS_KEY] and ver in ext[PG_VER_KEY] and ext['alias'] not in NOP_LIST
    elif distro.lower() in ('deb', 'u20', 'u22', 'u24', 'd12', 'd11'):
        REPO_KEY, HAS_KEY, PG_VER_KEY, PKG_KEY = 'deb_repo', 'has_deb', 'deb_pg', 'deb_pkg'
        pg_pkg_str = '  - postgresql-%s postgresql-client-%s postgresql-server-dev-%s postgresql-plpython3-%s postgresql-plperl-%s postgresql-pltcl-%s\n' % (ver,ver,ver,ver,ver,ver)
        filter = lambda ext: ext[HAS_KEY] and ver in ext[PG_VER_KEY] and ext['alias'] not in NOP_LIST
    elif distro.lower() in ('both'):
        REPO_KEY, HAS_KEY, PG_VER_KEY, PKG_KEY = 'rpm_repo', 'has_rpm', 'rpm_pg', 'rpm_pkg'
        filter = lambda ext: ext["has_deb"] and ext["has_rpm"] and ver in ext["rpm_pg"] and ver in ext["deb_pg"] and ext['alias'] not in NOP_LIST
    else:
        raise("invalid distro")

    repo_pkg, ext_list = [], []
    for cate in CATE:
        if category is not None and cate != category: continue
        repo_pkg_add, repo_pkg_nop, ext_list_add, ext_list_nop = [], [] ,[], []
        for ext in DATA:
            #if not ext[REPO_KEY]: continue
            if ext['repo'] == 'CONTRIB': continue
            if ext['category'] == cate:
                if filter(ext):
                    repo_pkg_add.append(ext[PKG_KEY].replace('$v', ver))
                    ext_list_add.append(ext['alias'])
                else:
                    repo_pkg_nop.append('#' + ext[PKG_KEY].replace('$v', ver))
                    ext_list_nop.append('#' + ext['alias'])

        repo_pkg.append(' '.join(list(dict.fromkeys(repo_pkg_add))) + ' ' + ' '.join(list(dict.fromkeys(repo_pkg_nop))))
        ext_list.append(' '.join(list(dict.fromkeys(ext_list_add))) + ' ' + ' '.join(list(dict.fromkeys(ext_list_nop))))

    if not category:
        repo_pkg_str = 'repo_packages:\n' + pg_pkg_str + '\n'.join([ '  - ' + i for i in repo_pkg ])
        ext_list_str = 'pg_extensions:\n' + '\n'.join([ '  - ' + i for i in ext_list ])
        return repo_pkg_str, ext_list_str
    else:
        return ' '.join(repo_pkg), ' '.join(ext_list)





LIST_TEMPLATE = """# Extension List\n
There are **%d** available extensions, including **%d** [**RPM**](/rpm) extensions available in EL, and **%d** [**DEB**](/deb) available in Debian/Ubuntu.\n
There are **%d** [**Contrib**](contrib) extensions provided by PostgreSQL and **%d** additional third-party extensions provide by PGDG & Pigsty. \n\n
%s\n\n
--------\n
## Inventory\n\n
> Click the "**Extension**" name will goes to the extension source homepage, click the "**Package**" goes to the metadata page.\n\n  
%s\n\n
> The CSV Raw data is available at [github.com/pgsty/extension](https://github.com/pgsty/extension/blob/main/data/pigsty.csv)\n\n
%s\n\n
"""



def generate_all_list():
    ext_table = tabulate(
        Columns(["cat", "id", "ext3", "ver", "pkg", "lic", "rpmrepo", "debrepo", "link", "load", "dylib", "ddl", "en_desc"]),
        lambda row: True
    )
    ver_sections = []
    for ver in PG_VERS:
        repo_str, ext_str = pg_ext_list(ver, 'both')
        ver_sections.append("""--------\n\n## PostgreSQL %s\n\n>Extensions that both available on PG%s as [RPM](/rpm#postgresql-%s) and [DEB](/deb#postgresql-%s) are shown below:\n\n\n```yaml\npg_version: %s\n%s\n```\n"""% (ver, ver, ver, ver, ver, ext_str))

    f = openw('list.md')
    f.write(LIST_TEMPLATE % (
        STAT["stat"]["all"],STAT["stat"]["rpm"],STAT["stat"]["deb"],
        STAT["stat"]["contrib"],STAT["stat"]["non-contrib"],
        tabulate_stats(['rpm_ext', 'deb_ext']),
        ext_table,
        '\n'.join(ver_sections)
    ))
    f.close()




RPM_TEMPLATE = """# RPM Extension Packages\n
There are **%d** extensions available on EL compatible systems, **%s** of them are EL exclusive, and missing **%s** Debian exclusive extensions.\n
There are **%d** built-in [**contrib**](contrib) extensions, in addition to **%d** rpm extensions provided by PGDG YUM repository, and **%d** extensions provided by Pigsty.\n
There are **%d** extensions available in the current major version PostgreSQL 16, and **%d** ready for the latest PostgreSQL 17.\n

%s\n\n
--------\n
## Inventory\n\n
> Click the "**Extension**" name will goes to the extension source homepage, click the "**Package**" goes to the metadata page.\n\n
%s\n\n
%s\n\n
"""


def generate_rpm_list():
    rpm_table = tabulate(
        Columns([ "cat", "pkg","rpmver", "lic", "rpmrepo", "rpmpkg", "r17", "r16", "r15", "r14", "r13", "r12", "en_desc"]),
        lambda row: row['has_rpm'] and row['repo'] != 'CONTRIB' and row['lead']
    )
    ver_sections = []
    for ver in PG_VERS:
        repo_str, ext_str = pg_ext_list(ver, 'rpm')
        ver_sections.append("""--------\n\n## PostgreSQL %s\n\n```yaml\npg_version: %s\n%s\n\n%s\n```\n"""% (ver, ver, repo_str, ext_str))
    f = openw('rpm.md')
    f.write(RPM_TEMPLATE % (
        STAT["rpm_ext"]["all"],STAT["rpm_ext"]["miss"],STAT["rpm_ext"]["miss"],
        STAT["stat"]["contrib"],STAT["rpm_ext"]["pgdg"], STAT["rpm_ext"]["pigsty"],
        STAT["rpm_ext"]["pg16"], STAT["rpm_ext"]["pg17"],
        tabulate_stats(['rpm_ext', 'rpm_pkg']),
        rpm_table,
        '\n'.join(ver_sections)
    ))
    f.close()




DEB_TEMPLATE = """# DEB Extension Packages\n
There are **%d** extensions available on Debian/Ubuntu compatible systems, **%s** of them are Debian exclusive, and missing **%s** EL exclusive extensions.\n
There are **%d** built-in [**contrib**](contrib) extensions, in addition to **%d** deb extensions provided by PGDG YUM repository, and **%d** extensions provided by Pigsty.\n
There are **%d** extensions available in the current major version PostgreSQL 16, and **%d** ready for the latest PostgreSQL 17.\n

%s\n\n
--------\n
## Inventory\n\n
> Click the "**Extension**" name will goes to the extension source homepage, click the "**Package**" goes to the metadata page.\n\n
%s\n\n
%s\n\n
"""


def generate_deb_list():
    deb_table = tabulate(
        Columns(["cat", "pkg", "debver", "lic", "debrepo", "debpkg", "d17", "d16", "d15", "d14", "d13", "d12", "en_desc"]),
        lambda row: row['has_deb'] and row['repo'] != 'CONTRIB' and row['lead']
    )
    ver_sections = []
    for ver in PG_VERS:
        repo_str, ext_str = pg_ext_list(ver, 'deb')
        ver_sections.append("""--------\n\n## PostgreSQL %s\n\n```yaml\npg_version: %s\n%s\n\n%s\n```\n"""% (ver, ver, repo_str, ext_str))
    f = openw('deb.md')
    f.write(DEB_TEMPLATE % (
        STAT["deb_ext"]["all"],STAT["deb_ext"]["miss"],STAT["deb_ext"]["miss"],
        STAT["stat"]["contrib"],STAT["deb_ext"]["pgdg"], STAT["deb_ext"]["pigsty"],
        STAT["deb_ext"]["pg16"], STAT["deb_ext"]["pg17"],
        tabulate_stats(['deb_ext', 'deb_pkg']),
        deb_table,
        '\n'.join(ver_sections)
    ))
    f.close()


CONTRIB_TEMPLATE = """# Contrib Extension Packages\n
There are **%d** built-in [**contrib**](contrib) extensions which are shipping alone with PostgreSQL.\n
## Inventory\n\n%s
"""

def generate_contrib_list():
    contrib_table = tabulate(
        Columns(["cat", "id", "ext2", "ver", "pkg", "r17", "r16", "r15", "r14", "r13", "r12", "load", "dylib", "ddl","trust", "reloc", "en_desc"]),
        lambda row: row['repo'] == 'CONTRIB'
    )
    f = openw('contrib.md')
    f.write(CONTRIB_TEMPLATE % (STAT["stat"]["contrib"], contrib_table))
    f.close()


CATEGORY_INDEX_TEMPLATE = """# %s\n\n
> %s
## Extensions\n\n
There are %d available extensions in this category\n\n
%s\n\n%s\n\n
--------\n
## RPM Packages\n\n
%s\n\n%s\n\n
--------\n
## DEB Packages\n\n
%s\n\n%s\n\n
"""


def generate_category():
    for cate in CATE:
        extensions = [row for row in DATA if row['category'] == cate]
        cate_dir = os.path.join(DOCS_PATH, cate.lower())
        cate_index = os.path.join(DOCS_PATH, cate.lower() + '.md')
        if not os.path.exists(cate_dir): os.mkdir(cate_dir)

        ext_table = tabulate(
            Columns(["id", "ext3", "ver", "pkg", "lic", "rpmrepo", "debrepo", "link", "load", "dylib", "ddl", "en_desc"]),
            lambda row: row['category'] == cate
        )
        rpm_table = tabulate(
            Columns(["pkg", "rpmver", "lic", "rpmrepo", "rpmpkg", "r17", "r16", "r15", "r14", "r13", "r12", "en_desc"]),
            lambda row: row['has_rpm'] and row['lead'] and row['category'] == cate
        )
        deb_table = tabulate(
            Columns(["pkg", "debver", "lic", "debrepo", "debpkg", "d17", "d16", "d15", "d14", "d13", "d12", "en_desc"]),
            lambda row: row['has_deb'] and row['lead'] and row['category'] == cate
        )
        ext_list, rpm_list, deb_list  = [], [], []
        for ver in PG_VERS:
            _, ext_str = pg_ext_list(ver, 'both', cate)
            rpm_repo_str, rpm_ext_str = pg_ext_list(ver, 'rpm', cate)
            deb_repo_str, deb_ext_str = pg_ext_list(ver, 'rpm', cate)
            ext_list.append('pg%s: %s'% (ver, ext_str))
            rpm_list.append('pg%s: %s'% (ver, rpm_repo_str))
            deb_list.append('pg%s: %s'% (ver, deb_repo_str))
        with open(cate_index, 'w') as f:
            f.write(CATEGORY_INDEX_TEMPLATE%(
                cate,CATES.get(cate,''),
                len(extensions),
                ext_table, """\n```yaml\n%s\n```\n"""% ('\n'.join(ext_list)),
                rpm_table, """\n```yaml\n%s\n```\n"""% ('\n'.join(rpm_list)),
                deb_table, """\n```yaml\n%s\n```\n"""% ('\n'.join(deb_list)),
            )
        )





EXTENSION_TEMPLATE = """# %s\n\n\n> %s: %s\n\n\n-------\n
## Extension\n\n
%s\n\n%s\n%s\n%s\n
-----------\n\n
## Packages\n\n
%s\n\n%s
-----------\n\n
## Category: %s\n\n
%s\n\n
"""

def getcol(col, ext):
    return COLS[col]['func'](ext)

def generate_extension():

    for ext in DATA:
        name, alias, category = ext['name'], ext['alias'], ext['category']
        ext_path = os.path.join(DOCS_PATH, name + '.md')

        # part 1: extension table
        ext_table = tabulate(
            Columns(["id", "ext", "ver", "lic", "rpmrepo", "debrepo", "load", "dylib", "ddl", "trust", "reloc", "req"]),
            lambda row: row['name'] == name
        )
        comment = ''
        if ext['comment']: comment = '> **Comment**: ' + ext['comment']
        create_ddl = ''
        if ext['need_ddl']: create_ddl = """\n```sql\nCREATE EXTENSION %s%s;\n```\n""" % ('"' + name + '"' if '-' in name else name , 'CASCADE' if ext['requires'] else '')
        config_ini= ''
        if ext['need_load']: config_ini = """\n```bash\nshared_preload_libraries = '%s'; # add this extension to postgresql.conf\n```\n""" % name


        # part 2: package table
        rpm_table = tabulate(
            Columns(["distro", "rpmver", "lic", "rpmrepo", "rpmpkg", "r17", "r16", "r15", "r14", "r13", "r12", "rpmdep"]),
            lambda row: row['has_rpm'] and row['lead'] and row['alias'] == alias
        )
        deb_table = tabulate(
            Columns(["distro", "debver", "lic", "debrepo", "debpkg", "r17", "r16", "r15", "r14", "r13", "r12", "debdep"]),
            lambda row: row['has_deb'] and row['lead'] and row['alias'] == alias
        )
        rpm_table = rpm_table.replace('Distro-'+name, '[RPM](/rpm)')
        deb_table = '\n'.join(deb_table.replace('Distro-'+name, '[DEB](/deb)').split('\n')[2:])
        pkg_table = rpm_table + deb_table

        # install info
        yum_install_preface = '\nInstall `%s` [RPM](/rpm) from the %s **YUM** repo:\n\n' % (getcol("alias", ext), getcol("rpmrepo", ext))
        yum_install_tmpl = """```bash\n%s\n```\n\n""" % '\n'.join([ 'dnf install ' + ext['rpm_pkg'].replace('$v', ver) + ';' for ver in ext['rpm_pg'] ])
        apt_install_preface = '\nInstall `%s` [DEB](/deb) from the %s **APT** repo:\n\n' % (getcol("alias", ext), getcol("rpmrepo", ext))
        apt_install_tmpl = """```bash\n%s\n```\n\n""" % '\n'.join([ 'apt install ' + ext['deb_pkg'].replace('$v', ver) + ';' for ver in ext['deb_pg'] ])
        install_tmpl = ''
        if ext['has_rpm']: install_tmpl = install_tmpl + yum_install_preface + yum_install_tmpl
        if ext['has_deb']: install_tmpl = install_tmpl + apt_install_preface + apt_install_tmpl

        sib_table = tabulate(
            Columns(["id", "ext3", "ver", "pkg", "lic", "rpmrepo", "debrepo", "lang", "tag", "schema", "req", "load", "dylib", "ddl", "trust", "reloc"]),
            lambda row: row['category'] == category
        )

        content = EXTENSION_TEMPLATE % (
            ext['alias'], getcol('pkg2', ext ) , ext['en_desc'],
            ext_table, comment, config_ini, create_ddl,
            pkg_table, install_tmpl,
            category, sib_table
        )
        with open(ext_path, 'w') as f:
            f.write(content)


generate_all_list()
generate_rpm_list()
generate_deb_list()
generate_contrib_list()
generate_category()
generate_extension()
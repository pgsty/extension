
--------

## Usage

Install `go-sqlcmd`:

```bash
curl -LO https://github.com/microsoft/go-sqlcmd/releases/download/v1.4.0/sqlcmd-v1.4.0-linux-amd64.tar.bz2
tar xjvf sqlcmd-v1.4.0-linux-amd64.tar.bz2
sudo mv sqlcmd* /usr/bin/
```

Try go-sqlcmd

```bash
$ sqlcmd -S 10.10.10.10,1433 -U dbuser_mssql -P DBUser.MSSQL
1> select @@version
2> go
version                                                                                                                                                                                                                                                         
-----------------------------
Babelfish for PostgreSQL with SQL Server Compatibility - 12.0.2000.8
Oct 22 2023 17:48:32
Copyright (c) Amazon Web Services
PostgreSQL 15.4 (EL 1:15.4.wiltondb3.3_2-2.el8) on x86_64-redhat-linux-gnu (Babelfish 3.3.0)                                        

(1 row affected)
```

Access pigsty exposed primary/replica service port

```bash 
sqlcmd -S 10.10.10.11,5433 -U dbuser_mssql -P DBUser.MSSQL

sqlcmd -S 10.10.10.11,5434 -U dbuser_mssql -P DBUser.MSSQL
```
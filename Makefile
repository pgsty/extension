#==============================================================#
# File      :   Makefile
# Ctime     :   2024-10-30
# Desc      :   Makefile shortcuts
# Path      :   Makefile
# Copyright (C) 2019-2020 Ruohang Feng
#==============================================================#

default: run

PGURL="postgres:///vonng"

# run http server to serve the docs
run:
	docs/run

# update docs from the data/pigsty.csv
gen:
	bin/tabulate.py

all: dump gen run

dump: save
save-save: save-data save-mini save-cate
save-data:
	psql $(PGURL) -c "COPY (SELECT * FROM ext.pigsty ORDER BY id) TO '/Users/vonng/pgsty/extension/data/pigsty.csv' CSV HEADER;"
save-mini:
	psql $(PGURL) -c "COPY (select id,name,alias,category,lead,rpm_repo,rpm_pkg,rpm_pg,deb_repo,deb_pkg,deb_pg FROM ext.pigsty ORDER BY id) TO '/Users/vonng/pgsty/extension/data/extension.csv' CSV HEADER;"
save-cate:
	psql $(PGURL) -c "COPY (select * FROM ext.category ORDER BY id) TO '/Users/vonng/pgsty/extension/data/category.csv' CSV HEADER;"

load:
	psql $(PGURL) -c "TRUNCATE ext.pigsty; COPY ext.pigsty FROM '/Users/vonng/pgsty/extension/data/pigsty.csv' CSV HEADER;"


.PHONY: default run gen dump save load
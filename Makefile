#==============================================================#
# File      :   Makefile
# Ctime     :   2024-10-29
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

save:
	psql $(PGURL) -c "COPY (SELECT * FROM ext.pigsty ORDER BY id) TO '/Users/vonng/pgsty/extension/data/pigsty.csv' CSV HEADER;"

load:
	psql $(PGURL) -c "TRUNCATE ext.pigsty; COPY ext.pigsty FROM '/Users/vonng/pgsty/extension/data/pigsty.csv' CSV HEADER;"


.PHONY: default doc
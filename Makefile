# Snapshoter
# Lets you take a snapshot of a file on HTTPS for datamining
# Github: https://www.github.com/0x4248/snapshoter
# Licence: GNU General Public License v3.0
# By: 0x4248

PYTHON=python3
SRC=src/snapshot.py

all: run

run: 
	$(PYTHON) $(SRC)
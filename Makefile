.PHONY: run

USR     ?= 1
CSVFILE  := data.csv

run: 
	python3 recommend.py --file $(CSVFILE) --user $(USR)



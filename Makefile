.PHONY: run

USR       ?= 1
CSVFILE   := data/data.csv
DAYFILE   := data/context_day.csv
PLACEFILE := data/context_place.csv
OUTFILE   := User_$(USR).json

run:
	python3 recommend.py --data-file $(CSVFILE) \
			     --day-file $(DAYFILE) \
			     --place-file $(PLACEFILE) \
			     --user $(USR) > $(OUTFILE)

sparql:
	python3 sparql.py

clean:
	find . -name '*~' -exec rm -rf \{\} \+
	find . -name '__pycache__' -exec rm -rf \{\} \+

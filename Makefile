.PHONY: run

USR      ?= 1
CSVFILE   := data.csv
DAYFILE   := context_day.csv
PLACEFILE := context_place.csv
OUTFILE   := User_$(USR).json

run:
	python3 recommend.py --data-file $(CSVFILE) \
			     --day-file $(DAYFILE) \
			     --place-file $(PLACEFILE) \
			     --user $(USR) > $(OUTFILE)

clean:
	find . -name '*~' -exec rm -rf \{\} \+
	find . -name '__pycache__' -exec rm -rf \{\} \+

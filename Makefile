.PHONY: run

USR      ?= 1
CSVFILE  := data.csv
OUTFILE  := User_$(USR).json

run:
	python3 recommend.py --file $(CSVFILE) --user $(USR) > $(OUTFILE)

clean:
	find . -name '*~' -exec rm -rf \{\} \+
	find . -name '__pycache__' -exec rm -rf \{\} \+

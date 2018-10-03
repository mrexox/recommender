.PHONY: run

USER     := 1
CSVFILE  := data.csv

run: 
	python3 recommend.py --file $(CSVFILE) --user $(USER)



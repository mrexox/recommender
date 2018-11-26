#!/usr/bin/env python3

import json
import re

from SPARQLWrapper import SPARQLWrapper, JSON
from sys import argv

def get_movie_name():
    "Gets filename of films ordered by number in data.csv"
    if len(argv) <= 2:
        print("Using default film")
        return "Robin Hood"

    recommendation_file = argv[1]
    movies_file = argv[2]

    rec_json = None
    with open(recommendation_file) as rec_f:
        rec_json = json.load(rec_f)

    if not "1" in rec_json:
        return "Robin Hood"
    
    best_status = 0
    best_movie = None
    for movie, status in rec_json["1"].items():
        if float(status) > best_status:
            best_status = float(status)
            best_movie = movie
    
    movie_number = int(re.sub(r"[^\d]", "", best_movie)) - 1
                    
    with open(movies_file) as f:
        cnt = 0
        for line in f.readlines():
            if cnt == movie_number:
                return line.strip() # the film
            cnt += 1

    return "Robin Hood"



MOVIE_NAME = get_movie_name()

sparql = SPARQLWrapper("https://query.wikidata.org/sparql")

query = """
SELECT DISTINCT ?filmLabel ?countryLabel WHERE {
  BIND("%s"@en AS ?la)
  ?f wdt:P31 wd:Q11424;
     rdfs:label ?la;
     wdt:P495 ?country.
  ?film wdt:P495 ?country.
  ?film wdt:P31 wd:Q11424.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
} LIMIT 10
"""

print(query % MOVIE_NAME)
sparql.setQuery(query % MOVIE_NAME)

sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    film = result['filmLabel']['value']
    country = result['countryLabel']['value']
    print("{}  -  {}".format(film ,country))

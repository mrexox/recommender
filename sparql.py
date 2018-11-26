#!/usr/bin/env python3

from SPARQLWrapper import SPARQLWrapper, JSON
from sys import argv

MOVIE_NAME = "Robin Hood"
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
} LIMIT 400
"""

print(query % MOVIE_NAME)
sparql.setQuery(query % MOVIE_NAME)

sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    film = result['filmLabel']['value']
    country = result['countryLabel']['value']
    print("{}  -  {}".format(film ,country))

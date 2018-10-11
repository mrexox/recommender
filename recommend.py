#!/usr/bin/python3

from os.path import isfile
from sys import stderr, argv
from argparse import ArgumentParser
from numpy import array
from json import dumps

from lib.lib import readCsv, getRatingForUser, getTheBestFilms

def checkArgs(user: int, file):
    if user < 1:
        stderr.write("User can't be less than 1.")
        exit(1)
    if not isfile(file):
        stderr.write(f"File '{file}' is not accessible.")
        exit(1)

def getArgs():
    parser = ArgumentParser(description='Getting file and user number')
    parser.add_argument('--data-file', dest='csvfile', help='CSV data file')
    parser.add_argument('--day-file', dest='csvdayfile', help='CSV day context file')
    parser.add_argument('--place-file', dest='csvplacefile', help='CSV place context file')
    parser.add_argument('--user', dest='user', help='User id from file')
    args = parser.parse_args()
    return args.csvfile, args.csvdayfile, args.csvplacefile, int(args.user)

if __name__ == '__main__':
    csvFile, csvDayFile, csvPlaceFile, user = getArgs()   # Parsing args
    checkArgs(user, csvFile)    # Checking if user given was fine

    usersDict, movieNames = readCsv(csvFile)
    daysDict, _ = readCsv(csvDayFile)
    placesDict, _ = readCsv(csvPlaceFile)
    assert user <= max(usersDict.keys())
    assert user <= max(daysDict.keys())
    assert user <= max(placesDict.keys())

    # Transform python's dict to numpy's array
    usersArr = array(
        [ list(map(lambda x: int(x), usersDict[user])) for user in sorted(usersDict.keys()) ]
    )
    daysArr = [ daysDict[user] for user in sorted(daysDict.keys()) ]
    placesArr = [ placesDict[user] for user in sorted(placesDict.keys()) ]
    # So now the users are counted from 0
    user -= 1

    ratings = dict(getRatingForUser(user=user, data=usersArr))
    theBestFilms = getTheBestFilms(user=user, days=daysArr, places=placesArr, data=usersArr)
    data = {
        "user": user+1,
        "1": {movieNames[k]: round(v, 3) for k, v in ratings.items()},
        "2": {movieNames[k]: round(v, 3) for k, v in theBestFilms.items()},
    }
    print(dumps(data, indent=4))

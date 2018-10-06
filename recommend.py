#!/usr/bin/python3

from os.path import isfile
from sys import stderr, argv
from argparse import ArgumentParser
from numpy import array

from lib.lib import readCsv, getRatingForUser

def checkArgs(user: int, file):
    if user < 1:
        stderr.write("User can't be less than 1.")
        exit(1)
    if not isfile(file):
        stderr.write(f"File '{file}' is not accessible.")
        exit(1)

def getArgs():
    parser = ArgumentParser(description='Getting file and user number')
    parser.add_argument('--file', dest='csvfile', help='CSV data file')
    parser.add_argument('--user', dest='user', help='User id from file')
    args = parser.parse_args()
    return args.csvfile, int(args.user)

if __name__ == '__main__':
    csvFile, user = getArgs()   # Parsing args
    checkArgs(user, csvFile)    # Checking if user given was fine

    usersDict, movieNames = readCsv(csvFile)
    assert user <= max(usersDict.keys())

    # Transform python's dict to numpy's array
    usersArr = array(
        [ usersDict[user] for user in sorted(usersDict.keys()) ]
    )
    # So now the users are counted from 0
    user -= 1

    ratings = dict(getRatingForUser(user=user, data=usersArr))
    for key, value in ratings.items():
        print(movieNames[key], ':', round(value, 3))

from csv import reader
from re import compile, IGNORECASE
from numpy import ndarray, nditer, arange, size

from lib.recommender import Recommender


def readCsv(filename):
    """Parsing 2d table into dictionary and a list of movie names"""
    delWordRegex = compile(r"[a-z]", IGNORECASE)
    
    with open(filename) as csvfile:
        table = reader(csvfile, delimiter=',')
        rowN = 0
        usersDict = {}
        for row in table:
            if rowN == 0:
                row.pop(0)
                movieNames = [i.lower().strip() for i in row]
            else:
                username = int(row.pop(0).replace('User', '').strip())
                users = [int(i.strip()) for i in row]
                usersDict[username] = users
            rowN += 1
    return usersDict, movieNames

def getRatingForUser(user: int, data: ndarray):
    """
    Gets the job done. Finding the rating for films, that
    the given user didn't watch|rate.
    """
    
    if user < 0 or user >= data.size:
        raise Exception('Bad parameters given')

    # Get the rates for all the films `user` didn't rate
    r = Recommender(user, data)
    return r.recommend()

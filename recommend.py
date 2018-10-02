import os, sys, re
import csv

def errCheck():
    if len(sys.argv) < 2:
        sys.stderr.write("You should profile a CSV file as an argument\n")
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        sys.stderr.write(f"File '{sys.argv[1]}' does not exist\n")
        exit(1)

def readCsv(filename):
    """Parsing 2d table into dictionary and a list of movie names"""
    delWordRegex = re.compile(r"[a-z]", re.IGNORECASE)
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        rowN = 0
        usersDict = {}
        for row in reader:
            if rowN == 0:
                row.pop(0)
                movieNames = [i.lower().strip() for i in row]
            else:
                username = int(row.pop(0).replace('User', '').strip())
                users = [int(i.strip()) for i in row]
                usersDict[username] = users
            rowN += 1
    return usersDict, movieNames

if __name__ == '__main__':
    errCheck()                  # Checking if script was properly called
    csvFile = sys.argv[1]       # data.csv
    usersDict, movieNames = readCsv(csvFile)
    print(usersDict)
    print(movieNames)
    

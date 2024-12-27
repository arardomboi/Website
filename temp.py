import SQL
import random as ran
import requests
import Webscraping as wb
from difflib import SequenceMatcher
import pandas as pd
###
"""
def returnRandomMovie():
    movieList = SQL.returnAllMovies()
    if len(movieList) != 0:
        print("has")
    else:
        print("not has")
###
#var = returnRandomMovie()
###
movies = ["Titanic", "Inception", "Minions", "Blade Runner", "Blade Runner 2049"]
a = []
for m in movies:
    a.append(SQL.returnMovieDataByName(m))
"""
###
"""movieName = "Titanic"
movieData = wb.returnMovieDBData(movieName)
print(movieData)
"""
###
"""
movies = ["Titanic", "Inception", "Blade Runner", "Blade Runner 2049", "Minions", "Home Alone", "Home Alone 2"]
for m in movies:
    SQL.returnMovieDataByName(m)
    pass
"""
###
"""
movie = "deadpool and wolverine"
var = SQL.returnMovieDataByName(movie)
print(var.genreString)
"""

"""
def checkSimilarity(stringA = None, stringB = None):
    if stringA and stringB:
        similarityRatio = SequenceMatcher(None, stringA, stringB).ratio()
        if similarityRatio > 0.8:
            return True
    return False
"""
###
"""
movieNames = ["Titanic", "Home Alone", "Home Alone 2", "Inception", "Blade Runner 2049"]

movieObjects = [wb.returnMovieDBData(movieName) for movieName in movieNames]
"""
###
#The Moviedb
global genreDict
Moviedb_APIKEY = "66ab025a7673a17b6e9789838dc21fc0"
#Creating the Genre Dictionary
genreURL = f"https://api.themoviedb.org/3/genre/movie/list?api_key={Moviedb_APIKEY}"
response = requests.get(genreURL)
genreData = response.json()
genreDict = {genre["id"]: genre["name"] for genre in genreData["genres"]}

genreIDList = []
genreList = []

for id in genreIDList:
    genreList.append(genreDict[id])

def convertGenreIDToString(listID):
    temp = [genreDict[id] for id in listID]
    return temp
###
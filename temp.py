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

movieName = "Titanic"

apiKey = "66ab025a7673a17b6e9789838dc21fc0"
apiURL = f"https://api.themoviedb.org/3/search/movie?api_key={apiKey}&query={movieName}&append_to_response=runtime"

response = requests.get(apiURL)

returnData = response.json()["results"]

movieData = None

for m in returnData:
    if m["title"].title() == movieName.title():
        movieData = m
        break
if not movieData:
    movieData = returnData[0]

genreURL = f"https://api.themoviedb.org/3/genre/movie/list?api_key={apiKey}"
response = requests.get(genreURL)
genreData = response.json()

genreDict = {genre["id"]: genre["name"] for genre in genreData["genres"]}

for key in genreDict:
    print(f"{key} : {genreDict[key]}")

creditURL = f"https://api.themoviedb.org/3/movie/{movieData["id"]}/credits?api_key={apiKey}"
creditResponse = requests.get(creditURL)
creditData = creditResponse.json()

for key in creditData:
    print(f"{key} : {creditData[key]}")
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
"""for key in creditData["crew"]:
    print(f"{key} : {creditData["crew"][key]}")"""

director = "Unknown"

for worker in creditData["crew"]:
    if worker["job"] == "Director":
        director = worker["name"]
        break
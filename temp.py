import SQL
import random as ran
import requests
import Webscraping as wb
"""def returnRandomMovie():
    movieList = SQL.returnAllMovies()
    if len(movieList) != 0:
        print("has")
    else:
        print("not has")

#var = returnRandomMovie()

movies = ["Titanic", "Inception", "Minions", "Blade Runner", "Blade Runner 2049"]
a = []
for m in movies:
    a.append(SQL.returnMovieDataByName(m))
"""

"""movieName = "Titanic"
movieData = wb.returnMovieDBData(movieName)
print(movieData)
"""

def temp(movieName = None, Moviedb_APIKEY = "66ab025a7673a17b6e9789838dc21fc0"): #remade for bug fixing
    ###
    genreURL = f"https://api.themoviedb.org/3/genre/movie/list?api_key={Moviedb_APIKEY}"
    response = requests.get(genreURL)
    genreData = response.json()
    genreDict = {genre["id"]: genre["name"] for genre in genreData["genres"]}
    ###
    movieURL = f"https://api.themoviedb.org/3/search/movie?api_key={Moviedb_APIKEY}&query={movieName}&append_to_response=runtime"
    response = requests.get(movieURL)
    data = response.json()
    pageData = data["results"][0]
    genreIDList = pageData["genre_ids"]
    genreList = []
    for genreID in genreIDList:
        genreList.append(genreDict[genreID])
    print(genreList)

"""temp("Titanic")

var = wb.returnMovieDBData("Inception")

print(var)"""
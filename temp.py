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

movies = ["Titanic", "Inception", "Blade Runner", "Blade Runner 2049", "Minions", "Home Alone", "Home Alone 2"]
for m in movies:
    SQL.returnMovieDataByName(m)
    pass
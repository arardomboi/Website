import SQL
import random as ran

def returnRandomMovie():
    movieList = SQL.returnAllMovies()
    if len(movieList) != 0:
        print("has")
    else:
        print("not has")

var = returnRandomMovie()

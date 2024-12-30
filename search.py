#imports
import SQL as sql #me
import Webscraping as wb #me
#functions
def collateNamesFromAPI(movieName):
    moviePage = wb.returnMovieDBLikeMovies(movieName)
    movieNames = [item["title"].title() for item in moviePage]
    return movieNames

def collateRelevantMovies(movieName):
    movieSet = {sql.returnMovieDataByName(movieName)}
    similarMovieNames = collateNamesFromAPI(movieName)
    for name in similarMovieNames:
        movieSet.add(sql.returnMovieDataByName(name))
    return movieSet

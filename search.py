#imports
import SQL as sql #me
import Webscraping as wb
#functions
def collateNamesFromAPI(moviePage):
    movieNames = [item["title"].title() for item in moviePage]
    return movieNames

def collateRelevantMovies(movieName):
    movieSet = {sql.returnMovieDataByName(movieName)}
    similarMovieNames = wb.returnMovieDBLikeMovies(movieName)
    for name in similarMovieNames:
        movieSet.add(sql.returnMovieDataByName(name))
    return movieSet
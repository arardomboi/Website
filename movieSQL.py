#imports
import Webscraping as wb #me
import sqlite3 as sql # not me
from initSQL import conn, cursor #me
#functions
def classifyMovieList(movieList): #idk
    movieDataClass = wb.movieStatsClass(movieList[1], movieList[2], movieList[3], movieList[4], movieList[5], movieList[6], movieList[7], movieList[8])
    movieDataClass.genreList = convertListToString(movieDataClass.genreList)
    return movieDataClass

def convertListToString(dataList):
    var = dataList[0]
    for item in dataList:
        var += f", {str(item)}"
    return var

def convertStringToList(dataString):
    var = dataString.split(", ")
    return var

def addDataToMovieData(movieList):
    movieDataClass = classifyMovieList(movieList)
    cursor.execute(""" INSERT INTO movieData (movieName, movieSummary, movieRating, movieReleaseDate, movieLength, movieDirector, movieGenre, moviePosterLink)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?);""",
                   (movieDataClass.title, movieDataClass.summary,movieDataClass.rating, movieDataClass.releaseDate, movieDataClass.length, movieDataClass.director, movieDataClass.genreList, movieDataClass.posterLink))
    conn.commit()
    print("Movie data added to database.")

def checkMovieDataTable(movieID):
    #Select statement
    temp = cursor.execute(f"""SELECT * FROM movieData
                   WHERE movieID = '{movieID}'; 
                   """)
    result = cursor.fetchall()
    #Result is list of tuple(s)
    if len(result) != 0:
        print("Movie found in database.")
        return [True, result[0]]
    else:
        print("Movie not found in database.")
        return [False, None]

def returnMovieDataByID(movieID):
    databaseCheck = checkMovieDataTable(movieID)
    #If in database:
    if databaseCheck[0]:
        print("Returning dictionary of movieData")
        var = wb.classify(databaseCheck[1][1:])
        return var
    else:
        raise Exception("What now :(")
        dataList = wb.returnMovieDBData()
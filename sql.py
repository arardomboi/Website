#Imports
import sqlite3 as sql
import Webscraping as wb
#Yea
global cursor
conn = sql.connect("static/Database.db")
cursor = conn.cursor()
#Functions
def classify(movieList): #idk
    movieDataClass = wb.movieStatsClass(movieList[0], movieList[1], movieList[2], movieList[3], movieList[4], movieList[5], movieList[6], movieList[7])
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

def deleteTableMovieData():
    try:
        cursor.execute("DROP TABLE movieData;")
        print("Table 'movieData' deleted successfully.")
    except:
        print("Error deleting table 'movieData'.")

def createTableMovieData():
    cursor.execute("""CREATE TABLE movieData (
                   movieID INTEGER PRIMARY KEY AUTOINCREMENT,
                   movieName VARCHAR(50),
                   movieSummary TEXT,
                   movieRating VARCHAR(10),
                   movieReleaseDate CHAR(8),
                   movieLength VARCHAR(10),
                   movieDirector VARCHAR(50),
                   movieGenre TEXT,
                   moviePosterLink VARCHAR(200)
                   );""")
    print("Table 'movieData' made.")

def addDataToMovieData(movieList):
    movieDataClass = classify(movieList)
    cursor.execute(""" INSERT INTO movieData (movieName, movieSummary, movieRating, movieReleaseDate, movieLength, movieDirector, movieGenre, moviePosterLink)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?);""",
                   (movieDataClass.title, movieDataClass.summary,movieDataClass.rating, movieDataClass.releaseDate, movieDataClass.length, movieDataClass.director, movieDataClass.genreList, movieDataClass.posterLink))
    conn.commit()
    print("Movie data added to database.")

def checkDatabase(movieName):
    #Select statement
    temp = cursor.execute(f"""SELECT * FROM movieData
                   WHERE movieName = '{movieName}'; 
                   """)
    result = cursor.fetchall()
    #For loop in list of results
    for row in result:
        if row[1] == movieName: #Row is tuple data type
            print("Movie found in database.")
            return [True,row] #Returns both true for finding the movie, and the tuple of the movie data
    print("Movie not found :(.")
    return [False,None] #Returns false and None to stop a index error


def returnMovieData(movieName):
    var = checkDatabase(movieName)
    #If not in database
    if not var[0]:
        print("Movie returned from webscraping.")
        movieData = wb.returnMovieDBData(movieName)
        addDataToMovieData(movieData)
        return movieData
    print("Movie returned from database.")
    return var[1]
#trials
"""movieData = wb.returnMovieDBData("Titanic")
movieData.genreList = convertListToString(movieData.genreList)
print(movieData.length)"""
#addDataToMovieData(movieData)
movieName = "Minions"
print(returnMovieData(movieName))
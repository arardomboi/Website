#Imports
import sqlite3 as sql
import Webscraping as wb
#Yea
global cursor
conn = sql.connect("static/Database.db")
cursor = conn.cursor()
#Functions
def classify(movieList): #idk
    print(type(movieList))
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
                    movieReleaseDate CHAR(8),
                    movieLength VARCHAR(10),
                    movieDirector VARCHAR(50),
                    movieGenre TEXT,
                    moviePosterLink VARCHAR(200)
                    );""")
    print("Table 'movieData' made.")

def addDataToMovieData(movieData):
    movieData = classify(movieData)
    cursor.execute(""" INSERT INTO movieData (movieName, movieSummary, movieReleaseDate, movieLength, movieDirector, movieGenre, moviePosterLink)
                   VALUES (?, ?, ?, ?, ?, ?, ?);""",
                   (movieData.title, movieData.summary, movieData.releaseDate, movieData.length, movieData.director, movieData.genreList, movieData.posterLink))
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

def convertListToString(dataList):
    var = dataList[0]
    for item in dataList:
        var += f", {str(item)}"
    return var

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
movieName = "Inception"
print(returnMovieData(movieName))
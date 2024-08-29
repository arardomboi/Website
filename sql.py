#Imports
import sqlite3 as sql
import Webscraping as wb
movie = wb.returnMovieDBData("Inception")
#Yea
global cursor
conn = sql.connect("static/Database.db")
cursor = conn.cursor()
#Functions
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
    print(movieData.length)
    cursor.execute(""" INSERT INTO movieData (movieName, movieSummary, movieReleaseDate, movieLength, movieDirector, movieGenre, moviePosterLink)
                   VALUES (?, ?, ?, ?, ?, ?, ?);""",
                   (movieData.title, movieData.summary, movieData.releaseDate, movieData.length, movieData.director, movieData.genreList, movieData.posterLink))
    conn.commit()
    print("Movie data added to database.")

def checkDatabase(movieName):
    temp = cursor.execute(f"""SELECT * FROM movieData
                   WHERE movieName = '{movieName}'; 
                   """)
    return temp

def convertListToString(dataList):
    var = dataList[0]
    for item in dataList:
        var += f", {str(item)}"
    return var

deleteTableMovieData()
createTableMovieData()
#trials
movieData = wb.returnMovieDBData("Titanic")
movieData.genreList = convertListToString(movieData.genreList)
print(movieData.length)
#addDataToMovieData(movieData)
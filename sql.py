#Imports
import sqlite3 as sql #me
import Webscraping as wb #me
import hashlib #not me
#Yea
print("Connecting to database.")
global cursor
conn = sql.connect("static/Database.db", check_same_thread=False)
cursor = conn.cursor()
print("Connected successfully.")
#Movie Data

def classify(movieList): #idk
    print(movieList)
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

def checkDatabase(movieID):
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
    databaseCheck = checkDatabase(movieID)
    #If in database:
    if databaseCheck[0]:
        print("Returning dictionary of movieData")
        var = wb.convertToDict(movieList = databaseCheck[1], typeSource = "database")
        return var
    else:
        raise Exception("What now :(")
        dataList = wb.returnMovieDBData()

#Sign Up/ Log In

def createUserDatabase():
    cursor.execute("""CREATE TABLE userData (
                   userID INTEGER PRIMARY KEY AUTOINCREMENT,
                   firstName VARCHAR(50),
                   lastName VARCHAR(50),
                   userName VARCHAR (30),
                   email VARHCAR(100) NOT NULL,
                   hashedPassword TEXT);""")
    print("User Data table created successfully.")

def createReviewDatabase():
    cursor.execute("""CREATE TABLE reviewData (
                   reviewID INTEGER PRIMARY KEY AUTOINCREMENT,
                   movieID INTEGER,
                   userID INTEGER,
                   reviewText TEXT,
                   movieRating INTEGER
                   reviwDate DATE,
                   FOREIGN KEY (movieID) REFERENCES movieData(movieID),
                   FOREIGN KEY (userID) REFERENCES userData(userID));""")
    print("Review Data table created successfully.")

def deleteUserDatabase():
    try:
        cursor.execute("""DROP TABLE userData;""")
        print("Deleted userData table successfully.")
    except:
        print("Error deleting userData table")

def deleteReviewDatabase():
    try:
        cursor.execute("DROP TABLE reviewData")
        print("Deleted reviewData table successfully.")
    except:
        print("Error deleting reviewData.")

def checkUserDatabasePresence(userName, password):
    temp = cursor.execute(f"""SELECT * FROM userData
                   WHERE userName = '{userName}'; 
                   """)
    result = cursor.fetchall()
    if len(result) == 0:
        return False
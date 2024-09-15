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
#Moviedb Table
def classifyMovieList(movieList): #idk
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

def deleteTableMovieData():
    try:
        cursor.execute("DROP TABLE movieData;")
        print("Table 'movieData' deleted successfully.")
    except:
        print("Error deleting table 'movieData'.")

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
        var = wb.convertToDict(movieList = databaseCheck[1], typeSource = "database")
        return var
    else:
        raise Exception("What now :(")
        dataList = wb.returnMovieDBData()

#Sign Up/ Log In
def dictUserData(userList):
    userDict = {
        "userID" : userList[0],
        "firstName" : userList[1],
        "lastName" : userList[2],
        "userName" : userList[3],
        "email" : userList[4],
        "hashedPassword" : userList[5],
        "age" : userList[6],
        "gender" : userList[7]
    }
    return userDict

def dictReviewData(reviewList):
    reviewDict = {
        "reviewID" : reviewList[0],
        "movieID" : reviewList[1],
        "userID" : reviewList[2],
        "reviewText" : reviewList[3],
        "movieRating" : reviewList[4],
        "reviewDate" : reviewList[5],
    }
    return reviewDict

def createUserTable():
    cursor.execute("""CREATE TABLE userData (
                   userID INTEGER PRIMARY KEY AUTOINCREMENT,
                   firstName VARCHAR(50),
                   lastName VARCHAR(50),
                   userName VARCHAR (30),
                   email VARHCAR(100) NOT NULL,
                   hashedPassword TEXT NOT NULL,
                   age INTEGER,
                   gender CHARACTER);""")
    print("User Data table created successfully.")

def deleteUserTable():
    try:
        cursor.execute("""DROP TABLE userData;""")
        print("Deleted userData table successfully.")
    except:
        print("Error deleting userData table")

def resetUserTable():
    try:
        deleteUserTable()
        createReviewTable()
    except:
        createUserTable()
    print("UserData table reset successfully.")

def createReviewTable():
    cursor.execute("""CREATE TABLE reviewData (
                   reviewID INTEGER PRIMARY KEY AUTOINCREMENT,
                   movieID INTEGER,
                   userID INTEGER,
                   reviewText TEXT,
                   movieRating INTEGER
                   reviewDate DATE,
                   FOREIGN KEY (movieID) REFERENCES movieData(movieID),
                   FOREIGN KEY (userID) REFERENCES userData(userID));""")
    print("Review Data table created successfully.")

def deleteReviewTable():
    try:
        cursor.execute("DROP TABLE reviewData")
        print("Deleted reviewData table successfully.")
    except:
        print("Error deleting reviewData.")

def resetReviewDataTable():
    try:
        deleteReviewTable()
        createReviewTable()
    except:
        createReviewTable()
    print("ReviewData table reset successfully.")

def addUserDataToUserTable(userDict):
    if not checkUserTablePresenceByUsername(userDict["userName"]): #if user not found
        cursor.execute(""" INSERT INTO userData (firstName, lastName, userName, email, hashedPassword, age, gender)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?);""",
                   (userDict["firstName"], userDict["lastName"], userDict["userName"], userDict["email"], userDict["hashedPassword"], userDict["age"], userDict["gender"]))
        conn.commit()
        print("userData added to userTable successfully.") 
    else: #if user found
        print(f"Entry for user {userDict["username"]} already found in userTable.")

def checkUserTablePresenceByUsername(userName = None):
    #Error Checking
    if not(userName):
        print("Error with username.")
        return False
    #select where usernames match
    temp = cursor.execute(f"""SELECT userName FROM userData
                   WHERE userName = '{userName}'; 
                   """)
    result = cursor.fetchall()
    #If list is empty
    if len(result) == 0:
        return False
    return True

def checkUserTablePresenceByID(userID = None):
    #Error Checking
    if not(userID):
        print("Error with userID")
        return False
    #Select statement
    temp = cursor.execute(f"""SELECT * FROM userData
                          WHERE userID = {userID}""")
    result = cursor.fetchall()
    #If list is empty
    if len(result) == 0:
        return False
    return True
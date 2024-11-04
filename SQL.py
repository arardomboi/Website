#Imports
import sqlite3 as sql #not me
import Webscraping as wb #me
import Registration as reg #me
import random as ran #not me
#Yea
print("Connecting to database.")
global cursor
conn = sql.connect("static/Database.db", check_same_thread=False)
cursor = conn.cursor()
print("Connected successfully.")

#Moviedb Table
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

#Sign Up/ Log In

def createUserTable():
    cursor.execute("""CREATE TABLE userData (
                   userID INTEGER PRIMARY KEY AUTOINCREMENT,
                   firstName VARCHAR(50),
                   lastName VARCHAR(50),
                   userName VARCHAR (30),
                   email VARHCAR(100) NOT NULL,
                   hashedPassword TEXT NOT NULL,
                   gender CHARACTER);""")

def resetUserTable():
    try:
        cursor.execute("""DROP TABLE userData;""")
        createUserTable()
    except:
        createUserTable()
    print("UserData table reset successfully.")

def createReviewDataTable():
    cursor.execute("""CREATE TABLE reviewData (
                   reviewID INTEGER PRIMARY KEY AUTOINCREMENT,
                   movieID INTEGER,
                   userID INTEGER,
                   reviewText TEXT,
                   movieRating INTEGER,
                   reviewDate DATE,
                   FOREIGN KEY (movieID) REFERENCES movieData(movieID),
                   FOREIGN KEY (userID) REFERENCES userData(userID));""")

def resetReviewDataTable():
    try:
        #delete
        cursor.execute("DROP TABLE reviewData")
        #create
        createReviewDataTable()
    except:
        createReviewDataTable()
    print("ReviewData table reset.")

#Movie DB
def classifyMovieDataSQL(movieList):
    movieClass = wb.movieStatsClass(movieList[0])
    return movieClass
def convertListToString(dataList):
    var = dataList[0]
    for item in dataList:
        var += f", {str(item)}"
    return var

def convertStringToList(dataString):
    var = dataString.split(", ")
    return var

def addDataToMovieData(movieDataClass):
    cursor.execute(""" INSERT INTO movieData (movieName, movieSummary, movieRating, movieReleaseDate, movieLength, movieDirector, movieGenre, moviePosterLink)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?);""",
                   (movieDataClass.title, movieDataClass.summary,movieDataClass.rating, movieDataClass.releaseDate, movieDataClass.length, movieDataClass.director, movieDataClass.returnGenreAsString(), movieDataClass.posterLink))
    conn.commit()
    print("Movie data added to database.")

def checkMovieDataTableByID(movieID):
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
    databaseCheck = checkMovieDataTableByID(movieID)
    #If in database:
    if databaseCheck[0]:
        print("Returning class of movieData")
        var = wb.classify(databaseCheck[1])
        return var
    else:
        return None
def returnMovieDataByName(movieName):
    print(f"Attempting to return movie data where name = {movieName}")
    temp = cursor.execute(f"""SELECT * FROM movieData
                          WHERE movieName = '{movieName}' """)
    result = cursor.fetchall()
    if len(result) != 0:
        print(f"Movie found in database with name '{movieName}'.")
        return result[0]
    else:
        print(f"Movie not found in database with name '{movieName}")
        movieData = wb.returnMovieDBData(movieName)
        addDataToMovieData(movieData)
        returnMovieDataByName(movieName)

def returnRandomMovie(): #lol
    temp = cursor.execute("""SELECT * FROM movieData
                          ORDER BY RANDOM()
                          LIMIT 1""")
    result = cursor.fetchall()[0]
    movieClass = classifyMovieDataSQL(result)
    return movieClass

#Reg
def classifyUserDataSQL(userList):
    classTemp = reg.userClass(userList[0], userList[1], userList[2], userList[3], userList[4], userList[5], userList[6], userList[7], userList[8], userList[9])
    return classTemp

def addUserDataToUserTable(userClass):
    if not checkUserTablePresence(userClass.uName, type = "user"): #if user not found by username
        cursor.execute(""" INSERT INTO userData (firstName, lastName, userName, email, hashedPassword, age, gender)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?);""",
                   (userClass.fName,userClass.lName,userClass.uName,userClass.email,userClass.hashPass,userClass.age,userClass.gender))
        conn.commit()
        print("userData added to userTable successfully.") 
    else: #if user found
        print(f"Entry for user {userClass.uName} already found in userTable.")

def checkUserTablePresence(searchVal = None, type = None):
    #assigning searchType dependant on given arguement
    if type == "user":
        print("Searhing userTable with type of 'user'.", end = "")
        searchType = "username"
    elif type == "id":
        print("Searching userTable with type of 'id'.", end  = "")
        searchType = "userID"
        print(f" With given value of {searchVal}")
    else: #type not equal to either user or id
        return False
    #select where type match
    temp = cursor.execute(f"""SELECT userName FROM userData
                   WHERE {searchType} = '{searchVal}'; 
                   """)
    result = cursor.fetchall() #tuple of arrays ([],[],[]...)
    #If list is empty
    if len(result) == 0:
        return False
    return True

if __name__ == "__main__":
    var = returnRandomMovie()
    print(var)
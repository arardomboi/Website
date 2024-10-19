#Imports
import sqlite3 as sql #not me
import Webscraping as wb #me
import Registration as reg #me
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
    print("Returning movie data where")
    temp = cursor.execute(f"""SELECT * FROM movieData
                          WHERE movieName = '{movieName}' """)
    result = cursor.fetchall()
    if len(result) != 0:
        print(f"Movie found in database with name '{movieName}'.")
        return result[0]
    else:
        movieData = wb.returnMovieDBData(movieName)
        movieClass = wb.classify(movieData)
        addDataToMovieData(movieClass)
        return movieClass

#Reg
def classifyUserDataSQL(userList):
    classTemp = reg.userClass(userList[0], userList[1], userList[2], userList[3], userList[4], userList[5], userList[6], userList[7], userList[8], userList[9])
    return classTemp

def addUserDataToUserTable(userClass):
    if not checkUserTablePresenceByUsername(userClass.uName): #if user not found by username
        cursor.execute(""" INSERT INTO userData (firstName, lastName, userName, email, hashedPassword, age, gender)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?);""",
                   (userClass.fName,userClass.lName,userClass.uName,userClass.email,userClass.hashPass,userClass.age,userClass.gender))
        conn.commit()
        print("userData added to userTable successfully.") 
    else: #if user found
        print(f"Entry for user {userClass.uName} already found in userTable.")

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
    else:
        return True

if __name__ == "__main__":
    pass
#imports
import sqlite3 as sql #not me
from initSQL import cursor #me
import Registration as reg #me
#functions
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
        print(f"Entry for user {userClass.fName} already found in userTable.")

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

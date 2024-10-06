#imports
import hashlib #not me
import smtplib #not me
from email.message import EmailMessage #not me
import random as r #not me
#functions
class userClass:
    def __init__(self, firstName, lastName, userName, email, password, age, gender):
        self.fName = firstName
        self.lName = lastName
        self.uName = userName
        self.gender = gender
        self.email = email
        self.hashPass = hashPassword(password)
        self.age = age
        self.gender = gender
    def returnAsList(self):
        return [self.fName,self.lName,self.uName,self.email,self.hashPass,self.age,self.gender]

def hashPassword(password):
    hashedPassword = hashlib.sha256(password.encode("utf-8")).hexdigest()
    print(f"Given password of {password} hashed into {hashedPassword} with length of {len(hashedPassword)}")
    return hashedPassword

def checkPassword(password): #True = valid, False = invalid 
    passwordSet = set(password)
    specialChar = ["!", ".", "*", "?", "/"]
    specialSet = set(specialChar)
    numSet = set(list(str(range(0,10))))
    return [len(password) >= 8, len(passwordSet.intersection(numSet)) != 0, len(passwordSet.intersection(specialSet)) != 0] 
    #[length, has number, has special char], returned as list

#nfwh cjsa udzi tvji - ignore
def sendEmailCode(email):
    smtpServer = "smpt.gmail.com"
    server = smtplib.SMTP(smtpServer, 587)
    #setup message
    randomCode = r.randint(10000,99999)
    msg = EmailMessage()
    msg["From"] = "cineverse.noreply0@gmail.com"
    msg["To"] = email
    msg["Subject"] = "Cineverse Account Creation Code"
    #send message
    try: #try send 
        print("Attempting to create email smtp server.")
        server.starttls()
        server.login("cineverse.noreply0@gmail.com", "nfwh cjsa udzi tvji")
        print(f"Server created\nAttempting to send message to email {email} with code {randomCode}.")
        temp = msg.as_string()
        server.sendmail("cineverse.noreply0@gmail.com", email, temp)
        print("Email sent.")
    except Exception as e: #if error sending mail
        print(f"Error sending email\n{str(e)}")
    finally: #after everyting
        print("Closing email server")
        server.quit()
    return randomCode

code = sendEmailCode("tedhill07@icloud.com")
if code == int(input("Enter Code: \n")):
    print("yea")
else:
    print(f"nah\ncode = {code}")
#imports
import hashlib #not me
import smtplib #not me
from email.message import EmailMessage #not me
import email.mime.text as mime 
import random as r #not me
import re #not me
import Registration as reg
#functions
class userClass:
    def __init__(self, firstName, lastName, userName, email, password, gender):
        self.fName = firstName
        self.lName = lastName
        self.uName = userName
        self.email = email
        self.hashPass = hashPassword(password)
        self.gender = gender
    def returnAsList(self):
        return [self.fName,self.lName,self.uName,self.email,self.hashPass,self.gender]

def hashPassword(password):
    hashedPassword = hashlib.sha256(password.encode("utf-8")).hexdigest()
    print(f"Given password of {password} hashed into {hashedPassword} with length of {len(hashedPassword)}")
    return hashedPassword

def checkPassword(password):
    passwordSet = set(password) #set version of password string
    specialSet = set(["!", ".", "*", "?", "/"])
    numSet = set(list(str(range(0,10)))) #set of numbers 1-10 inclusive
    passwordDict = {
        "lengthBool" : len(password) >= 8, #checking if length equal or above 8
        "numBool" : len(passwordSet.intersection(numSet)) != 0, #checking if has any numbers
        "specialBool" : len(passwordSet.intersection(specialSet) != 0) #schecking if has any special chars
        }
    return passwordDict

def checkEmail(email):
    valid = re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email) #awful regex
    return valid

def sendEmailCode(recieveEmail):
    #init email
    randomCode = r.randint(10000,99999)
    sendEmail = "cineverse.noreply0@gmail.com"
    msg = mime.MIMEText(str(randomCode))
    msg["subject"] = "Verification Code Cineverse"
    msg["from"] = sendEmail
    msg["To"] = recieveEmail
    #create server
    smtpServer = "smtp.gmail.com"
    port = 587
    smtpPassword = "nfwh cjsa udzi tvji"
    server = smtplib.SMTP(smtpServer, port)
    server.starttls()
    server.login(sendEmail, smtpPassword)
    #send email
    server.sendmail(sendEmail, recieveEmail, msg.as_string())
    server.quit()
    return randomCode

def returnLogInFormData(pageData = None): #returns class
    dic = {key : pageData.getlist(key)[0] for key in pageData} #painful to read but cheeky
    if dic["password1"] == dic["password2"]: #matching pw
        passwordCheck = checkPassword(dic["password1"])
        if passwordCheck["lengthBool"] and passwordCheck["numBool"] and passwordCheck["specialBool"]: #if meets all conditions
            userClassInstance = reg.userClass(firstName=dic["fname"],lastName=dic["lname"],userName=dic["uname"],email=dic["email"],password=dic["password1"],gender=dic["gender"]) #large ahh statement
            return [True, userClassInstance]
        else:
            return [False, passwordCheck]
    else:
        return [False, "passwords do not match"]
import hashlib #not me
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

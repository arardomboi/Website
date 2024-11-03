#imports
import urllib.request, json #not me
from flask import request #not me
from werkzeug.datastructures import ImmutableMultiDict  #not me
import Registration as reg
#functions

def returnSignFormData(pageData = None): #returns class
    dic = {key : pageData.getlist(key)[0] for key in pageData} #painful to read
    if dic["password1"] == dic["password2"]: #matching pw
        passwordCheck = reg.checkPassword(dic["password1"])
        if passwordCheck["lengthBool"] and passwordCheck["numBool"] and passwordCheck["specialBool"]: #if meets all conditions
            userClassInstance = reg.userClass(firstName=dic["fname"],lastName=dic["lname"],userName=dic["uname"],email=dic["email"],password=dic["password1"],gender=dic["gender"])
            return userClassInstance
        else:
            return [-2, "password does not meet all conditions"] 
    else:
        return [-1, "passwords do not match"]

trial = ImmutableMultiDict([('fname', 'ted'), 
                    ('lname', 'hill'), 
                    ('uname', 'doggo'), 
                    ('gender', 'M'), 
                    ('email', 'tedhill07@icloud.com'), 
                    ('password1', 'DogRizz123'), 
                    ('password2', 'DogRizz123'), 
                    ('submit', 'Create Account')])

dic = returnSignFormData(trial)
print(dic)
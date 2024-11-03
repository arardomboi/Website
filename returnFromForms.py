#imports
import urllib.request, json #not me
from flask import request #not me
from werkzeug.datastructures import ImmutableMultiDict  #not me
import Registration as reg
#functions

def returnSignFormData(pageData = None): #returns class
    dic = {key : pageData.getlist(key)[0] for key in pageData} #painful to read
    if dic["password1"] == dic["password2"]:
        passwordCheck = reg.checkPassword(dic)
        userClassInstance = reg.userClass()

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
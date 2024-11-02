#imports
import urllib.request, json #not me
from flask import request #not me
from werkzeug.datastructures import ImmutableMultiDict  #not me
#functions
def returnSignFormData(pageData = None):
    pass

ImmutableMultiDict([('fname', 'ted'), 
                    ('lname', 'hill'), 
                    ('uname', 'doggo'), 
                    ('gender', 'M'), 
                    ('email', 'tedhill07@icloud.com'), 
                    ('password1', 'EdwardHill12'), 
                    ('password2', 'EdwardHill12'), 
                    ('submit', 'Create Account')])

print(ImmutableMultiDict.getlist("fname"))
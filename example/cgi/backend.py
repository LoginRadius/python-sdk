#!/usr/bin/python
#################################################
# Example Implementation of LoginRadius Class   #
#################################################
# This is an example on how to use LoginRadius  #
# Python SDK                                    #
#################################################
# Copyright 2015-2016 LoginRadius Inc.          #
# - www.LoginRadius.com                         #
#################################################
# This file is part of the LoginRadius SDK      #
# package.                                      #
#################################################

#Your API Credentials
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_SECRET_KEY"
FILE_PATH = "http://______________________/"
#example http://localhost/python-sdk-v2/example/cgi/

#Essential package for LoginRadius to communicate
from LoginRadius import LoginRadius as LR
LR.API_KEY = API_KEY
LR.API_SECRET = API_SECRET
#LR.LIBRARY ='urllib2'
login = LR()
#We need a request
import cgi 
#Get the 'token' from the POST request
arguments = cgi.FieldStorage()
token = arguments.getvalue('token')
#login = LoginRadius(token)
print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Python Demo</title>')
print ('<link href="style.css" rel="stylesheet" type="text/css" media="all" />')
print ('<script src="//code.jquery.com/jquery-2.2.1.min.js"></script>')
print ('<script src="//auth.lrcontent.com/v2/js/LoginRadiusV2.js"></script>')
print ('<script type="text/javascript">var commonOptions = {};commonOptions.apiKey = "' + API_KEY +'";commonOptions.verificationUrl = window.location.origin+window.location.pathname;commonOptions.resetPasswordUrl = window.location.origin+window.location.pathname;commonOptions.formValidationMessage = true;commonOptions.hashTemplate = true;</script>')
print ('<script src="LoginRadiusFrontEnd.js"></script>')
print ('<script type="text/javascript">var check_options= {};check_options.onError = function(response) {window.location="'+ FILE_PATH +'frontend.py'+'"};LRObject.util.ready(function() {LRObject.init("ssoNotLoginThenLogout", check_options);});</script>')
print ('</head>')
print ('<body>')
profile = login.sociallogin.profile(token)
#It is good practice to check if the token is valid
if login.accesstoken.validate(token):
    print ('<div class="lr-profile-frame lr-input-style">')
    print ('<div class="lr-profile-header">')
    print ('<div class="lr-logo-center">')
    if profile.get('ImageUrl') is not None:
        print ('<span class="lr-image-frame">')
        print ('<img src='+profile.get('ImageUrl')+' alt='+profile.get('FirstName')+'>')
        print ('</span>')
    else:
        print ('<span class="lr-image-frame">')
        print ('<img src="'+ FILE_PATH +'images/user-blank.png'+'" alt="">')
        print ('</span>')
    
    print ('<div class="lr-heading">Hello, <span class="lr-user-name">'+str(profile.get('FullName'))+'</span></div>')
    print ('<div class="lr-profile-info">')
    print ('</div>')
    if profile.get('Email') is not None:
        for email in profile.get('Email'):
            print ('<div class="lr-email-info">')
            print ('<span class="lr-value lr-em">'+email['Value']+'</span>')
            print ('</div>')           
    print ('<div class="lr-uid-info">')
    print ('<span class="lr-label">UID: </span>')
    print ('<span class="lr-value">'+profile.get('Uid')+'</span>')
    print ('</div>')
    print ('</div>')

    print ('<div class="lr-menu-buttons">')
    print ('<a class="lr-logout" href="'+ FILE_PATH +'logout.py'+'" style="font-size: 14px;">Logout</a>')
    print ('</div>')
         

    print ('<div id="lr-profile" class="lr-frame lr-input-style lr-align-left" style="display:block">')
    if profile.get('Provider') is not None:
            print ('<label class="lr-input-frame lr-inline">')
            print ('<span class="lr-input-label">Provider</span>')
            print ('<input type="text"  value="'+profile.get('Provider')+'">')
            print ('</label>')
    if profile.get('FirstName') is not None:
        print ('<label class="lr-input-frame lr-inline">')
        print ('<span class="lr-input-label">First Name</span>')
        print ('<input type="text"  value="'+profile.get('FirstName')+'">')
        print ('</label>')
    if profile.get('LastName') is not None:
        print ('<label class="lr-input-frame lr-inline">')
        print ('<span class="lr-input-label">Last Name</span>')
        print ('<input type="text"  value="'+profile.get('LastName')+'">')
        print ('</label>')
    if profile.get('UserName') is not None:
        print ('<label class="lr-input-frame lr-inline">')
        print ('<span class="lr-input-label">User Name</span>')
        print ('<input type="text"  value="'+profile.get('UserName')+'">')
        print ('</label>')
  
    print ('</div>')
    
    #We shouldn't post without explicit permission!
    #login.sociallogin.status_update("LoginRadius is pretty neat!")

else:
    #Something has gone wrong.
    print ("Something has gone wrong ")
print ('</body>')
print ('</html>')

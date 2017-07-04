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

#Your API Secret
API_SECRET = "YOUR_API_SECRET"
API_KEY = "YOUR_API_KEY"

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
print ("Content-Type: text/html\n\n")
print """
<link href="style.css" rel="stylesheet" type="text/css" media="all" />
"""
profile = login.sociallogin.profile(token)
#It is good practice to check if the token is valid
if login.accesstoken.validate(token):
    print '<div class="lr-profile-frame lr-input-style">'
    print '<div class="lr-profile-header">'
    if profile.get('ImageUrl') is not None:
        print '<span class="lr-image-frame">'
        print '<img src='+profile.get('ImageUrl')+' alt='+profile.get('FirstName')+'>'
        print '</span>'
    
    print '<div class="lr-heading">Hello, <span class="lr-user-name">'+str(profile.get('FullName'))+'</span></div>'
    print '<div class="lr-profile-info">'
    if profile.get('Email') is not None:
        for email in profile.get('Email'):
            print '<div class="lr-email-info">'
            print '<span class="lr-value lr-em">'+email['Value']+'</span>'
            print '</div>'
    print '<div class="lr-uid-info">'
    print '<span class="lr-label">UID: </span>'
    print '<span class="lr-value">'+profile.get('Uid')+'</span>'
    print '</div>'
    print '</div>'

    print '<div id="lr-profile" class="lr-frame lr-input-style lr-align-left" style="display:block">'
    if profile.get('Provider') is not None:
            print '<label class="lr-input-frame lr-inline">'
            print '<span class="lr-input-label">Provider</span>'
            print '<input type="text"  value="'+profile.get('Provider')+'">'
            print '</label>'
    if profile.get('FirstName') is not None:
        print '<label class="lr-input-frame lr-inline">'
        print '<span class="lr-input-label">First Name</span>'
        print '<input type="text"  value="'+profile.get('FirstName')+'">'
        print '</label>'
  
    print '</div>'

    print "<br>None of this information has been stored, it is only for your viewing purpose and remains " + \
        "confidential for the purpose of this demo."

    #We shouldn't post without explicit permission!
    #login.sociallogin.status_update("LoginRadius is pretty neat!")

else:
    #Something has gone wrong.
    print ("Something has gone wrong ")

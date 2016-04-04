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

#Essential package for LoginRadius to communicate
from LoginRadius import LoginRadius
from LoginRadius import LoginRadiusExceptions

#We need a request
import cgi

#Get the 'token' from the POST request
arguments = cgi.FieldStorage()
token = arguments.getvalue('token')

#Create the LoginRadius object with our API_secret and token
LoginRadius.API_SECRET = API_SECRET
login = LoginRadius(token)

print ("Content-Type: text/html\n\n")
print '<link href="style.css" rel="stylesheet" type="text/css" media="all" />'

#It is good practice to check if the token is valid
if login.access.valid():
    print '<div class="lr-profile-frame lr-input-style">'
    print '<div class="lr-profile-header">'
    if login.user.profile['ImageUrl'] is not None:
        print '<span class="lr-image-frame">'
	print '<img src='+login.user.profile['ImageUrl']+' alt='+login.user.profile['FirstName']+'>'
	print '</span>'
    
    print '<div class="lr-heading">Hello, <span class="lr-user-name">'+login.user.profile['FullName']+'</span></div>'
    print '<div class="lr-profile-info">'
    if login.user.profile['Email'] is not None:
        for email in login.user.profile['Email']:
            print '<div class="lr-email-info">'
            print '<span class="lr-value lr-em">'+email['Value']+'</span>'
            print '</div>'
    print '<div class="lr-uid-info">'
    print '<span class="lr-label">UID: </span>'
    print '<span class="lr-value">'+login.user.profile['Uid']+'</span>'
    print '</div>'
    print '</div>'

    print '<div id="lr-profile" class="lr-frame lr-input-style lr-align-left" style="display:block">'
    if login.user.profile['Provider'] is not None:
	print '<label class="lr-input-frame lr-inline">'
	print '<span class="lr-input-label">Provider</span>'

	print '<input type="text"  value="'+login.user.profile['Provider']+'">'
	print '</label>'
    if login.user.profile['FirstName'] is not None:
        print '<label class="lr-input-frame lr-inline">'
	print '<span class="lr-input-label">First Name</span>'
	print '<input type="text"  value="'+login.user.profile['FirstName']+'">'
	print '</label>'
    if login.user.profile['LastName'] is not None:
	print '<label class="lr-input-frame lr-inline">'
	print '<span class="lr-input-label">Last Name</span>'
	print '<input type="text"  value="'+login.user.profile['LastName']+'">'
	print '</label>'
    if login.user.profile['BirthDate'] is not None:
	print '<label class="lr-input-frame lr-inline">'
	print '<span class="lr-input-label">BirthDate</span>'
	print '<input type="text"  value="'+login.user.profile['BirthDate']+'">'
	print '</label>'
    if login.user.profile['LocalCountry'] is not None:
	print '<label class="lr-input-frame lr-inline">'
	print '<span class="lr-input-label">LocalCountry</span>'
	print '<input type="text"  value="'+login.user.profile['LocalCountry']+'">'
	print '</label>'
    if login.user.profile['City'] is not None:
	print '<label class="lr-input-frame lr-inline">'
	print '<span class="lr-input-label">City</span>'

	print '<input type="text"  value="'+login.user.profile['City']+'">'
	print '</label>'
    print '</div>'

    print "<br>None of this information has been stored, it is only for your viewing purpose and remains " + \
        "confidential for the purpose of this demo."

    #We shouldn't post without explicit permission!
    #login.user.status_update("LoginRadius is pretty neat!")

else:
    #Something has gone wrong.
    print login.error

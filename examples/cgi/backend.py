#!/usr/bin/python
#################################################
# Example Implementation of LoginRadius Class   #
#################################################
# This is an example on how to use LoginRadius  #
# Python SDK                                    #
#################################################
# Copyright 2013-2014 LoginRadius Inc.          #
# - www.LoginRadius.com                         #
#################################################
# This file is part of the LoginRadius SDK      #
# package.                                      #
#################################################

#Your API Secret
API_SECRET = "API SECRET HERE"

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
print ("Successfully made LoginRadius Object<br>")
print ("HTTP library: " + login.settings.library + "<br>")
print ("Raw Access Object: " + str(login.access.raw))

print ("<br><br> That's pretty neat! <br><br>")
print ("You can also access information as a parsed named tuple!<br>")
print ("Token: " + login.access.token + " Through which we access all API calls!<br>")
print ("Expires: " + login.access.expire + "<br>")
print ("Is this token still valid?(Not expired): " + str(login.access.valid()) + "<br>")

#It is good practice to check if the token is valid
if login.access.valid():

    #Print a hello message for our guest from their profile!
    print "Hello there, " + login.user.profile['FirstName'] + \
          "! You have successfully made a call to the LoginRadius API!<br><br>"
    try:
        likes = login.user.like
        print "Here is a some of things you like according to your profile!:<br>"

        #Limit to three likes
        for like in likes[:3]:
            print like['Name'] + "<br>"

    except LoginRadiusExceptions:
        print login.error

    print "<br>None of this information has been stored, it is only for your viewing purpose and remains " + \
        "confidential for the purpose of this demo."

    #We shouldn't post without explicit permission!
    #login.user.status_update("LoginRadius is pretty neat!")

else:
    #Something has gone wrong.
    print login.error

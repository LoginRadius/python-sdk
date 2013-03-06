#!/usr/bin/python
#################################################
# Example Implementation of LoginRadius Class   #
#################################################
# This is an example on how to use LoginRadius  #
# Python SDK                                    #
#################################################
# Copyright 2013 LoginRadius Inc.               #
# - www.LoginRadius.com                         #
#################################################
# This file is part of the LoginRadius SDK      #
# package.                                      #
#################################################

#Your API Secret
API_SECRET="LoginRadius-API-secret-goes-here"

#Essential package for LoginRadius to communicate
from LoginRadius import LoginRadius

#We need a GET request
import cgi

#Get the 'token' from the GET request ?token='some value'
arguments = cgi.FieldStorage()
Token = arguments.getvalue('token')

#Create the LoginRadius Object
login = LoginRadius(API_SECRET, Token)

print "Content-Type: text/html\n\n"
print "Successfully made LoginRadius Object<br>"
print "token: " + login.token + "<br>"
print "library: " + login.library + "<br>"

#Let us try getting the user's profile information
profile = login.loginradius_get_data()

#Print a hello message for our guest!
print "Hello there, " + profile['FirstName']+ "! You have successfully made a call to the LoginRadius API!<br>"


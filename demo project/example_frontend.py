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

#Callback to your backend. 
CALLBACK_URL="Your-website-callback-URL"

#Print out our example iframe
print "Content-Type: text/html\n\n"
print "<html>"
print "<head>"
print "<title>LoginRadius - Example</title>"
print "</head>"
print "<body>"
print "<iframe src=\"http://hub.loginradius.com/Control/PluginSlider.aspx?apikey=" + "LoginRadius-API-Key" + "&callback=" + CALLBACK_URL + "\" width=\"200\" height=\"70\" frameborder=\"0\" scrolling=\"no\"></iframe>"
print "</body>"
print "</html>"

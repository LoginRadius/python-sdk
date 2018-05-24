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
CALLBACK_URL = "http://______________frontend.py"

#Print out our example Interface
print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Python Demo</title>')
print ('<link href="style.css" rel="stylesheet" type="text/css" media="all" />')
print ('<link href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css" rel="stylesheet" />')
print ('<script src="//code.jquery.com/jquery-2.2.1.min.js"></script>')
print ('<script src="//auth.lrcontent.com/v2/js/LoginRadiusV2.js"></script>')
print ('<script type="text/javascript">var commonOptions = {};commonOptions.apiKey = "' + API_KEY + '";commonOptions.verificationUrl = window.location.origin+window.location.pathname;commonOptions.resetPasswordUrl = window.location.origin+window.location.pathname;commonOptions.formValidationMessage = true;commonOptions.hashTemplate = true;</script>')
print ('<script src="LoginRadiusFrontEnd.js"></script>')
print ('<script type="text/javascript">var logout_options= {};logout_options.onSuccess = function(response) {window.location="'+ CALLBACK_URL +'"};LRObject.util.ready(function() {LRObject.init("logout", logout_options);});</script>')
print ('</head>')
print ('<div>')
print ('<span>Redirecting to front page</span>')
print ('</div>')
print ('</html>')

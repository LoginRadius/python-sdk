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

"""
API Key and Callback to your backend.
In this case: example_backend.py

You must change these!

You can find your API key here:
https://secure.loginradius.com/account#dashboard
"""
CALLBACK_URL = "http://_____/backend.py"
API_KEY = "API KEY HERE"

#Print out our example Interface
print "Content-Type: text/html;charset=utf-8\r\n\r\n"
print '<html>'
print '<head>'
print '<title>LoginRadius - Example</title>'
print '<script src="http://hub.loginradius.com/include/js/LoginRadius.js"></script>'
print '<script type="text/javascript">var options={};options.login=true;LoginRadius_SocialLogin.util.ready(function () { $ui = LoginRadius_SocialLogin.lr_login_settings;$ui.interfacesize = "";$ui.apikey = "' + API_KEY + '";$ui.callback="'+ CALLBACK_URL +'"; $ui.lrinterfacecontainer ="interfacecontainerdiv"; LoginRadius_SocialLogin.init(options);  }); </script>'
print '</head>'
print '<body>'
print '<div id="interfacecontainerdiv" class="interfacecontainerdiv"></div>'
print '</body>'
print '</html>'

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

"""
API Key and Callback to your backend.
In this case: example_backend.py

You must change these!

You can find your API key here:
https://secure.loginradius.com/account#dashboard
"""
CALLBACK_URL = "http://______________backend.py"
API_KEY = "YOUR_API_KEY"

#Print out our example Interface
print "Content-Type: text/html;charset=utf-8\r\n\r\n"
print '<html>'
print '<head>'
print '<title>LoginRadius - Example</title>'
print '<link href="style.css" rel="stylesheet" type="text/css" media="all" />'
print '<script src="http://code.jquery.com/jquery-2.2.1.min.js"></script>'
print '<script src="https://auth.lrcontent.com/v2/js/LoginRadiusV2.js"></script>'
print '<script type="text/javascript">var raasoption = {};raasoption.apiKey = "' + API_KEY +'";raasoption.v2Recaptcha = true;raasoption.verificationUrl  = window.location.origin+window.location.pathname;raasoption.forgotPasswordUrl = window.location.origin+window.location.pathname;raasoption.formValidationMessage = true;raasoption.hashTemplate = true;</script>'
print '<script src="LoginRadiusFrontEnd.js"></script>'
print '</head>'
print '<body>'
print '<script type="text/html" id="loginradiuscustom_tmpl"><a class="lr-provider-label" href="javascript:void(0)" onclick="return  LRObject.util.openWindow(\'<#= Endpoint #>\');" title="<#= Name #>" alt="Sign in with <#=Name#>">Login with <#=Name#></a><br></script>'
print '<div class="main-nav">'
print '<div class="container">'
print '<div class="logo-box">'
print '<h1 class="logo">'
print 'LoginRadius'
print '</h1>'
print ' <div class="site-description">user registration demo</div>'
print '</div>'
print '</div>'
print '</div>'
print '<div class="messages" style="display:none">'
print '<ul>'
print '<li class="messageinfo">'
print '</li>'
print '<div class="clear"></div>'
print '</ul>'
print '</div>'
print '<div class="lr-frame lr-input-style">'
print '<div class="lr-heading">Login with</div>'
print '<div class="lr-login-buttons-frame lr-space-fix">'
print '<div class="interfacecontainerdiv"></div>'
print '</div>'
print '<div id="lr-sign-in" class="lr-traditional-frame lr-pos-r lr-trad-login">'
print '<div class="lr-heading lr-small lr-pos-a lr-or-bubble"><span>Or with email</span></div>'
print '<div class="lr-form-frame lr-align-left">'
print '<div id="login-container"></div>'
print '<div class="lr-submit-frame lr-align-right">'
print '<span class="lr-link-frame lr-pull-left">'
print '<span class="lr-link lr-register" data-form="lr-register"><a>Register</a></span>'
print '<span class="lr-link lr-forgot-pass" data-form="lr-forgot-pw"><a>Forgot Password?</a></span>'
print '</span>'
print '</div>'
print '<div style="clear: both"></div>'
print '</div>'
print '</div>'
print '<div id="lr-register" class="lr-traditional-frame lr-trad-register lr-pos-r">'
print '<div class="lr-heading lr-small lr-pos-a lr-or-bubble"><span>Or create your account</span></div>'
print '<div class="lr-form-frame lr-align-left">'
print '<div id="registeration-container">'
print '</div>'
print '<div class="lr-submit-frame lr-align-right">'
print '<span class="lr-link-frame lr-pull-left">'
print '<span class="lr-link lr-sign-in" data-form="lr-sign-in"><a>Sign In</a></span>'
print '<span class="lr-link lr-forgot-pass" data-form="lr-forgot-pw"><a>Forgot Password?</a></span>'
print '</span>'
print '</div>'
print '<div style="clear: both"></div>'
print '</div>'
print '</div>'
print '<div id="lr-social-register" class="lr-traditional-frame lr-social-register lr-pos-r">'
print '<div class="lr-heading lr-small lr-pos-a lr-or-bubble"><span>Complete your profile to Register</span></div>'
print '<div class="lr-form-frame lr-align-left">'
print '<div id="social-registration-container">'
print '</div>'
print ' <div class="lr-submit-frame lr-align-right">'
print '<span class="lr-link-frame lr-pull-left">'
print '<span class="lr-link lr-sign-in" data-form="lr-sign-in"><a>Sign In</a></span>'
print '<span class="lr-link lr-forgot-pass" data-form="lr-forgot-pw"><a>Forgot Password?</a></span>'
print '</span>'
print '</div>'
print '<div style="clear: both"></div>'
print '</div>'
print '</div>'
print '<div id="lr-forgot-pw" class="lr-traditional-frame lr-pos-r lr-trad-forgot-pw">'
print '<div class="lr-heading lr-small lr-pos-a lr-or-bubble"><span>Forgot Password</span></div>'
print '<div class="lr-form-frame lr-align-left">'
print '<div id="forgotpassword-container">'
print '</div>'
print '<div class="lr-submit-frame lr-align-right">'
print '<span class="lr-link-frame lr-pull-left">'
print '<span class="lr-link lr-sign-in" data-form="lr-sign-in"><a>Sign In</a></span>'
print '<span class="lr-link lr-register" data-form="lr-register"><a>Register</a></span>'
print '</span>'
print ' </div>'
print '<div style="clear: both"></div>'
print '</div>'
print ' </div>'
print ' <div id="lr-reset-pw" class="lr-traditional-frame lr-pos-r lr-trad-reset-pw">'
print ' <div class="lr-heading lr-small lr-pos-a lr-or-bubble"><span>Reset Password</span></div>'
print ' <div class="lr-form-frame lr-align-left">'
print ' <div id="resetpassword-container">'
print '</div>'
print '<div class="lr-submit-frame lr-align-right">'
print '<span class="lr-link-frame lr-pull-left">'
print '<span class="lr-link lr-sign-in" data-form="lr-sign-in"><a>Sign In</a></span>'
print '<span class="lr-link lr-register" data-form="lr-register"><a>Register</a></span>'
print '</span>'
print '</div>'
print '<div style="clear: both"></div>'
print '</div>'
print '</div>'
print '</div>'
print '</body>'
print '</html>'

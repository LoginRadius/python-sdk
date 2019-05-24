#!/usr/bin/python
#################################################
# Class for User Registration                   #
#################################################
# This is the main class to communicate with    #
# LoginRadius' Unified User Registration API.
#                                               #
# Please note that some API calls are for       #
# premium or enterprise members only.           #
# In which case, an exception will be raised.   #
#################################################
# Copyright 2017-2018 LoginRadius Inc.          #
# - www.LoginRadius.com                         #
#################################################
# This file is part of the LoginRadius SDK      #
# package.                                      #
#################################################


class LoginRadiusExceptions(Exception):
    """
    This is the base for all LoginRadius Exceptions. Makes dealing with exceptions easy!
    """

    def __init__(self):
        pass

    def __str__(self):
        return ""


class Exceptions:
    """
    Common exceptions used by LoginRadius.
    """

    def __init__(self):
        pass

    class RequestsLibraryDated(LoginRadiusExceptions):
        """
        Raise exception if module requests is outdated.
        By default 0.12 is included in Python. We need at least version 2.0
        """

        def __init__(self, version):
            self.version = str(version)

        def __str__(self):
            return "LoginRadius needs at least requests 2.0, found: " \
                + self.version + "\nPlease upgrade to the latest version."

    class InvalidLibrary(LoginRadiusExceptions):
        """
        Raised on trying to change library to through _settings on invalid library argument.
        """

        def __init__(self, library):
            self.library = library

        def __str__(self):
            return "Invalid library string given. Got: " + str(self.library) + ". Valid cases: 'requests' or " + \
                "'urllib2'"

    class NoAPISecret(LoginRadiusExceptions):
        """
        Raised on construction of the LoginRadius object,
        if no API_SECRET has been set for the class.
        """
        def __init__(self):
            pass
			
        def __str__(self):
            return "No API_SECRET set. Please initialize a API_SECRET first.\n" \
                + "ie. LoginRadius.API_SECRET = \"Really_Secret_Key\""

    class NoAPIKey(LoginRadiusExceptions):
        	
        """
        Raised on construction of the LoginRadius object,
        if no API_KEY has been set for the class.
        """
        def __init__(self):
            pass
        			
        def __str__(self):		
            return "No API_KEY set. Please initialize a APP_KEY first.\n" \
                + "ie. LoginRadius.API_Key = \"Really_Application_Key\""

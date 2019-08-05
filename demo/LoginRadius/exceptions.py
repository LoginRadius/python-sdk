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
# Copyright 2019 LoginRadius Inc.               #
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

    class MissingJsonResponseParameter(LoginRadiusExceptions):
        """
        Raised if construction of namedtuple would fail
        because missing expected response from LoginRadius API.
        """

        def __init__(self, missing_parameter, raw=None):
            self.missing_parameter = missing_parameter
            self.raw = raw

        def __str__(self):
            exception_string = "Expected parameter from JSON response does not exist." + \
                " Expected: " + self.missing_parameter + " but was not in" + \
                " the dictionary."
            if self.raw:
                exception_string += " Instead, we got: " + str(self.raw)
                return exception_string

    class TokenExpired(LoginRadiusExceptions):
        """
        Raised if the request cannot be completed because the access token has expired.
        """

        def __init__(self, time):
            self.time = time

        def __str__(self):
            return "The request cannot be completed because the token has expired. " + \
                "The token expired on: " + self.time

    class FeatureNotSupported(LoginRadiusExceptions):
        """
        Raised if the request cannot be completed because your account/API access does not include this.
        """

        def __init__(self):
            pass

        def __str__(self):
            return "Your LoginRadius site doesn't have permission to access this endpoint, please contact " + \
                "LoginRadius support if you need more information."

    class UnknownJsonError(LoginRadiusExceptions):
        """
        Raised if cannot determine error number from Json
        """

        def __init__(self, result):
            self.result = result

        def __str__(self):
            return str(self.result)

    class APIKeyInvalid(LoginRadiusExceptions):
        """
        Raised if you entered your API wrong, or not at all.
        """

        def __init__(self):
            pass

        def __str__(self):
            return "The LoginRadius API Key is not valid, please double check your account."

    class APISecretInvalid(LoginRadiusExceptions):
        """
        Raised if you your API Secret is invalid.
        """

        def __init__(self):
            pass

        def __str__(self):
            return "The LoginRadius API Secret is not valid, please double check your account."

    class InvalidRequestToken(LoginRadiusExceptions):
        """
        Raised if you your request token is invalid from the POST request.
        """

        def __init__(self):
            pass

        def __str__(self):
            return "The LoginRadius Request Token is invalid, please verify the authentication response."

    class RequestTokenExpired(LoginRadiusExceptions):
        """
        Raised if you your request token has expired from the POST request.
        """

        def __init__(self):
            pass

        def __str__(self):
            return "The LoginRadius Request Token has expired, please verify the authentication response."

    class InvalidAccessToken(LoginRadiusExceptions):
        """
        Raised if you access token is invalid.
        """

        def __init__(self):
            pass

        def __str__(self):
            return "The LoginRadius Access Token has expired, please get a new token from the LoginRadius API."

    class ParameterMissing(LoginRadiusExceptions):
        """
        Raised if a parameter in the GET or POST request is missing.
        """

        def __init__(self):
            pass

        def __str__(self):
            return "A parameter is missing in the request, please check all parameters in the API call."

    class ParameterNotFormatted(LoginRadiusExceptions):
        """
        Raised if a parameter in the GET or POST request is not formatted properly for the provider.
        """

        def __init__(self):
            pass

        def __str__(self):
            return "A parameter is not formatted well in the request, please check all the parameters in the API call."

    class EndPointNotSupported(LoginRadiusExceptions):
        """
        Raised if a the endpoint is not supported by the provider which correlates to the token.
        """

        def __init__(self):
            pass

        def __str__(self):
            return "The requested endpoint is not supported by the current ID provider, " + \
                "please check the API support page at http://www.loginradius.com/datapoints"

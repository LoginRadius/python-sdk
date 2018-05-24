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

__author__ = "LoginRadius"
__copyright__ = "Copyright 2017-2018, LoginRadius"
__email__ = "developers@loginradius.com"
__status__ = "Production"
__version__ = "3.1.0"


tokenEndpoint = "/api/v2/access_token"

class AccessToken:
    
    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object
        
    def exchange(self, token):
        """The Access Token API is used to get the LoginRadius access token after authentication. It will be valid for the specific duration of time specified in the response"""
        payload = {'token': token, 'secret': self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + tokenEndpoint
        return self._lr_object._get_json(url, payload)
    
    def validate(self, access_token):
        """Token Validate( GET )"""
        payload = {'key': self._lr_object._get_api_key(), 'secret': self._lr_object._get_api_secret(),'access_token':access_token}
        url = self._lr_object.SECURE_API_URL + tokenEndpoint + "/Validate"
        return self._lr_object._get_json(url, payload)
    
    def invalidate(self, access_token):
        """Token Validate( GET )"""
        payload = {'key': self._lr_object._get_api_key(), 'secret': self._lr_object._get_api_secret(),'access_token':access_token}
        url = self._lr_object.SECURE_API_URL + tokenEndpoint + "/invalidate"
        return self._lr_object._get_json(url, payload)

    def refresh(self, access_token):
        """Token Validate( GET )"""
        payload = {'key': self._lr_object._get_api_key(), 'secret': self._lr_object._get_api_secret(),'access_token':access_token}
        url = self._lr_object.SECURE_API_URL + tokenEndpoint + "/refresh"
        return self._lr_object._get_json(url, payload)
    
    def getFacebookToken(self, fb_access_token):
        """Token Validate( GET )"""
        payload = {'key': self._lr_object._get_api_key(),'fb_access_token':fb_access_token}
        url = self._lr_object.SECURE_API_URL + tokenEndpoint + "/facebook"
        return self._lr_object._get_json(url, payload)

    def getTwitterToken(self, tw_access_token, tw_token_secret):
        """Token Validate( GET )"""
        payload = {'key': self._lr_object._get_api_key(),'tw_access_token':tw_access_token, 'tw_token_secret':tw_token_secret}
        url = self._lr_object.SECURE_API_URL + tokenEndpoint + "/twitter"
        return self._lr_object._get_json(url, payload)
        
        

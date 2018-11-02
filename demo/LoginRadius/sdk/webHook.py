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
__version__ = "3.2.0"


webHookEndpoint = "/api/v2/webhook/"

class WebHook:
    
    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object
        
    def subscribe(self, target_url, event):
        # WebHook Subscribe API (POST)
        payload ={'TargetUrl':target_url,'Event':event}
        params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+self._lr_object._get_api_secret()
        url = self._lr_object.SECURE_API_URL + webHookEndpoint  + "?" + params
        return self._lr_object._post_json(url, payload)
    
    def test(self):
        # Webhook Test (GET)
        payload = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + webHookEndpoint  + "test"
        return self._lr_object._get_json(url, payload)
    
    def unsubscribe(self, target_url, event):
        # WebHook Unsubscribe (DEL)
        payload ={'TargetUrl':target_url,'Event':event}
        params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+self._lr_object._get_api_secret()
        url = self._lr_object.SECURE_API_URL + webHookEndpoint  + "?" + params
        return self._lr_object._delete_json(url, payload)

    def getSubscribed(self, event):
        # Webhook Subscribed URLs (GET)
        payload = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret(), 'event': event}
        url = self._lr_object.SECURE_API_URL + webHookEndpoint
        return self._lr_object._get_json(url, payload)

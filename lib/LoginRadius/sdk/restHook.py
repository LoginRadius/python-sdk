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
__version__ = "3.0"


restHookEndpoint = "/api/v2/"

class RestHook:
    
    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object
        
    def subscribe(self, target_url, event):
        payload ={'target_url':target_url,'event':event}
        params = 'api_key='+self._lr_object._get_api_key() + '&api_secret='+self._lr_object._get_api_secret()
        url = self._lr_object.SECURE_API_URL + restHookEndpoint  + "resthook/subscribe?" + params
        return self._lr_object._post_json(url, payload)
    
    def aggregationQueryData(self, fromKey, to, first_data_point, stats_type):
        payload ={'firstDatapoint':first_data_point,'statsType':stats_type}
        params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+self._lr_object._get_api_secret()+'&from='+fromKey+'&to='+to
        url = self._lr_object.SECURE_API_URL + restHookEndpoint  + "insights?" + params
        return self._lr_object._post_json(url, payload)
    
    def userList(self, fromKey, select, where, orderby, skip, limit):
        payload ={'from':fromKey,'select':select,'where':where,'orderby':orderby,'skip':skip,'limit':limit}
        params = 'key='+self._lr_object._get_api_key() + '&secret='+self._lr_object._get_api_secret()
        url = self._lr_object.SECURE_API_URL + restHookEndpoint  + "resthook/identity?" + params
        return self._lr_object._post_json(url, payload)
    
    def settings(self):
        payload = {'api_key': self._lr_object._get_api_key(), 'api_secret': self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + restHookEndpoint  + "resthook/test"
        return self._lr_object._get_json(url, payload)
    
    def unsubscribe(self, target_url):
        payload ={'target_url':target_url}
        params = 'api_key='+self._lr_object._get_api_key() + '&api_secret='+self._lr_object._get_api_secret()
        url = self._lr_object.SECURE_API_URL + restHookEndpoint  + "resthook/unsubscribe?" + params
        return self._lr_object._delete_json(url, payload)

    def getSubscribed(self, event):
        payload = {'api_key': self._lr_object._get_api_key(), 'api_secret':self._lr_object._get_api_secret(), 'event': event}
        url = self._lr_object.SECURE_API_URL + restHookEndpoint + "resthook/subscription"
        return self._lr_object._get_json(url, payload)

    def getFields(self):
        payload = {'api_key': self._lr_object._get_api_key(), 'api_secret':self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + restHookEndpoint + "resthook/fields"
        return self._lr_object._get_json(url, payload)

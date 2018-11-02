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


accountEndpoint = "/identity/v2/manage/account/"

class CustomObject:
    
    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object
        
    def create(self, uid, objectName, payload):
        # Create Custom Object by UID (POST)
        params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+ self._lr_object._get_api_secret() + '&objectname='  +objectName
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "/customobject?" + params
        return self._lr_object._post_json(url, payload)
    
    def update(self, uid, objectRecordId, objectName, payload, updatetype = 'partialreplace'):
        # Custom Object Update by UID (PUT)
        params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+ self._lr_object._get_api_secret() + '&objectname='  +objectName + '&updatetype=' + updatetype
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "/customobject/"+objectRecordId+"?" + params
        return self._lr_object._put_json(url, payload)
    
    def getByUID(self, uid, objectName):
        # Custom Object By UID (GET)
        payload = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret(),'objectname':objectName}
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "/customobject"
        return self._lr_object._get_json(url, payload)
    
    def getByObjectRecordId(self, uid, objectRecordId, objectName):
        # Custom Object by ObjectRecordId and UID (GET)
        payload = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret(),'objectname':objectName}
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "/customobject/" +objectRecordId
        return self._lr_object._get_json(url, payload)

    def remove(self, uid, objectRecordId, objectName):
        # Delete Custom Object by ObjectRecordId (DEL)
        params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+ self._lr_object._get_api_secret() +'&objectname='  +objectName
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "/customobject/" + objectRecordId + "?" + params
        return self._lr_object._delete_json(url, {})

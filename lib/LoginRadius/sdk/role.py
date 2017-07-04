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


roleEndpoint = "/identity/v2/manage/";

class Role:
    
    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object
        
    def create(self, payload):
        params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+self._lr_object._get_api_secret()
        url = self._lr_object.SECURE_API_URL + roleEndpoint  + "role?" + params
        return self._lr_object._post_json(url, payload)
    
    def get(self):
        payload = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + roleEndpoint  + "role"
        return self._lr_object._get_json(url, payload)
    
    def remove(self, role):
        params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+self._lr_object._get_api_secret()
        url = self._lr_object.SECURE_API_URL + roleEndpoint  + "role/"+role +"?" + params
        return self._lr_object._delete_json(url, {})
    
    def unassignRoles(self, uid, rolePayload):
        params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+self._lr_object._get_api_secret()
        url = self._lr_object.SECURE_API_URL + roleEndpoint  + "account/"+ uid + "/role" + "?" + params
        return self._lr_object._delete_json(url, rolePayload)

    class Permission:
        def __init__(self, lr_object):
            """
            :param lr_object: this is the reference to the parent LoginRadius object.
            """
            self._lr_object = lr_object

        def add(self, role, payload):
            params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+self._lr_object._get_api_secret()
            url = self._lr_object.SECURE_API_URL + roleEndpoint  + "role/" +role+ "/permission?" + params
            return self._lr_object._put_json(url, payload)
    
        def remove(self, role, payload):
            params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+self._lr_object._get_api_secret()
            url = self._lr_object.SECURE_API_URL + roleEndpoint  + "role/" +role+ "/permission?" + params
            return self._lr_object._delete_json(url, payload)

    class Context:
        def __init__(self, lr_object):
            """
            :param lr_object: this is the reference to the parent LoginRadius object.
            """
            self._lr_object = lr_object

        def get(self, uid):
            """Get Context with Roles and Permissions( GET )"""
            payload = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            url = self._lr_object.SECURE_API_URL + roleEndpoint  + "account/" +uid+ "/rolecontext"
            return self._lr_object._get_json(url, payload)
    
        def add(self, uid, payload):
            """Add/Update Role Context with  Roles and Permissions( PUT )"""
            params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+self._lr_object._get_api_secret()
            url = self._lr_object.SECURE_API_URL + roleEndpoint  + "account/" +uid+ "/rolecontext?" + params
            return self._lr_object._put_json(url, payload)

        def delete(self, uid, rolecontextname):
            """Delete Role Context( DELETE )"""
            params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+self._lr_object._get_api_secret()
            url = self._lr_object.SECURE_API_URL + roleEndpoint  + "account/" +uid+ "/rolecontext/" +rolecontextname+ "/?" + params
            return self._lr_object._delete_json(url, {})

        def deleteRole(self, uid, rolecontextname, rolenamePayload):
            """Delete Role Context( DELETE )"""
            params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+self._lr_object._get_api_secret()
            url = self._lr_object.SECURE_API_URL + roleEndpoint  + "account/" +uid+ "/rolecontext/" +rolecontextname+ "/role?" + params
            return self._lr_object._delete_json(url, rolenamePayload)

        def deletePermission(self, uid, rolecontextname, additionalpermissionPayload):
            """Delete Role Context( DELETE )"""
            params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+self._lr_object._get_api_secret()
            url = self._lr_object.SECURE_API_URL + roleEndpoint  + "account/" +uid+ "/rolecontext/" +rolecontextname+ "/additionalpermission?" + params
            return self._lr_object._delete_json(url, additionalpermissionPayload) 
        

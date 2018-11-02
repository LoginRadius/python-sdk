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


class Configuration:
    
    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object
        
    def getConfiguration(self):
        # Get Configurations (GET)
        params = 'apikey='+self._lr_object._get_api_key()
        url = self._lr_object.CONFIG_API_URL + "ciam/appinfo"+ "?" + params
        return self._lr_object._get_json(url, {})  
    

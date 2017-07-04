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


accountEndpoint = "identity/v2/manage/account/"
archivedEndpoint = "/api/v2/identity/archived";

class Account:
    
    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object
        
    def create(self, payload):
        """Create Account( POST )"""
        params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+ self._lr_object._get_api_secret()
        url = self._lr_object.SECURE_API_URL + accountEndpoint + "?" + params
        return self._lr_object._post_json(url, payload)
            
    def update(self, uid, payload):
        """Create Account( POST )"""
        params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+ self._lr_object._get_api_secret()
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "?" + params
        return self._lr_object._put_json(url, payload)
    
    def remove(self, uid):
        """Account Delete( DELETE )"""
        params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+ self._lr_object._get_api_secret()
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "?" + params
        return self._lr_object._delete_json(url, {})
    
    def setPassword(self, uid, password):
        """Account Set Password( PUT )"""
        params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+ self._lr_object._get_api_secret()
        payload = {"password": password}
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "/password"+"?" + params
        return self._lr_object._put_json(url, payload)
    
    def getPassword(self, uid):
        payload = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "/password"
        return self._lr_object._get_json(url, payload)
    
    def invalidateVerificationEmail(self, uid, verificationUrl = '', emailTemplate = ''):
        payload = '?apikey='+ self._lr_object._get_api_key() + '&apisecret='+ self._lr_object._get_api_secret() + '&verificationUrl=' + verificationUrl + "&emailTemplate=" +emailTemplate
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "/invalidateemail"
        return self._lr_object._put_json(url+payload, {})
    
    def getDeletedAccountByEmail(self, email):
        payload = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret(), 'email':email}
        url = self._lr_object.SECURE_API_URL + archivedEndpoint
        return self._lr_object._get_json(url, payload)
    
    def getDeletedAccountByPhone(self, phone):
        payload = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret(), 'phone':phone}
        url = self._lr_object.SECURE_API_URL + archivedEndpoint
        return self._lr_object._get_json(url, payload)
    
    def getDeletedAccountByUid(self, uid):
        payload = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret(), 'uid':uid}
        url = self._lr_object.SECURE_API_URL + archivedEndpoint
        return self._lr_object._get_json(url, payload)
    
    def assignRole(self, uid, payload):
        """Put Assign Role( PUT )"""
        params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+ self._lr_object._get_api_secret()
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "/role"+"?" + params
        return self._lr_object._put_json(url, payload)
    
    def getRoleByUid(self, uid):
        payload = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "/role"
        return self._lr_object._get_json(url, payload)
    
    def updateSecurityQuestion(self, uid, payload):
        params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+self._lr_object._get_api_secret()
        url = self._lr_object.SECURE_API_URL + accountEndpoint  + uid + "?" + params
        return self._lr_object._put_json(url, payload)
    
    def getForgotPasswordToken(self, email):
        payload = {"email":email}
        params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+self._lr_object._get_api_secret()
        url = self._lr_object.SECURE_API_URL + accountEndpoint + "forgot/token?" + params
        return self._lr_object._post_json(url, payload)
    
    def getEmailVerificationToken(self, email):
        payload = {"email":email}
        params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+self._lr_object._get_api_secret()
        url = self._lr_object.SECURE_API_URL + accountEndpoint + "verify/token?" + params
        return self._lr_object._post_json(url, payload)
    
    def getAccessToken(self, uid):
        payload = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret(),'uid':uid}
        url = self._lr_object.SECURE_API_URL + accountEndpoint + "/access_token"
        return self._lr_object._get_json(url, payload)

    def resetPhoneIdVerification(self, uid):
        params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+self._lr_object._get_api_secret()
        url = self._lr_object.SECURE_API_URL + accountEndpoint  + uid + "/invalidatephone?" + params
        return self._lr_object._put_json(url, {})

    def getBackupCodeByUid(self, uid):
        payload = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret(),'uid':uid}
        url = self._lr_object.SECURE_API_URL + accountEndpoint  + "/2fa/backupcode"
        return self._lr_object._get_json(url, payload)

    def resetBackupCodeByUid(self, uid):
        payload = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret(),'uid':uid}
        url = self._lr_object.SECURE_API_URL + accountEndpoint  + "/2fa/backupcode/reset"
        return self._lr_object._get_json(url, payload)
        
    
    class Profile:

        def __init__(self, lr_object):
            self._lr_object = lr_object
        
        def getByEmail(self, email):
            payload = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret(), 'email':email}
            url = self._lr_object.SECURE_API_URL + accountEndpoint 
            return self._lr_object._get_json(url, payload)
    
        def getByUsername(self, username):
            payload = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret(), 'username':username}
            url = self._lr_object.SECURE_API_URL + accountEndpoint
            return self._lr_object._get_json(url, payload)

        def getByPhone(self, phone):
            payload = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret(),'phone':phone}
            url = self._lr_object.SECURE_API_URL + accountEndpoint
            return self._lr_object._get_json(url, payload)
    
        def getByUid(self, uid):
            payload = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            url = self._lr_object.SECURE_API_URL + accountEndpoint + uid
            return self._lr_object._get_json(url, payload)

    class TwoFactor:

        def __init__(self, lr_object):
            self._lr_object = lr_object

        def removeAuthByUid(self, uid, authenticator):
            payload = {}
            payload[authenticator] = True
            params = 'apikey='+self._lr_object._get_api_key() + '&apisecret='+ self._lr_object._get_api_secret()+'&uid='+uid
            url = self._lr_object.SECURE_API_URL + accountEndpoint  + "2FA/authenticator?" + params
            return self._lr_object._delete_json(url, payload)
            

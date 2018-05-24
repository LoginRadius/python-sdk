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


accountEndpoint = "identity/v2/manage/account/"
registrationDataEndpoint = "identity/v2/manage/"
archivedEndpoint = "/api/v2/identity/archived";

class Account:
    
    
    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object
        
    def create(self, payload, fields = '*'):
        """Create Account( POST )"""
        headers  = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        params = 'fields='+fields
        url = self._lr_object.SECURE_API_URL + accountEndpoint + "?" + params
        return self._lr_object._post_json(url, payload, headers)
            
    def update(self, uid, payload, isNullSupport = False, fields = '*'):
        """Update Account( POST )"""
        headers  = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        params = 'nullsupport=' + isNullSupport + "&fields=" +fields
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "?" + params
        return self._lr_object._put_json(url, payload, headers)
    
    def remove(self, uid):
        """Account Delete( DELETE )"""
        headers  = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid
        return self._lr_object._delete_json(url, {}, headers)

    def generateSott(self, timediff = '10'):
        """Account generate sott( GET )"""
        headers  = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        params = 'timedifference='+timediff
        url = self._lr_object.SECURE_API_URL + accountEndpoint + "sott"+"?" + params
        return self._lr_object._get_json(url, {}, headers)
    
    def setPassword(self, uid, password):
        """Account Set Password( PUT )"""
        headers  = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        payload = {"password": password}
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "/password"+"?" + params
        return self._lr_object._put_json(url, payload, headers)
    
    def getPassword(self, uid):
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "/password"
        return self._lr_object._get_json(url, {}, headers)
    
    def invalidateVerificationEmail(self, uid, verificationUrl = '', emailTemplate = ''):
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        params = 'verificationUrl=' + verificationUrl + "&emailTemplate=" +emailTemplate
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "/invalidateemail"+"?" + params
        return self._lr_object._put_json(url, {}, headers)
    
    def getDeletedAccountByEmail(self, email):
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        payload = {'email':email}
        url = self._lr_object.SECURE_API_URL + archivedEndpoint
        return self._lr_object._get_json(url, payload, headers)
    
    def getDeletedAccountByPhone(self, phone):
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        payload = {'phone':phone}
        url = self._lr_object.SECURE_API_URL + archivedEndpoint
        return self._lr_object._get_json(url, payload, headers)
    
    def getDeletedAccountByUid(self, uid):
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        payload = {'uid':uid}
        url = self._lr_object.SECURE_API_URL + archivedEndpoint
        return self._lr_object._get_json(url, payload, headers)
    
    def assignRole(self, uid, payload):
        """Put Assign Role( PUT )"""
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "/role"
        return self._lr_object._put_json(url, payload, headers)
    
    def getRoleByUid(self, uid):
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "/role"
        return self._lr_object._get_json(url, {}, headers)
    
    def updateSecurityQuestion(self, uid, payload):
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + accountEndpoint  + uid
        return self._lr_object._put_json(url, payload, headers)
    
    def getForgotPasswordToken(self, email):
        payload = {"email":email}
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + accountEndpoint + "forgot/token"
        return self._lr_object._post_json(url, payload, headers)
    
    def getEmailVerificationToken(self, email):
        payload = {"email":email}
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + accountEndpoint + "verify/token"
        return self._lr_object._post_json(url, payload, headers)
    
    def getAccessToken(self, uid):
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        payload = {"uid":uid}
        url = self._lr_object.SECURE_API_URL + accountEndpoint + "access_token"
        return self._lr_object._get_json(url, payload, headers)

    def getIdentities(self, email, fields= '*'):
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        params = 'email=' + email + "&fields=" +fields
        url = self._lr_object.SECURE_API_URL + accountEndpoint + "identities"  + "?" + params
        return self._lr_object._get_json(url, {}, headers)

    def resetPhoneIdVerification(self, uid):
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + accountEndpoint  + uid + "/invalidatephone"
        return self._lr_object._put_json(url, {}, headers)

    def getBackupCodeByUid(self, uid):
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        payload = {"uid":uid}
        url = self._lr_object.SECURE_API_URL + accountEndpoint  + "2fa/backupcode"
        return self._lr_object._get_json(url, payload, headers)

    def resetBackupCodeByUid(self, uid):
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        payload = {"uid":uid}
        url = self._lr_object.SECURE_API_URL + accountEndpoint  + "2fa/backupcode/reset"
        return self._lr_object._get_json(url, payload, headers)
        
    
    class Profile:

        def __init__(self, lr_object):
            self._lr_object = lr_object
        
        def getByEmail(self, email, fields = '*'):
            headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            params = 'email=' + email + "&fields=" +fields
            url = self._lr_object.SECURE_API_URL + accountEndpoint + "?" + params
            return self._lr_object._get_json(url, {}, headers)
    
        def getByUsername(self, username, fields = '*'):
            headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            params = 'username=' + username + "&fields=" +fields
            url = self._lr_object.SECURE_API_URL + accountEndpoint + "?" + params
            return self._lr_object._get_json(url, {}, headers)

        def getByPhone(self, phone, fields = '*'):
            headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            params = 'phone=' + phone + "&fields=" +fields
            url = self._lr_object.SECURE_API_URL + accountEndpoint + "?" + params
            return self._lr_object._get_json(url, {}, headers)
    
        def getByUid(self, uid, fields = '*'):
            headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            params = "fields=" +fields
            url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "?" + params
            return self._lr_object._get_json(url, {}, headers)

    class TwoFactor:

        def __init__(self, lr_object):
            self._lr_object = lr_object

        def removeAuthByUid(self, uid, authenticator):
            payload = {}
            payload[authenticator] = True
            headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            params = 'uid='+uid
            url = self._lr_object.SECURE_API_URL + accountEndpoint  + "2FA/authenticator?" + params
            return self._lr_object._delete_json(url, payload, headers)

    class RegistrationData:

        def __init__(self, lr_object):
            self._lr_object = lr_object

        def addRegistrationData(self, payload):
            headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            url = self._lr_object.SECURE_API_URL + registrationDataEndpoint  + "registrationdata"
            return self._lr_object._post_json(url, payload, headers)

        def getRegistrationDataServer(self, datasourcetype, parentid='', skip = '', limit = ''):
            headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            params = 'parentid='+ parentid+'&skip='+ skip+'&limit='+ limit
            url = self._lr_object.SECURE_API_URL + registrationDataEndpoint + "registrationdata/" + datasourcetype + "?" + params
            return self._lr_object._get_json(url, {}, headers)

        def updateRegistrationData(self, recordid, payload):
            """Update Registration Data( PUT )"""
            headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            url = self._lr_object.SECURE_API_URL + registrationDataEndpoint + "registrationdata/" + recordid
            return self._lr_object._put_json(url, payload, headers)

        def deleteRegistrationData(self, recordid):
            """Delete Registration Data( delete )"""
            headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            url = self._lr_object.SECURE_API_URL + registrationDataEndpoint + "registrationdata/" + recordid
            return self._lr_object._delete_json(url, {}, headers)
            

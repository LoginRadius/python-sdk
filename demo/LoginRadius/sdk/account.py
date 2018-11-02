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
        # Account Create (POST)
        headers  = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        params = 'fields='+fields
        url = self._lr_object.SECURE_API_URL + accountEndpoint + "?" + params
        return self._lr_object._post_json(url, payload, headers)
            
    def update(self, uid, payload, isNullSupport = False, fields = '*'):
        # Account Update (PUT)
        headers  = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        params = 'nullsupport=' + str(isNullSupport) + "&fields=" +fields
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "?" + params
        return self._lr_object._put_json(url, payload, headers)
    
    def remove(self, uid):
        # Account Delete (DEL)
        headers  = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid
        return self._lr_object._delete_json(url, {}, headers)

    def generateSott(self, timediff = '10'):
        # Generate SOTT (GET)
        headers  = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        params = 'timedifference='+timediff
        url = self._lr_object.SECURE_API_URL + accountEndpoint + "sott"+"?" + params
        return self._lr_object._get_json(url, {}, headers)
    
    def setPassword(self, uid, password):
        # Account Set Password (PUT)
        headers  = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        payload = {"password": password}
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "/password"
        return self._lr_object._put_json(url, payload, headers)
    
    def getPassword(self, uid):
        # Account Password (GET)
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "/password"
        return self._lr_object._get_json(url, {}, headers)
    
    def invalidateVerificationEmail(self, uid, verificationUrl = '', emailTemplate = ''):
        # Account Invalidate Verification Email (PUT)
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
    
    def updateSecurityQuestion(self, uid, payload):
        # Account Update Security Question Configuration (PUT)
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + accountEndpoint  + uid
        return self._lr_object._put_json(url, payload, headers)
    
    def getForgotPasswordToken(self, email):
        # Forgot Password Token (POST)
        payload = {"email":email}
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + accountEndpoint + "forgot/token"
        return self._lr_object._post_json(url, payload, headers)
    
    def getEmailVerificationToken(self, email):
        # Email Verification Token (POST)
        payload = {"email":email}
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + accountEndpoint + "verify/token"
        return self._lr_object._post_json(url, payload, headers)
    
    def getAccessToken(self, uid):
        # Access Token based on UID or User impersonation API (GET)
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        params = 'uid=' + uid
        url = self._lr_object.SECURE_API_URL + accountEndpoint + "access_token" + "?" + params
        return self._lr_object._get_json(url, {}, headers)

    def getIdentities(self, email, fields= '*'):
        # Account Identities by Email (GET)
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        params = 'email=' + email + "&fields=" +fields
        url = self._lr_object.SECURE_API_URL + accountEndpoint + "identities"  + "?" + params
        return self._lr_object._get_json(url, {}, headers)

    def resetPhoneIdVerification(self, uid):
        # Reset phone ID verification (PUT)
        headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + accountEndpoint  + uid + "/invalidatephone"
        return self._lr_object._put_json(url, {}, headers)

    def removeEmail(self, uid, email):
        # Account Email Delete (DEL)
        payload = {'email':email}
        headers  = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
        url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + '/email'
        return self._lr_object._delete_json(url, payload, headers)
        
    
    class Profile:

        def __init__(self, lr_object):
            self._lr_object = lr_object
        
        def getByEmail(self, email, fields = '*'):
            # Account Profiles by Email (GET)
            headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            params = 'email=' + email + "&fields=" +fields
            url = self._lr_object.SECURE_API_URL + accountEndpoint + "?" + params
            return self._lr_object._get_json(url, {}, headers)
    
        def getByUsername(self, username, fields = '*'):
            # Account Profiles by Username (GET)
            headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            params = 'username=' + username + "&fields=" +fields
            url = self._lr_object.SECURE_API_URL + accountEndpoint + "?" + params
            return self._lr_object._get_json(url, {}, headers)

        def getByPhone(self, phone, fields = '*'):
            # Account Profile by Phone ID (GET)
            headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            params = 'phone=' + phone + "&fields=" +fields
            url = self._lr_object.SECURE_API_URL + accountEndpoint + "?" + params
            return self._lr_object._get_json(url, {}, headers)
    
        def getByUid(self, uid, fields = '*'):
            # Account Profiles by UID (GET)
            headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            params = "fields=" +fields
            url = self._lr_object.SECURE_API_URL + accountEndpoint + uid + "?" + params
            return self._lr_object._get_json(url, {}, headers)

    class TwoFactor:

        def __init__(self, lr_object):
            self._lr_object = lr_object

        def removeAuthByUid(self, uid, authenticator):
            # MFA Reset Google Authenticator By UID (DEL) & MFA Reset SMS Authenticator By UID (DEL)
            payload = {}
            payload[authenticator] = True
            headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            params = 'uid='+uid
            url = self._lr_object.SECURE_API_URL + accountEndpoint  + "2FA/authenticator?" + params
            return self._lr_object._delete_json(url, payload, headers)

        def getBackupCodeByUid(self, uid):
            # MFA Backup Code by UID (GET)
            headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            payload = {"uid":uid}
            url = self._lr_object.SECURE_API_URL + accountEndpoint  + "2fa/backupcode"
            return self._lr_object._get_json(url, payload, headers)

        def resetBackupCodeByUid(self, uid):
            # MFA Reset Backup Code by UID (GET)
            headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            payload = {"uid":uid}
            url = self._lr_object.SECURE_API_URL + accountEndpoint  + "2fa/backupcode/reset"
            return self._lr_object._get_json(url, payload, headers)

    class RegistrationData:

        def __init__(self, lr_object):
            self._lr_object = lr_object

        def addRegistrationData(self, payload):
            # Add Registration Data (POST)
            headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            url = self._lr_object.SECURE_API_URL + registrationDataEndpoint  + "registrationdata"
            return self._lr_object._post_json(url, payload, headers)

        def getRegistrationDataServer(self, datasourcetype, parentid='', skip = '', limit = ''):
            # Get Registration Data (GET)
            headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            params = 'parentid='+ parentid+'&skip='+ skip+'&limit='+ limit
            url = self._lr_object.SECURE_API_URL + registrationDataEndpoint + "registrationdata/" + datasourcetype + "?" + params
            return self._lr_object._get_json(url, {}, headers)

        def updateRegistrationData(self, recordid, payload):
            # Update Registration Data (PUT)
            headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            url = self._lr_object.SECURE_API_URL + registrationDataEndpoint + "registrationdata/" + recordid
            return self._lr_object._put_json(url, payload, headers)

        def deleteRegistrationData(self, recordid):
            # Delete Registration Data (DEL)
            headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            url = self._lr_object.SECURE_API_URL + registrationDataEndpoint + "registrationdata/" + recordid
            return self._lr_object._delete_json(url, {}, headers)

        def deleteAllRecordsByDatasource(self, datasourcetype):
            # Delete All Records by Datasource (DEL)
            headers = {'apikey': self._lr_object._get_api_key(), 'apisecret': self._lr_object._get_api_secret()}
            url = self._lr_object.SECURE_API_URL + registrationDataEndpoint + "registrationdata/type/" + datasourcetype
            return self._lr_object._delete_json(url, {}, headers)
            

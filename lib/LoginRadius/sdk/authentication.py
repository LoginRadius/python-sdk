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


authEndpoint = "identity/v2/auth/"

class Authentication:
    
    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object
        
    def register(self, payload, verificationUrl = '', emailTemplate = '', getLRServerTime = False):
        """User Registration( POST )"""
        from LoginRadius.sdk.sott import SOTT
        sottAPI = SOTT(self._lr_object)
        
        sott = sottAPI.encrypt('10', getLRServerTime)
        params = 'apikey='+self._lr_object._get_api_key() +'&sott='+sott+'&verificationUrl='+verificationUrl+'&emailTemplate='+emailTemplate
        url = self._lr_object.SECURE_API_URL + authEndpoint + "register" + "?" + params
        return self._lr_object._post_json(url, payload)

    def getServerTime(self, timeDifference):
        if timeDifference != '':
            timeDifference = '10';
        payload = {'apikey': self._lr_object._get_api_key(), 'timedifference':timeDifference}
        url = self._lr_object.SECURE_API_URL  +  "identity/v2/serverinfo"
        return self._lr_object._get_json(url, payload)
    
    def captchaRegister(self, payload, verificationUrl = '', emailTemplate = ''):
        params = 'apikey='+self._lr_object._get_api_key() +'&verificationUrl='+verificationUrl+'&emailTemplate='+emailTemplate
        url = self._lr_object.SECURE_API_URL + authEndpoint + "register/captcha" + "?" + params
        return self._lr_object._post_json(url, payload)
    
    def resendEmailVerification(self, email, verificationUrl = '', emailTemplate = ''):
        """Resend Email Verification( PUT )"""
        payload ={'email':email}
        params = 'apikey='+self._lr_object._get_api_key() +'&verificationUrl='+verificationUrl+'&emailTemplate='+emailTemplate
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "register" + "?" + params
        return self._lr_object._put_json(url, payload)
    
    def removeAccountByEmailConfirmation(self, access_token, deleteUrl = '', emailTemplate = ''):
        """Delete Account With Email Confirmation( DELETE )"""
        params = 'apikey='+self._lr_object._get_api_key() +'&access_token='+access_token+'&verificationUrl='+deleteUrl+'&emailTemplate='+emailTemplate
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "account" + "?" + params
        return self._lr_object._delete_json(url, {})
    
    def forgotPassword(self, email, resetPasswordUrl, emailTemplate = ''):
        """Forgot Password( POST )"""
        payload ={'email':email}
        params = 'apikey='+self._lr_object._get_api_key() +'&resetPasswordUrl='+resetPasswordUrl+'&emailTemplate='+emailTemplate
        url = self._lr_object.SECURE_API_URL + authEndpoint + "password" + "?" + params
        return self._lr_object._post_json(url, payload)
    
    def resetPassword(self, resettoken, password):
        """Reset Password( PUT )"""
        payload ={'resettoken':resettoken, 'password':password}
        params = 'apikey='+self._lr_object._get_api_key()
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "password" + "?" + params
        return self._lr_object._put_json(url, payload)

    def resetPasswordbySecurityQuestion(self, securityanswer, userid, password):
        """Reset Password( PUT ) By SecurityQuestion"""
        payload ={'securityanswer':securityanswer, 'userid':userid, 'password':password}
        params = 'apikey='+self._lr_object._get_api_key()
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "password/securityanswer" + "?" + params
        return self._lr_object._put_json(url, payload)

    def updateSecurityQuestionByAccessToken(self, access_token, payload):
        """Update Security Question by Access_token( PUT )"""
        params = 'apikey='+self._lr_object._get_api_key()+'&access_token='+ access_token
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "account?" + params
        return self._lr_object._put_json(url, payload)
    
    def changePassword(self, access_token, oldpassword, newpassword):
        """Change Password( PUT )"""
        payload ={'oldpassword':oldpassword, 'newpassword':newpassword}
        params = 'apikey='+self._lr_object._get_api_key()+'&access_token='+ access_token
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "password" + "?" + params
        return self._lr_object._put_json(url, payload)
    
    def addEmail(self, access_token, email, emailtype, verificationUrl = '', emailTemplate = ''):
        """Add Email( POST )"""
        payload ={'email':email,'type':emailtype}
        params = 'apikey='+self._lr_object._get_api_key() +'&access_token='+access_token+'&emailTemplate='+emailTemplate+'&verificationUrl='+verificationUrl
        url = self._lr_object.SECURE_API_URL + authEndpoint + "email" + "?" + params
        return self._lr_object._post_json(url, payload)
    
    def removeEmail(self, access_token, deleteurl = '', emailtemplate = ''):
        """Delete Account With Email Confirmation( DELETE )"""
        params = 'apikey='+self._lr_object._get_api_key() +'&access_token='+access_token+'&deleteurl='+deleteurl+'&emailtemplate='+ emailtemplate
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "account" + "?" + params
        return self._lr_object._delete_json(url, {})

    def getVerifyEmail(self, verificationToken, url = ''):
        payload = {'apikey': self._lr_object._get_api_key(), 'verificationToken':verificationToken, 'url':url}
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'email'
        return self._lr_object._get_json(url, payload)
    
    def getCheckEmail(self, email):
        payload = {'apikey': self._lr_object._get_api_key(), 'email':email}
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'email'
        return self._lr_object._get_json(url, payload)
    
    def changeUsername(self, access_token, username):
        """Change Username( PUT )"""
        payload ={'username':username}
        params = 'apikey='+self._lr_object._get_api_key()+'&access_token='+ access_token
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "username" + "?" + params
        return self._lr_object._put_json(url, payload)
    
    def checkUsername(self, username):
        payload = {'apikey': self._lr_object._get_api_key(), 'username':username}
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'username'
        return self._lr_object._get_json(url, payload)
    
    def accountLink(self, access_token, candidateToken):
        """Change Username( PUT )"""
        payload ={'candidateToken':candidateToken}
        params = 'apikey='+self._lr_object._get_api_key()+'&access_token='+ access_token
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "socialIdentity" + "?" + params
        return self._lr_object._put_json(url, payload)

    def accountUnlink(self, access_token, provider, providerid):
        """Account Unlink( DELETE )"""
        payload ={'provider':provider, 'providerid':providerid}
        params = 'apikey='+self._lr_object._get_api_key() +'&access_token='+access_token
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "socialIdentity" + "?" + params
        return self._lr_object._delete_json(url, payload)
    
    def getSocialProfile(self, access_token):
        payload = {'apikey': self._lr_object._get_api_key(), 'access_token':access_token}
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'socialIdentity'
        return self._lr_object._get_json(url, payload)

    def tokenValidate(self, access_token):
        payload = {'apikey': self._lr_object._get_api_key(), 'access_token':access_token}
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'access_token/validate'
        return self._lr_object._get_json(url, payload)
    
    def tokenInvalidate(self, access_token):
        payload = {'apikey': self._lr_object._get_api_key(), 'access_token':access_token}
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'access_token/invalidate'
        return self._lr_object._get_json(url, payload)

    def securityQuestionByToken(self, access_token):
        payload = {'apikey': self._lr_object._get_api_key(), 'access_token':access_token}
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'securityquestion/accesstoken'
        return self._lr_object._get_json(url, payload)
    
    def securityQuestionByEmail(self, email):
        payload = {'apikey': self._lr_object._get_api_key(), 'email':email}
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'securityquestion/email'
        return self._lr_object._get_json(url, payload)

    def securityQuestionByUsername(self, username):
        payload = {'apikey': self._lr_object._get_api_key(), 'username':username}
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'securityquestion/username'
        return self._lr_object._get_json(url, payload)

    def securityQuestionByPhone(self, phone):
        payload = {'apikey': self._lr_object._get_api_key(), 'phone':phone}
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'securityquestion/phone'
        return self._lr_object._get_json(url, payload)

    def getBackupCode(self, access_token):
        payload = {'apikey': self._lr_object._get_api_key(), 'access_token':access_token}
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'account/2fa/backupcode'
        return self._lr_object._get_json(url, payload)

    def resetBackupCode(self, access_token):
        payload = {'apikey': self._lr_object._get_api_key(), 'access_token':access_token}
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'account/2fa/backupcode/reset'
        return self._lr_object._get_json(url, payload)

        
        


    class Login:

        def __init__(self, lr_object):
            self._lr_object = lr_object

        def byEmail(self, email, password, verificationUrl = '', loginUrl = '', emailTemplate = ''):
            payload = {'apikey': self._lr_object._get_api_key(), 'email':email, 'password':password, 'loginUrl':loginUrl, 'verificationUrl':verificationUrl,'emailTemplate':emailTemplate}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login'
            return self._lr_object._get_json(url, payload)

        def byUsername(self, username, password, verificationUrl = '', loginUrl = '', emailTemplate = ''):
            payload = {'apikey': self._lr_object._get_api_key(), 'username':username, 'password':password, 'loginUrl':loginUrl, 'verificationUrl':verificationUrl,'emailTemplate':emailTemplate}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login'
            return self._lr_object._get_json(url, payload)

        def byOTP(self, phone, otp, smstemplate = ''):
            payload = {'apikey': self._lr_object._get_api_key(), 'phone':phone, 'otp':otp, 'smstemplate':smstemplate}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login'
            return self._lr_object._get_json(url, payload)

        def byBackupCode(self, secondfactorauthenticationtoken, backupcode):
            payload = {'apikey': self._lr_object._get_api_key(), 'secondfactorauthenticationtoken':secondfactorauthenticationtoken, 'backupcode':backupcode}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login/2fa/backupcode'
            return self._lr_object._get_json(url, payload)

        def autoLoginByUsername(self, username, password, clientguid, autologinemailtemplate  = '', welcomeemailtemplate  = '', redirecturl  = ''):
            payload = {'apikey': self._lr_object._get_api_key(), 'clientguid':clientguid,'username':username, 'password':password, 'redirecturl':redirecturl , 'autologinemailtemplate':autologinemailtemplate,'welcomeemailtemplate':welcomeemailtemplate}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login/autologin'
            return self._lr_object._get_json(url, payload)

        def autoLoginByEmail(self, email, password, clientguid, autologinemailtemplate  = '', welcomeemailtemplate  = '', redirecturl  = ''):
            payload = {'apikey': self._lr_object._get_api_key(), 'clientguid':clientguid,'email':email, 'password':password, 'redirecturl':redirecturl , 'autologinemailtemplate':autologinemailtemplate,'welcomeemailtemplate':welcomeemailtemplate}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login/autologin'
            return self._lr_object._get_json(url, payload)

        def ping(self, clientguid):
            payload = {'apikey': self._lr_object._get_api_key(),'clientguid':clientguid}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login/autologin/ping'
            return self._lr_object._get_json(url, payload)

        def oneClickSignInByEmail(self, email, oneclicksignintemplate   = '', verificationurl   = ''):
            payload = {'apikey': self._lr_object._get_api_key(), 'email':email, 'oneclicksignintemplate':oneclicksignintemplate , 'verificationurl':verificationurl}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login/oneclicksignin'
            return self._lr_object._get_json(url, payload)

        def oneClickSignInByUsername(self, username, oneclicksignintemplate  = '', verificationurl  = ''):
            payload = {'apikey': self._lr_object._get_api_key(), 'username':username, 'oneclicksignintemplate':oneclicksignintemplate , 'verificationurl':verificationurl}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login/oneclicksignin'
            return self._lr_object._get_json(url, payload)

        def oneClickSignInVerification(self, verificationtoken, welcomeemailtemplate = ''):
            payload = {'apikey': self._lr_object._get_api_key(), 'verificationtoken':verificationtoken, 'welcomeemailtemplate':welcomeemailtemplate}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login/oneclickverify'
            return self._lr_object._get_json(url, payload)
        
    class Profile:
        
        def __init__(self, lr_object):
            self._lr_object = lr_object
            
        def getByToken(self, access_token):
            payload = {'apikey': self._lr_object._get_api_key(), 'access_token':access_token}
            url = self._lr_object.SECURE_API_URL + authEndpoint + "account"
            return self._lr_object._get_json(url, payload)
        
        def updateByToken(self, access_token, payload, verificationUrl = '', emailTemplate = ''):
            """Resend Email Verification( PUT )"""
            params = 'apikey='+self._lr_object._get_api_key() +'&access_token='+access_token+'&verificationUrl='+verificationUrl+'&emailTemplate='+emailTemplate
            url = self._lr_object.SECURE_API_URL + authEndpoint +  "account" + "?" + params
            return self._lr_object._put_json(url, payload)
    
    class CustomObject:

        def __init__(self, lr_object):
            self._lr_object = lr_object

        def create(self, access_token, objectName, payload):
            """Create Custom Object By Access Token( POST )"""
            params = 'apikey='+self._lr_object._get_api_key() +'&access_token='+access_token+'&objectName='+objectName
            url = self._lr_object.SECURE_API_URL + authEndpoint + "customobject" + "?" + params
            return self._lr_object._post_json(url, payload)

        def update(self, access_token, objectRecordId, objectName, payload, updatetype='partialreplace'):
            """Update Custom Object Data( PUT )"""
            params = 'apikey='+self._lr_object._get_api_key() +'&access_token='+access_token+'&objectname='+objectName+'&updatetype='+updatetype
            url = self._lr_object.SECURE_API_URL + authEndpoint +  "customobject/" + objectRecordId +"?" + params
            return self._lr_object._put_json(url, payload)
        
        def getByToken(self, access_token, objectName):
            payload = {'apikey': self._lr_object._get_api_key(), 'access_token':access_token, 'objectname':objectName}
            url = self._lr_object.SECURE_API_URL + authEndpoint + "customobject"
            return self._lr_object._get_json(url, payload)
        
        def getByID(self, access_token, objectRecordId, objectName):
            payload = {'apikey': self._lr_object._get_api_key(), 'access_token':access_token, 'objectname':objectName}
            url = self._lr_object.SECURE_API_URL + authEndpoint + "customobject/"+objectRecordId
            return self._lr_object._get_json(url, payload)
        
        def delete(self, access_token, objectRecordId, objectName):
            """Delete Custom Object Set( DELETE )"""
            params = 'apikey='+self._lr_object._get_api_key() +'&access_token='+access_token + '&objectname='+objectName
            url = self._lr_object.SECURE_API_URL + authEndpoint +  "customobject/" +objectRecordId + "?" + params
            return self._lr_object._delete_json(url, {})

    class TwoFactor:
        def __init__(self, lr_object):
            self._lr_object = lr_object

        def byToken(self, access_token, smsTemplate2FA = ''):
            """Get 2FA by Token( GET )"""
            payload = {'apikey': self._lr_object._get_api_key(), 'access_token':access_token, 'smsTemplate2FA':smsTemplate2FA}
            url = self._lr_object.SECURE_API_URL + authEndpoint + "account/2FA"
            return self._lr_object._get_json(url, payload)
        
        def phoneLogin(self, phone, password, loginUrl = '', verificationUrl = '', smsTemplate = '', smsTemplate2FA = ''):
            """Get 2FA Phone Login( GET )"""
            payload = {'apikey': self._lr_object._get_api_key(), 'phone':phone, 'password':password,'loginUrl':loginUrl,'verificationUrl':verificationUrl,'smsTemplate':smsTemplate,'smsTemplate2FA':smsTemplate2FA}
            url = self._lr_object.SECURE_API_URL + authEndpoint + "login/2FA"
            return self._lr_object._get_json(url, payload)
        
        def emailLogin(self, email, password, loginUrl = '', verificationUrl = '', emailTemplate = '', smsTemplate2FA = ''):
            """Get 2FA Phone Login( GET )"""
            payload = {'apikey': self._lr_object._get_api_key(), 'email':email, 'password':password,'loginUrl':loginUrl,'verificationUrl':verificationUrl,'emailTemplate':emailTemplate,'smsTemplate2FA':smsTemplate2FA}
            url = self._lr_object.SECURE_API_URL + authEndpoint + "login/2FA"
            return self._lr_object._get_json(url, payload)

        def usernameLogin(self, username, password, loginUrl = '', verificationUrl = '', emailTemplate = '', smsTemplate2FA = '', emailTemplate2FA = ''):
            """Get 2FA Phone Login( GET )"""
            payload = {'apikey': self._lr_object._get_api_key(), 'username':username, 'password':password,'loginUrl':loginUrl,'verificationUrl':verificationUrl,'emailTemplate':emailTemplate,'emailTemplate2FA':emailTemplate2FA}
            url = self._lr_object.SECURE_API_URL + authEndpoint + "login/2FA"
            return self._lr_object._get_json(url, payload)

        def updatePhone(self, secondFactorAuthenticationToken, phoneNo2FA, smsTemplate2FA = ''):
            """Update Custom Object Data( PUT )"""
            payload ={'phoneNo2FA':phoneNo2FA}
            params = 'apikey='+self._lr_object._get_api_key() +'&secondFactorAuthenticationToken='+secondFactorAuthenticationToken+'&smsTemplate2FA='+smsTemplate2FA
            url = self._lr_object.SECURE_API_URL + authEndpoint +  "login/2FA"  +"?" + params
            return self._lr_object._put_json(url, payload)

        def verifyGoogleAuth(self, secondFactorAuthenticationToken, googleAuthenticatorCode, otp, smsTemplate2FA = ''):
            """Get 2FA Verify Google Authenticator Code OR OTP( GET )"""
            payload = {'apikey': self._lr_object._get_api_key(), 'secondFactorAuthenticationToken':secondFactorAuthenticationToken, 'googleAuthenticatorCode':googleAuthenticatorCode,'otp':otp,'smsTemplate2FA':smsTemplate2FA}
            url = self._lr_object.SECURE_API_URL + authEndpoint + "login/2FA/Verification"
            return self._lr_object._get_json(url, payload)
        
        def updatePhoneByToken(self, access_token, phoneNo2FA, smsTemplate2FA = ''):
            """Update Custom Object Data( PUT )"""
            payload ={'phoneNo2FA':phoneNo2FA}
            params = 'apikey='+self._lr_object._get_api_key() +'&access_token='+access_token+'&smsTemplate2FA='+smsTemplate2FA
            url = self._lr_object.SECURE_API_URL + authEndpoint +  "account/2FA"  +"?" + params
            return self._lr_object._put_json(url, payload)
        
        def googleAuthByToken(self, access_token, googleAuthenticatorCode, otp, smsTemplate2FA = ''):
            """Get 2FA Verify Google Authenticator Code OR OTP( GET )"""
            payload = {'apikey': self._lr_object._get_api_key(), 'access_token':access_token, 'googleAuthenticatorCode':googleAuthenticatorCode,'otp':otp,'smsTemplate2FA':smsTemplate2FA}
            url = self._lr_object.SECURE_API_URL + authEndpoint + "account/2FA/Verification"
            return self._lr_object._get_json(url, payload)
            
        def removeAuthByToken(self, access_token, authenticator):
            """Delete Custom Object Set( DELETE )"""
            payload = {}
            payload[authenticator]= True
            params = 'apikey='+self._lr_object._get_api_key() +'&access_token='+access_token
            url = self._lr_object.SECURE_API_URL + authEndpoint +  "account/2FA/authenticator"  + "?" + params
            return self._lr_object._delete_json(url, payload)
        
        

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
        # User Registration by Email (POST)
        from LoginRadius.sdk.sott import SOTT
        sottAPI = SOTT(self._lr_object)        
        sott = sottAPI.encrypt('10', getLRServerTime)

        payload['sott'] = sott
        params = 'apikey='+self._lr_object._get_api_key()+'&verificationUrl='+verificationUrl+'&emailtemplate='+emailTemplate
        url = self._lr_object.SECURE_API_URL + authEndpoint + "register" + "?" + params
        return self._lr_object._post_json(url, payload)

    def getServerTime(self, timeDifference):
        # Get Server Time (GET)
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
        # Resend Email Verification (PUT)
        payload ={'email':email}
        params = 'apikey='+self._lr_object._get_api_key() +'&verificationUrl='+verificationUrl+'&emailTemplate='+emailTemplate
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "register" + "?" + params
        return self._lr_object._put_json(url, payload)
    
    def deleteAccountByEmailConfirmation(self, access_token, deleteUrl = '', emailTemplate = ''):
        # Delete Account with Email Confirmation (DEL)
        params = 'apikey='+self._lr_object._get_api_key() +'&access_token='+access_token+'&verificationUrl='+deleteUrl+'&emailTemplate='+emailTemplate
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "account" + "?" + params
        return self._lr_object._delete_json(url, {})
    
    def forgotPassword(self, email, resetPasswordUrl, emailTemplate = ''):
        # Forgot Password (POST)
        payload ={'email':email}
        params = 'apikey='+self._lr_object._get_api_key() +'&resetPasswordUrl='+resetPasswordUrl+'&emailTemplate='+emailTemplate
        url = self._lr_object.SECURE_API_URL + authEndpoint + "password" + "?" + params
        return self._lr_object._post_json(url, payload)
    
    def resetPassword(self, payload):
        # Reset Password by Reset Token (PUT)
        params = 'apikey='+self._lr_object._get_api_key()
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "password/reset" + "?" + params
        return self._lr_object._put_json(url, payload)

    def resetPasswordByOTP(self, payload):
        # Reset Password by OTP (PUT)
        params = 'apikey='+self._lr_object._get_api_key()
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "password/reset" + "?" + params
        return self._lr_object._put_json(url, payload)

    def resetPasswordBySecurityAnswerAndEmail(self, securityanswer, email, password):
        # Reset Password by Security Answer and Email (PUT)
        payload ={'securityanswer':securityanswer, 'email':email, 'password':password}
        params = 'apikey='+self._lr_object._get_api_key()
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "password/securityanswer" + "?" + params
        return self._lr_object._put_json(url, payload)

    def resetPasswordBySecurityAnswerAndPhone(self, securityanswer, phone, password):
        # Reset Password by Security Answer and Phone (PUT)
        payload ={'securityanswer':securityanswer, 'phone':phone, 'password':password}
        params = 'apikey='+self._lr_object._get_api_key()
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "password/securityanswer" + "?" + params
        return self._lr_object._put_json(url, payload)

    def resetPasswordBySecurityAnswerAndUsername(self, securityanswer, username, password):
        # Reset Password by Security Answer and UserName (PUT)
        payload ={'securityanswer':securityanswer, 'username':username, 'password':password}
        params = 'apikey='+self._lr_object._get_api_key()
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "password/securityanswer" + "?" + params
        return self._lr_object._put_json(url, payload)

    def updateSecurityQuestionByAccessToken(self, access_token, payload):
        # Update Security Question by Access token (PUT)
        params = 'apikey='+self._lr_object._get_api_key()+'&access_token='+ access_token
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "account?" + params
        return self._lr_object._put_json(url, payload)
    
    def changePassword(self, access_token, oldpassword, newpassword):
        # Change Password (PUT)
        payload ={'oldpassword':oldpassword, 'newpassword':newpassword}
        params = 'apikey='+self._lr_object._get_api_key()+'&access_token='+ access_token
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "password/change" + "?" + params
        return self._lr_object._put_json(url, payload)
    
    def addEmail(self, access_token, email, emailtype, verificationUrl = '', emailTemplate = ''):
        # Add Email (POST)
        payload ={'email':email,'type':emailtype}
        params = 'apikey='+self._lr_object._get_api_key() +'&access_token='+access_token+'&emailTemplate='+emailTemplate+'&verificationUrl='+verificationUrl
        url = self._lr_object.SECURE_API_URL + authEndpoint + "email" + "?" + params
        return self._lr_object._post_json(url, payload)
    
    def removeEmail(self, access_token, email):
        # Remove Email (DEL)
        params = 'apikey='+self._lr_object._get_api_key() +'&access_token='+access_token
        payload = {'email':email}
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "email" + "?" + params
        return self._lr_object._delete_json(url, payload)

    def getVerifyEmail(self, verificationToken, url='', welcomeemailtemplate=''):
        # Verify Email (GET)
        payload = {'apikey': self._lr_object._get_api_key(), 'verificationToken':verificationToken, 'url':url, 'welcomeemailtemplate':welcomeemailtemplate}
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'email'
        return self._lr_object._get_json(url, payload)

    def verifyEmailbyOTP(self, payload, url='', welcomeemailtemplate=''):
        # Verify Email by OTP (PUT)
        params = 'apikey=' + self._lr_object._get_api_key() + '&url=' + url + '&welcomeemailtemplate=' + welcomeemailtemplate
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'email' + '?' + params
        return self._lr_object._put_json(url, payload)
    
    def getCheckEmail(self, email):
        # Check Email Availability (GET)
        payload = {'apikey': self._lr_object._get_api_key(), 'email':email}
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'email'
        return self._lr_object._get_json(url, payload)
    
    def changeUsername(self, access_token, username):
        # Set or Change UserName (PUT)
        payload ={'username':username}
        params = 'apikey='+self._lr_object._get_api_key()+'&access_token='+ access_token
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "username" + "?" + params
        return self._lr_object._put_json(url, payload)
    
    def checkUsername(self, username):
        # Check Username Availability (GET)
        payload = {'apikey': self._lr_object._get_api_key(), 'username':username}
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'username'
        return self._lr_object._get_json(url, payload)
    
    def accountLink(self, access_token, candidateToken):
        # Link Social Identities (PUT)
        payload ={'candidateToken':candidateToken}
        params = 'apikey='+self._lr_object._get_api_key()+'&access_token='+ access_token
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "socialIdentity" + "?" + params
        return self._lr_object._put_json(url, payload)

    def accountUnlink(self, access_token, provider, providerid):
        # Unlink Social Identities (DEL)
        payload ={'provider':provider, 'providerid':providerid}
        params = 'apikey='+self._lr_object._get_api_key() +'&access_token='+access_token
        url = self._lr_object.SECURE_API_URL + authEndpoint +  "socialIdentity" + "?" + params
        return self._lr_object._delete_json(url, payload)
    
    def getSocialProfile(self, access_token, fields = '*'):
        # Social Identity (GET)
        params = 'apikey='+self._lr_object._get_api_key() +'&access_token='+access_token +'&fields='+fields
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'socialIdentity' + "?" + params
        return self._lr_object._get_json(url, {})

    def tokenValidate(self, access_token):
        # Validate Access Token (GET)
        payload = {'apikey': self._lr_object._get_api_key(), 'access_token':access_token}
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'access_token/validate'
        return self._lr_object._get_json(url, payload)
    
    def tokenInvalidate(self, access_token):
        # Invalidate Access Token (GET)
        payload = {'apikey': self._lr_object._get_api_key(), 'access_token':access_token}
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'access_token/invalidate'
        return self._lr_object._get_json(url, payload)

    def securityQuestionByToken(self, access_token):
        # Security Questions by Access Token (GET)
        payload = {'apikey': self._lr_object._get_api_key(), 'access_token':access_token}
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'securityquestion/accesstoken'
        return self._lr_object._get_json(url, payload)
    
    def securityQuestionByEmail(self, email):
        # Security Questions by Email (GET)
        payload = {'apikey': self._lr_object._get_api_key(), 'email':email}
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'securityquestion/email'
        return self._lr_object._get_json(url, payload)

    def securityQuestionByUsername(self, username):
        # Security Questions by Username (GET)
        payload = {'apikey': self._lr_object._get_api_key(), 'username':username}
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'securityquestion/username'
        return self._lr_object._get_json(url, payload)

    def securityQuestionByPhone(self, phone):
        # Security Questions by Phone (GET)
        payload = {'apikey': self._lr_object._get_api_key(), 'phone':phone}
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'securityquestion/phone'
        return self._lr_object._get_json(url, payload)

    def validateSecretCode(self, payload):
        # Validate secret code (POST)
        params = 'apikey='+self._lr_object._get_api_key()
        url = self._lr_object.SECURE_API_URL + authEndpoint + "registrationdata/validatecode" + "?" + params
        return self._lr_object._post_json(url, payload)

    def authGetRegistrationDataServer(self, datasourcetype, parentid='', skip = '', limit = ''):
        # Get Registration Data Server (GET)
        params = 'apikey='+self._lr_object._get_api_key()+'&parentid='+ parentid+'&skip='+ skip+'&limit='+ limit
        url = self._lr_object.SECURE_API_URL + authEndpoint + "registrationdata/" + datasourcetype + "?" + params
        return self._lr_object._get_json(url, {})

    def privacyPolicyAccept(self, access_token):
        # Privacy Policy Accept (GET)
        params = 'apikey='+self._lr_object._get_api_key() + '&access_token=' + access_token
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'privacypolicy/accept' + "?" + params
        return self._lr_object._get_json(url, {})

    def sendWelcomeEmail(self, access_token, welcomeemailtemplate=''):
        # Send Welcome Email (GET)
        params = 'apikey='+self._lr_object._get_api_key() + '&access_token=' + access_token + '&welcomeemailtemplate=' + welcomeemailtemplate
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'account/sendwelcomeemail' + "?" + params
        return self._lr_object._get_json(url, {})

    def deleteAccount(self, deletetoken):
        # Delete Account (GET)
        params = 'apikey='+self._lr_object._get_api_key() + '&deletetoken=' + deletetoken
        url = self._lr_object.SECURE_API_URL + authEndpoint + 'account/delete' + "?" + params
        return self._lr_object._get_json(url, {})


    class Login:

        def __init__(self, lr_object):
            self._lr_object = lr_object

        def byEmail(self, payload, verificationUrl = '', loginUrl = '', emailTemplate = '', gRecaptchaResponse = '', fields = '*'):
            # Login by Email (POST)
            params = 'apikey='+self._lr_object._get_api_key()+'&verificationurl='+verificationUrl+'&loginurl='+loginUrl+'&emailtemplate='+emailTemplate+'&g-recaptcha-response='+gRecaptchaResponse+'&fields='+fields
            url = self._lr_object.SECURE_API_URL + authEndpoint + "login" + "?" + params
            return self._lr_object._post_json(url, payload)

        def byUsername(self, payload, verificationUrl = '', loginUrl = '', emailTemplate = '', gRecaptchaResponse = '', fields = '*'):
            # Login by Username (POST)
            params = 'apikey='+self._lr_object._get_api_key() +'&verificationurl='+verificationUrl+'&loginurl='+loginUrl+'&emailtemplate='+emailTemplate+'&g-recaptcha-response='+gRecaptchaResponse+'&fields='+fields
            url = self._lr_object.SECURE_API_URL + authEndpoint + "login" + "?" + params
            return self._lr_object._post_json(url, payload)

        def byOTP(self, phone, otp, smstemplate  = ''):            
            payload = {'apikey': self._lr_object._get_api_key(), 'phone':phone, 'otp' : otp, 'smstemplate':smstemplate}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login'
            return self._lr_object._get_json(url, payload)

        def byBackupCode(self, secondfactorauthenticationtoken, backupcode):
            payload = {'apikey': self._lr_object._get_api_key(), 'secondfactorauthenticationtoken':secondfactorauthenticationtoken, 'backupcode':backupcode}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login/2fa/backupcode'
            return self._lr_object._get_json(url, payload)
        
        def passwordlessLoginByEmail(self, email, oneclicksignintemplate   = '', verificationurl   = ''):
            # Passwordless Login By Email (GET)
            payload = {'apikey': self._lr_object._get_api_key(), 'email':email, 'oneclicksignintemplate':oneclicksignintemplate , 'verificationurl':verificationurl}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login/passwordlesslogin/email'
            return self._lr_object._get_json(url, payload)

        def passwordlessLoginByUsername(self, username, oneclicksignintemplate  = '', verificationurl  = ''):
            # Passwordless Login By UserName (GET)
            payload = {'apikey': self._lr_object._get_api_key(), 'username':username, 'oneclicksignintemplate':oneclicksignintemplate , 'verificationurl':verificationurl}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login/passwordlesslogin/email'
            return self._lr_object._get_json(url, payload)

        def passwordlessLoginVerification(self, verificationtoken, welcomeemailtemplate = ''):
            # Passwordless Login Verification (GET)
            payload = {'apikey': self._lr_object._get_api_key(), 'verificationtoken':verificationtoken, 'welcomeemailtemplate':welcomeemailtemplate}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login/passwordlesslogin/email/verify'
            return self._lr_object._get_json(url, payload)

        def passwordlessLoginVerifyOTP(self, payload, smstemplate=''):
            # Phone Login Using One Time Passcode (PUT)
            params = '?apikey=' + self._lr_object._get_api_key() + '&smstemplate=' + smstemplate
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login/passwordlesslogin/otp/verify' + params
            return self._lr_object._put_json(url, payload)

        def passwordlessLoginSendOTP(self, phone, smstemplate = ''):
            # Phone Send One time Passcode (GET)
            params = '?apikey=' + self._lr_object._get_api_key() + '&phone=' + phone + '&smstemplate=' + smstemplate
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login/passwordlesslogin/otp' + params
            return self._lr_object._get_json(url, {})

        def smartLoginByEmail(self, email, clientguid, smartloginemailtemplate = '', welcomeemailtemplate  = '', redirecturl  = ''):
            # Smart Login By Email (GET)
            payload = {'apikey': self._lr_object._get_api_key(), 'email':email, 'clientguid':clientguid, 'redirecturl':redirecturl , 'smartloginemailtemplate':smartloginemailtemplate,'welcomeemailtemplate':welcomeemailtemplate}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login/smartlogin'
            return self._lr_object._get_json(url, payload)

        def smartLoginByUsername(self, username, clientguid, smartloginemailtemplate  = '', welcomeemailtemplate  = '', redirecturl  = ''):
            # Smart Login By Username (GET)
            payload = {'apikey': self._lr_object._get_api_key(), 'username':username, 'clientguid':clientguid, 'redirecturl':redirecturl , 'smartloginemailtemplate':smartloginemailtemplate,'welcomeemailtemplate':welcomeemailtemplate}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login/smartlogin'
            return self._lr_object._get_json(url, payload)     

        def smartLoginPing(self, clientguid):
            # Smart Login Ping (GET)
            payload = {'apikey': self._lr_object._get_api_key(),'clientguid':clientguid}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login/smartlogin/ping'
            return self._lr_object._get_json(url, payload)
    
        def smartLoginVerifyToken(self, verificationtoken, welcomeemailtemplate  = ''):
            # Smart Login Verify Token (GET)
            payload = {'apikey': self._lr_object._get_api_key(), 'verificationtoken':verificationtoken,'welcomeemailtemplate':welcomeemailtemplate}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'email/smartlogin'
            return self._lr_object._get_json(url, payload)

        def oneTouchLoginByEmail(self, email, clientguid, name = '', redirecturl  = '', noregistrationemailtemplate  = '', welcomeemailtemplate  = ''):
            # One Touch Login by Email (GET)
            payload = {'apikey': self._lr_object._get_api_key(), 'email':email, 'clientguid':clientguid, 'name':name, 'redirecturl':redirecturl , 'noregistrationemailtemplate':noregistrationemailtemplate,'welcomeemailtemplate':welcomeemailtemplate}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'onetouchlogin/email'
            return self._lr_object._get_json(url, payload)

        def oneTouchLoginByPhone(self, phone, clientguid, name = '', smstemplate  = ''):
            # One Touch Login by Phone (GET)
            payload = {'apikey': self._lr_object._get_api_key(), 'phone':phone, 'name':name, 'smstemplate':smstemplate}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'onetouchlogin/phone'
            return self._lr_object._get_json(url, payload)

        def oneTouchEmailVerification(self, verificationtoken, welcomeemailtemplate=''):
            # One Touch Email Verification (GET)
            params = '?apikey='+self._lr_object._get_api_key()+'&verificationtoken='+ verificationtoken + '&welcomeemailtemplate=' + welcomeemailtemplate
            url = self._lr_object.SECURE_API_URL + authEndpoint +  "email/smartlogin" + params
            return self._lr_object._get_json(url, {})

        def oneTouchOtpVerification(self, otp, phone, smstemplate = ''):
            # One Touch OTP Verification (PUT)
            payload ={'phone':phone}
            params = 'apikey='+self._lr_object._get_api_key()+'&otp='+ otp
            url = self._lr_object.SECURE_API_URL + authEndpoint +  "onetouchlogin/phone/verify" + "?" + params
            return self._lr_object._put_json(url, payload)

        
    class Profile:
        
        def __init__(self, lr_object):
            self._lr_object = lr_object
            
        def getByToken(self, access_token, fields = '*'):
            # Read all Profiles by Token (GET)
            payload = {'apikey': self._lr_object._get_api_key(), 'access_token':access_token, 'fields':fields}
            url = self._lr_object.SECURE_API_URL + authEndpoint + "account"
            return self._lr_object._get_json(url, payload)
        
        def updateByToken(self, access_token, payload, verificationUrl = '', emailTemplate = '', isNullSupport = False, fields = '*'):
            # Update Profile by Token (PUT)
            params = 'apikey='+self._lr_object._get_api_key() +'&access_token='+access_token+'&verificationUrl='+verificationUrl+'&emailTemplate='+emailTemplate + '&nullsupport=' + str(isNullSupport) + "&fields=" +fields
            url = self._lr_object.SECURE_API_URL + authEndpoint +  "account" + "?" + params
            return self._lr_object._put_json(url, payload)
    

    class CustomObject:

        def __init__(self, lr_object):
            self._lr_object = lr_object

        def create(self, access_token, objectName, payload):
            # Create Custom Object by Token (POST)
            params = 'apikey='+self._lr_object._get_api_key() +'&access_token='+access_token+'&objectName='+objectName
            url = self._lr_object.SECURE_API_URL + authEndpoint + "customobject" + "?" + params
            return self._lr_object._post_json(url, payload)

        def update(self, access_token, objectRecordId, objectName, payload, updatetype='partialreplace'):
            # Custom Object Update by Access Token (PUT)
            params = 'apikey='+self._lr_object._get_api_key() +'&access_token='+access_token+'&objectname='+objectName+'&updatetype='+updatetype
            url = self._lr_object.SECURE_API_URL + authEndpoint +  "customobject/" + objectRecordId +"?" + params
            return self._lr_object._put_json(url, payload)
        
        def getByToken(self, access_token, objectName):
            # Custom Object by Token (GET)
            payload = {'apikey': self._lr_object._get_api_key(), 'access_token':access_token, 'objectname':objectName}
            url = self._lr_object.SECURE_API_URL + authEndpoint + "customobject"
            return self._lr_object._get_json(url, payload)
        
        def getByID(self, access_token, objectRecordId, objectName):
            # Custom Object by ObjectRecordId and Token (GET)
            payload = {'apikey': self._lr_object._get_api_key(), 'access_token':access_token, 'objectname':objectName}
            url = self._lr_object.SECURE_API_URL + authEndpoint + "customobject/"+objectRecordId
            return self._lr_object._get_json(url, payload)
        
        def delete(self, access_token, objectRecordId, objectName):
            # Custom Object Delete by Record Id And Token (DEL)
            params = 'apikey='+self._lr_object._get_api_key() +'&access_token='+access_token + '&objectname='+objectName
            url = self._lr_object.SECURE_API_URL + authEndpoint +  "customobject/" +objectRecordId + "?" + params
            return self._lr_object._delete_json(url, {})

    class TwoFactor:
        def __init__(self, lr_object):
            self._lr_object = lr_object

        def byToken(self, access_token, smsTemplate2FA = ''):
            # MFA Validate Access Token (GET)
            payload = {'apikey': self._lr_object._get_api_key(), 'access_token':access_token, 'smsTemplate2FA':smsTemplate2FA}
            url = self._lr_object.SECURE_API_URL + authEndpoint + "account/2FA"
            return self._lr_object._get_json(url, payload)
        
        def phoneLogin(self, phone, password, loginUrl = '', verificationUrl = '', smsTemplate = '', smsTemplate2FA = '', emailTemplate = ''):
            # MFA Phone Login (POST)
            payload = {'phone':phone, 'password':password}
            params = '?apikey=' + self._lr_object._get_api_key() + '&loginUrl=' + loginUrl + '&verificationUrl=' + verificationUrl + '&smsTemplate=' + smsTemplate + '&smsTemplate2FA=' + smsTemplate2FA + '&emailTemplate=' + emailTemplate
            url = self._lr_object.SECURE_API_URL + authEndpoint + "login/2fa" + params
            return self._lr_object._post_json(url, payload)
        
        def emailLogin(self, email, password, loginUrl = '', verificationUrl = '', emailTemplate = '', smsTemplate2FA = ''):
            # MFA Email Login (POST)
            payload = {'email':email, 'password':password}
            params = 'apikey=' + self._lr_object._get_api_key() + '&loginUrl=' + loginUrl + '&verificationUrl=' + verificationUrl + '&emailTemplate=' + emailTemplate + '&smsTemplate2FA=' + smsTemplate2FA
            url = self._lr_object.SECURE_API_URL + authEndpoint + "login/2fa?" + params
            return self._lr_object._post_json(url, payload)

        def usernameLogin(self, username, password, loginUrl = '', verificationUrl = '', emailTemplate = '', smsTemplate2FA = '', emailTemplate2FA = ''):
            # MFA UserName Login (POST)
            payload = {'username':username, 'password':password}
            params = '?apikey=' + self._lr_object._get_api_key() + '&loginUrl=' + loginUrl + '&verificationUrl=' + verificationUrl + '&emailTemplate=' + emailTemplate + '&smsTemplate2FA=' + smsTemplate2FA + '&emailTemplate2FA=' + emailTemplate2FA
            url = self._lr_object.SECURE_API_URL + authEndpoint + "login/2fa" + params
            return self._lr_object._post_json(url, payload)

        def updatePhone(self, secondFactorAuthenticationToken, phoneNo2FA, smsTemplate2FA = ''):
            # MFA Update Phone Number (PUT)
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
            # MFA Update Phone Number by Token (PUT)
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
            # MFA Reset Google Authenticator by Token (DEL) & MFA Reset SMS Authenticator by Token (DEL)
            payload = {}
            payload[authenticator]= True
            params = 'apikey='+self._lr_object._get_api_key() +'&access_token='+access_token
            url = self._lr_object.SECURE_API_URL + authEndpoint +  "account/2FA/authenticator"  + "?" + params
            return self._lr_object._delete_json(url, payload)

        def getBackupCode(self, access_token):
            # MFA Backup Code by Access Token (GET)
            payload = {'apikey': self._lr_object._get_api_key(), 'access_token':access_token}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'account/2fa/backupcode'
            return self._lr_object._get_json(url, payload)

        def resetBackupCode(self, access_token):
            # Reset Backup Code by access token (GET)
            payload = {'apikey': self._lr_object._get_api_key(), 'access_token':access_token}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'account/2fa/backupcode/reset'
            return self._lr_object._get_json(url, payload)

        def validateBackupCode(self, secondfactorauthenticationtoken, backupcode):
            # MFA Validate Backup code (PUT)
            param = '?apikey=' + self._lr_object._get_api_key() + '&secondfactorauthenticationtoken=' + secondfactorauthenticationtoken
            payload = {'backupcode':backupcode}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login/2fa/verification/backupcode' + param
            return self._lr_object._put_json(url, payload)

        def validateOTP(self, payload, secondfactorauthenticationtoken, smstemplate2fa=''):
            # MFA Validate OTP (PUT)
            param = '?apikey=' + self._lr_object._get_api_key() + '&secondfactorauthenticationtoken=' + secondfactorauthenticationtoken + '&smstemplate2fa=' + smstemplate2fa
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login/2fa/verification/otp' + param
            return self._lr_object._put_json(url, payload)

        def validateGoogleAuthCode(self, googleauthenticatorcode, secondfactorauthenticationtoken, smstemplate2fa=''):
            # MFA Validate Google Auth Code (PUT)
            param = '?apikey=' + self._lr_object._get_api_key() + '&secondfactorauthenticationtoken=' + secondfactorauthenticationtoken + '&smstemplate2fa=' + smstemplate2fa
            payload = {'googleauthenticatorcode':googleauthenticatorcode}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'login/2fa/verification/googleauthenticatorcode' + param
            return self._lr_object._put_json(url, payload)

        def updateByAccessToken(self, access_token, googleauthenticatorcode, smstemplate=''):
            # Update MFA by Access Token (PUT)
            param = '?apikey=' + self._lr_object._get_api_key() + '&access_token=' + access_token + '&smstemplate=' + smstemplate
            payload = {'googleauthenticatorcode':googleauthenticatorcode}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'account/2fa/verification/googleauthenticatorcode' + param
            return self._lr_object._put_json(url, payload)

        def updateSetting(self, access_token, payload):
            # Update MFA Setting (PUT)
            param = '?apikey=' + self._lr_object._get_api_key() + '&access_token=' + access_token
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'account/2fa/verification/otp' + param
            return self._lr_object._put_json(url, payload)

        def reAuth(self, access_token, smstemplate2fa=''):
            # Multi Factor Re-Authenticate (GET)
            param = '?apikey=' + self._lr_object._get_api_key() + '&access_token=' + access_token + '&smstemplate2fa=' + smstemplate2fa
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'account/reauth/2fa' + param
            return self._lr_object._get_json(url, {})

        def reAuthByGoogleAuthCode(self, access_token, googleauthenticatorcode):
            # Validate MFA by Google Authenticator Code (PUT)
            param = '?apikey=' + self._lr_object._get_api_key() + '&access_token=' + access_token
            payload = {'googleauthenticatorcode':googleauthenticatorcode}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'account/reauth/2fa/googleauthenticatorcode' + param
            return self._lr_object._put_json(url, payload)

        def reAuthByBackupCode(self, access_token, backupcode):
            # Validate MFA by Backup Code (PUT)
            param = '?apikey=' + self._lr_object._get_api_key() + '&access_token=' + access_token
            payload = {'backupcode':backupcode}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'account/reauth/2fa/backupcode' + param
            return self._lr_object._put_json(url, payload)

        def reAuthByOTP(self, access_token, otp, smstemplate2fa=''):
            # Validate MFA by OTP (PUT)
            param = '?apikey=' + self._lr_object._get_api_key() + '&access_token=' + access_token + '&smstemplate2fa=' + smstemplate2fa
            payload = {'otp':otp}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'account/reauth/2fa/otp' + param
            return self._lr_object._put_json(url, payload)

        def reAuthByPassword(self, access_token, password, smstemplate2fa=''):
            # Validate MFA by Password (PUT)
            param = '?apikey=' + self._lr_object._get_api_key() + '&access_token=' + access_token
            payload = {'password':password}
            url = self._lr_object.SECURE_API_URL + authEndpoint + 'account/reauth/password' + param
            return self._lr_object._put_json(url, payload)
        

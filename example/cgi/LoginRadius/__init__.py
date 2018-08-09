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
from datetime import datetime

#Requires Python 2.6>
from collections import namedtuple
#Requires Python 2.7>
from importlib import import_module
import sys
import os
import urllib3
import json

__author__ = "LoginRadius"
__copyright__ = "Copyright 2017-2018, LoginRadius"
__email__ = "developers@loginradius.com"
__status__ = "Production"
__version__ = "3.1.0"

HEADERS = {'Accept': "application/json"}

from LoginRadius.sdk.accessToken import AccessToken
from LoginRadius.sdk.account import Account
from LoginRadius.sdk.authentication import Authentication
from LoginRadius.sdk.customObject import CustomObject
from LoginRadius.sdk.phoneAuthentication import PhoneAuthentication
from LoginRadius.sdk.webHook import WebHook
from LoginRadius.sdk.role import Role
from LoginRadius.sdk.config import Configuration
from LoginRadius.sdk.socialLogin import SocialLogin
from LoginRadius.Exceptions import Exceptions

class LoginRadius:
    """
    LoginRadius Class. Use this to obtain social data and other information
    from the LoginRadius API. Requires Python 2.7 or greater.
    """

    API_KEY = None
    API_SECRET = None
    LIBRARY = None
        
    def __init__(self):
        """
        Constructed when you want to retrieve social data with respect to the acquired token.
        :raise Exceptions.NoAPIKey: Raised if you did not set an API_KEY.
        :raise Exceptions.NoAPISecret: Raised if you did not set an API_SECRET.
        """
        
        self.error = {}
        self.sociallogin_raw = False;

        if not self.API_KEY:
            raise Exceptions.NoAPIKey

        if not self.API_SECRET:
            raise Exceptions.NoAPISecret
        self.SECURE_API_URL = "https://api.loginradius.com/"
        self.CONFIG_API_URL = "https://config.lrcontent.com/"
                
        
        # proxy server detail
        self.Is_Proxy_Enable = False
        self.USER_NAME = "your-username"
        self.PASSWORD = "your-password"
        self.HOST = "host-name"
        self.PORT = "port"
        
        # Namedtuple for settings for each request and the api functions.
        self.settings = namedtuple("Settings", ['library', 'urllib', 'urllib2', 'json', 'requests'])        
        self.accesstoken = self._get_accesstoken_tuple()
        self.account = self._get_account_tuple()
        self.authentication = self._get_authentication_tuple()
        self.customobject = self._get_customobject_tuple()
        self.phoneauthentication = self._get_phoneauthentication_tuple()
        self.webhook = self._get_webhook_tuple()
        self.config = self._get_config_tuple()        
        self.role = self._get_role_tuple()
        self.sociallogin = self._get_sociallogin_tuple()

        # We prefer to use requests with the updated urllib3 module.
        try:
            from distutils.version import StrictVersion
            import requests
                       
            if StrictVersion(requests.__version__) < StrictVersion("2.0"):
                raise Exceptions.RequestsLibraryDated(requests.__version__)
            else:
                self._settings("requests")

        # However, we can use urllib if there is no requests or it is outdated.
        except (ImportError, Exceptions.RequestsLibraryDated):
            self._settings("urllib2")

        # Well, something went wrong here.
        except:
            raise

        else:
            # Namedtuples for api, and user.
            self.accesstoken = self._get_accesstoken_tuple()

    #
    # Internal private functions
    #

    def _settings(self, library):
        """This sets the name tuple settings to whatever library you want. You may change this as you wish."""
        if LoginRadius.LIBRARY is not None:            
            if LoginRadius.LIBRARY == "requests":              
                self._set_requests()
            elif LoginRadius.LIBRARY == "urllib2":             
                self._set_urllib2()
            else:
                raise Exceptions.InvalidLibrary(LoginRadius.LIBRARY)
        else:
            if library == "requests":
                self._set_requests()
            elif library == "urllib2":
                self._set_urllib2()
            else:
                raise Exceptions.InvalidLibrary(library)

    def _set_requests(self):
        """Change to the requests library to use."""
        self.settings.library = "requests"
        self.settings.requests = import_module("requests")
        self.settings.urllib2 = False

    def _set_urllib2(self):
        """Change to the requests urllib2 library to use."""
        if sys.version_info[0] == 2:
            self.settings.urllib2 = import_module("urllib2")
            self.settings.urllib = import_module("urllib")           
        else:
            self.settings.urllib2 = import_module("urllib.request")
            self.settings.urllib = import_module("urllib.parse")
        self.settings.library = "urllib2"
        self.settings.requests = False
        self.settings.json = import_module("json")

    def _get_accesstoken_tuple(self):
        self.accessTokenAPI = AccessToken(self)
        """All the functions relative to the user with the token."""
        accessToken = namedtuple("AccessToken", ['exchange', 'validate','invalidate','refresh','getFacebookToken','getTwitterToken','getAccessTokenByGoogleJWT'])

        #Get methods
        accessToken.exchange = self.accessTokenAPI.exchange
        accessToken.validate = self.accessTokenAPI.validate
        accessToken.invalidate = self.accessTokenAPI.invalidate
        accessToken.refresh = self.accessTokenAPI.refresh
        accessToken.getFacebookToken = self.accessTokenAPI.getFacebookToken
        accessToken.getTwitterToken = self.accessTokenAPI.getTwitterToken
        return accessToken
    
    
    def _get_webhook_tuple(self):
        self.webhookAPI = WebHook(self)
        webhook = namedtuple("WebHook", ['subscribe', 'test', 'unsubscribe','getSubscribed'])
        webhook.subscribe = self.webhookAPI.subscribe;
        webhook.unsubscribe = self.webhookAPI.unsubscribe;
        webhook.getSubscribed = self.webhookAPI.getSubscribed;
        webhook.test = self.webhookAPI.test;
        return webhook;
    
    def _get_config_tuple(self):
        self.configAPI = Configuration(self)
        config = namedtuple("Configuration", ['getConfiguration'])
        config.getConfiguration = self.configAPI.getConfiguration;    
        return config;
        
    def _get_role_tuple(self):
        self.roleAPI = Role(self)
        self.rolePermissionAPI = Role.Permission(self)
        self.roleContextAPI = Role.Context(self)
        role = namedtuple("Role", ['create', 'get', 'remove','permission','unassignRoles'])
        role.permission =  namedtuple("Role_Permission", ['add', 'remove'])
        role.context =  namedtuple("Role_Context", ['get', 'add','delete','deleteRole', 'deletePermission'])
        role.create = self.roleAPI.create;
        role.get = self.roleAPI.get;
        role.remove = self.roleAPI.remove;
        role.unassignRoles = self.roleAPI.unassignRoles;
        role.permission.add = self.rolePermissionAPI.add;
        role.permission.remove = self.rolePermissionAPI.remove;
        role.context.get = self.roleContextAPI.get;
        role.context.add = self.roleContextAPI.add;
        role.context.delete = self.roleContextAPI.delete;
        role.context.deleteRole = self.roleContextAPI.deleteRole;
        role.context.deletePermission = self.roleContextAPI.deletePermission;
        return role;
    
    def _get_sociallogin_tuple(self):
        self.socialloginAPI = SocialLogin(self)
        user = namedtuple("User", ['profile', 'photo', 'check_in', 'audio', 'album', 'video',
                                   'contacts', 'status', 'group', 'post', 'event', 'mention',
                                   'company', 'following', 'page', 'like', 'status_update', 'direct_message','get_message','get_status_update'])
        if self.sociallogin_raw:
            user.profile = self.socialloginAPI.get_user_profile_raw;
        else:
            user.profile = self.socialloginAPI.get_user_profile;
        if self.sociallogin_raw:
            user.photo = self.socialloginAPI.get_photo_raw;
        else:
            user.photo = self.socialloginAPI.get_photo;
        if self.sociallogin_raw:
            user.check_in = self.socialloginAPI.get_checkin_raw;
        else:
            user.check_in = self.socialloginAPI.get_checkin;
        if self.sociallogin_raw:
            user.audio = self.socialloginAPI.get_audio_raw;
        else:
            user.audio = self.socialloginAPI.get_audio;
        if self.sociallogin_raw:
            user.album = self.socialloginAPI.get_album_raw;
        else:
            user.album = self.socialloginAPI.get_album;
        if self.sociallogin_raw:
            user.video = self.socialloginAPI.get_video_raw;
        else:
            user.video = self.socialloginAPI.get_video;
        if self.sociallogin_raw:
            user.contacts = self.socialloginAPI.get_contacts_raw;
        else:
            user.contacts = self.socialloginAPI.get_contacts;
        if self.sociallogin_raw:
            user.status = self.socialloginAPI.get_status_raw;
        else:
            user.status = self.socialloginAPI.get_status;
        if self.sociallogin_raw:
            user.group = self.socialloginAPI.get_group_raw;
        else:
            user.group = self.socialloginAPI.get_group;
        if self.sociallogin_raw:
            user.profile = self.socialloginAPI.get_user_profile_raw;
        else:
            user.profile = self.socialloginAPI.get_user_profile;
        if self.sociallogin_raw:
            user.post = self.socialloginAPI.get_post_raw;
        else:
            user.post = self.socialloginAPI.get_post;
        if self.sociallogin_raw:
            user.event = self.socialloginAPI.get_event_raw;
        else:
            user.event = self.socialloginAPI.get_event;
        if self.sociallogin_raw:
            user.mention = self.socialloginAPI.get_mention_raw;
        else:
            user.mention = self.socialloginAPI.get_mention;
        if self.sociallogin_raw:
            user.company = self.socialloginAPI.get_company_raw;
        else:
            user.company = self.socialloginAPI.get_company;
        if self.sociallogin_raw:
            user.following = self.socialloginAPI.get_following_raw;
        else:
            user.following = self.socialloginAPI.get_following;
        if self.sociallogin_raw:
            user.activity = self.socialloginAPI.get_activity_raw;
        else:
            user.activity = self.socialloginAPI.get_activity;
        if self.sociallogin_raw:
            user.page = self.socialloginAPI.get_page_raw;
        else:
            user.page = self.socialloginAPI.get_page;
        if self.sociallogin_raw:
            user.like = self.socialloginAPI.get_like_raw;
        else:
            user.like = self.socialloginAPI.get_like;
        user.get_status_update = self.socialloginAPI.get_status_update;
        user.status_update = self.socialloginAPI.status_update;
        user.direct_message = self.socialloginAPI.direct_message;
        user.message = self.socialloginAPI.get_message;
            
        return user;
    
    def _get_phoneauthentication_tuple(self):
        self.phoneauthenticationAPI = PhoneAuthentication(self)
        self.phoneauthenticationOTPAPI = PhoneAuthentication.OTP(self)
        phoneauthentication = namedtuple("PhoneAuthentication", ['register', 'login', 'update', 'getPhoneAvailable', 'forgotPassword','resetPassword'])
        phoneauthentication.otp = namedtuple("PhoneAuthentication_OTP", ['resend', 'resendByToken', 'verify', 'verifyByToken', 'send'])
        phoneauthentication.register = self.phoneauthenticationAPI.register;
        phoneauthentication.login = self.phoneauthenticationAPI.login;
        phoneauthentication.update = self.phoneauthenticationAPI.update;
        phoneauthentication.getPhoneAvailable = self.phoneauthenticationAPI.getPhoneAvailable;
        phoneauthentication.forgotPassword = self.phoneauthenticationAPI.forgotPassword;
        phoneauthentication.resetPassword = self.phoneauthenticationAPI.resetPassword;
        phoneauthentication.otp.resend = self.phoneauthenticationOTPAPI.resend;
        phoneauthentication.otp.verify = self.phoneauthenticationOTPAPI.verify;
        phoneauthentication.otp.verifyByToken = self.phoneauthenticationOTPAPI.verifyByToken;
        phoneauthentication.otp.resendByToken = self.phoneauthenticationOTPAPI.resendByToken;
        phoneauthentication.otp.send = self.phoneauthenticationOTPAPI.send;
        return phoneauthentication;
        
        
    def _get_customobject_tuple(self):
        self.customobjectAPI = CustomObject(self)
        customobject = namedtuple("CustomObject", ['create', 'update', 'getByUID', 'getByObjectRecordId', 'remove'])
        customobject.create = self.customobjectAPI.create;
        customobject.update = self.customobjectAPI.update;
        customobject.getByUID = self.customobjectAPI.getByUID;
        customobject.getByObjectRecordId = self.customobjectAPI.getByObjectRecordId;
        customobject.remove = self.customobjectAPI.remove;
        return customobject
        
    
    def _get_authentication_tuple(self):
        self.authenticationAPI = Authentication(self)
        self.authenticationLoginAPI = Authentication.Login(self)
        self.authenticationProfileAPI = Authentication.Profile(self)
        self.authenticationCustomObjectAPI = Authentication.CustomObject(self)
        self.authenticationTwoFactorAPI = Authentication.TwoFactor(self)
        authentication = namedtuple("Authentication", ['getBackupCode','resetBackupCode','register', 'getServerTime','captchaRegister', 'resendEmailVerification', 'removeAccountByEmailConfirmation', 'forgotPassword', 'resetPassword',
                                                'changePassword','addEmail','removeEmail','getVerifyEmail','getCheckEmail','changeUsername','checkUsername','oneTouchLoginByEmail','oneTouchLoginByPhone','oneTouchOtpVerification',
                                                'accountLink','accountUnlink','getSocialProfile','tokenValidate','tokenInvalidate','resetPasswordByOTP','resetPasswordBySecurityAnswerAndEmail','resetPasswordBySecurityAnswerAndPhone','resetPasswordBySecurityAnswerAndUsername','updateSecurityQuestionByAccessToken',
                                                       'validateSecretCode','authGetRegistrationDataServer','securityQuestionByToken','securityQuestionByEmail','securityQuestionByUsername','securityQuestionByPhone'])
        authentication.login = namedtuple("Authentication_Login", ['byBackupCode', 'byEmail', 'byUsername','smartLoginByUsername','smartLoginByEmail','smartLoginPing',
                                                                   'smartLoginVerifyToken','passwordlessLoginByEmail','passwordlessLoginVerification','passwordlessLoginByUsername'])
        authentication.profile = namedtuple("Authentication_Profile", ['getByToken','updateByToken'])
        authentication.customobject = namedtuple("Authentication_CustomObject", ['create','update','getByID','getByToken', 'delete'])
        authentication.twofactor = namedtuple("Authentication_TwoFactor", ['byToken','phoneLogin','emailLogin','usernameLogin','updatePhone','verifyGoogleAuth','updatePhoneByToken',
                                                'googleAuthByToken','removeAuthByToken'])
        authentication.register = self.authenticationAPI.register;
        authentication.getBackupCode = self.authenticationAPI.getBackupCode;
        authentication.resetBackupCode = self.authenticationAPI.resetBackupCode;
        authentication.getServerTime = self.authenticationAPI.getServerTime;
        authentication.captchaRegister = self.authenticationAPI.captchaRegister;
        authentication.resendEmailVerification = self.authenticationAPI.resendEmailVerification;
        authentication.removeAccountByEmailConfirmation = self.authenticationAPI.removeAccountByEmailConfirmation;
        authentication.forgotPassword = self.authenticationAPI.forgotPassword;
        authentication.resetPassword = self.authenticationAPI.resetPassword;
        authentication.resetPasswordByOTP = self.authenticationAPI.resetPasswordByOTP;
        authentication.resetPasswordBySecurityAnswerAndEmail = self.authenticationAPI.resetPasswordBySecurityAnswerAndEmail;
        authentication.resetPasswordBySecurityAnswerAndPhone = self.authenticationAPI.resetPasswordBySecurityAnswerAndPhone;
        authentication.resetPasswordBySecurityAnswerAndUsername = self.authenticationAPI.resetPasswordBySecurityAnswerAndUsername;
        authentication.updateSecurityQuestionByAccessToken = self.authenticationAPI.updateSecurityQuestionByAccessToken;
        authentication.changePassword = self.authenticationAPI.changePassword;
        authentication.addEmail = self.authenticationAPI.addEmail;
        authentication.removeEmail = self.authenticationAPI.removeEmail;
        authentication.getVerifyEmail = self.authenticationAPI.getVerifyEmail;
        authentication.getCheckEmail = self.authenticationAPI.getCheckEmail;
        authentication.changeUsername = self.authenticationAPI.changeUsername;
        authentication.checkUsername = self.authenticationAPI.checkUsername;
        authentication.accountLink = self.authenticationAPI.accountLink;
        authentication.accountUnlink = self.authenticationAPI.accountUnlink;
        authentication.getSocialProfile = self.authenticationAPI.getSocialProfile;
        authentication.tokenValidate = self.authenticationAPI.tokenValidate;
        authentication.tokenInvalidate = self.authenticationAPI.tokenInvalidate;
        authentication.oneTouchLoginByEmail = self.authenticationAPI.oneTouchLoginByEmail;
        authentication.oneTouchLoginByPhone = self.authenticationAPI.oneTouchLoginByPhone;
        authentication.oneTouchOtpVerification = self.authenticationAPI.oneTouchOtpVerification;
        authentication.validateSecretCode = self.authenticationAPI.validateSecretCode;
        authentication.authGetRegistrationDataServer = self.authenticationAPI.authGetRegistrationDataServer;
        authentication.securityQuestionByToken = self.authenticationAPI.securityQuestionByToken;
        authentication.securityQuestionByEmail = self.authenticationAPI.securityQuestionByEmail;
        authentication.securityQuestionByUsername = self.authenticationAPI.securityQuestionByUsername;
        authentication.securityQuestionByPhone = self.authenticationAPI.securityQuestionByPhone;
        authentication.login.byEmail = self.authenticationLoginAPI.byEmail;
        authentication.login.byBackupCode = self.authenticationLoginAPI.byBackupCode;
        authentication.login.byUsername = self.authenticationLoginAPI.byUsername;
        authentication.login.byOTP = self.authenticationLoginAPI.byOTP;
        authentication.login.smartLoginByEmail = self.authenticationLoginAPI.smartLoginByEmail;
        authentication.login.smartLoginByUsername = self.authenticationLoginAPI.smartLoginByUsername;        
        authentication.login.smartLoginPing = self.authenticationLoginAPI.smartLoginPing;
        authentication.login.smartLoginVerifyToken= self.authenticationLoginAPI.smartLoginVerifyToken;
        authentication.login.passwordlessLoginByEmail = self.authenticationLoginAPI.passwordlessLoginByEmail;
        authentication.login.passwordlessLoginByUsername = self.authenticationLoginAPI.passwordlessLoginByUsername;
        authentication.login.passwordlessLoginVerification = self.authenticationLoginAPI.passwordlessLoginVerification;
        authentication.profile.getByToken = self.authenticationProfileAPI.getByToken;
        authentication.profile.updateByToken = self.authenticationProfileAPI.updateByToken;
        authentication.customobject.create = self.authenticationCustomObjectAPI.create;
        authentication.customobject.update = self.authenticationCustomObjectAPI.update;
        authentication.customobject.getByID = self.authenticationCustomObjectAPI.getByID;
        authentication.customobject.delete = self.authenticationCustomObjectAPI.delete;
        authentication.customobject.getByToken = self.authenticationCustomObjectAPI.getByToken;
        authentication.twofactor.byToken = self.authenticationTwoFactorAPI.byToken;
        authentication.twofactor.phoneLogin = self.authenticationTwoFactorAPI.phoneLogin;
        authentication.twofactor.emailLogin = self.authenticationTwoFactorAPI.emailLogin;
        authentication.twofactor.usernameLogin = self.authenticationTwoFactorAPI.usernameLogin;
        authentication.twofactor.updatePhone = self.authenticationTwoFactorAPI.updatePhone;
        authentication.twofactor.verifyGoogleAuth = self.authenticationTwoFactorAPI.verifyGoogleAuth;
        authentication.twofactor.updatePhoneByToken = self.authenticationTwoFactorAPI.updatePhoneByToken;
        authentication.twofactor.googleAuthByToken = self.authenticationTwoFactorAPI.googleAuthByToken;
        authentication.twofactor.removeAuthByToken = self.authenticationTwoFactorAPI.removeAuthByToken;
        return authentication;
        
    def _get_account_tuple(self):
        self.accountProfileAPI = Account.Profile(self)
        self.accountAPI = Account(self)
        self.accountTwoFactorAPI = Account.TwoFactor(self)
        self.accountRegistrationDataAPI = Account.RegistrationData(self)
        account = namedtuple("Account", ['updateSecurityQuestion','assignRole','getRoleByUid','create', 'update', 'remove', 'generateSott', 'setPassword',
                                         'getPassword','invalidateVerificationEmail','getDeletedAccountByEmail','getDeletedAccountByPhone',
                                         'getDeletedAccountByUid','getForgotPasswordToken','getEmailVerificationToken','getAccessToken','getIdentities','resetPhoneIdVerification',
                                         'getBackupCodeByUid','resetBackupCodeByUid'])
        account.profile = namedtuple("Account_Profile", ['getByEmail','getByUsername','getByPhone','getByUid'])
        account.twofactor = namedtuple("Account_TwoFactor", ['removeAuthByUid'])
        account.registrationdata = namedtuple("Account_RegistrationData", ['addRegistrationData','getRegistrationDataServer','updateRegistrationData','deleteRegistrationData'])
        account.create=  self.accountAPI.create
        account.getBackupCodeByUid=  self.accountAPI.getBackupCodeByUid
        account.resetBackupCodeByUid=  self.accountAPI.resetBackupCodeByUid
        account.updateSecurityQuestion=  self.accountAPI.updateSecurityQuestion
        account.update=  self.accountAPI.update
        account.remove=  self.accountAPI.remove
        account.generateSott=  self.accountAPI.generateSott
        account.setPassword=  self.accountAPI.setPassword
        account.getPassword=  self.accountAPI.getPassword
        account.resetPhoneIdVerification=  self.accountAPI.resetPhoneIdVerification
        account.invalidateVerificationEmail=  self.accountAPI.invalidateVerificationEmail
        account.getDeletedAccountByEmail=  self.accountAPI.getDeletedAccountByEmail
        account.getDeletedAccountByPhone=  self.accountAPI.getDeletedAccountByPhone
        account.getDeletedAccountByUid=  self.accountAPI.getDeletedAccountByUid
        account.getForgotPasswordToken=  self.accountAPI.getForgotPasswordToken
        account.getEmailVerificationToken=  self.accountAPI.getEmailVerificationToken
        account.getAccessToken=  self.accountAPI.getAccessToken
        account.getIdentities=  self.accountAPI.getIdentities
        account.assignRole=  self.accountAPI.assignRole
        account.getRoleByUid=  self.accountAPI.getRoleByUid
        account.profile.getByEmail = self.accountProfileAPI.getByEmail
        account.profile.getByUsername = self.accountProfileAPI.getByUsername
        account.profile.getByPhone = self.accountProfileAPI.getByPhone
        account.profile.getByUid = self.accountProfileAPI.getByUid
        account.twofactor.removeAuthByUid = self.accountTwoFactorAPI.removeAuthByUid
        account.registrationdata.addRegistrationData = self.accountRegistrationDataAPI.addRegistrationData
        account.registrationdata.getRegistrationDataServer = self.accountRegistrationDataAPI.getRegistrationDataServer
        account.registrationdata.updateRegistrationData = self.accountRegistrationDataAPI.updateRegistrationData
        account.registrationdata.deleteRegistrationData = self.accountRegistrationDataAPI.deleteRegistrationData
        return account


    def _get_json(self, url, payload, headkey=False):
        """Get JSON from LoginRadius"""
        HEADERS = {'Content-Type': "application/json"}
        proxies = self._get_proxy()     
        if headkey:
            HEADERS = {'Content-Type': HEADERS['Content-Type'], 'X-LoginRadius-ApiKey': headkey.get('apikey'),'X-LoginRadius-ApiSecret': headkey.get('apisecret')}
        if self.settings.requests:
            r = self.settings.requests.get(url, proxies=proxies, params=payload, headers=HEADERS)          
            return self._process_result(r.json())
        else:
            http = urllib3.PoolManager()
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)         
            r = http.request('GET', url, fields=payload, headers=HEADERS)
            return json.loads(r.data.decode('utf-8'))


    def _post_json(self, url, payload, headkey=False):
        return self.__submit_json('POST', url, payload, headkey)
            
    def _put_json(self, url, payload, headkey=False):
        return self.__submit_json('PUT', url, payload, headkey)
        
    def _delete_json(self, url, payload, headkey=False):
        return self.__submit_json('DELETE', url, payload, headkey)
        
    def __submit_json(self, method, url, payload, headkey):
        if self.settings.requests:
            import json
            HEADERS = {'content-type': 'application/json'}
            proxies = self._get_proxy() 
            if headkey:
                HEADERS = {'content-type': HEADERS['content-type'],'X-LoginRadius-ApiKey': headkey.get('apikey'),'X-LoginRadius-ApiSecret': headkey.get('apisecret')}
            if payload.get('sott'):
                HEADERS = {'content-type': HEADERS['content-type'], 'X-LoginRadius-Sott': payload.get('sott')}
            if method == 'PUT':
                r = self.settings.requests.put(url, proxies=proxies, data=json.dumps(payload), headers=HEADERS)                             
            elif method == 'DELETE':
                r = self.settings.requests.delete(url, proxies=proxies, data=json.dumps(payload), headers=HEADERS)
            else:
                r = self.settings.requests.post(url, proxies=proxies, data=json.dumps(payload), headers=HEADERS)            
            return self._process_result(r.json())

        else:
            import json
            data = json.dumps(payload)
            if sys.version_info[0] == 3:
                data = data.encode('utf-8')
            HEADERS = {'content-type': 'application/json'}
            r = self.settings.urllib2.Request(url, data, {'Content-Type': 'application/json'})
            if method == 'PUT' or method == 'DELETE':
                r.get_method = lambda: method
            for key, value in HEADERS.items():
                r.add_header(key, value)
            try:
                result = self.settings.urllib2.urlopen(r)
            except self.settings.urllib2.HTTPError as e:
                return (e.read())
                                              
            import codecs
            reader = codecs.getreader("utf-8")    
            return self._process_result(self.settings.json.load(reader(result)))

        
    def _get_api_key(self):
        return self.API_KEY

    def _get_api_secret(self):
        return self.API_SECRET

    def _get_proxy(self):
        if self.Is_Proxy_Enable:
            proxies = { 'https': 'https://'+self.USER_NAME+':'+self.PASSWORD+'@'+self.HOST+':'+self.PORT }
        else:
            proxies = {}
        return proxies  
            
    def _process_result(self, result):
        """Anything we need to parse or look for. In this case, just the ErrorCode"""
        if "ErrorCode" in result:
            return self._process_error(result)           
        else:
            return result

    def _process_error(self, result):
        """If there is an errorCode, let's figure out which one and raise the corresponding exception."""
        self.error = result
        
        if result['ErrorCode'] == 901:
            raise Exceptions.APIKeyInvalid
        elif result['ErrorCode'] == 902:
            raise Exceptions.APISecretInvalid
        elif result['ErrorCode'] == 903:
            raise Exceptions.InvalidRequestToken
        elif result['ErrorCode'] == 904:
            raise Exceptions.RequestTokenExpired
        elif result['ErrorCode'] == 905:
            raise Exceptions.InvalidAccessToken
        elif result['ErrorCode'] == 906:
            raise Exceptions.TokenExpired(self.access.expire)
        elif result['ErrorCode'] == 907:
            raise Exceptions.ParameterMissing
        elif result['ErrorCode'] == 908:
            raise Exceptions.ParameterNotFormatted
        elif result['ErrorCode'] == 909:
            raise Exceptions.FeatureNotSupported
        elif result['ErrorCode'] == 910:
            raise Exceptions.EndPointNotSupported
        else:
            return result



    #
    # Public functions
    #

    def change_library(self, library):
        self._settings(library)

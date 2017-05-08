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
# Copyright 2016-2017 LoginRadius Inc.          #
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

__author__ = "LoginRadius"
__copyright__ = "Copyright 2015-2016, LoginRadius"
__email__ = "developers@loginradius.com"
__status__ = "Production"
__version__ = "2.8.1"

SECURE_API_URL = "https://api.loginradius.com/"
HEADERS = {'Accept': "application/json"}


class UserRegistration:
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
        self.user = None
        self.error = {}

        if not self.API_KEY:
            raise Exceptions.NoAPIKey

        if not self.API_SECRET:
            raise Exceptions.NoAPISecret

        # Namedtuple for settings for each request and the api functions.
        self.settings = namedtuple("Settings", ['library', 'urllib', 'urllib2', 'json', 'requests'])
        self.api = UserRegistrationAPI(self)
        self.user = self._get_user_tuple()

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
            self.user = self._get_user_tuple()

    #
    # Internal private functions
    #

    def _settings(self, library):
        """This sets the name tuple settings to whatever library you want. You may change this as you wish."""
        if UserRegistration.LIBRARY is not None:
            if UserRegistration.LIBRARY == "requests":
                self._set_requests()
            elif UserRegistration.LIBRARY == "urllib2":
                self._set_urllib2()
            else:
                raise Exceptions.InvalidLibrary(UserRegistration.LIBRARY)
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

    def _get_user_tuple(self):
        """All the functions relative to the user with the token."""
        user = namedtuple("User", ['register_user', 'create_user', 'change_password', 'edit_user',
                                   'get_user_by_id', 'get_user_by_email', 'get_account', 'delete_account', 'set_username', 'generate_forgot_password_token', 'check_email', 
                                   'link_account', 'unlink_account', 'create_raas_profile', 'authenticate_user', 'authenticate_user_by_email', 'delete_user_with_email_confirmation', 'resend_verification_email'
                                   'delete_account_with_email_confirmation', 'get_account_password', 'get_custom_object_by_accountid', 'get_custom_object_by_accountids',
                                   'check_custom_object', 'get_custom_object_by_objectid', 'get_custom_object_stats', 'get_custom_object_by_query', 'check_token_validate', 'check_token_invalidate',
                                    'add_or_remove_user_email', 'set_password', 'set_status', 'upsert_custom_object',
                                   'set_custom_object_status','check_username','password_reset','invalidate_email','update_account','update_user_by_token'])

        #Get methods
        user.get_user_by_id = self.api.get_user_by_id
        user.get_user_by_email = self.api.get_user_by_email
        user.get_account = self.api.get_account
        user.delete_account = self.api.delete_account
        user.authenticate_user = self.api.authenticate_user
        user.authenticate_user_by_email = self.api.authenticate_user_by_email
        user.delete_user_with_email_confirmation = self.api.delete_user_with_email_confirmation
        user.generate_forgot_password_token = self.api.generate_forgot_password_token
        user.check_email = self.api.check_email
        user.resend_verification_email = self.api.resend_verification_email
        user.delete_account_with_email_confirmation = self.api.delete_account_with_email_confirmation
        user.get_account_password = self.api.get_account_password
        user.get_custom_object_by_accountid = self.api.get_custom_object_by_accountid
        user.get_custom_object_by_accountids = self.api.get_custom_object_by_accountids
        user.check_custom_object = self.api.check_custom_object
        user.get_custom_object_by_objectid = self.api.get_custom_object_by_objectid
        user.get_custom_object_stats = self.api.get_custom_object_stats
        user.get_custom_object_by_query = self.api.get_custom_object_by_query
        user.check_token_validate =  self.api.check_token_validate
        user.check_token_invalidate =  self.api.check_token_invalidate
        user.check_username = self.api.check_username
        
        #Post methods
        user.register_user = self.api.register_user
        user.create_user = self.api.create_user
        user.create_raas_profile = self.api.create_raas_profile
        user.edit_user = self.api.edit_user
        user.update_user_by_token = self.api.update_user_by_token
        user.update_account = self.api.update_account
        user.change_password = self.api.change_password
        user.set_username = self.api.set_username
        user.link_account = self.api.link_account
        user.unlink_account = self.api.unlink_account
        user.add_or_remove_user_email = self.api.add_or_remove_user_email
        user.set_password = self.api.set_password
        user.change_username = self.api.change_username
        user.password_reset = self.api.password_reset
        user.set_status = self.api.set_status
        user.upsert_custom_object = self.api.upsert_custom_object
        user.set_custom_object_status = self.api.set_custom_object_status

        #Put methods
        user.invalidate_email = self.api.invalidate_email
        
        
        return user


    def _get_json(self, url, payload):
        """Get JSON from LoginRadius"""
        if self.settings.requests:
            r = self.settings.requests.get(url, params=payload, headers=HEADERS)
            return self._process_result(r.json())
        else:
            payload = self.settings.urllib.urlencode(payload)
            r = self.settings.urllib2.Request(url + "?" + payload)
            r.add_header('Accept', HEADERS['Accept'])
            try:
                data = self.settings.urllib2.urlopen(r)
            except self.settings.urllib2.HTTPError:
                raise
            return self._process_result(self.settings.json.load(data))

    def __submit_json(self, method,url, payload):
        """Post JSON to LoginRadius"""
        if self.settings.requests:
            import json
            HEADERS = {'content-type': 'application/json'}
            if method == 'put':
                r = self.settings.requests.put(url, data=json.dumps(payload), headers=HEADERS)
            else:
                r = self.settings.requests.post(url, data=json.dumps(payload), headers=HEADERS)
            return self._process_result(r.json())

        else:
            import json
            data = json.dumps(payload)
            if sys.version_info[0] == 3:
                data = data.encode('ascii')
            HEADERS = {'content-type': 'application/json'}
            r = self.settings.urllib2.Request(url, data, {'Content-Type': 'application/json'})
            if method == 'put':
                r.get_method = lambda: method
            for key, value in HEADERS.items():
                r.add_header(key, value)
            try:
                data = self.settings.urllib2.urlopen(r)
            except self.settings.urllib2.HTTPError:
                raise
            return self._process_result(self.settings.json.load(data))

    def _post_json(self, url, payload):
        return self.__submit_json('post', url, payload)
    
    def _put_json(self, url, payload):
        return self.__submit_json('put', url, payload)
        

    def _get_api_key(self):
        return self.API_KEY

    def _get_api_secret(self):
        return self.API_SECRET

    def _process_result(self, result):
        """Anything we need to parse or look for. In this case, just the errorCode"""
        if "errorCode" in result:
            self._process_error(result)
        else:
            return result

    def _process_error(self, result):
        """If there is an errorCode, let's figure out which one and raise the corresponding exception."""
        self.error = result
        if result['errorCode'] == 901:
            raise Exceptions.APIKeyInvalid
        elif result['errorCode'] == 902:
            raise Exceptions.APISecretInvalid
        elif result['errorCode'] == 903:
            raise Exceptions.InvalidRequestToken
        elif result['errorCode'] == 904:
            raise Exceptions.RequestTokenExpired
        elif result['errorCode'] == 905:
            raise Exceptions.InvalidAccessToken
        elif result['errorCode'] == 906:
            raise Exceptions.TokenExpired(self.access.expire)
        elif result['errorCode'] == 907:
            raise Exceptions.ParameterMissing
        elif result['errorCode'] == 908:
            raise Exceptions.ParameterNotFormatted
        elif result['errorCode'] == 909:
            raise Exceptions.FeatureNotSupported
        elif result['errorCode'] == 910:
            raise Exceptions.EndPointNotSupported
        else:
            raise Exceptions.UnknownJsonError(result)


    #
    # Public functions
    #

    def change_library(self, library):
        self._settings(library)


class UserRegistrationAPI(object):
    """Where all the API commands can be invoked locally."""

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    #
    # Read permissions
    #
    def get_user_by_id(self, userid):
        """Retrieve User profile information."""
        payload = {'appkey': self._lr_object._get_api_key(), 'appsecret': self._lr_object._get_api_secret(),
                   'userid': userid}
        url = SECURE_API_URL + "raas/v1/user"
        return self._lr_object._get_json(url, payload)

    def get_user_by_email(self, emailid):
        """Retrieve User profile information."""
        payload = {'appkey': self._lr_object._get_api_key(), 'appsecret': self._lr_object._get_api_secret(),
                   'emailid': emailid}
        url = SECURE_API_URL + "raas/v1/user"
        return self._lr_object._get_json(url, payload)

    def get_account(self, accountid):
        """Retrieve User profile information."""
        payload = {'appkey': self._lr_object._get_api_key(), 'appsecret': self._lr_object._get_api_secret(),
                   'accountid': accountid}
        url = SECURE_API_URL + "raas/v1/account"
        return self._lr_object._get_json(url, payload)

    def delete_account(self, accountid):
        """Delete the User account and allows them to re-register for a new account."""
        payload = {'appkey': self._lr_object._get_api_key(), 'appsecret': self._lr_object._get_api_secret(),
                   'accountid': accountid}
        url = SECURE_API_URL + "raas/v1/account/delete"
        return self._lr_object._get_json(url, payload)
        
    def authenticate_user(self, username, password):
        """This API is used to authenticate users and returns the profile data associated with the authenticated user."""
        payload = {'appkey': self._lr_object._get_api_key(), 'appsecret': self._lr_object._get_api_secret(),
                   'username': username, 'password': password}
        url = SECURE_API_URL + "raas/v1/user"
        return self._lr_object._get_json(url, payload)

    def authenticate_user_by_email(self, emailid, password):
        """This API is used to authenticate users and returns the profile data associated with the authenticated user."""
        payload = {'appkey': self._lr_object._get_api_key(), 'appsecret': self._lr_object._get_api_secret(),
                   'emailid': emailid, 'password': password}
        url = SECURE_API_URL + "raas/v1/user"
        return self._lr_object._get_json(url, payload)
        
    def check_email(self, emailid):
        """This API is used to authenticate users and returns the profile data associated with the authenticated user."""
        payload = {'appkey': self._lr_object._get_api_key(), 'appsecret': self._lr_object._get_api_secret(),
                   'emailid': emailid}
        url = SECURE_API_URL + "raas/v1/user/checkemail"
        return self._lr_object._get_json(url, payload)

    def generate_forgot_password_token(self, email):
        """This API generates a forgot password token so you can manually pass into the reset password page and reset some's password."""
        payload = {'appkey': self._lr_object._get_api_key(), 'appsecret': self._lr_object._get_api_secret(),
                   'email': email}
        url = SECURE_API_URL + "raas/v1/account/password/forgot"
        return self._lr_object._get_json(url, payload)
        
    def resend_verification_email(self, emailid, link, template=''):
        """This API is used to generate an email-token that can be sent out to a user in a link in order to verify their email."""
        payload = {'appkey': self._lr_object._get_api_key(), 'appsecret': self._lr_object._get_api_secret(),
                   'emailid': emailid, 'link': link,'template':template}
        url = SECURE_API_URL + "raas/v1/account/verificationemail"
        return self._lr_object._get_json(url, payload)
        
    def delete_user_with_email_confirmation(self, userid, deleteuserlink, template=''):
        """ This API is used to remove an user's account from LoginRadius system. For security and mis-click concerns, it will send a delete confirmation email to user's email inbox to ask user to confirm the action."""
        payload = {'appkey': self._lr_object._get_api_key(), 'appsecret': self._lr_object._get_api_secret(),
                   'userid':userid, 'deleteuserlink':deleteuserlink,'template':template}
        url = SECURE_API_URL + "raas/v1/user/deleteuseremail"
        return self._lr_object._get_json(url, payload)
        
    def delete_account_with_email_confirmation(self, accountId, deleteuserlink, template=''):
        """ This API deletes the User account with email confirmation and allows them to re-register for a new account."""
        payload = {'appkey': self._lr_object._get_api_key(), 'appsecret': self._lr_object._get_api_secret(),
                   'accountId':accountId, 'deleteuserlink':deleteuserlink,'template':template}
        url = SECURE_API_URL + "raas/v1/account/deleteuseremail"
        return self._lr_object._get_json(url, payload)
        
    def get_account_password(self, accountid):
        """This API is used to get the password field of an account."""
        payload = {'appkey': self._lr_object._get_api_key(), 'appsecret': self._lr_object._get_api_secret(),
                   'accountid':accountid}
        url = SECURE_API_URL + "raas/v1/account/password"
        return self._lr_object._get_json(url, payload)
        
    def get_custom_object_by_accountid(self, objectid, accountid):
        """This API is used to retrieve the Custom Object for the specified account based on the account ID(UID)."""
        payload = {'appkey': self._lr_object._get_api_key(), 'appsecret': self._lr_object._get_api_secret(),
                   'objectid':objectid,'accountid':accountid}
        url = SECURE_API_URL + "raas/v1/user/customObject"
        return self._lr_object._get_json(url, payload)
        
    def get_custom_object_by_accountids(self, objectid, accountids):
        """This API is used to retrieve the Custom Objects for multiple accounts based on their account IDs(UID)."""
        payload = {'appkey': self._lr_object._get_api_key(), 'appsecret': self._lr_object._get_api_secret(),
                   'objectid':objectid,'accountids':accountids}
        url = SECURE_API_URL + "raas/v1/user/customObject"
        return self._lr_object._get_json(url, payload)
        
    def check_custom_object(self, objectid, accountid):
        """This API is used to check the presence of a Custom Object for the specified account ID(UID)"""
        payload = {'appkey': self._lr_object._get_api_key(), 'appsecret': self._lr_object._get_api_secret(),
                   'objectid':objectid,'accountid':accountid}
        url = SECURE_API_URL + "raas/v1/user/customObject/check"
        return self._lr_object._get_json(url, payload)
        
        
    def get_custom_object_by_objectid(self, objectid, cursor = 0):
        """This API is used to retrieve all of the Custom objects based on the Object ID."""
        payload = {'appkey': self._lr_object._get_api_key(), 'appsecret': self._lr_object._get_api_secret(),
                   'objectid':objectid}
        url = SECURE_API_URL + "raas/v1/user/customObject"
        return self._lr_object._get_json(url, payload)
        
    def get_custom_object_stats(self, objectid):
        """This API is used to get the current storage information for a specified Custom Object."""
        payload = {'appkey': self._lr_object._get_api_key(), 'appsecret': self._lr_object._get_api_secret(),
                   'objectid':objectid}
        url = SECURE_API_URL + "raas/v1/user/customObject/stats"
        return self._lr_object._get_json(url, payload)
        
    def get_custom_object_by_query(self, objectid, q, cursor = 1):
        """This API is used to retrieve all of the custom objects by an object unique ID and filtered by a query"""
        payload = {'appkey': self._lr_object._get_api_key(), 'appsecret': self._lr_object._get_api_secret(),
                   'objectid':objectid, 'query':q, 'cursor':cursor}
        url = SECURE_API_URL + "raas/v1/user/customObject"
        return self._lr_object._get_json(url, payload)
    
    def check_token_validate(self, token):
        """This API validate access token (access_token)."""
        payload = {'key': self._lr_object._get_api_key(), 'secret': self._lr_object._get_api_secret(), 'access_token': token}
        url = SECURE_API_URL + "api/v2/access_token/Validate/"
        return self._lr_object._get_json(url, payload)

    def check_token_invalidate(self, token):
        """This API invalidates (expire) active access token (access_token)"""
        payload = {'key': self._lr_object._get_api_key(), 'secret': self._lr_object._get_api_secret(), 'access_token': token}
        url = SECURE_API_URL + "api/v2/access_token/invalidate/"
        return self._lr_object._get_json(url, payload)

    def check_username(self, username):
        """This api is use to check the username(server) exists or not on your site."""
        payload = {'appkey': self._lr_object._get_api_key(), 'appsecret': self._lr_object._get_api_secret(),'username':username}
        url = SECURE_API_URL + "raas/v1/user/checkusername/"
        return self._lr_object._get_json(url, payload)
        
    #
    #Write Permissions
    # TODO: custom fields for register user and create user
    def register_user(self, payload):
        """
            Register a user
        """
        auth = 'appkey=' + self._lr_object._get_api_key() + '&appsecret=' + self._lr_object._get_api_secret()
        url = SECURE_API_URL + "raas/v1/user/register" + "?" + auth
        return self._lr_object._post_json(url, payload)

    def create_user(self, payload):
        """
            Create a user
        """
        auth = 'appkey=' + self._lr_object._get_api_key() + '&appsecret=' + self._lr_object._get_api_secret()
        url = SECURE_API_URL + "raas/v1/user/" + "?"+ auth
        return self._lr_object._post_json(url, payload)

    def edit_user(self, userid, payload):
        """
            Update a user
        """
        auth = 'appkey=' + self._lr_object._get_api_key() + '&appsecret=' + self._lr_object._get_api_secret() +'&userid=' + userid
        url = SECURE_API_URL + "raas/v1/user/" + "?"+ auth
        return self._lr_object._post_json(url, payload)
    
    def update_user_by_token(self, token, payload, emailverificationurl = '', template = ''):
        """
            Update a user
        """
        auth = 'appkey=' + self._lr_object._get_api_key() + '&appsecret=' + self._lr_object._get_api_secret() +'&token=' + token + "&emailverificationurl=" + emailverificationurl + "&template=" + template
        url = SECURE_API_URL + "raas/v1/user/update/" + "?"+ auth
        return self._lr_object._post_json(url, payload)


    def create_raas_profile(self, accountid, password, emailid):
        """
            Create a user
        """
        payload = {'accountid': accountid, 'password': password, 'emailid': emailid}
        auth = 'appkey=' + self._lr_object._get_api_key() + '&appsecret=' + self._lr_object._get_api_secret()
        url = SECURE_API_URL + "raas/v1/account/profile" + "?" + auth
        return self._lr_object._post_json(url, payload)

    def add_or_remove_user_email(self, accountid, action, EmailId, EmailType):
        """
            This API is used to add or remove a particular email from one user's account.
        """
        payload = {'EmailId': EmailId, 'EmailType': EmailType}
        auth = 'appkey=' + self._lr_object._get_api_key() + '&appsecret=' + self._lr_object._get_api_secret() + '&accountid=' + accountid + '&action=' + action
        url = SECURE_API_URL + "raas/v1/account/email" + "?" + auth
        return self._lr_object._post_json(url, payload)

    def update_account(self, accountid, payload):
        """
            Update account
        """
        auth = 'appkey=' + self._lr_object._get_api_key() + '&appsecret=' + self._lr_object._get_api_secret() +'&accountid=' + accountid
        url = SECURE_API_URL + "raas/v1/account/edit" + "?" + auth
        return self._lr_object._post_json(url, payload)
    
    def change_password(self, accountid, oldpassword, newpassword):
        """
            Change user password
        """
        auth = 'appkey=' + self._lr_object._get_api_key() + '&appsecret=' + self._lr_object._get_api_secret() +'&accountid=' + accountid 
        payload = {'oldpassword': oldpassword, 'newpassword': newpassword}
        url = SECURE_API_URL + "raas/v1/account/password" + "?" + auth
        return self._lr_object._post_json(url, payload)

    def set_password(self, accountid, password):
        """
            Set user password
        """
        auth = 'appkey=' + self._lr_object._get_api_key() + '&appsecret=' + self._lr_object._get_api_secret() +'&accountid=' + accountid + '&action=set'
        payload = {'password': password}
        url = SECURE_API_URL + "raas/v1/account/password" + "?" + auth
        return self._lr_object._post_json(url, payload)
    
    def set_username(self, accountid, newusername):
        """
            Set username by account id
        """
        auth = 'appkey='+ self._lr_object._get_api_key()+ '&appsecret='+ self._lr_object._get_api_secret() + '&accountid=' + accountid
        payload = {'newusername': newusername}
        url = SECURE_API_URL + "raas/v1/account/setusername" + "?" + auth
        return self._lr_object._post_json(url, payload)

    def change_username(self, accountid, oldusername, newusername):
        """
            This API is used for changing user name by account Id.
        """
        auth = 'appkey='+ self._lr_object._get_api_key()+ '&appsecret='+ self._lr_object._get_api_secret() + '&accountid=' + accountid
        payload = {'oldusername': oldusername, 'newusername': newusername}
        url = SECURE_API_URL + "raas/v1/account/changeusername" + "?" + auth
        return self._lr_object._post_json(url, payload)

    def set_status(self, accountid, action):
        """
            This API is used to block or un-block a user using the users unique UserID (UID).
        """
        auth = 'appkey='+ self._lr_object._get_api_key()+ '&appsecret='+ self._lr_object._get_api_secret() + '&accountid=' + accountid
        payload = {'isblock': action}
        url = SECURE_API_URL + "raas/v1/account/status" + "?" + auth
        return self._lr_object._post_json(url, payload)
    
    def link_account(self, accountid, provider, providerid):
        """
            Link up a social provider account with the specified account based on the account ID(UID) and the social
            providers user ID(ID).
        """
        auth = 'appkey='+ self._lr_object._get_api_key()+ '&appsecret='+ self._lr_object._get_api_secret()
        payload = {'accountid': accountid, 'provider': provider, 'providerid': providerid}
        url = SECURE_API_URL + "raas/v1/account/link" + "?" + auth
        return self._lr_object._post_json(url, payload)

    def unlink_account(self, accountid, provider, providerid):
        """
            Unlink a social provider account with the specified account based on the account ID(UID) and the social
            providers user ID(ID). The unlinked account will automatically gets removed from your database.
        """
        auth = 'appkey='+ self._lr_object._get_api_key()+ '&appsecret='+ self._lr_object._get_api_secret()
        payload = {'accountid': accountid, 'provider': provider, 'providerid': providerid}
        url = SECURE_API_URL + "raas/v1/account/unlink" + "?" + auth
        return self._lr_object._post_json(url, payload)

    def password_reset(self, password, vtoken, welcomeEmailTemplate = ''):
        """
            This API is used to block Custom Object.
        """
        auth = 'appkey='+ self._lr_object._get_api_key()+ '&appsecret='+ self._lr_object._get_api_secret() + '&vtoken=' + vtoken
        payload =  {'password': password}
        url = SECURE_API_URL + "raas/v1/account/password/reset" + "?" + auth
        return self._lr_object._post_json(url, payload)

    def upsert_custom_object(self, objectid, accountid, payload):
        """
            This API is used to save custom objects, by providing ID of object, to a specified account if the object is not exist it will create a new object.
        """
        auth = 'appkey='+ self._lr_object._get_api_key()+ '&appsecret='+ self._lr_object._get_api_secret() + '&objectid=' + objectid + '&accountid=' + accountid
        
        url = SECURE_API_URL + "raas/v1/user/customObject/upsert" + "?" + auth
        return self._lr_object._post_json(url, payload)

    def set_custom_object_status(self, objectid, accountid, action = True):
        """
            This API is used to block Custom Object.
        """
        auth = 'appkey='+ self._lr_object._get_api_key()+ '&appsecret='+ self._lr_object._get_api_secret() + '&objectid=' + objectid + '&accountid=' + accountid
        payload =  {'isblock': action}
        url = SECURE_API_URL + "raas/v1/user/customObject/status" + "?" + auth
        return self._lr_object._post_json(url, payload)

    def invalidate_email(self, accountid, verificationUrl = '', emailTemplate = ''):
        """
            This API is used to invalidate the email verification.
        """
        auth = 'appkey='+ self._lr_object._get_api_key()+ '&appsecret='+ self._lr_object._get_api_secret() + '&accountid=' + accountid + '&emailTemplate='+emailTemplate+'&verificationUrl='+verificationUrl
        payload =  {}
        url = SECURE_API_URL + "raas/v1/account/invalidateemail" + "?" + auth
        return self._lr_object._put_json(url, payload)


class LoginRadiusExceptions(Exception):
    """
    This is the base for all LoginRadius Exceptions. Makes dealing with exceptions easy!
    """

    def __init__(self):
        pass

    def __str__(self):
        return ""


class Exceptions:
    """
    Common exceptions used by LoginRadius.
    """

    def __init__(self):
        pass

    class RequestsLibraryDated(LoginRadiusExceptions):
        """
        Raise exception if module requests is outdated.
        By default 0.12 is included in Python. We need at least version 2.0
        """

        def __init__(self, version):
            self.version = str(version)

        def __str__(self):
            return "LoginRadius needs at least requests 2.0, found: " \
                   + self.version + "\nPlease upgrade to the latest version."

    class InvalidLibrary(LoginRadiusExceptions):
        """
        Raised on trying to change library to through _settings on invalid library argument.
        """

        def __init__(self, library):
            self.library = library

        def __str__(self):
            return "Invalid library string given. Got: " + str(self.library) + ". Valid cases: 'requests' or " + \
                "'urllib2'"

    class NoAPISecret(LoginRadiusExceptions):
        """
        Raised on construction of the LoginRadius object,
        if no API_SECRET has been set for the class.
        """

        def __init__(self, version):
            self.version = str(version)

        def __str__(self):
            return "No API_SECRET set. Please initialize a API_SECRET first.\n" \
                   + "ie. LoginRadius.API_SECRET = \"Really_Secret_Key\""

    class NoAPIKey(LoginRadiusExceptions):
        """
        Raised on construction of the LoginRadius object,
        if no API_KEY has been set for the class.
        """

        def __init__(self, version):
            self.version = str(version)

        def __str__(self):
            return "No API_KEY set. Please initialize a APP_KEY first.\n" \
                   + "ie. LoginRadius.API_Key = \"Really_Application_Key\""

    class MissingJsonResponseParameter(LoginRadiusExceptions):
        """
        Raised if construction of namedtuple would fail
        because missing expected response from LoginRadius API.
        """

        def __init__(self, missing_parameter, raw=None):
            self.missing_parameter = missing_parameter
            self.raw = raw

        def __str__(self):
            exception_string = "Expected parameter from JSON response does not exist." + \
                " Expected: " + self.missing_parameter + " but was not in" + \
                " the dictionary."
            if self.raw:
                exception_string += " Instead, we got: " + str(self.raw)
                return exception_string

    class TokenExpired(LoginRadiusExceptions):
        """
        Raised if the request cannot be completed because the access token has expired.
        """
        def __init__(self, time):
            self.time = time

        def __str__(self):
            return "The request cannot be completed because the token has expired. " + \
                "The token expired on: " + self.time

    class FeatureNotSupported(LoginRadiusExceptions):
        """
        Raised if the request cannot be completed because your account/API access does not include this.
        """
        def __init__(self):
            pass

        def __str__(self):
            return "Your LoginRadius site doesn't have permission to access this endpoint, please contact " +\
                   "LoginRadius support if you need more information."

    class UnknownJsonError(LoginRadiusExceptions):
        """
        Raised if cannot determine error number from Json
        """
        def __init__(self, result):
            self.result = result

        def __str__(self):
            return "The request cannot be completed because LoginRadius raised an unknown error in the API request." + \
                   " More information can be found in the error attribute or in this raw data: " + str(self.result)

    class APIKeyInvalid(LoginRadiusExceptions):
        """
        Raised if you entered your API wrong, or not at all.
        """
        def __init__(self):
            pass

        def __str__(self):
            return "The LoginRadius API Key is not valid, please double check your account."

    class APISecretInvalid(LoginRadiusExceptions):
        """
        Raised if you your API Secret is invalid.
        """
        def __init__(self):
            pass

        def __str__(self):
            return "The LoginRadius API Secret is not valid, please double check your account."

    class InvalidRequestToken(LoginRadiusExceptions):
        """
        Raised if you your request token is invalid from the POST request.
        """
        def __init__(self):
            pass

        def __str__(self):
            return "The LoginRadius Request Token is invalid, please verify the authentication response."

    class RequestTokenExpired(LoginRadiusExceptions):
        """
        Raised if you your request token has expired from the POST request.
        """
        def __init__(self):
            pass

        def __str__(self):
            return "The LoginRadius Request Token has expired, please verify the authentication response."

    class InvalidAccessToken(LoginRadiusExceptions):
        """
        Raised if you access token is invalid.
        """
        def __init__(self):
            pass

        def __str__(self):
            return "The LoginRadius Access Token has expired, please get a new token from the LoginRadius API."

    class ParameterMissing(LoginRadiusExceptions):
        """
        Raised if a parameter in the GET or POST request is missing.
        """
        def __init__(self):
            pass

        def __str__(self):
            return "A parameter is missing in the request, please check all parameters in the API call."

    class ParameterNotFormatted(LoginRadiusExceptions):
        """
        Raised if a parameter in the GET or POST request is not formatted properly for the provider.
        """
        def __init__(self):
            pass

        def __str__(self):
            return "A parameter is not formatted well in the request, please check all the parameters in the API call."

    class EndPointNotSupported(LoginRadiusExceptions):
        """
        Raised if a the endpoint is not supported by the provider which correlates to the token.
        """
        def __init__(self):
            pass

        def __str__(self):
            return "The requested endpoint is not supported by the current ID provider, " + \
                   "please check the API support page at http://www.loginradius.com/datapoints"

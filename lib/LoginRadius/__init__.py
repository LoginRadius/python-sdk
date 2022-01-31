#!/usr/bin/python
#################################################
# Class for Initilizing the LoginRadius Class   #
#################################################
# This is the main class to communicate with    #
# LoginRadius' Unified User Registration API.
#                                               #
# Please note that some API calls are for       #
# premium or enterprise members only.           #
# In which case, an exception will be raised.   #
#################################################
# Copyright 2019 LoginRadius Inc.               #
# - www.LoginRadius.com                         #
#################################################
# This file is part of the LoginRadius SDK      #
# package.                                      #
#################################################

__author__ = "LoginRadius"
__copyright__ = "Copyright 2019, LoginRadius"
__email__ = "developers@loginradius.com"
__status__ = "Production"
__version__ = "11.3.0"

import json
import sys
import urllib3
import hmac
import hashlib
import base64
from collections import namedtuple
from datetime import datetime, timedelta
from importlib import import_module

import binascii
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers import algorithms
from cryptography.hazmat.primitives.ciphers import modes
from pbkdf2 import PBKDF2

# Authentication APIs
from LoginRadius.api.authentication.authentication_api import AuthenticationApi
from LoginRadius.api.authentication.onetouchlogin_api import OneTouchLoginApi
from LoginRadius.api.authentication.passwordlesslogin_api import PasswordLessLoginApi
from LoginRadius.api.authentication.phoneauthentication_api import PhoneAuthenticationApi
from LoginRadius.api.authentication.riskbasedauthentication_api import RiskBasedAuthenticationApi
from LoginRadius.api.authentication.smartlogin_api import SmartLoginApi
from LoginRadius.api.authentication.pinauthentication_api import PINAuthenticationApi
# Account APIs
from LoginRadius.api.account.account_api import AccountApi
from LoginRadius.api.account.role_api import RoleApi
from LoginRadius.api.account.sott_api import SottApi
# Advance APIs
from LoginRadius.api.advanced.customobject_api import CustomObjectApi
from LoginRadius.api.advanced.customregistrationdata_api import CustomRegistrationDataApi
from LoginRadius.api.advanced.multifactorauthentication_api import MultiFactorAuthenticationApi
from LoginRadius.api.advanced.configuration_api import ConfigurationApi
from LoginRadius.api.advanced.webhook_api import WebHookApi
from LoginRadius.api.advanced.reauthentication_api import ReAuthenticationApi
from LoginRadius.api.advanced.consentmanagement_api import ConsentManagementApi

# Social APIs
from LoginRadius.api.social.nativesocial_api import NativeSocialApi
from LoginRadius.api.social.social_api import SocialApi
# exception
from LoginRadius.exceptions import Exceptions


class LoginRadius:
    """
    LoginRadius Class. Use this to obtain social data and other information
    from the LoginRadius API. Requires Python 2.7 or greater.
    """

    API_KEY = None
    API_SECRET = None
    LIBRARY = None
    CUSTOM_DOMAIN = None
    API_REQUEST_SIGNING = False
    ORIGIN_IP = None
    SERVER_REGION = None
    CONST_INITVECTOR = "tu89geji340t89u2"
    CONST_KEYSIZE = 256

    def __init__(self):
        """
        Constructed when you want to retrieve social data with respect to the acquired token.
        :raise Exceptions.NoAPIKey: Raised if you did not set an API_KEY.
        :raise Exceptions.NoAPISecret: Raised if you did not set an API_SECRET.
        """

        self.error = {}
        self.sociallogin_raw = False
        self.bs = 16

        if not self.API_KEY:
            raise Exceptions.NoAPIKey

        if not self.API_SECRET:
            raise Exceptions.NoAPISecret

        if self.CUSTOM_DOMAIN is not None:
            self.SECURE_API_URL = self.CUSTOM_DOMAIN
        else:
            self.SECURE_API_URL = "https://api.loginradius.com/"

        self.CONFIG_API_URL = "https://config.lrcontent.com/"

        # proxy server detail
        self.IS_PROXY_ENABLE = False
        self.USER_NAME = "your-username"
        self.PASSWORD = "your-password"
        self.HOST = "host-name"
        self.PORT = "port"

        # Namedtuple for settings for each request and the api functions.
        self.settings = namedtuple(
            "Settings", ['library', 'urllib', 'urllib3', 'json', 'requests'])

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
            self._settings("urllib3")

        self.authentication = AuthenticationApi(self)
        self.one_touch_login = OneTouchLoginApi(self)
        self.password_less_login = PasswordLessLoginApi(self)
        self.risk_based_authentication = RiskBasedAuthenticationApi(self)
        self.smart_login = SmartLoginApi(self)
        self.phone_authentication = PhoneAuthenticationApi(self)
        self.pin_authentication = PINAuthenticationApi(self)
        self.consent_management = ConsentManagementApi(self)

        self.account = AccountApi(self)
        self.role = RoleApi(self)
        self.sott = SottApi(self)

        self.custom_object = CustomObjectApi(self)
        self.custom_registration_data = CustomRegistrationDataApi(self)
        self.mfa = MultiFactorAuthenticationApi(self)
        self.configuration = ConfigurationApi(self)
        self.web_hook = WebHookApi(self)
        self.re_authentication = ReAuthenticationApi(self)

        self.native_social = NativeSocialApi(self)
        self.social = SocialApi(self)
        if sys.version_info[0] < 3:
            from urllib import quote
            self.quote = quote
        else:
            from urllib.parse import quote
            self.quote = quote

    #
    # Internal private functions
    #
    def _settings(self, library):
        """This sets the name tuple settings to whatever library you want.
        You may change this as you wish."""
        if LoginRadius.LIBRARY is not None:
            if LoginRadius.LIBRARY == "requests":
                self._set_requests()
            elif LoginRadius.LIBRARY == "urllib3":
                self._set_urllib3()
            else:
                raise Exceptions.InvalidLibrary(LoginRadius.LIBRARY)
        else:
            if library == "requests":
                self._set_requests()
            elif library == "urllib3":
                self._set_urllib3()
            else:
                raise Exceptions.InvalidLibrary(library)

    def _set_requests(self):
        """Change to the requests library to use."""

        self.settings.library = "requests"
        self.settings.requests = import_module("requests")
        self.settings.urllib3 = False

    def _set_urllib3(self):
        """Change to the requests urllib3 library to use."""
        if sys.version_info[0] == 2:
            self.settings.urllib3 = import_module("urllib3")
            self.settings.urllib = import_module("urllib")
        else:
            self.settings.urllib3 = import_module("urllib.request")
            self.settings.urllib = import_module("urllib.parse")

        self.settings.library = "urllib3"
        self.settings.requests = False
        self.settings.json = import_module("json")

    def get_expiry_time(self):
        utc_time = datetime.utcnow()
        expiry_time = utc_time + timedelta(hours=1)
        return expiry_time.strftime("%Y-%m-%d %H:%M:%S")

    def get_digest(self, expiry_time, url, payload=None):
        encoded_url = self.quote(url.lower(), safe='')
        signing_str = expiry_time + ":" + encoded_url
        signing_str = signing_str.lower()
        if payload is not None:
            signing_str = signing_str + ":" + json.dumps(payload)

        key_bytes = self.get_api_secret()
        data_bytes = signing_str
        if sys.version_info[0] >= 3:
            key_bytes = bytes(self.get_api_secret(), 'latin-1')
            data_bytes = bytes(signing_str, 'latin-1')
        dig = hmac.new(key_bytes, msg=data_bytes, digestmod=hashlib.sha256).digest()
        if sys.version_info[0] >= 3:
            return base64.b64encode(dig).decode("utf-8")
        return base64.b64encode(dig)

    def execute(self, method, resource_url, query_params, payload):

        api_end_point = self.SECURE_API_URL + resource_url

        if resource_url == "ciam/appinfo":
            api_end_point = self.CONFIG_API_URL + resource_url

        if self.SERVER_REGION is not None and self.SERVER_REGION != "":
            query_params['region'] = self.SERVER_REGION

        apiSecret = None
        if "apiSecret" in query_params:
            apiSecret = query_params['apiSecret']
            query_params.pop("apiSecret")

        headers = {'Content-Type': "application/json",
                   'Accept-encoding': 'gzip'}

        if "access_token" in query_params and "/auth" in resource_url:
            headers.update({"Authorization": "Bearer " + query_params['access_token']})
            query_params.pop("access_token")

        if "sott" in query_params:
            headers.update({"X-LoginRadius-Sott": query_params['sott']})
            query_params.pop("sott")

        if apiSecret and "/manage" in resource_url and not self.API_REQUEST_SIGNING:
            headers.update({"X-LoginRadius-ApiSecret": apiSecret})

        if self.ORIGIN_IP is not None and self.ORIGIN_IP != "":
            headers.update({"X-Origin-IP": self.ORIGIN_IP})

        api_end_point = api_end_point + "?"
        for key, value in query_params.items():
            api_end_point = api_end_point + key + "=" + str(value) + "&"

        api_end_point = api_end_point[:-1]

        if apiSecret and "/manage" in resource_url and self.API_REQUEST_SIGNING:
            expiry_time = self.get_expiry_time()
            digest = self.get_digest(expiry_time, api_end_point, payload)
            headers.update({"X-Request-Expires": expiry_time})
            headers.update({"digest": "SHA-256=" + digest})

        try:
            if method.upper() == 'GET':
                return self._get_json(api_end_point, {}, headers)
            else:
                return self.__submit_json(method.upper(), api_end_point, payload, headers)
        except IOError as e:
            return {
                'ErrorCode': 105,
                'Description': e.message
            }
        except ValueError as e:
            return {
                'ErrorCode': 102,
                'Description': e.message
            }
        except Exception as e:
            return {
                'ErrorCode': 101,
                'Description': e.message
            }

    def _get_json(self, url, payload, HEADERS):
        """Get JSON from LoginRadius"""

        proxies = self._get_proxy()

        if self.settings.requests:
            r = self.settings.requests.get(
                url, proxies=proxies, params=payload, headers=HEADERS)
            if(r.status_code == 429):
                return self.too_many_request_error()
            else:
                return self._process_result(r.json())
        else:
            if not len(proxies) == 0:
                http = urllib3.ProxyManager(proxies['https'])
            else:
                http = urllib3.PoolManager()
            
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            r = http.request('GET', url, fields=payload, headers=HEADERS)
            if(r.status == 429):
                return self.too_many_request_error()
            else:
                return json.loads(r.data.decode('utf-8'))

    def __submit_json(self, method, url, payload, HEADERS):
        proxies = self._get_proxy()
        if self.settings.requests:
            import json
            if method == 'PUT':
                r = self.settings.requests.put(
                    url, proxies=proxies, data=json.dumps(payload), headers=HEADERS)
            elif method == 'DELETE':
                r = self.settings.requests.delete(
                    url, proxies=proxies, data=json.dumps(payload), headers=HEADERS)
            else:
                r = self.settings.requests.post(
                    url, proxies=proxies, data=json.dumps(payload), headers=HEADERS)

            if(r.status_code == 429):
                return self.too_many_request_error()
            else:
                return self._process_result(r.json())

        else:
            import json
            if not len(proxies) == 0:
                http = urllib3.ProxyManager(proxies['https'])
            else:
                http = urllib3.PoolManager()
            data = json.dumps(payload)
            r = http.request(method,  url, headers=HEADERS, body=data)
            if(r.status == 429):
                return self.too_many_request_error()
            else:
                return json.loads(r.data.decode('utf-8'))

    def get_api_key(self):
        return self.API_KEY

    def get_api_secret(self):
        return self.API_SECRET

    def _get_proxy(self):
        if self.IS_PROXY_ENABLE:
            proxies = {'https': 'https://' + self.USER_NAME + ':' + self.PASSWORD + '@' + self.HOST + ':' + self.PORT}
        else:
            proxies = {}
        return proxies

    def _process_result(self, result):
        # For now, directly returning the API response
        return result

    #
    # 429 error code handling for "Too Many Request in a particular time frame"
    #
    def too_many_request_error(self):
        return {
            'ErrorCode': 106,
            'Description': "Too Many Request in a particular time frame"
        }

    #
    # Public functions
    #
    def change_library(self, library):
        self._settings(library)

    def is_null_or_whitespace(self, value):
        if value is None:
            return True
        if str(value).strip() == "":
            return True

    def get_validation_message(self, field):
        return "Invalid value for field " + str(field)

    #
    # Function to generate SOTT manually
    #
    def get_sott(self, timeDifference='', getLRserverTime=False, apiKey="", apiSecret=""):
    
        time = '10'
        secret = self.API_SECRET
        key = self.API_KEY

        if(not self.is_null_or_whitespace(timeDifference)):
            time = timeDifference

        if(not self.is_null_or_whitespace(apiSecret)):
            secret = apiSecret

        if(not self.is_null_or_whitespace(apiKey)):
            key = apiKey

        now = datetime.utcnow()
        now = now - timedelta(minutes=0)
        now_plus_10m = now + timedelta(minutes=int(time))
        now = now.strftime("%Y/%m/%d %I:%M:%S")
        now_plus_10m = now_plus_10m.strftime("%Y/%m/%d %I:%M:%S")

        if getLRserverTime:
            result = self.configuration.get_server_info(time)
            if result.get('Sott') is not None:
                Sott = result.get('Sott')
                for timeKey, val in Sott.items():
                    if timeKey == 'StartTime':
                        now = val
                    if timeKey == 'EndTime':
                        now_plus_10m = val

        plaintext = now + "#" + key + "#" + now_plus_10m
        padding = 16 - (len(plaintext) % 16)
        if sys.version_info[0] == 3:
            plaintext += (bytes([padding]) * padding).decode()
        else:
            plaintext += (chr(padding) * padding).decode()

        salt = "\0\0\0\0\0\0\0\0"
        cipher_key = PBKDF2(secret,
                            salt, 10000).read(self.CONST_KEYSIZE // 8)

        if sys.version_info[0] == 3:
            iv = bytes(self.CONST_INITVECTOR, 'utf-8')
            text = bytes(plaintext, 'utf-8')
        else:
            iv = str(self.CONST_INITVECTOR)
            text = str(plaintext)

        backend = default_backend()
        cipher = Cipher(algorithms.AES(cipher_key),
                        modes.CBC(iv), backend=backend)
        encryptor = cipher.encryptor()
        ct = encryptor.update(text) + encryptor.finalize()

        base64cipher = base64.b64encode(ct)

        md5 = hashlib.md5()
        md5.update(base64cipher.decode('utf8').encode('ascii'))
        return base64cipher.decode('utf-8')+"*"+binascii.hexlify(md5.digest()).decode('ascii')

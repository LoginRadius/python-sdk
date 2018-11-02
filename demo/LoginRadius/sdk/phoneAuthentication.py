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


phoneAuthEndpoint = "/identity/v2/auth/"

class PhoneAuthentication:
    
    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object
        
    def register(self, payload, verificationUrl = '', smsTemplate = '', getLRServerTime = False):
        # Phone User Registration by SMS (POST)
        from LoginRadius.sdk.sott import SOTT
        sottAPI = SOTT(self._lr_object)        
        sott = sottAPI.encrypt('10', getLRServerTime)
        
        payload['sott'] = sott
        params = 'apikey='+self._lr_object._get_api_key()+'&verificationUrl='+verificationUrl+'&smsTemplate='+smsTemplate
        url = self._lr_object.SECURE_API_URL + phoneAuthEndpoint + "register" + "?" + params
        return self._lr_object._post_json(url, payload)
    
    def login(self, payload, loginUrl = '', smsTemplate = '', gRecaptchaResponse = '', fields = '*'):
        # Phone Login (POST)
        params = 'apikey='+self._lr_object._get_api_key() +'&loginurl='+loginUrl+'&smstemplate='+smsTemplate+'&g-recaptcha-response='+gRecaptchaResponse+'&fields='+fields
        url = self._lr_object.SECURE_API_URL + phoneAuthEndpoint + "login" + "?" + params
        return self._lr_object._post_json(url, payload)
    
    def update(self, phone, access_token, smsTemplate = ''):
        # Phone Number Update (PUT)
        params = 'apikey='+self._lr_object._get_api_key() + '&access_token='+ access_token + '&smsTemplate='  +smsTemplate
        payload = {'phone': phone}
        url = self._lr_object.SECURE_API_URL + phoneAuthEndpoint  + "phone?" + params
        return self._lr_object._put_json(url, payload)

    def getPhoneAvailable(self, phone):
        # Phone Number Availability (GET)
        payload = {'apikey': self._lr_object._get_api_key(), 'phone': phone}
        url = self._lr_object.SECURE_API_URL + phoneAuthEndpoint  + "phone"
        return self._lr_object._get_json(url, payload)
    
    def forgotPassword(self, phone, smsTemplate = ''):
        # Phone Forgot Password by OTP (POST)
        payload = {"phone":phone}
        params = 'apikey='+self._lr_object._get_api_key() + '&smsTemplate='  +smsTemplate
        url = self._lr_object.SECURE_API_URL + phoneAuthEndpoint  + "password/otp?" + params
        return self._lr_object._post_json(url, payload)
    
    def resetPassword(self, phone, otp, password, smsTemplate = '', resetpasswordemailtemplate=''):
        # Phone Reset Password by OTP (PUT)
        payload = {"phone": phone,"otp": otp,"password": password,"smsTemplate": smsTemplate,"resetpasswordemailtemplate": resetpasswordemailtemplate}
        params = 'apikey='+self._lr_object._get_api_key()
        url = self._lr_object.SECURE_API_URL + phoneAuthEndpoint  + "password/otp?" + params
        return self._lr_object._put_json(url, payload)

    def removePhoneIdByToken(self, access_token):
        # Remove Phone ID by Access Token (DEL)
        params = '?apikey='+self._lr_object._get_api_key() + '&access_token=' + access_token
        url = self._lr_object.SECURE_API_URL + phoneAuthEndpoint  + "phone" + params
        return self._lr_object._delete_json(url, {})


    class OTP:
        def __init__(self, lr_object):
            """
            :param lr_object: this is the reference to the parent LoginRadius object.
            """
            self._lr_object = lr_object
            
        def resend(self, phone, smsTemplate = ''):
            # Phone Resend Verification OTP (POST)
            params = 'apikey='+self._lr_object._get_api_key() + '&smsTemplate='  +smsTemplate
            payload = {"phone": phone}
            url = self._lr_object.SECURE_API_URL + phoneAuthEndpoint  + "phone/otp?" + params
            return self._lr_object._post_json(url, payload)
        
        def resendByToken(self, phone, access_token, smsTemplate = ''):
            # Phone Resend Verification OTP by Token (POST)
            params = 'apikey='+self._lr_object._get_api_key() + '&access_token='+access_token+ '&smsTemplate='  +smsTemplate
            payload = {"phone": phone}
            url = self._lr_object.SECURE_API_URL + phoneAuthEndpoint  + "phone/otp?" + params
            return self._lr_object._post_json(url, payload)

        def verify(self, phone, otp, smsTemplate = ''):
            # Phone Verification by OTP (PUT)
            payload = {"phone": phone}
            params = 'apikey='+self._lr_object._get_api_key() + '&otp='+otp+'&smsTemplate='  +smsTemplate
            url = self._lr_object.SECURE_API_URL + phoneAuthEndpoint  + "phone/otp?" + params
            return self._lr_object._put_json(url, payload)
        
        def verifyByToken(self, access_token, otp, smsTemplate = ''):
            # Phone Verification OTP by Token (PUT)
            params = 'apikey='+self._lr_object._get_api_key() + '&access_token='+access_token+'&otp='+otp+'&smsTemplate=' +smsTemplate
            url = self._lr_object.SECURE_API_URL + phoneAuthEndpoint  + "phone/otp?" + params
            return self._lr_object._put_json(url, {})

        def send(self, phone, smsTemplate = ''):
            payload = {'apikey': self._lr_object._get_api_key(), 'phone': phone, 'smsTemplate':smsTemplate}
            url = self._lr_object.SECURE_API_URL + phoneAuthEndpoint  + "login/otp"
            return self._lr_object._get_json(url, payload)
       
        

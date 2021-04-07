# -- coding: utf-8 --
# Created by LoginRadius Development Team
# Copyright 2019 LoginRadius Inc. All rights reserved.
#


class OneTouchLoginApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    def one_touch_login_by_email(self, one_touch_login_by_email_model, one_touch_login_email_template=None, redirecturl=None,
        welcomeemailtemplate=None):
        """This API is used to send a link to a specified email for a frictionless login/registration
        
        Args:
            one_touch_login_by_email_model: Model Class containing Definition of payload for OneTouchLogin By EmailModel API
            one_touch_login_email_template: Name of the One Touch Login Email Template
            redirecturl: Url where the user will redirect after success authentication
            welcomeemailtemplate: Name of the welcome email template
		
        Returns:
            Response containing Definition of Complete Validation data
        1.2
        """
        if(one_touch_login_by_email_model is None):
            raise Exception(self._lr_object.get_validation_message("one_touch_login_by_email_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(one_touch_login_email_template)):
            query_parameters["oneTouchLoginEmailTemplate"] = one_touch_login_email_template
        if(not self._lr_object.is_null_or_whitespace(redirecturl)):
            query_parameters["redirecturl"] = redirecturl
        if(not self._lr_object.is_null_or_whitespace(welcomeemailtemplate)):
            query_parameters["welcomeemailtemplate"] = welcomeemailtemplate

        resource_path = "identity/v2/auth/onetouchlogin/email"
        return self._lr_object.execute("POST", resource_path, query_parameters, one_touch_login_by_email_model)

    def one_touch_login_by_phone(self, one_touch_login_by_phone_model, sms_template=None):
        """This API is used to send one time password to a given phone number for a frictionless login/registration.
        
        Args:
            one_touch_login_by_phone_model: Model Class containing Definition of payload for OneTouchLogin By PhoneModel API
            sms_template: SMS Template name
		
        Returns:
            Response containing Definition of Complete Validation data
        1.4
        """
        if(one_touch_login_by_phone_model is None):
            raise Exception(self._lr_object.get_validation_message("one_touch_login_by_phone_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(sms_template)):
            query_parameters["smsTemplate"] = sms_template

        resource_path = "identity/v2/auth/onetouchlogin/phone"
        return self._lr_object.execute("POST", resource_path, query_parameters, one_touch_login_by_phone_model)

    def one_touch_login_otp_verification(self, otp, phone, fields='',
        sms_template=None):
        """This API is used to verify the otp for One Touch Login.
        
        Args:
            otp: The Verification Code
            phone: New Phone Number
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            sms_template: SMS Template name
		
        Returns:
            Response Containing Access Token and Complete Profile Data
        1.5
        """

        if(self._lr_object.is_null_or_whitespace(otp)):
            raise Exception(self._lr_object.get_validation_message("otp"))

        if(self._lr_object.is_null_or_whitespace(phone)):
            raise Exception(self._lr_object.get_validation_message("phone"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["otp"] = otp
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(not self._lr_object.is_null_or_whitespace(sms_template)):
            query_parameters["smsTemplate"] = sms_template

        body_parameters = {}
        body_parameters["phone"] = phone

        resource_path = "identity/v2/auth/onetouchlogin/phone/verify"
        return self._lr_object.execute("PUT", resource_path, query_parameters, body_parameters)

    def one_touch_email_verification(self, verification_token, welcome_email_template=None):
        """This API verifies the provided token for One Touch Login
        
        Args:
            verification_token: Verification token received in the email
            welcome_email_template: Name of the welcome email template
		
        Returns:
            Complete verified response data
        8.4.2
        """

        if(self._lr_object.is_null_or_whitespace(verification_token)):
            raise Exception(self._lr_object.get_validation_message("verification_token"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["verificationToken"] = verification_token
        if(not self._lr_object.is_null_or_whitespace(welcome_email_template)):
            query_parameters["welcomeEmailTemplate"] = welcome_email_template

        resource_path = "identity/v2/auth/email/onetouchlogin"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def one_touch_login_ping(self, client_guid, fields=''):
        """This API is used to check if the One Touch Login link has been clicked or not.
        
        Args:
            client_guid: Unique string used in the Smart Login request
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
		
        Returns:
            Response containing User Profile Data and access token
        9.21.2
        """

        if(self._lr_object.is_null_or_whitespace(client_guid)):
            raise Exception(self._lr_object.get_validation_message("client_guid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["clientGuid"] = client_guid
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields

        resource_path = "identity/v2/auth/login/smartlogin/ping"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

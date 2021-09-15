# -- coding: utf-8 --
# Created by LoginRadius Development Team
# Copyright 2019 LoginRadius Inc. All rights reserved.
#


class PasswordLessLoginApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    def passwordless_login_phone_verification(self, password_less_login_otp_model, fields='', sms_template=None):
        """This API verifies an account by OTP and allows the customer to login.
        
        Args:
            password_less_login_otp_model: Model Class containing Definition of payload for PasswordLessLoginOtpModel API
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            sms_template: SMS Template name
		
        Returns:
            Response containing User Profile Data and access token
        9.6
        """
        if(password_less_login_otp_model is None):
            raise Exception(self._lr_object.get_validation_message("password_less_login_otp_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(not self._lr_object.is_null_or_whitespace(sms_template)):
            query_parameters["smsTemplate"] = sms_template

        resource_path = "identity/v2/auth/login/passwordlesslogin/otp/verify"
        return self._lr_object.execute("PUT", resource_path, query_parameters, password_less_login_otp_model)

    def passwordless_login_by_phone(self, phone, sms_template=None):
        """API can be used to send a One-time Passcode (OTP) provided that the account has a verified PhoneID
        
        Args:
            phone: The Registered Phone Number
            sms_template: SMS Template name
		
        Returns:
            Response Containing Definition of SMS Data
        9.15
        """

        if(self._lr_object.is_null_or_whitespace(phone)):
            raise Exception(self._lr_object.get_validation_message("phone"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["phone"] = phone
        if(not self._lr_object.is_null_or_whitespace(sms_template)):
            query_parameters["smsTemplate"] = sms_template

        resource_path = "identity/v2/auth/login/passwordlesslogin/otp"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def passwordless_login_by_email(self, email, password_less_login_template=None, verification_url=None):
        """This API is used to send a Passwordless Login verification link to the provided Email ID
        
        Args:
            email: Email of the user
            password_less_login_template: Passwordless Login Template Name
            verification_url: Email verification url
		
        Returns:
            Response containing Definition of Complete Validation data
        9.18.1
        """

        if(self._lr_object.is_null_or_whitespace(email)):
            raise Exception(self._lr_object.get_validation_message("email"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["email"] = email
        if(not self._lr_object.is_null_or_whitespace(password_less_login_template)):
            query_parameters["passwordLessLoginTemplate"] = password_less_login_template
        if(not self._lr_object.is_null_or_whitespace(verification_url)):
            query_parameters["verificationUrl"] = verification_url

        resource_path = "identity/v2/auth/login/passwordlesslogin/email"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def passwordless_login_by_user_name(self, username, password_less_login_template=None, verification_url=None):
        """This API is used to send a Passwordless Login Verification Link to a customer by providing their UserName
        
        Args:
            username: UserName of the user
            password_less_login_template: Passwordless Login Template Name
            verification_url: Email verification url
		
        Returns:
            Response containing Definition of Complete Validation data
        9.18.2
        """

        if(self._lr_object.is_null_or_whitespace(username)):
            raise Exception(self._lr_object.get_validation_message("username"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["username"] = username
        if(not self._lr_object.is_null_or_whitespace(password_less_login_template)):
            query_parameters["passwordLessLoginTemplate"] = password_less_login_template
        if(not self._lr_object.is_null_or_whitespace(verification_url)):
            query_parameters["verificationUrl"] = verification_url

        resource_path = "identity/v2/auth/login/passwordlesslogin/email"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def passwordless_login_verification(self, verification_token, fields='', welcome_email_template=None):
        """This API is used to verify the Passwordless Login verification link. Note: If you are using Passwordless Login by Phone you will need to use the Passwordless Login Phone Verification API
        
        Args:
            verification_token: Verification token received in the email
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            welcome_email_template: Name of the welcome email template
		
        Returns:
            Response containing User Profile Data and access token
        9.19
        """

        if(self._lr_object.is_null_or_whitespace(verification_token)):
            raise Exception(self._lr_object.get_validation_message("verification_token"))

        query_parameters = {}
        query_parameters["apikey"] = self._lr_object.get_api_key()
        query_parameters["verificationToken"] = verification_token
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(not self._lr_object.is_null_or_whitespace(welcome_email_template)):
            query_parameters["welcomeEmailTemplate"] = welcome_email_template

        resource_path = "identity/v2/auth/login/passwordlesslogin/email/verify"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def passwordless_login_verification_by_email_and_otp(self, password_less_login_by_email_and_otp_model, fields=''):
        """This API is used to verify the otp sent to the email when doing a passwordless login. 
        
        Args:
            password_less_login_by_email_and_otp_model: payload
            fields: Fields
		
        Returns:
            Response containing User Profile Data and access token
        9.23
        """
        if(password_less_login_by_email_and_otp_model is None):
            raise Exception(self._lr_object.get_validation_message("password_less_login_by_email_and_otp_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields

        resource_path = "identity/v2/auth/login/passwordlesslogin/email/verifyotp"
        return self._lr_object.execute("POST", resource_path, query_parameters, password_less_login_by_email_and_otp_model)

    def passwordless_login_verification_by_user_name_and_otp(self, password_less_login_by_user_name_and_otp_model, fields=''):
        """This API is used to verify the otp sent to the email when doing a passwordless login.
        
        Args:
            password_less_login_by_user_name_and_otp_model: payload
            fields: Fields
		
        Returns:
            Response containing User Profile Data and access token
        9.24
        """
        if(password_less_login_by_user_name_and_otp_model is None):
            raise Exception(self._lr_object.get_validation_message("password_less_login_by_user_name_and_otp_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields

        resource_path = "identity/v2/auth/login/passwordlesslogin/username/verifyotp"
        return self._lr_object.execute("POST", resource_path, query_parameters, password_less_login_by_user_name_and_otp_model)

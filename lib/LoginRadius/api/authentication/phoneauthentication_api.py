# -- coding: utf-8 --
# Created by LoginRadius Development Team
# Copyright 2019 LoginRadius Inc. All rights reserved.
#


class PhoneAuthenticationApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    def login_by_phone(self, phone_authentication_model, fields='', login_url=None,
        sms_template=None):
        """This API retrieves a copy of the user data based on the Phone
        
        Args:
            phone_authentication_model: Model Class containing Definition of payload for PhoneAuthenticationModel API
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            login_url: Url where the user is logging from
            sms_template: SMS Template name
		
        Returns:
            Response containing User Profile Data and access token
        9.2.3
        """
        if(phone_authentication_model is None):
            raise Exception(self._lr_object.get_validation_message("phone_authentication_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(not self._lr_object.is_null_or_whitespace(login_url)):
            query_parameters["loginUrl"] = login_url
        if(not self._lr_object.is_null_or_whitespace(sms_template)):
            query_parameters["smsTemplate"] = sms_template

        resource_path = "identity/v2/auth/login"
        return self._lr_object.execute("POST", resource_path, query_parameters, phone_authentication_model)

    def forgot_password_by_phone_otp(self, phone, sms_template=None):
        """This API is used to send the OTP to reset the account password.
        
        Args:
            phone: New Phone Number
            sms_template: SMS Template name
		
        Returns:
            Response Containing Validation Data and SMS Data
        10.4
        """

        if(self._lr_object.is_null_or_whitespace(phone)):
            raise Exception(self._lr_object.get_validation_message("phone"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(sms_template)):
            query_parameters["smsTemplate"] = sms_template

        body_parameters = {}
        body_parameters["phone"] = phone

        resource_path = "identity/v2/auth/password/otp"
        return self._lr_object.execute("POST", resource_path, query_parameters, body_parameters)

    def reset_password_by_phone_otp(self, reset_password_by_otp_model):
        """This API is used to reset the password
        
        Args:
            reset_password_by_otp_model: Model Class containing Definition of payload for ResetPasswordByOTP API
		
        Returns:
            Response containing Definition of Complete Validation data
        10.5
        """
        if(reset_password_by_otp_model is None):
            raise Exception(self._lr_object.get_validation_message("reset_password_by_otp_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/password/otp"
        return self._lr_object.execute("PUT", resource_path, query_parameters, reset_password_by_otp_model)

    def phone_verification_by_otp(self, otp, phone, fields='',
        sms_template=None):
        """This API is used to validate the verification code sent to verify a user's phone number
        
        Args:
            otp: The Verification Code
            phone: New Phone Number
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            sms_template: SMS Template name
		
        Returns:
            Response containing User Profile Data and access token
        11.1.1
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

        resource_path = "identity/v2/auth/phone/otp"
        return self._lr_object.execute("PUT", resource_path, query_parameters, body_parameters)

    def phone_verification_otp_by_access_token(self, access_token, otp, sms_template=None):
        """This API is used to consume the verification code sent to verify a user's phone number. Use this call for front-end purposes in cases where the user is already logged in by passing the user's access token.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            otp: The Verification Code
            sms_template: SMS Template name
		
        Returns:
            Response containing Definition of Complete Validation data
        11.1.2
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(otp)):
            raise Exception(self._lr_object.get_validation_message("otp"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["otp"] = otp
        if(not self._lr_object.is_null_or_whitespace(sms_template)):
            query_parameters["smsTemplate"] = sms_template

        resource_path = "identity/v2/auth/phone/otp"
        return self._lr_object.execute("PUT", resource_path, query_parameters, {})

    def phone_resend_verification_otp(self, phone, sms_template=None):
        """This API is used to resend a verification OTP to verify a user's Phone Number. The user will receive a verification code that they will need to input
        
        Args:
            phone: New Phone Number
            sms_template: SMS Template name
		
        Returns:
            Response Containing Validation Data and SMS Data
        11.2.1
        """

        if(self._lr_object.is_null_or_whitespace(phone)):
            raise Exception(self._lr_object.get_validation_message("phone"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(sms_template)):
            query_parameters["smsTemplate"] = sms_template

        body_parameters = {}
        body_parameters["phone"] = phone

        resource_path = "identity/v2/auth/phone/otp"
        return self._lr_object.execute("POST", resource_path, query_parameters, body_parameters)

    def phone_resend_verification_otp_by_token(self, access_token, phone, sms_template=None):
        """This API is used to resend a verification OTP to verify a user's Phone Number in cases in which an active token already exists
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            phone: New Phone Number
            sms_template: SMS Template name
		
        Returns:
            Response Containing Validation Data and SMS Data
        11.2.2
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(phone)):
            raise Exception(self._lr_object.get_validation_message("phone"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(sms_template)):
            query_parameters["smsTemplate"] = sms_template

        body_parameters = {}
        body_parameters["phone"] = phone

        resource_path = "identity/v2/auth/phone/otp"
        return self._lr_object.execute("POST", resource_path, query_parameters, body_parameters)

    def update_phone_number(self, access_token, phone, sms_template=None):
        """This API is used to update the login Phone Number of users
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            phone: New Phone Number
            sms_template: SMS Template name
		
        Returns:
            Response Containing Validation Data and SMS Data
        11.5
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(phone)):
            raise Exception(self._lr_object.get_validation_message("phone"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(sms_template)):
            query_parameters["smsTemplate"] = sms_template

        body_parameters = {}
        body_parameters["phone"] = phone

        resource_path = "identity/v2/auth/phone"
        return self._lr_object.execute("PUT", resource_path, query_parameters, body_parameters)

    def check_phone_number_availability(self, phone):
        """This API is used to check the Phone Number exists or not on your site.
        
        Args:
            phone: The Registered Phone Number
		
        Returns:
            Response containing Definition Complete ExistResponse data
        11.6
        """

        if(self._lr_object.is_null_or_whitespace(phone)):
            raise Exception(self._lr_object.get_validation_message("phone"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["phone"] = phone

        resource_path = "identity/v2/auth/phone"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def remove_phone_id_by_access_token(self, access_token):
        """This API is used to delete the Phone ID on a user's account via the access token
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
		
        Returns:
            Response containing Definition of Delete Request
        11.7
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/phone"
        return self._lr_object.execute("DELETE", resource_path, query_parameters, {})

    def user_registration_by_phone(self, auth_user_registration_model, sott, fields='',
        options='', sms_template=None, verification_url=None, welcome_email_template=None):
        """This API registers the new users into your Cloud Storage and triggers the phone verification process.
        
        Args:
            auth_user_registration_model: Model Class containing Definition of payload for Auth User Registration API
            sott: LoginRadius Secured One Time Token
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            options: PreventVerificationEmail (Specifying this value prevents the verification email from being sent. Only applicable if you have the optional email verification flow)
            sms_template: SMS Template name
            verification_url: Email verification url
            welcome_email_template: Name of the welcome email template
		
        Returns:
            Response containing Definition of Complete Validation, UserProfile data and Access Token
        17.1.2
        """
        if(auth_user_registration_model is None):
            raise Exception(self._lr_object.get_validation_message("auth_user_registration_model"))

        if(self._lr_object.is_null_or_whitespace(sott)):
            raise Exception(self._lr_object.get_validation_message("sott"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["sott"] = sott
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(not self._lr_object.is_null_or_whitespace(options)):
            query_parameters["options"] = options
        if(not self._lr_object.is_null_or_whitespace(sms_template)):
            query_parameters["smsTemplate"] = sms_template
        if(not self._lr_object.is_null_or_whitespace(verification_url)):
            query_parameters["verificationUrl"] = verification_url
        if(not self._lr_object.is_null_or_whitespace(welcome_email_template)):
            query_parameters["welcomeEmailTemplate"] = welcome_email_template

        resource_path = "identity/v2/auth/register"
        return self._lr_object.execute("POST", resource_path, query_parameters, auth_user_registration_model)

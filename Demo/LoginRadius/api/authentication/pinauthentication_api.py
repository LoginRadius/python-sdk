# -- coding: utf-8 --
# Created by LoginRadius Development Team
# Copyright 2019 LoginRadius Inc. All rights reserved.
#


class PINAuthenticationApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    def pin_login(self, login_by_pin_model, session_token):
        """This API is used to login a user by pin and session token.
        
        Args:
            login_by_pin_model: Model Class containing Definition of payload for LoginByPin API
            session_token: Session Token of user
		
        Returns:
            Response containing User Profile Data and access token
        9.22
        """
        if(login_by_pin_model is None):
            raise Exception(self._lr_object.get_validation_message("login_by_pin_model"))

        if(self._lr_object.is_null_or_whitespace(session_token)):
            raise Exception(self._lr_object.get_validation_message("session_token"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["session_token"] = session_token

        resource_path = "identity/v2/auth/login/pin"
        return self._lr_object.execute("POST", resource_path, query_parameters, login_by_pin_model)

    def send_forgot_pin_email_by_email(self, forgot_pin_link_by_email_model, email_template=None, reset_pin_url=None):
        """This API sends the reset pin email to specified email address.
        
        Args:
            forgot_pin_link_by_email_model: Model Class containing Definition for Forgot Pin Link By Email API
            email_template: Email template name
            reset_pin_url: Reset PIN Url
		
        Returns:
            Response containing Definition of Complete Validation data
        42.1
        """
        if(forgot_pin_link_by_email_model is None):
            raise Exception(self._lr_object.get_validation_message("forgot_pin_link_by_email_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(email_template)):
            query_parameters["emailTemplate"] = email_template
        if(not self._lr_object.is_null_or_whitespace(reset_pin_url)):
            query_parameters["resetPINUrl"] = reset_pin_url

        resource_path = "identity/v2/auth/pin/forgot/email"
        return self._lr_object.execute("POST", resource_path, query_parameters, forgot_pin_link_by_email_model)

    def send_forgot_pin_email_by_username(self, forgot_pin_link_by_user_name_model, email_template=None, reset_pin_url=None):
        """This API sends the reset pin email using username.
        
        Args:
            forgot_pin_link_by_user_name_model: Model Class containing Definition for Forgot Pin Link By UserName API
            email_template: Email template name
            reset_pin_url: Reset PIN Url
		
        Returns:
            Response containing Definition of Complete Validation data
        42.2
        """
        if(forgot_pin_link_by_user_name_model is None):
            raise Exception(self._lr_object.get_validation_message("forgot_pin_link_by_user_name_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(email_template)):
            query_parameters["emailTemplate"] = email_template
        if(not self._lr_object.is_null_or_whitespace(reset_pin_url)):
            query_parameters["resetPINUrl"] = reset_pin_url

        resource_path = "identity/v2/auth/pin/forgot/username"
        return self._lr_object.execute("POST", resource_path, query_parameters, forgot_pin_link_by_user_name_model)

    def reset_pin_by_reset_token(self, reset_pin_by_reset_token):
        """This API is used to reset pin using reset token.
        
        Args:
            reset_pin_by_reset_token: Model Class containing Definition of payload for Reset Pin By Reset Token API
		
        Returns:
            Response containing Definition of Complete Validation data
        42.3
        """
        if(reset_pin_by_reset_token is None):
            raise Exception(self._lr_object.get_validation_message("reset_pin_by_reset_token"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/pin/reset/token"
        return self._lr_object.execute("PUT", resource_path, query_parameters, reset_pin_by_reset_token)

    def reset_pin_by_email_and_security_answer(self, reset_pin_by_security_question_answer_and_email_model):
        """This API is used to reset pin using security question answer and email.
        
        Args:
            reset_pin_by_security_question_answer_and_email_model: Model Class containing Definition of payload for Reset Pin By Security Question and Email API
		
        Returns:
            Response containing Definition of Complete Validation data
        42.4
        """
        if(reset_pin_by_security_question_answer_and_email_model is None):
            raise Exception(self._lr_object.get_validation_message("reset_pin_by_security_question_answer_and_email_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/pin/reset/securityanswer/email"
        return self._lr_object.execute("PUT", resource_path, query_parameters, reset_pin_by_security_question_answer_and_email_model)

    def reset_pin_by_username_and_security_answer(self, reset_pin_by_security_question_answer_and_username_model):
        """This API is used to reset pin using security question answer and username.
        
        Args:
            reset_pin_by_security_question_answer_and_username_model: Model Class containing Definition of payload for Reset Pin By Security Question and UserName API
		
        Returns:
            Response containing Definition of Complete Validation data
        42.5
        """
        if(reset_pin_by_security_question_answer_and_username_model is None):
            raise Exception(self._lr_object.get_validation_message("reset_pin_by_security_question_answer_and_username_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/pin/reset/securityanswer/username"
        return self._lr_object.execute("PUT", resource_path, query_parameters, reset_pin_by_security_question_answer_and_username_model)

    def reset_pin_by_phone_and_security_answer(self, reset_pin_by_security_question_answer_and_phone_model):
        """This API is used to reset pin using security question answer and phone.
        
        Args:
            reset_pin_by_security_question_answer_and_phone_model: Model Class containing Definition of payload for Reset Pin By Security Question and Phone API
		
        Returns:
            Response containing Definition of Complete Validation data
        42.6
        """
        if(reset_pin_by_security_question_answer_and_phone_model is None):
            raise Exception(self._lr_object.get_validation_message("reset_pin_by_security_question_answer_and_phone_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/pin/reset/securityanswer/phone"
        return self._lr_object.execute("PUT", resource_path, query_parameters, reset_pin_by_security_question_answer_and_phone_model)

    def send_forgot_pin_sms_by_phone(self, forgot_pin_otp_by_phone_model, sms_template=None):
        """This API sends the OTP to specified phone number
        
        Args:
            forgot_pin_otp_by_phone_model: Model Class containing Definition for Forgot Pin Otp By Phone API
            sms_template: 
		
        Returns:
            Response Containing Validation Data and SMS Data
        42.7
        """
        if(forgot_pin_otp_by_phone_model is None):
            raise Exception(self._lr_object.get_validation_message("forgot_pin_otp_by_phone_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(sms_template)):
            query_parameters["smsTemplate"] = sms_template

        resource_path = "identity/v2/auth/pin/forgot/otp"
        return self._lr_object.execute("POST", resource_path, query_parameters, forgot_pin_otp_by_phone_model)

    def change_pin_by_access_token(self, access_token, change_pin_model):
        """This API is used to change a user's PIN using access token.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            change_pin_model: Model Class containing Definition for change PIN Property
		
        Returns:
            Response containing Definition of Complete Validation data
        42.8
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))
        if(change_pin_model is None):
            raise Exception(self._lr_object.get_validation_message("change_pin_model"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/pin/change"
        return self._lr_object.execute("PUT", resource_path, query_parameters, change_pin_model)

    def reset_pin_by_phone_and_otp(self, reset_pin_by_phone_and_otp_model):
        """This API is used to reset pin using phoneId and OTP.
        
        Args:
            reset_pin_by_phone_and_otp_model: Model Class containing Definition of payload for Reset Pin By Phone and Otp API
		
        Returns:
            Response containing Definition of Complete Validation data
        42.9
        """
        if(reset_pin_by_phone_and_otp_model is None):
            raise Exception(self._lr_object.get_validation_message("reset_pin_by_phone_and_otp_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/pin/reset/otp/phone"
        return self._lr_object.execute("PUT", resource_path, query_parameters, reset_pin_by_phone_and_otp_model)

    def reset_pin_by_email_and_otp(self, reset_pin_by_email_and_otp_model):
        """This API is used to reset pin using email and OTP.
        
        Args:
            reset_pin_by_email_and_otp_model: Model Class containing Definition of payload for Reset Pin By Email and Otp API
		
        Returns:
            Response containing Definition of Complete Validation data
        42.10
        """
        if(reset_pin_by_email_and_otp_model is None):
            raise Exception(self._lr_object.get_validation_message("reset_pin_by_email_and_otp_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/pin/reset/otp/email"
        return self._lr_object.execute("PUT", resource_path, query_parameters, reset_pin_by_email_and_otp_model)

    def reset_pin_by_username_and_otp(self, reset_pin_by_username_and_otp_model):
        """This API is used to reset pin using username and OTP.
        
        Args:
            reset_pin_by_username_and_otp_model: Model Class containing Definition of payload for Reset Pin By Username and Otp API
		
        Returns:
            Response containing Definition of Complete Validation data
        42.11
        """
        if(reset_pin_by_username_and_otp_model is None):
            raise Exception(self._lr_object.get_validation_message("reset_pin_by_username_and_otp_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/pin/reset/otp/username"
        return self._lr_object.execute("PUT", resource_path, query_parameters, reset_pin_by_username_and_otp_model)

    def set_pin_by_pin_auth_token(self, pin_required_model, pin_auth_token):
        """This API is used to change a user's PIN using Pin Auth token.
        
        Args:
            pin_required_model: Model Class containing Definition for PIN
            pin_auth_token: Pin Auth Token
		
        Returns:
            Response containing User Profile Data and access token
        42.12
        """
        if(pin_required_model is None):
            raise Exception(self._lr_object.get_validation_message("pin_required_model"))

        if(self._lr_object.is_null_or_whitespace(pin_auth_token)):
            raise Exception(self._lr_object.get_validation_message("pin_auth_token"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["pinAuthToken"] = pin_auth_token

        resource_path = "identity/v2/auth/pin/set/pinauthtoken"
        return self._lr_object.execute("POST", resource_path, query_parameters, pin_required_model)

    def in_validate_pin_session_token(self, session_token):
        """This API is used to invalidate pin session token.
        
        Args:
            session_token: Session Token of user
		
        Returns:
            Response containing Definition of Complete Validation data
        44.1
        """

        if(self._lr_object.is_null_or_whitespace(session_token)):
            raise Exception(self._lr_object.get_validation_message("session_token"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["session_token"] = session_token

        resource_path = "identity/v2/auth/session_token/invalidate"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

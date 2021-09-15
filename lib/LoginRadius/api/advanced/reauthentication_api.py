# -- coding: utf-8 --
# Created by LoginRadius Development Team
# Copyright 2019 LoginRadius Inc. All rights reserved.
#


class ReAuthenticationApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    def mfa_re_authenticate(self, access_token, sms_template2_f_a=None):
        """This API is used to trigger the Multi-Factor Autentication workflow for the provided access token
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            sms_template2_f_a: SMS Template Name
		
        Returns:
            Response containing Definition of Complete Multi-Factor Authentication Settings data
        14.3
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(sms_template2_f_a)):
            query_parameters["smsTemplate2FA"] = sms_template2_f_a

        resource_path = "identity/v2/auth/account/reauth/2fa"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def mfa_re_authenticate_by_otp(self, access_token, reauth_by_otp_model):
        """This API is used to re-authenticate via Multi-factor authentication by passing the One Time Password received via SMS
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            reauth_by_otp_model: Model Class containing Definition for MFA Reauthentication by OTP
		
        Returns:
            Complete user Multi-Factor Authentication Token data
        14.4
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))
        if(reauth_by_otp_model is None):
            raise Exception(self._lr_object.get_validation_message("reauth_by_otp_model"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/account/reauth/2fa/otp"
        return self._lr_object.execute("PUT", resource_path, query_parameters, reauth_by_otp_model)

    def mfa_re_authenticate_by_backup_code(self, access_token, reauth_by_backup_code_model):
        """This API is used to re-authenticate by set of backup codes via access token on the site that has Multi-factor authentication enabled in re-authentication for the user that does not have the device
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            reauth_by_backup_code_model: Model Class containing Definition for MFA Reauthentication by Backup code
		
        Returns:
            Complete user Multi-Factor Authentication Token data
        14.5
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))
        if(reauth_by_backup_code_model is None):
            raise Exception(self._lr_object.get_validation_message("reauth_by_backup_code_model"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/account/reauth/2fa/backupcode"
        return self._lr_object.execute("PUT", resource_path, query_parameters, reauth_by_backup_code_model)

    def mfa_re_authenticate_by_google_auth(self, access_token, reauth_by_google_authenticator_code_model):
        """This API is used to re-authenticate via Multi-factor-authentication by passing the google authenticator code
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            reauth_by_google_authenticator_code_model: Model Class containing Definition for MFA Reauthentication by Google Authenticator
		
        Returns:
            Complete user Multi-Factor Authentication Token data
        14.6
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))
        if(reauth_by_google_authenticator_code_model is None):
            raise Exception(self._lr_object.get_validation_message("reauth_by_google_authenticator_code_model"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/account/reauth/2fa/googleauthenticatorcode"
        return self._lr_object.execute("PUT", resource_path, query_parameters, reauth_by_google_authenticator_code_model)

    def mfa_re_authenticate_by_password(self, access_token, password_event_based_auth_model_with_lockout, sms_template2_f_a=None):
        """This API is used to re-authenticate via Multi-factor-authentication by passing the password
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            password_event_based_auth_model_with_lockout: Model Class containing Definition of payload for PasswordEventBasedAuthModel with Lockout API
            sms_template2_f_a: SMS Template Name
		
        Returns:
            Complete user Multi-Factor Authentication Token data
        14.7
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))
        if(password_event_based_auth_model_with_lockout is None):
            raise Exception(self._lr_object.get_validation_message("password_event_based_auth_model_with_lockout"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(sms_template2_f_a)):
            query_parameters["smsTemplate2FA"] = sms_template2_f_a

        resource_path = "identity/v2/auth/account/reauth/password"
        return self._lr_object.execute("PUT", resource_path, query_parameters, password_event_based_auth_model_with_lockout)

    def verify_multi_factor_otp_reauthentication(self, event_based_multi_factor_token, uid):
        """This API is used on the server-side to validate and verify the re-authentication token created by the MFA re-authentication API. This API checks re-authentications created by OTP.
        
        Args:
            event_based_multi_factor_token: Model Class containing Definition for SecondFactorValidationToken
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition of Complete Validation data
        18.38
        """
        if(event_based_multi_factor_token is None):
            raise Exception(self._lr_object.get_validation_message("event_based_multi_factor_token"))

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/account/" + uid + "/reauth/2fa"
        return self._lr_object.execute("POST", resource_path, query_parameters, event_based_multi_factor_token)

    def verify_multi_factor_password_reauthentication(self, event_based_multi_factor_token, uid):
        """This API is used on the server-side to validate and verify the re-authentication token created by the MFA re-authentication API. This API checks re-authentications created by password.
        
        Args:
            event_based_multi_factor_token: Model Class containing Definition for SecondFactorValidationToken
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition of Complete Validation data
        18.39
        """
        if(event_based_multi_factor_token is None):
            raise Exception(self._lr_object.get_validation_message("event_based_multi_factor_token"))

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/account/" + uid + "/reauth/password"
        return self._lr_object.execute("POST", resource_path, query_parameters, event_based_multi_factor_token)

    def verify_multi_factor_pin_reauthentication(self, event_based_multi_factor_token, uid):
        """This API is used on the server-side to validate and verify the re-authentication token created by the MFA re-authentication API. This API checks re-authentications created by PIN.
        
        Args:
            event_based_multi_factor_token: Model Class containing Definition for SecondFactorValidationToken
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition of Complete Validation data
        18.40
        """
        if(event_based_multi_factor_token is None):
            raise Exception(self._lr_object.get_validation_message("event_based_multi_factor_token"))

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/account/" + uid + "/reauth/pin"
        return self._lr_object.execute("POST", resource_path, query_parameters, event_based_multi_factor_token)

    def verify_pin_authentication(self, access_token, pin_auth_event_based_auth_model_with_lockout, sms_template2_f_a=None):
        """This API is used to validate the triggered MFA authentication flow with a password.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            pin_auth_event_based_auth_model_with_lockout: Model Class containing Definition of payload for PIN
            sms_template2_f_a: SMS Template Name
		
        Returns:
            Response containing Definition response of MFA reauthentication
        42.13
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))
        if(pin_auth_event_based_auth_model_with_lockout is None):
            raise Exception(self._lr_object.get_validation_message("pin_auth_event_based_auth_model_with_lockout"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(sms_template2_f_a)):
            query_parameters["smsTemplate2FA"] = sms_template2_f_a

        resource_path = "identity/v2/auth/account/reauth/pin"
        return self._lr_object.execute("PUT", resource_path, query_parameters, pin_auth_event_based_auth_model_with_lockout)

    def re_auth_validate_email_otp(self, access_token, reauth_by_email_otp_model):
        """This API is used to validate the triggered MFA authentication flow with an Email OTP.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            reauth_by_email_otp_model: payload
		
        Returns:
            Response containing Definition response of MFA reauthentication
        42.14
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))
        if(reauth_by_email_otp_model is None):
            raise Exception(self._lr_object.get_validation_message("reauth_by_email_otp_model"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/account/reauth/2fa/otp/email/verify"
        return self._lr_object.execute("PUT", resource_path, query_parameters, reauth_by_email_otp_model)

    def re_auth_send_email_otp(self, access_token, email_id, email_template2_f_a=None):
        """This API is used to send the MFA Email OTP to the email for Re-authentication
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            email_id: EmailId
            email_template2_f_a: EmailTemplate2FA
		
        Returns:
            Response containing Definition of Complete Validation data
        42.15
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(email_id)):
            raise Exception(self._lr_object.get_validation_message("email_id"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["emailId"] = email_id
        if(not self._lr_object.is_null_or_whitespace(email_template2_f_a)):
            query_parameters["emailTemplate2FA"] = email_template2_f_a

        resource_path = "identity/v2/auth/account/reauth/2fa/otp/email"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def re_auth_by_security_question(self, access_token, security_question_answer_update_model):
        """This API is used to validate the triggered MFA re-authentication flow with security questions answers.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            security_question_answer_update_model: payload
		
        Returns:
            Response containing Definition response of MFA reauthentication
        42.16
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))
        if(security_question_answer_update_model is None):
            raise Exception(self._lr_object.get_validation_message("security_question_answer_update_model"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/account/reauth/2fa/securityquestionanswer/verify"
        return self._lr_object.execute("POST", resource_path, query_parameters, security_question_answer_update_model)

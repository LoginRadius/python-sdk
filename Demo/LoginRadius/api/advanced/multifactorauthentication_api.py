# -- coding: utf-8 --
# Created by LoginRadius Development Team
# Copyright 2019 LoginRadius Inc. All rights reserved.
#


class MultiFactorAuthenticationApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    def mfa_configure_by_access_token(self, access_token, sms_template2_f_a=None):
        """This API is used to configure the Multi-factor authentication after login by using the access token when MFA is set as optional on the LoginRadius site.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            sms_template2_f_a: SMS Template Name
		
        Returns:
            Response containing Definition of Complete Multi-Factor Authentication Settings data
        5.7
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(sms_template2_f_a)):
            query_parameters["smsTemplate2FA"] = sms_template2_f_a

        resource_path = "identity/v2/auth/account/2fa"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def mfa_update_setting(self, access_token, multi_factor_auth_model_with_lockout, fields=''):
        """This API is used to trigger the Multi-factor authentication settings after login for secure actions
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            multi_factor_auth_model_with_lockout: Model Class containing Definition of payload for MultiFactorAuthModel With Lockout API
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
		
        Returns:
            Response containing Definition for Complete profile data
        5.9
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))
        if(multi_factor_auth_model_with_lockout is None):
            raise Exception(self._lr_object.get_validation_message("multi_factor_auth_model_with_lockout"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields

        resource_path = "identity/v2/auth/account/2fa/verification/otp"
        return self._lr_object.execute("PUT", resource_path, query_parameters, multi_factor_auth_model_with_lockout)

    def mfa_update_by_access_token(self, access_token, multi_factor_auth_model_by_google_authenticator_code, fields='',
        sms_template=None):
        """This API is used to Enable Multi-factor authentication by access token on user login
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            multi_factor_auth_model_by_google_authenticator_code: Model Class containing Definition of payload for MultiFactorAuthModel By GoogleAuthenticator Code API
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            sms_template: SMS Template name
		
        Returns:
            Response containing Definition for Complete profile data
        5.10
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))
        if(multi_factor_auth_model_by_google_authenticator_code is None):
            raise Exception(self._lr_object.get_validation_message("multi_factor_auth_model_by_google_authenticator_code"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(not self._lr_object.is_null_or_whitespace(sms_template)):
            query_parameters["smsTemplate"] = sms_template

        resource_path = "identity/v2/auth/account/2fa/verification/googleauthenticatorcode"
        return self._lr_object.execute("PUT", resource_path, query_parameters, multi_factor_auth_model_by_google_authenticator_code)

    def mfa_update_phone_number_by_token(self, access_token, phone_no2_f_a, sms_template2_f_a=None):
        """This API is used to update the Multi-factor authentication phone number by sending the verification OTP to the provided phone number
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            phone_no2_f_a: Phone Number For 2FA
            sms_template2_f_a: SMS Template Name
		
        Returns:
            Response containing Definition for Complete SMS data
        5.11
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(phone_no2_f_a)):
            raise Exception(self._lr_object.get_validation_message("phone_no2_f_a"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(sms_template2_f_a)):
            query_parameters["smsTemplate2FA"] = sms_template2_f_a

        body_parameters = {}
        body_parameters["phoneNo2FA"] = phone_no2_f_a

        resource_path = "identity/v2/auth/account/2fa"
        return self._lr_object.execute("PUT", resource_path, query_parameters, body_parameters)

    def mfa_reset_google_auth_by_token(self, access_token, googleauthenticator):
        """This API Resets the Google Authenticator configurations on a given account via the access token
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            googleauthenticator: boolean type value,Enable google Authenticator Code.
		
        Returns:
            Response containing Definition of Delete Request
        5.12.1
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        body_parameters = {}
        body_parameters["googleauthenticator"] = googleauthenticator

        resource_path = "identity/v2/auth/account/2fa/authenticator"
        return self._lr_object.execute("DELETE", resource_path, query_parameters, body_parameters)

    def mfa_reset_sms_auth_by_token(self, access_token, otpauthenticator):
        """This API resets the SMS Authenticator configurations on a given account via the access token.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            otpauthenticator: Pass 'otpauthenticator' to remove SMS Authenticator
		
        Returns:
            Response containing Definition of Delete Request
        5.12.2
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        body_parameters = {}
        body_parameters["otpauthenticator"] = otpauthenticator

        resource_path = "identity/v2/auth/account/2fa/authenticator"
        return self._lr_object.execute("DELETE", resource_path, query_parameters, body_parameters)

    def mfa_backup_code_by_access_token(self, access_token):
        """This API is used to get a set of backup codes via access token to allow the user login on a site that has Multi-factor Authentication enabled in the event that the user does not have a secondary factor available. We generate 10 codes, each code can only be consumed once. If any user attempts to go over the number of invalid login attempts configured in the Dashboard then the account gets blocked automatically
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
		
        Returns:
            Response containing Definition of Complete Backup Code data
        5.13
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/account/2fa/backupcode"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def mfa_reset_backup_code_by_access_token(self, access_token):
        """API is used to reset the backup codes on a given account via the access token. This API call will generate 10 new codes, each code can only be consumed once
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
		
        Returns:
            Response containing Definition of Complete Backup Code data
        5.14
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/account/2fa/backupcode/reset"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def mfa_email_otp_by_access_token(self, access_token, email_id, email_template2_f_a=None):
        """This API is created to send the OTP to the email if email OTP authenticator is enabled in app's MFA configuration.
        
        Args:
            access_token: access_token
            email_id: EmailId
            email_template2_f_a: EmailTemplate2FA
		
        Returns:
            Response containing Definition of Complete Validation data
        5.17
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

        resource_path = "identity/v2/auth/account/2fa/otp/email"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def mfa_validate_email_otp_by_access_token(self, access_token, multi_factor_auth_model_by_email_otp_with_lockout):
        """This API is used to set up MFA Email OTP authenticator on profile after login.
        
        Args:
            access_token: access_token
            multi_factor_auth_model_by_email_otp_with_lockout: payload
		
        Returns:
            Response containing Definition for Complete profile data
        5.18
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))
        if(multi_factor_auth_model_by_email_otp_with_lockout is None):
            raise Exception(self._lr_object.get_validation_message("multi_factor_auth_model_by_email_otp_with_lockout"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/account/2fa/verification/otp/email"
        return self._lr_object.execute("PUT", resource_path, query_parameters, multi_factor_auth_model_by_email_otp_with_lockout)

    def mfa_reset_email_otp_authenticator_by_access_token(self, access_token):
        """This API is used to reset the Email OTP Authenticator settings for an MFA-enabled user
        
        Args:
            access_token: access_token
		
        Returns:
            Response containing Definition of Delete Request
        5.19
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/account/2fa/authenticator/otp/email"
        return self._lr_object.execute("DELETE", resource_path, query_parameters, {})

    def mfa_security_question_answer_by_access_token(self, access_token, security_question_answer_model_by_access_token):
        """This API is used to set up MFA Security Question authenticator on profile after login.
        
        Args:
            access_token: access_token
            security_question_answer_model_by_access_token: payload
		
        Returns:
            Response containing Definition of Complete Validation data
        5.20
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))
        if(security_question_answer_model_by_access_token is None):
            raise Exception(self._lr_object.get_validation_message("security_question_answer_model_by_access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/account/2fa/securityquestionanswer"
        return self._lr_object.execute("PUT", resource_path, query_parameters, security_question_answer_model_by_access_token)

    def mfa_reset_security_question_authenticator_by_access_token(self, access_token):
        """This API is used to Reset MFA Security Question Authenticator By Access Token
        
        Args:
            access_token: access_token
		
        Returns:
            Response containing Definition of Delete Request
        5.21
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/account/2fa/authenticator/securityquestionanswer"
        return self._lr_object.execute("DELETE", resource_path, query_parameters, {})

    def mfa_login_by_email(self, email, password, email_template=None, fields='',
        login_url=None, sms_template=None,sms_template2_f_a=None, 
        verification_url=None,email_template2_f_a=None):
        """This API can be used to login by emailid on a Multi-factor authentication enabled LoginRadius site.
        
        Args:
            email: user's email
            password: Password for the email
            email_template: Email template name
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            login_url: Url where the user is logging from
            sms_template: SMS Template name
            sms_template2_f_a: SMS Template Name
            verification_url: Email verification url
            email_template2_f_a: 2FA Email Template name

		
        Returns:
            Complete user UserProfile data
        9.8.1
        """

        if(self._lr_object.is_null_or_whitespace(email)):
            raise Exception(self._lr_object.get_validation_message("email"))

        if(self._lr_object.is_null_or_whitespace(password)):
            raise Exception(self._lr_object.get_validation_message("password"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(email_template)):
            query_parameters["emailTemplate"] = email_template
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(not self._lr_object.is_null_or_whitespace(login_url)):
            query_parameters["loginUrl"] = login_url
        if(not self._lr_object.is_null_or_whitespace(sms_template)):
            query_parameters["smsTemplate"] = sms_template
        if(not self._lr_object.is_null_or_whitespace(sms_template2_f_a)):
            query_parameters["smsTemplate2FA"] = sms_template2_f_a
        if(not self._lr_object.is_null_or_whitespace(verification_url)):
            query_parameters["verificationUrl"] = verification_url
        if(not self._lr_object.is_null_or_whitespace(email_template2_f_a)):
            query_parameters["emailTemplate2FA"] = email_template2_f_a

        body_parameters = {}
        body_parameters["email"] = email
        body_parameters["password"] = password

        resource_path = "identity/v2/auth/login/2fa"
        return self._lr_object.execute("POST", resource_path, query_parameters, body_parameters)

    def mfa_login_by_user_name(self, password, username, email_template=None, fields='',
        login_url=None, sms_template=None,sms_template2_f_a=None,
        verification_url=None, email_template2_f_a=None):
        """This API can be used to login by username on a Multi-factor authentication enabled LoginRadius site.
        
        Args:
            password: Password for the email
            username: Username of the user
            email_template: Email template name
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            login_url: Url where the user is logging from
            sms_template: SMS Template name
            sms_template2_f_a: SMS Template Name
            verification_url: Email verification url
            email_template2_f_a: 2FA Email Template name

		
        Returns:
            Complete user UserProfile data
        9.8.2
        """

        if(self._lr_object.is_null_or_whitespace(password)):
            raise Exception(self._lr_object.get_validation_message("password"))

        if(self._lr_object.is_null_or_whitespace(username)):
            raise Exception(self._lr_object.get_validation_message("username"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(email_template)):
            query_parameters["emailTemplate"] = email_template
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(not self._lr_object.is_null_or_whitespace(login_url)):
            query_parameters["loginUrl"] = login_url
        if(not self._lr_object.is_null_or_whitespace(sms_template)):
            query_parameters["smsTemplate"] = sms_template
        if(not self._lr_object.is_null_or_whitespace(sms_template2_f_a)):
            query_parameters["smsTemplate2FA"] = sms_template2_f_a
        if(not self._lr_object.is_null_or_whitespace(verification_url)):
            query_parameters["verificationUrl"] = verification_url
        if(not self._lr_object.is_null_or_whitespace(email_template2_f_a)):
            query_parameters["emailTemplate2FA"] = email_template2_f_a

        body_parameters = {}
        body_parameters["password"] = password
        body_parameters["username"] = username

        resource_path = "identity/v2/auth/login/2fa"
        return self._lr_object.execute("POST", resource_path, query_parameters, body_parameters)

    def mfa_login_by_phone(self, password, phone, email_template=None,
        fields='', login_url=None, sms_template=None,sms_template2_f_a=None,
        verification_url=None, email_template2_f_a=None,):
        """This API can be used to login by Phone on a Multi-factor authentication enabled LoginRadius site.
        
        Args:
            password: Password for the email
            phone: New Phone Number
            email_template: Email template name
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            login_url: Url where the user is logging from
            sms_template: SMS Template name
            sms_template2_f_a: SMS Template Name
            verification_url: Email verification url
            email_template2_f_a: 2FA Email Template name

		
        Returns:
            Complete user UserProfile data
        9.8.3
        """

        if(self._lr_object.is_null_or_whitespace(password)):
            raise Exception(self._lr_object.get_validation_message("password"))

        if(self._lr_object.is_null_or_whitespace(phone)):
            raise Exception(self._lr_object.get_validation_message("phone"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(email_template)):
            query_parameters["emailTemplate"] = email_template
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(not self._lr_object.is_null_or_whitespace(login_url)):
            query_parameters["loginUrl"] = login_url
        if(not self._lr_object.is_null_or_whitespace(sms_template)):
            query_parameters["smsTemplate"] = sms_template
        if(not self._lr_object.is_null_or_whitespace(sms_template2_f_a)):
            query_parameters["smsTemplate2FA"] = sms_template2_f_a
        if(not self._lr_object.is_null_or_whitespace(verification_url)):
            query_parameters["verificationUrl"] = verification_url
        if(not self._lr_object.is_null_or_whitespace(email_template2_f_a)):
            query_parameters["emailTemplate2FA"] = email_template2_f_a

        body_parameters = {}
        body_parameters["password"] = password
        body_parameters["phone"] = phone

        resource_path = "identity/v2/auth/login/2fa"
        return self._lr_object.execute("POST", resource_path, query_parameters, body_parameters)

    def mfa_validate_otp_by_phone(self, multi_factor_auth_model_with_lockout, second_factor_authentication_token, fields='', 
        sms_template2_f_a=None, rba_browser_email_template=None, rba_city_email_template=None, rba_country_email_template=None, 
        rba_ip_email_template=None):
        """This API is used to login via Multi-factor authentication by passing the One Time Password received via SMS
        
        Args:
            multi_factor_auth_model_with_lockout: Model Class containing Definition of payload for MultiFactorAuthModel With Lockout API
            second_factor_authentication_token: A Uniquely generated MFA identifier token after successful authentication
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            sms_template2_f_a: SMS Template Name
            rba_browser_email_template: 
            rba_city_email_template: 
            rba_country_email_template: 
            rba_ip_email_template: 
		
        Returns:
            Complete user UserProfile data
        9.12
        """
        if(multi_factor_auth_model_with_lockout is None):
            raise Exception(self._lr_object.get_validation_message("multi_factor_auth_model_with_lockout"))

        if(self._lr_object.is_null_or_whitespace(second_factor_authentication_token)):
            raise Exception(self._lr_object.get_validation_message("second_factor_authentication_token"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["secondFactorAuthenticationToken"] = second_factor_authentication_token
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(not self._lr_object.is_null_or_whitespace(rba_browser_email_template)):
            query_parameters["rbaBrowserEmailTemplate"] = rba_browser_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_city_email_template)):
            query_parameters["rbaCityEmailTemplate"] = rba_city_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_country_email_template)):
            query_parameters["rbaCountryEmailTemplate"] = rba_country_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_ip_email_template)):
            query_parameters["rbaIpEmailTemplate"] = rba_ip_email_template
        if(not self._lr_object.is_null_or_whitespace(sms_template2_f_a)):
            query_parameters["smsTemplate2FA"] = sms_template2_f_a

        resource_path = "identity/v2/auth/login/2fa/verification/otp"
        return self._lr_object.execute("PUT", resource_path, query_parameters, multi_factor_auth_model_with_lockout)

    def mfa_validate_google_auth_code(self, google_authenticator_code, second_factor_authentication_token, fields='',
        rba_browser_email_template=None, rba_city_email_template=None, rba_country_email_template=None, rba_ip_email_template=None):
        """This API is used to login via Multi-factor-authentication by passing the google authenticator code.
        
        Args:
            google_authenticator_code: The code generated by google authenticator app after scanning QR code
            second_factor_authentication_token: SecondFactorAuthenticationToken
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            rba_browser_email_template: RbaBrowserEmailTemplate
            rba_city_email_template: RbaCityEmailTemplate
            rba_country_email_template: RbaCountryEmailTemplate
            rba_ip_email_template: RbaIpEmailTemplate
		
        Returns:
            Complete user UserProfile data
        9.13
        """

        if(self._lr_object.is_null_or_whitespace(google_authenticator_code)):
            raise Exception(self._lr_object.get_validation_message("google_authenticator_code"))

        if(self._lr_object.is_null_or_whitespace(second_factor_authentication_token)):
            raise Exception(self._lr_object.get_validation_message("second_factor_authentication_token"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["secondFactorAuthenticationToken"] = second_factor_authentication_token
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(not self._lr_object.is_null_or_whitespace(rba_browser_email_template)):
            query_parameters["rbaBrowserEmailTemplate"] = rba_browser_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_city_email_template)):
            query_parameters["rbaCityEmailTemplate"] = rba_city_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_country_email_template)):
            query_parameters["rbaCountryEmailTemplate"] = rba_country_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_ip_email_template)):
            query_parameters["rbaIpEmailTemplate"] = rba_ip_email_template

        body_parameters = {}
        body_parameters["googleAuthenticatorCode"] = google_authenticator_code

        resource_path = "identity/v2/auth/login/2fa/verification/googleauthenticatorcode"
        return self._lr_object.execute("PUT", resource_path, query_parameters, body_parameters)

    def mfa_validate_backup_code(self, multi_factor_auth_model_by_backup_code, second_factor_authentication_token, fields='',
        rba_browser_email_template=None, rba_city_email_template=None, rba_country_email_template=None, rba_ip_email_template=None):
        """This API is used to validate the backup code provided by the user and if valid, we return an access token allowing the user to login incases where Multi-factor authentication (MFA) is enabled and the secondary factor is unavailable. When a user initially downloads the Backup codes, We generate 10 codes, each code can only be consumed once. if any user attempts to go over the number of invalid login attempts configured in the Dashboard then the account gets blocked automatically
        
        Args:
            multi_factor_auth_model_by_backup_code: Model Class containing Definition of payload for MultiFactorAuth By BackupCode API
            second_factor_authentication_token: A Uniquely generated MFA identifier token after successful authentication
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            rba_browser_email_template: 
            rba_city_email_template: 
            rba_country_email_template: 
            rba_ip_email_template: 
		
        Returns:
            Complete user UserProfile data
        9.14
        """
        if(multi_factor_auth_model_by_backup_code is None):
            raise Exception(self._lr_object.get_validation_message("multi_factor_auth_model_by_backup_code"))

        if(self._lr_object.is_null_or_whitespace(second_factor_authentication_token)):
            raise Exception(self._lr_object.get_validation_message("second_factor_authentication_token"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["secondFactorAuthenticationToken"] = second_factor_authentication_token
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(not self._lr_object.is_null_or_whitespace(rba_browser_email_template)):
            query_parameters["rbaBrowserEmailTemplate"] = rba_browser_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_city_email_template)):
            query_parameters["rbaCityEmailTemplate"] = rba_city_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_country_email_template)):
            query_parameters["rbaCountryEmailTemplate"] = rba_country_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_ip_email_template)):
            query_parameters["rbaIpEmailTemplate"] = rba_ip_email_template

        resource_path = "identity/v2/auth/login/2fa/verification/backupcode"
        return self._lr_object.execute("PUT", resource_path, query_parameters, multi_factor_auth_model_by_backup_code)

    def mfa_update_phone_number(self, phone_no2_f_a, second_factor_authentication_token, sms_template2_f_a=None):
        """This API is used to update (if configured) the phone number used for Multi-factor authentication by sending the verification OTP to the provided phone number
        
        Args:
            phone_no2_f_a: Phone Number For 2FA
            second_factor_authentication_token: A Uniquely generated MFA identifier token after successful authentication
            sms_template2_f_a: SMS Template Name
		
        Returns:
            Response containing Definition for Complete SMS data
        9.16
        """

        if(self._lr_object.is_null_or_whitespace(phone_no2_f_a)):
            raise Exception(self._lr_object.get_validation_message("phone_no2_f_a"))

        if(self._lr_object.is_null_or_whitespace(second_factor_authentication_token)):
            raise Exception(self._lr_object.get_validation_message("second_factor_authentication_token"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["secondFactorAuthenticationToken"] = second_factor_authentication_token
        if(not self._lr_object.is_null_or_whitespace(sms_template2_f_a)):
            query_parameters["smsTemplate2FA"] = sms_template2_f_a

        body_parameters = {}
        body_parameters["phoneNo2FA"] = phone_no2_f_a

        resource_path = "identity/v2/auth/login/2fa"
        return self._lr_object.execute("PUT", resource_path, query_parameters, body_parameters)

    def mfa_resend_otp(self, second_factor_authentication_token, sms_template2_f_a=None):
        """This API is used to resending the verification OTP to the provided phone number
        
        Args:
            second_factor_authentication_token: A Uniquely generated MFA identifier token after successful authentication
            sms_template2_f_a: SMS Template Name
		
        Returns:
            Response containing Definition for Complete SMS data
        9.17
        """

        if(self._lr_object.is_null_or_whitespace(second_factor_authentication_token)):
            raise Exception(self._lr_object.get_validation_message("second_factor_authentication_token"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["secondFactorAuthenticationToken"] = second_factor_authentication_token
        if(not self._lr_object.is_null_or_whitespace(sms_template2_f_a)):
            query_parameters["smsTemplate2FA"] = sms_template2_f_a

        resource_path = "identity/v2/auth/login/2fa/resend"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def mfa_email_otp(self, email_id_model, second_factor_authentication_token, email_template2_f_a=None):
        """An API designed to send the MFA Email OTP to the email.
        
        Args:
            email_id_model: payload
            second_factor_authentication_token: SecondFactorAuthenticationToken
            email_template2_f_a: EmailTemplate2FA
		
        Returns:
            Response containing Definition of Complete Validation data
        9.18
        """
        if(email_id_model is None):
            raise Exception(self._lr_object.get_validation_message("email_id_model"))

        if(self._lr_object.is_null_or_whitespace(second_factor_authentication_token)):
            raise Exception(self._lr_object.get_validation_message("second_factor_authentication_token"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["secondFactorAuthenticationToken"] = second_factor_authentication_token
        if(not self._lr_object.is_null_or_whitespace(email_template2_f_a)):
            query_parameters["emailTemplate2FA"] = email_template2_f_a

        resource_path = "identity/v2/auth/login/2fa/otp/email"
        return self._lr_object.execute("POST", resource_path, query_parameters, email_id_model)

    def mfa_validate_email_otp(self, multi_factor_auth_model_by_email_otp, second_factor_authentication_token, rba_browser_email_template=None,
        rba_city_email_template=None, rba_country_email_template=None, rba_ip_email_template=None):
        """This API is used to Verify MFA Email OTP by MFA Token
        
        Args:
            multi_factor_auth_model_by_email_otp: payload
            second_factor_authentication_token: SecondFactorAuthenticationToken
            rba_browser_email_template: RbaBrowserEmailTemplate
            rba_city_email_template: RbaCityEmailTemplate
            rba_country_email_template: RbaCountryEmailTemplate
            rba_ip_email_template: RbaIpEmailTemplate
		
        Returns:
            Response Containing Access Token and Complete Profile Data
        9.25
        """
        if(multi_factor_auth_model_by_email_otp is None):
            raise Exception(self._lr_object.get_validation_message("multi_factor_auth_model_by_email_otp"))

        if(self._lr_object.is_null_or_whitespace(second_factor_authentication_token)):
            raise Exception(self._lr_object.get_validation_message("second_factor_authentication_token"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["secondFactorAuthenticationToken"] = second_factor_authentication_token
        if(not self._lr_object.is_null_or_whitespace(rba_browser_email_template)):
            query_parameters["rbaBrowserEmailTemplate"] = rba_browser_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_city_email_template)):
            query_parameters["rbaCityEmailTemplate"] = rba_city_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_country_email_template)):
            query_parameters["rbaCountryEmailTemplate"] = rba_country_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_ip_email_template)):
            query_parameters["rbaIpEmailTemplate"] = rba_ip_email_template

        resource_path = "identity/v2/auth/login/2fa/verification/otp/email"
        return self._lr_object.execute("PUT", resource_path, query_parameters, multi_factor_auth_model_by_email_otp)

    def mfa_security_question_answer(self, security_question_answer_update_model, second_factor_authentication_token):
        """This API is used to set the security questions on the profile with the MFA token when MFA flow is required.
        
        Args:
            security_question_answer_update_model: payload
            second_factor_authentication_token: SecondFactorAuthenticationToken
		
        Returns:
            Response Containing Access Token and Complete Profile Data
        9.26
        """
        if(security_question_answer_update_model is None):
            raise Exception(self._lr_object.get_validation_message("security_question_answer_update_model"))

        if(self._lr_object.is_null_or_whitespace(second_factor_authentication_token)):
            raise Exception(self._lr_object.get_validation_message("second_factor_authentication_token"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["secondFactorAuthenticationToken"] = second_factor_authentication_token

        resource_path = "identity/v2/auth/login/2fa/securityquestionanswer"
        return self._lr_object.execute("PUT", resource_path, query_parameters, security_question_answer_update_model)

    def mfa_security_question_answer_verification(self, security_question_answer_update_model, second_factor_authentication_token, rba_browser_email_template=None,
        rba_city_email_template=None, rba_country_email_template=None, rba_ip_email_template=None):
        """This API is used to resending the verification OTP to the provided phone number
        
        Args:
            security_question_answer_update_model: payload
            second_factor_authentication_token: SecondFactorAuthenticationToken
            rba_browser_email_template: RbaBrowserEmailTemplate
            rba_city_email_template: RbaCityEmailTemplate
            rba_country_email_template: RbaCountryEmailTemplate
            rba_ip_email_template: RbaIpEmailTemplate
		
        Returns:
            Response Containing Access Token and Complete Profile Data
        9.27
        """
        if(security_question_answer_update_model is None):
            raise Exception(self._lr_object.get_validation_message("security_question_answer_update_model"))

        if(self._lr_object.is_null_or_whitespace(second_factor_authentication_token)):
            raise Exception(self._lr_object.get_validation_message("second_factor_authentication_token"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["secondFactorAuthenticationToken"] = second_factor_authentication_token
        if(not self._lr_object.is_null_or_whitespace(rba_browser_email_template)):
            query_parameters["rbaBrowserEmailTemplate"] = rba_browser_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_city_email_template)):
            query_parameters["rbaCityEmailTemplate"] = rba_city_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_country_email_template)):
            query_parameters["rbaCountryEmailTemplate"] = rba_country_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_ip_email_template)):
            query_parameters["rbaIpEmailTemplate"] = rba_ip_email_template

        resource_path = "identity/v2/auth/login/2fa/verification/securityquestionanswer"
        return self._lr_object.execute("POST", resource_path, query_parameters, security_question_answer_update_model)

    def mfa_reset_sms_authenticator_by_uid(self, otpauthenticator, uid):
        """This API resets the SMS Authenticator configurations on a given account via the UID.
        
        Args:
            otpauthenticator: Pass 'otpauthenticator' to remove SMS Authenticator
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition of Delete Request
        18.21.1
        """

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        query_parameters["uid"] = uid

        body_parameters = {}
        body_parameters["otpauthenticator"] = otpauthenticator

        resource_path = "identity/v2/manage/account/2fa/authenticator"
        return self._lr_object.execute("DELETE", resource_path, query_parameters, body_parameters)

    def mfa_reset_google_authenticator_by_uid(self, googleauthenticator, uid):
        """This API resets the Google Authenticator configurations on a given account via the UID.
        
        Args:
            googleauthenticator: boolean type value,Enable google Authenticator Code.
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition of Delete Request
        18.21.2
        """

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        query_parameters["uid"] = uid

        body_parameters = {}
        body_parameters["googleauthenticator"] = googleauthenticator

        resource_path = "identity/v2/manage/account/2fa/authenticator"
        return self._lr_object.execute("DELETE", resource_path, query_parameters, body_parameters)

    def mfa_backup_code_by_uid(self, uid):
        """This API is used to reset the backup codes on a given account via the UID. This API call will generate 10 new codes, each code can only be consumed once.
        
        Args:
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition of Complete Backup Code data
        18.25
        """

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        query_parameters["uid"] = uid

        resource_path = "identity/v2/manage/account/2fa/backupcode"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def mfa_reset_backup_code_by_uid(self, uid):
        """This API is used to reset the backup codes on a given account via the UID. This API call will generate 10 new codes, each code can only be consumed once.
        
        Args:
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition of Complete Backup Code data
        18.26
        """

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        query_parameters["uid"] = uid

        resource_path = "identity/v2/manage/account/2fa/backupcode/reset"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def mfa_reset_email_otp_authenticator_by_uid(self, uid):
        """This API is used to reset the Email OTP Authenticator settings for an MFA-enabled user.
        
        Args:
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition of Delete Request
        18.42
        """

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        query_parameters["uid"] = uid

        resource_path = "identity/v2/manage/account/2fa/authenticator/otp/email"
        return self._lr_object.execute("DELETE", resource_path, query_parameters, {})

    def mfa_reset_security_question_authenticator_by_uid(self, uid):
        """This API is used to reset the Security Question Authenticator settings for an MFA-enabled user.
        
        Args:
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition of Delete Request
        18.43
        """

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        query_parameters["uid"] = uid

        resource_path = "identity/v2/manage/account/2fa/authenticator/securityquestionanswer"
        return self._lr_object.execute("DELETE", resource_path, query_parameters, {})

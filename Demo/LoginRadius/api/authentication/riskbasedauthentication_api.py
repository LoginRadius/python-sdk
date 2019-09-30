# -- coding: utf-8 --
# Created by LoginRadius Development Team
# Copyright 2019 LoginRadius Inc. All rights reserved.
#


class RiskBasedAuthenticationApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    def rba_login_by_email(self, email_authentication_model, email_template=None, fields='',
        login_url=None, password_delegation=None, password_delegation_app=None, rba_browser_email_template=None,
        rba_browser_sms_template=None, rba_city_email_template=None, rba_city_sms_template=None, rba_country_email_template=None,
        rba_country_sms_template=None, rba_ip_email_template=None, rba_ip_sms_template=None, rba_oneclick_email_template=None,
        rba_otp_sms_template=None, sms_template=None, verification_url=None):
        """This API retrieves a copy of the user data based on the Email
        
        Args:
            email_authentication_model: Model Class containing Definition of payload for Email Authentication API
            email_template: Email template name
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            login_url: Url where the user is logging from
            password_delegation: Password Delegation Allows you to use a third-party service to store your passwords rather than LoginRadius Cloud storage.
            password_delegation_app: RiskBased Authentication Password Delegation App
            rba_browser_email_template: Risk Based Authentication Browser EmailTemplate
            rba_browser_sms_template: Risk Based Authentication Browser Sms Template
            rba_city_email_template: Risk Based Authentication City Email Template
            rba_city_sms_template: Risk Based Authentication City SmsTemplate
            rba_country_email_template: Risk Based Authentication Country EmailTemplate
            rba_country_sms_template: Risk Based Authentication Country SmsTemplate
            rba_ip_email_template: Risk Based Authentication Ip EmailTemplate
            rba_ip_sms_template: Risk Based Authentication Ip SmsTemplate
            rba_oneclick_email_template: Risk Based Authentication Oneclick EmailTemplate
            rba_otp_sms_template: Risk Based Authentication Oneclick EmailTemplate
            sms_template: SMS Template name
            verification_url: Email verification url
		
        Returns:
            Response containing User Profile Data and access token
        9.2.4
        """
        if(email_authentication_model is None):
            raise Exception(self._lr_object.get_validation_message("email_authentication_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(email_template)):
            query_parameters["emailTemplate"] = email_template
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(not self._lr_object.is_null_or_whitespace(login_url)):
            query_parameters["loginUrl"] = login_url
        if(password_delegation is not None):
            query_parameters["passwordDelegation"] = password_delegation
        if(not self._lr_object.is_null_or_whitespace(password_delegation_app)):
            query_parameters["passwordDelegationApp"] = password_delegation_app
        if(not self._lr_object.is_null_or_whitespace(rba_browser_email_template)):
            query_parameters["rbaBrowserEmailTemplate"] = rba_browser_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_browser_sms_template)):
            query_parameters["rbaBrowserSmsTemplate"] = rba_browser_sms_template
        if(not self._lr_object.is_null_or_whitespace(rba_city_email_template)):
            query_parameters["rbaCityEmailTemplate"] = rba_city_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_city_sms_template)):
            query_parameters["rbaCitySmsTemplate"] = rba_city_sms_template
        if(not self._lr_object.is_null_or_whitespace(rba_country_email_template)):
            query_parameters["rbaCountryEmailTemplate"] = rba_country_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_country_sms_template)):
            query_parameters["rbaCountrySmsTemplate"] = rba_country_sms_template
        if(not self._lr_object.is_null_or_whitespace(rba_ip_email_template)):
            query_parameters["rbaIpEmailTemplate"] = rba_ip_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_ip_sms_template)):
            query_parameters["rbaIpSmsTemplate"] = rba_ip_sms_template
        if(not self._lr_object.is_null_or_whitespace(rba_oneclick_email_template)):
            query_parameters["rbaOneclickEmailTemplate"] = rba_oneclick_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_otp_sms_template)):
            query_parameters["rbaOTPSmsTemplate"] = rba_otp_sms_template
        if(not self._lr_object.is_null_or_whitespace(sms_template)):
            query_parameters["smsTemplate"] = sms_template
        if(not self._lr_object.is_null_or_whitespace(verification_url)):
            query_parameters["verificationUrl"] = verification_url

        resource_path = "identity/v2/auth/login"
        return self._lr_object.execute("POST", resource_path, query_parameters, email_authentication_model)

    def rba_login_by_user_name(self, user_name_authentication_model, email_template=None, fields='',
        login_url=None, password_delegation=None, password_delegation_app=None, rba_browser_email_template=None,
        rba_browser_sms_template=None, rba_city_email_template=None, rba_city_sms_template=None, rba_country_email_template=None,
        rba_country_sms_template=None, rba_ip_email_template=None, rba_ip_sms_template=None, rba_oneclick_email_template=None,
        rba_otp_sms_template=None, sms_template=None, verification_url=None):
        """This API retrieves a copy of the user data based on the Username
        
        Args:
            user_name_authentication_model: Model Class containing Definition of payload for Username Authentication API
            email_template: Email template name
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            login_url: Url where the user is logging from
            password_delegation: Password Delegation Allows you to use a third-party service to store your passwords rather than LoginRadius Cloud storage.
            password_delegation_app: RiskBased Authentication Password Delegation App
            rba_browser_email_template: Risk Based Authentication Browser EmailTemplate
            rba_browser_sms_template: Risk Based Authentication Browser Sms Template
            rba_city_email_template: Risk Based Authentication City Email Template
            rba_city_sms_template: Risk Based Authentication City SmsTemplate
            rba_country_email_template: Risk Based Authentication Country EmailTemplate
            rba_country_sms_template: Risk Based Authentication Country SmsTemplate
            rba_ip_email_template: Risk Based Authentication Ip EmailTemplate
            rba_ip_sms_template: Risk Based Authentication Ip SmsTemplate
            rba_oneclick_email_template: Risk Based Authentication Oneclick EmailTemplate
            rba_otp_sms_template: Risk Based Authentication OTPSmsTemplate
            sms_template: SMS Template name
            verification_url: Email verification url
		
        Returns:
            Response containing User Profile Data and access token
        9.2.5
        """
        if(user_name_authentication_model is None):
            raise Exception(self._lr_object.get_validation_message("user_name_authentication_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(email_template)):
            query_parameters["emailTemplate"] = email_template
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(not self._lr_object.is_null_or_whitespace(login_url)):
            query_parameters["loginUrl"] = login_url
        if(password_delegation is not None):
            query_parameters["passwordDelegation"] = password_delegation
        if(not self._lr_object.is_null_or_whitespace(password_delegation_app)):
            query_parameters["passwordDelegationApp"] = password_delegation_app
        if(not self._lr_object.is_null_or_whitespace(rba_browser_email_template)):
            query_parameters["rbaBrowserEmailTemplate"] = rba_browser_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_browser_sms_template)):
            query_parameters["rbaBrowserSmsTemplate"] = rba_browser_sms_template
        if(not self._lr_object.is_null_or_whitespace(rba_city_email_template)):
            query_parameters["rbaCityEmailTemplate"] = rba_city_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_city_sms_template)):
            query_parameters["rbaCitySmsTemplate"] = rba_city_sms_template
        if(not self._lr_object.is_null_or_whitespace(rba_country_email_template)):
            query_parameters["rbaCountryEmailTemplate"] = rba_country_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_country_sms_template)):
            query_parameters["rbaCountrySmsTemplate"] = rba_country_sms_template
        if(not self._lr_object.is_null_or_whitespace(rba_ip_email_template)):
            query_parameters["rbaIpEmailTemplate"] = rba_ip_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_ip_sms_template)):
            query_parameters["rbaIpSmsTemplate"] = rba_ip_sms_template
        if(not self._lr_object.is_null_or_whitespace(rba_oneclick_email_template)):
            query_parameters["rbaOneclickEmailTemplate"] = rba_oneclick_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_otp_sms_template)):
            query_parameters["rbaOTPSmsTemplate"] = rba_otp_sms_template
        if(not self._lr_object.is_null_or_whitespace(sms_template)):
            query_parameters["smsTemplate"] = sms_template
        if(not self._lr_object.is_null_or_whitespace(verification_url)):
            query_parameters["verificationUrl"] = verification_url

        resource_path = "identity/v2/auth/login"
        return self._lr_object.execute("POST", resource_path, query_parameters, user_name_authentication_model)

    def rba_login_by_phone(self, phone_authentication_model, email_template=None, fields='',
        login_url=None, password_delegation=None, password_delegation_app=None, rba_browser_email_template=None,
        rba_browser_sms_template=None, rba_city_email_template=None, rba_city_sms_template=None, rba_country_email_template=None,
        rba_country_sms_template=None, rba_ip_email_template=None, rba_ip_sms_template=None, rba_oneclick_email_template=None,
        rba_otp_sms_template=None, sms_template=None, verification_url=None):
        """This API retrieves a copy of the user data based on the Phone
        
        Args:
            phone_authentication_model: Model Class containing Definition of payload for PhoneAuthenticationModel API
            email_template: Email template name
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            login_url: Url where the user is logging from
            password_delegation: Password Delegation Allows you to use a third-party service to store your passwords rather than LoginRadius Cloud storage.
            password_delegation_app: RiskBased Authentication Password Delegation App
            rba_browser_email_template: Risk Based Authentication Browser EmailTemplate
            rba_browser_sms_template: Risk Based Authentication Browser Sms Template
            rba_city_email_template: Risk Based Authentication City Email Template
            rba_city_sms_template: Risk Based Authentication City SmsTemplate
            rba_country_email_template: Risk Based Authentication Country EmailTemplate
            rba_country_sms_template: Risk Based Authentication Country SmsTemplate
            rba_ip_email_template: Risk Based Authentication Ip EmailTemplate
            rba_ip_sms_template: Risk Based Authentication Ip SmsTemplate
            rba_oneclick_email_template: Risk Based Authentication Oneclick EmailTemplate
            rba_otp_sms_template: Risk Based Authentication OTPSmsTemplate
            sms_template: SMS Template name
            verification_url: Email verification url
		
        Returns:
            Response containing User Profile Data and access token
        9.2.6
        """
        if(phone_authentication_model is None):
            raise Exception(self._lr_object.get_validation_message("phone_authentication_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(email_template)):
            query_parameters["emailTemplate"] = email_template
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(not self._lr_object.is_null_or_whitespace(login_url)):
            query_parameters["loginUrl"] = login_url
        if(password_delegation is not None):
            query_parameters["passwordDelegation"] = password_delegation
        if(not self._lr_object.is_null_or_whitespace(password_delegation_app)):
            query_parameters["passwordDelegationApp"] = password_delegation_app
        if(not self._lr_object.is_null_or_whitespace(rba_browser_email_template)):
            query_parameters["rbaBrowserEmailTemplate"] = rba_browser_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_browser_sms_template)):
            query_parameters["rbaBrowserSmsTemplate"] = rba_browser_sms_template
        if(not self._lr_object.is_null_or_whitespace(rba_city_email_template)):
            query_parameters["rbaCityEmailTemplate"] = rba_city_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_city_sms_template)):
            query_parameters["rbaCitySmsTemplate"] = rba_city_sms_template
        if(not self._lr_object.is_null_or_whitespace(rba_country_email_template)):
            query_parameters["rbaCountryEmailTemplate"] = rba_country_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_country_sms_template)):
            query_parameters["rbaCountrySmsTemplate"] = rba_country_sms_template
        if(not self._lr_object.is_null_or_whitespace(rba_ip_email_template)):
            query_parameters["rbaIpEmailTemplate"] = rba_ip_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_ip_sms_template)):
            query_parameters["rbaIpSmsTemplate"] = rba_ip_sms_template
        if(not self._lr_object.is_null_or_whitespace(rba_oneclick_email_template)):
            query_parameters["rbaOneclickEmailTemplate"] = rba_oneclick_email_template
        if(not self._lr_object.is_null_or_whitespace(rba_otp_sms_template)):
            query_parameters["rbaOTPSmsTemplate"] = rba_otp_sms_template
        if(not self._lr_object.is_null_or_whitespace(sms_template)):
            query_parameters["smsTemplate"] = sms_template
        if(not self._lr_object.is_null_or_whitespace(verification_url)):
            query_parameters["verificationUrl"] = verification_url

        resource_path = "identity/v2/auth/login"
        return self._lr_object.execute("POST", resource_path, query_parameters, phone_authentication_model)

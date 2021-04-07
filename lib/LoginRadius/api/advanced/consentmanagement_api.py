# -- coding: utf-8 --
# Created by LoginRadius Development Team
# Copyright 2019 LoginRadius Inc. All rights reserved.
#


class ConsentManagementApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    def get_consent_logs_by_uid(self, uid):
        """This API is used to get the Consent logs of the user.
        
        Args:
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing consent logs
        18.37
        """

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/account/" + uid + "/consent/logs"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def submit_consent_by_consent_token(self, consent_token, consent_submit_model):
        """This API is to submit consent form using consent token.
        
        Args:
            consent_token: The consent token received after login error 1226 
            consent_submit_model: Model class containing list of multiple consent
		
        Returns:
            Response containing User Profile Data and access token
        43.1
        """

        if(self._lr_object.is_null_or_whitespace(consent_token)):
            raise Exception(self._lr_object.get_validation_message("consent_token"))
        if(consent_submit_model is None):
            raise Exception(self._lr_object.get_validation_message("consent_submit_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["consentToken"] = consent_token

        resource_path = "identity/v2/auth/consent"
        return self._lr_object.execute("POST", resource_path, query_parameters, consent_submit_model)

    def get_consent_logs(self, access_token):
        """This API is used to fetch consent logs.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
		
        Returns:
            Response containing consent logs
        43.2
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/consent/logs"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def submit_consent_by_access_token(self, access_token, consent_submit_model):
        """API to provide a way to end user to submit a consent form for particular event type.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            consent_submit_model: Model class containing list of multiple consent
		
        Returns:
            Response containing Definition for Complete profile data
        43.3
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))
        if(consent_submit_model is None):
            raise Exception(self._lr_object.get_validation_message("consent_submit_model"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/consent/profile"
        return self._lr_object.execute("POST", resource_path, query_parameters, consent_submit_model)

    def verify_consent_by_access_token(self, access_token, event, is_custom):
        """This API is used to check if consent is submitted for a particular event or not.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            event: Allowed events: Login, Register, UpdateProfile, ResetPassword, ChangePassword, emailVerification, AddEmail, RemoveEmail, BlockAccount, DeleteAccount, SetUsername, AssignRoles, UnassignRoles, SetPassword, LinkAccount, UnlinkAccount, UpdatePhoneId, VerifyPhoneNumber, CreateCustomObject, UpdateCustomobject, DeleteCustomObject
            is_custom: true/false
		
        Returns:
            Response containing consent profile
        43.4
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(event)):
            raise Exception(self._lr_object.get_validation_message("event"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["event"] = event
        query_parameters["isCustom"] = is_custom

        resource_path = "identity/v2/auth/consent/verify"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def update_consent_profile_by_access_token(self, access_token, consent_update_model):
        """This API is to update consents using access token.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            consent_update_model: Model class containg list of multiple consent
		
        Returns:
            Response containing consent profile
        43.5
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))
        if(consent_update_model is None):
            raise Exception(self._lr_object.get_validation_message("consent_update_model"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/consent"
        return self._lr_object.execute("PUT", resource_path, query_parameters, consent_update_model)

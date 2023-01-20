# -- coding: utf-8 --
# Created by LoginRadius Development Team
# Copyright 2019 LoginRadius Inc. All rights reserved.
#


class SocialApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    def exchange_access_token(self, token):
        """This API Is used to translate the Request Token returned during authentication into an Access Token that can be used with other API calls.
        
        Args:
            token: Token generated from a successful oauth from social platform
		
        Returns:
            Response containing Definition of Complete Token data
        20.1
        """

        if(self._lr_object.is_null_or_whitespace(token)):
            raise Exception(self._lr_object.get_validation_message("token"))

        query_parameters = {}
        query_parameters["secret"] = self._lr_object.get_api_secret()
        query_parameters["token"] = token

        resource_path = "api/v2/access_token"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def refresh_access_token(self, access_token, expires_in=0, is_web=False):
        """The Refresh Access Token API is used to refresh the provider access token after authentication. It will be valid for up to 60 days on LoginRadius depending on the provider. In order to use the access token in other APIs, always refresh the token using this API.<br><br><b>Supported Providers :</b> Facebook,Yahoo,Google,Twitter, Linkedin.<br><br> Contact LoginRadius support team to enable this API.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            expires_in: Allows you to specify a desired expiration time in minutes for the newly issued access token.
            is_web: Is web or not.
		
        Returns:
            Response containing Definition of Complete Token data
        20.2
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["secret"] = self._lr_object.get_api_secret()
        if(expires_in is not None):
            query_parameters["expiresIn"] = expires_in
        if(is_web is not None):
            query_parameters["isWeb"] = is_web

        resource_path = "api/v2/access_token/refresh"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def validate_access_token(self, access_token):
        """This API validates access token, if valid then returns a response with its expiry otherwise error.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
		
        Returns:
            Response containing Definition of Complete Token data
        20.9
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["key"] = self._lr_object.get_api_key()
        query_parameters["secret"] = self._lr_object.get_api_secret()

        resource_path = "api/v2/access_token/validate"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def in_validate_access_token(self, access_token):
        """This api invalidates the active access token or expires an access token validity.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
		
        Returns:
            Response containing Definition for Complete Validation data
        20.10
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["key"] = self._lr_object.get_api_key()
        query_parameters["secret"] = self._lr_object.get_api_secret()

        resource_path = "api/v2/access_token/invalidate"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_active_session(self, token):
        """This api is use to get all active session by Access Token.
        
        Args:
            token: Token generated from a successful oauth from social platform
		
        Returns:
            Response containing Definition for Complete active sessions
        20.11.1
        """

        if(self._lr_object.is_null_or_whitespace(token)):
            raise Exception(self._lr_object.get_validation_message("token"))

        query_parameters = {}
        query_parameters["key"] = self._lr_object.get_api_key()
        query_parameters["secret"] = self._lr_object.get_api_secret()
        query_parameters["token"] = token

        resource_path = "api/v2/access_token/activesession"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_active_session_by_account_id(self, account_id):
        """This api is used to get all active sessions by AccountID(UID).
        
        Args:
            account_id: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition for Complete active sessions
        20.11.2
        """

        if(self._lr_object.is_null_or_whitespace(account_id)):
            raise Exception(self._lr_object.get_validation_message("account_id"))

        query_parameters = {}
        query_parameters["accountId"] = account_id
        query_parameters["key"] = self._lr_object.get_api_key()
        query_parameters["secret"] = self._lr_object.get_api_secret()

        resource_path = "api/v2/access_token/activesession"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_active_session_by_profile_id(self, profile_id):
        """This api is used to get all active sessions by ProfileId.
        
        Args:
            profile_id: Social Provider Id
		
        Returns:
            Response containing Definition for Complete active sessions
        20.11.3
        """

        if(self._lr_object.is_null_or_whitespace(profile_id)):
            raise Exception(self._lr_object.get_validation_message("profile_id"))

        query_parameters = {}
        query_parameters["key"] = self._lr_object.get_api_key()
        query_parameters["profileId"] = profile_id
        query_parameters["secret"] = self._lr_object.get_api_secret()

        resource_path = "api/v2/access_token/activesession"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

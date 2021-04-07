# -- coding: utf-8 --
# Created by LoginRadius Development Team
# Copyright 2019 LoginRadius Inc. All rights reserved.
#


class SmartLoginApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    def smart_login_token_verification(self, verification_token, welcome_email_template=None):
        """This API verifies the provided token for Smart Login
        
        Args:
            verification_token: Verification token received in the email
            welcome_email_template: Name of the welcome email template
		
        Returns:
            Complete verified response data
        8.4.1
        """

        if(self._lr_object.is_null_or_whitespace(verification_token)):
            raise Exception(self._lr_object.get_validation_message("verification_token"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["verificationToken"] = verification_token
        if(not self._lr_object.is_null_or_whitespace(welcome_email_template)):
            query_parameters["welcomeEmailTemplate"] = welcome_email_template

        resource_path = "identity/v2/auth/email/smartlogin"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def smart_login_by_email(self, client_guid, email, redirect_url=None,
        smart_login_email_template=None, welcome_email_template=None):
        """This API sends a Smart Login link to the user's Email Id.
        
        Args:
            client_guid: Unique string used in the Smart Login request
            email: Email of the user
            redirect_url: Url where the user will redirect after success authentication
            smart_login_email_template: Email template for Smart Login link
            welcome_email_template: Name of the welcome email template
		
        Returns:
            Response containing Definition of Complete Validation data
        9.17.1
        """

        if(self._lr_object.is_null_or_whitespace(client_guid)):
            raise Exception(self._lr_object.get_validation_message("client_guid"))

        if(self._lr_object.is_null_or_whitespace(email)):
            raise Exception(self._lr_object.get_validation_message("email"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["clientGuid"] = client_guid
        query_parameters["email"] = email
        if(not self._lr_object.is_null_or_whitespace(redirect_url)):
            query_parameters["redirectUrl"] = redirect_url
        if(not self._lr_object.is_null_or_whitespace(smart_login_email_template)):
            query_parameters["smartLoginEmailTemplate"] = smart_login_email_template
        if(not self._lr_object.is_null_or_whitespace(welcome_email_template)):
            query_parameters["welcomeEmailTemplate"] = welcome_email_template

        resource_path = "identity/v2/auth/login/smartlogin"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def smart_login_by_user_name(self, client_guid, username, redirect_url=None,
        smart_login_email_template=None, welcome_email_template=None):
        """This API sends a Smart Login link to the user's Email Id.
        
        Args:
            client_guid: Unique string used in the Smart Login request
            username: UserName of the user
            redirect_url: Url where the user will redirect after success authentication
            smart_login_email_template: Email template for Smart Login link
            welcome_email_template: Name of the welcome email template
		
        Returns:
            Response containing Definition of Complete Validation data
        9.17.2
        """

        if(self._lr_object.is_null_or_whitespace(client_guid)):
            raise Exception(self._lr_object.get_validation_message("client_guid"))

        if(self._lr_object.is_null_or_whitespace(username)):
            raise Exception(self._lr_object.get_validation_message("username"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["clientGuid"] = client_guid
        query_parameters["username"] = username
        if(not self._lr_object.is_null_or_whitespace(redirect_url)):
            query_parameters["redirectUrl"] = redirect_url
        if(not self._lr_object.is_null_or_whitespace(smart_login_email_template)):
            query_parameters["smartLoginEmailTemplate"] = smart_login_email_template
        if(not self._lr_object.is_null_or_whitespace(welcome_email_template)):
            query_parameters["welcomeEmailTemplate"] = welcome_email_template

        resource_path = "identity/v2/auth/login/smartlogin"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def smart_login_ping(self, client_guid, fields=''):
        """This API is used to check if the Smart Login link has been clicked or not
        
        Args:
            client_guid: Unique string used in the Smart Login request
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
		
        Returns:
            Response containing User Profile Data and access token
        9.21.1
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

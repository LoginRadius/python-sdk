# -- coding: utf-8 --
# Created by LoginRadius Development Team
# Copyright 2019 LoginRadius Inc. All rights reserved.
#


class AuthenticationApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    def get_security_questions_by_email(self, email):
        """This API is used to retrieve the list of questions that are configured on the respective LoginRadius site.
        
        Args:
            email: Email of the user
		
        Returns:
            Response containing Definition for Complete SecurityQuestions data
        2.1
        """

        if(self._lr_object.is_null_or_whitespace(email)):
            raise Exception(self._lr_object.get_validation_message("email"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["email"] = email

        resource_path = "identity/v2/auth/securityquestion/email"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_security_questions_by_user_name(self, user_name):
        """This API is used to retrieve the list of questions that are configured on the respective LoginRadius site.
        
        Args:
            user_name: UserName of the user
		
        Returns:
            Response containing Definition for Complete SecurityQuestions data
        2.2
        """

        if(self._lr_object.is_null_or_whitespace(user_name)):
            raise Exception(self._lr_object.get_validation_message("user_name"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["userName"] = user_name

        resource_path = "identity/v2/auth/securityquestion/username"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_security_questions_by_phone(self, phone):
        """This API is used to retrieve the list of questions that are configured on the respective LoginRadius site.
        
        Args:
            phone: The Registered Phone Number
		
        Returns:
            Response containing Definition for Complete SecurityQuestions data
        2.3
        """

        if(self._lr_object.is_null_or_whitespace(phone)):
            raise Exception(self._lr_object.get_validation_message("phone"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["phone"] = phone

        resource_path = "identity/v2/auth/securityquestion/phone"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_security_questions_by_access_token(self, access_token):
        """This API is used to retrieve the list of questions that are configured on the respective LoginRadius site.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
		
        Returns:
            Response containing Definition for Complete SecurityQuestions data
        2.4
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/securityquestion/accesstoken"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def auth_validate_access_token(self, access_token):
        """This api validates access token, if valid then returns a response with its expiry otherwise error.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
		
        Returns:
            Response containing Definition of Complete Token data
        4.1
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/access_token/validate"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def auth_in_validate_access_token(self, access_token, prevent_refresh=False):
        """This api call invalidates the active access token or expires an access token's validity.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            prevent_refresh: Boolean value that when set as true, in addition of the access token being invalidated, it will no longer have the capability of being refreshed.
		
        Returns:
            Response containing Definition of Complete Validation data
        4.2
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(prevent_refresh is not None):
            query_parameters["preventRefresh"] = prevent_refresh

        resource_path = "identity/v2/auth/access_token/invalidate"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_access_token_info(self, access_token):
        """This api call provide the active access token Information
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
		
        Returns:
            Response containing Definition of Token Information
        4.3
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/access_token"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_profile_by_access_token(self, access_token, fields='', email_template=None,
        verification_url=None, welcome_email_template=None):
        """This API retrieves a copy of the user data based on the access token.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            email_template: 
            verification_url: 
            welcome_email_template: 
		
        Returns:
            Response containing Definition for Complete profile data
        5.2
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(email_template)):
            query_parameters["emailTemplate"] = email_template
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(not self._lr_object.is_null_or_whitespace(verification_url)):
            query_parameters["verificationUrl"] = verification_url
        if(not self._lr_object.is_null_or_whitespace(welcome_email_template)):
            query_parameters["welcomeEmailTemplate"] = welcome_email_template

        resource_path = "identity/v2/auth/account"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def send_welcome_email(self, access_token, welcome_email_template=None):
        """This API sends a welcome email
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            welcome_email_template: Name of the welcome email template
		
        Returns:
            Response containing Definition of Complete Validation data
        5.3
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(welcome_email_template)):
            query_parameters["welcomeEmailTemplate"] = welcome_email_template

        resource_path = "identity/v2/auth/account/sendwelcomeemail"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def update_profile_by_access_token(self, access_token, user_profile_update_model, email_template=None,
        fields='', null_support=None, sms_template=None, verification_url=None):
        """This API is used to update the user's profile by passing the access token.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            user_profile_update_model: Model Class containing Definition of payload for User Profile update API
            email_template: Email template name
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            null_support: Boolean, pass true if you wish to update any user profile field with a NULL value, You can get the details
            sms_template: SMS Template name
            verification_url: Email verification url
		
        Returns:
            Response containing Definition of Complete Validation and UserProfile data
        5.4
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))
        if(user_profile_update_model is None):
            raise Exception(self._lr_object.get_validation_message("user_profile_update_model"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(email_template)):
            query_parameters["emailTemplate"] = email_template
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(null_support is not None):
            query_parameters["nullSupport"] = null_support
        if(not self._lr_object.is_null_or_whitespace(sms_template)):
            query_parameters["smsTemplate"] = sms_template
        if(not self._lr_object.is_null_or_whitespace(verification_url)):
            query_parameters["verificationUrl"] = verification_url

        resource_path = "identity/v2/auth/account"
        return self._lr_object.execute("PUT", resource_path, query_parameters, user_profile_update_model)

    def delete_account_with_email_confirmation(self, access_token, delete_url=None, email_template=None):
        """This API will send a confirmation email for account deletion to the customer's email when passed the customer's access token
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            delete_url: Url of the site
            email_template: Email template name
		
        Returns:
            Response containing Definition of Delete Request
        5.5
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(delete_url)):
            query_parameters["deleteUrl"] = delete_url
        if(not self._lr_object.is_null_or_whitespace(email_template)):
            query_parameters["emailTemplate"] = email_template

        resource_path = "identity/v2/auth/account"
        return self._lr_object.execute("DELETE", resource_path, query_parameters, {})

    def delete_account_by_delete_token(self, deletetoken):
        """This API is used to delete an account by passing it a delete token.
        
        Args:
            deletetoken: Delete token received in the email
		
        Returns:
            Response containing Definition of Complete Validation data
        5.6
        """

        if(self._lr_object.is_null_or_whitespace(deletetoken)):
            raise Exception(self._lr_object.get_validation_message("deletetoken"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["deletetoken"] = deletetoken

        resource_path = "identity/v2/auth/account/delete"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def unlock_account_by_token(self, access_token, unlock_profile_model):
        """This API is used to allow a customer with a valid access token to unlock their account provided that they successfully pass the prompted Bot Protection challenges. The Block or Suspend block types are not applicable for this API. For additional details see our Auth Security Configuration documentation.You are only required to pass the Post Parameters that correspond to the prompted challenges.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            unlock_profile_model: Payload containing Unlock Profile API
		
        Returns:
            Response containing Definition of Complete Validation data
        5.15
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))
        if(unlock_profile_model is None):
            raise Exception(self._lr_object.get_validation_message("unlock_profile_model"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/account/unlock"
        return self._lr_object.execute("PUT", resource_path, query_parameters, unlock_profile_model)

    def get_profile_by_ping(self, client_guid, email_template=None, fields='',
        verification_url=None, welcome_email_template=None):
        """This API is used to get a user's profile using the clientGuid parameter if no callback feature enabled
        
        Args:
            client_guid: ClientGuid
            email_template: EmailTemplate
            fields: Fields
            verification_url: VerificationUrl
            welcome_email_template: WelcomeEmailTemplate
		
        Returns:
            Response containing User Profile Data and access token
        5.16
        """

        if(self._lr_object.is_null_or_whitespace(client_guid)):
            raise Exception(self._lr_object.get_validation_message("client_guid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["clientGuid"] = client_guid
        if(not self._lr_object.is_null_or_whitespace(email_template)):
            query_parameters["emailTemplate"] = email_template
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(not self._lr_object.is_null_or_whitespace(verification_url)):
            query_parameters["verificationUrl"] = verification_url
        if(not self._lr_object.is_null_or_whitespace(welcome_email_template)):
            query_parameters["welcomeEmailTemplate"] = welcome_email_template

        resource_path = "identity/v2/auth/account/ping"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def check_email_availability(self, email):
        """This API is used to check the email exists or not on your site.
        
        Args:
            email: Email of the user
		
        Returns:
            Response containing Definition Complete ExistResponse data
        8.1
        """

        if(self._lr_object.is_null_or_whitespace(email)):
            raise Exception(self._lr_object.get_validation_message("email"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["email"] = email

        resource_path = "identity/v2/auth/email"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def verify_email(self, verification_token, fields='', url=None,
        welcome_email_template=None):
        """This API is used to verify the email of user. Note: This API will only return the full profile if you have 'Enable auto login after email verification' set in your LoginRadius Admin Console's Email Workflow settings under 'Verification Email'.
        
        Args:
            verification_token: Verification token received in the email
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            url: Mention URL to log the main URL(Domain name) in Database.
            welcome_email_template: Name of the welcome email template
		
        Returns:
            Response containing Definition of Complete Validation, UserProfile data and Access Token
        8.2
        """

        if(self._lr_object.is_null_or_whitespace(verification_token)):
            raise Exception(self._lr_object.get_validation_message("verification_token"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["verificationToken"] = verification_token
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(not self._lr_object.is_null_or_whitespace(url)):
            query_parameters["url"] = url
        if(not self._lr_object.is_null_or_whitespace(welcome_email_template)):
            query_parameters["welcomeEmailTemplate"] = welcome_email_template

        resource_path = "identity/v2/auth/email"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def verify_email_by_otp(self, email_verification_by_otp_model, fields='', url=None,
        welcome_email_template=None):
        """This API is used to verify the email of user when the OTP Email verification flow is enabled, please note that you must contact LoginRadius to have this feature enabled.
        
        Args:
            email_verification_by_otp_model: Model Class containing Definition for EmailVerificationByOtpModel API
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            url: Mention URL to log the main URL(Domain name) in Database.
            welcome_email_template: Name of the welcome email template
		
        Returns:
            Response containing Definition of Complete Validation, UserProfile data and Access Token
        8.3
        """
        if(email_verification_by_otp_model is None):
            raise Exception(self._lr_object.get_validation_message("email_verification_by_otp_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(not self._lr_object.is_null_or_whitespace(url)):
            query_parameters["url"] = url
        if(not self._lr_object.is_null_or_whitespace(welcome_email_template)):
            query_parameters["welcomeEmailTemplate"] = welcome_email_template

        resource_path = "identity/v2/auth/email"
        return self._lr_object.execute("PUT", resource_path, query_parameters, email_verification_by_otp_model)

    def add_email(self, access_token, email, type,
        email_template=None, verification_url=None):
        """This API is used to add additional emails to a user's account.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            email: user's email
            type: String to identify the type of parameter
            email_template: Email template name
            verification_url: Email verification url
		
        Returns:
            Response containing Definition of Complete Validation data
        8.5
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(email)):
            raise Exception(self._lr_object.get_validation_message("email"))

        if(self._lr_object.is_null_or_whitespace(type)):
            raise Exception(self._lr_object.get_validation_message("type"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(email_template)):
            query_parameters["emailTemplate"] = email_template
        if(not self._lr_object.is_null_or_whitespace(verification_url)):
            query_parameters["verificationUrl"] = verification_url

        body_parameters = {}
        body_parameters["email"] = email
        body_parameters["type"] = type

        resource_path = "identity/v2/auth/email"
        return self._lr_object.execute("POST", resource_path, query_parameters, body_parameters)

    def remove_email(self, access_token, email):
        """This API is used to remove additional emails from a user's account.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            email: user's email
		
        Returns:
            Response containing Definition of Delete Request
        8.6
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(email)):
            raise Exception(self._lr_object.get_validation_message("email"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        body_parameters = {}
        body_parameters["email"] = email

        resource_path = "identity/v2/auth/email"
        return self._lr_object.execute("DELETE", resource_path, query_parameters, body_parameters)

    def login_by_email(self, email_authentication_model, email_template=None, fields='',
        login_url=None, verification_url=None):
        """This API retrieves a copy of the user data based on the Email
        
        Args:
            email_authentication_model: Model Class containing Definition of payload for Email Authentication API
            email_template: Email template name
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            login_url: Url where the user is logging from
            verification_url: Email verification url
		
        Returns:
            Response containing User Profile Data and access token
        9.2.1
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
        if(not self._lr_object.is_null_or_whitespace(verification_url)):
            query_parameters["verificationUrl"] = verification_url

        resource_path = "identity/v2/auth/login"
        return self._lr_object.execute("POST", resource_path, query_parameters, email_authentication_model)

    def login_by_user_name(self, user_name_authentication_model, email_template=None, fields='',
        login_url=None, verification_url=None):
        """This API retrieves a copy of the user data based on the Username
        
        Args:
            user_name_authentication_model: Model Class containing Definition of payload for Username Authentication API
            email_template: Email template name
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            login_url: Url where the user is logging from
            verification_url: Email verification url
		
        Returns:
            Response containing User Profile Data and access token
        9.2.2
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
        if(not self._lr_object.is_null_or_whitespace(verification_url)):
            query_parameters["verificationUrl"] = verification_url

        resource_path = "identity/v2/auth/login"
        return self._lr_object.execute("POST", resource_path, query_parameters, user_name_authentication_model)

    def forgot_password(self, email, reset_password_url, email_template=None):
        """This API is used to send the reset password url to a specified account. Note: If you have the UserName workflow enabled, you may replace the 'email' parameter with 'username'
        
        Args:
            email: user's email
            reset_password_url: Url to which user should get re-directed to for resetting the password
            email_template: Email template name
		
        Returns:
            Response containing Definition of Complete Validation data
        10.1
        """

        if(self._lr_object.is_null_or_whitespace(email)):
            raise Exception(self._lr_object.get_validation_message("email"))

        if(self._lr_object.is_null_or_whitespace(reset_password_url)):
            raise Exception(self._lr_object.get_validation_message("reset_password_url"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["resetPasswordUrl"] = reset_password_url
        if(not self._lr_object.is_null_or_whitespace(email_template)):
            query_parameters["emailTemplate"] = email_template

        body_parameters = {}
        body_parameters["email"] = email

        resource_path = "identity/v2/auth/password"
        return self._lr_object.execute("POST", resource_path, query_parameters, body_parameters)

    def reset_password_by_security_answer_and_email(self, reset_password_by_security_answer_and_email_model):
        """This API is used to reset password for the specified account by security question
        
        Args:
            reset_password_by_security_answer_and_email_model: Model Class containing Definition of payload for ResetPasswordBySecurityAnswerAndEmail API
		
        Returns:
            Response containing Definition of Validation data and access token
        10.3.1
        """
        if(reset_password_by_security_answer_and_email_model is None):
            raise Exception(self._lr_object.get_validation_message("reset_password_by_security_answer_and_email_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/password/securityanswer"
        return self._lr_object.execute("PUT", resource_path, query_parameters, reset_password_by_security_answer_and_email_model)

    def reset_password_by_security_answer_and_phone(self, reset_password_by_security_answer_and_phone_model):
        """This API is used to reset password for the specified account by security question
        
        Args:
            reset_password_by_security_answer_and_phone_model: Model Class containing Definition of payload for ResetPasswordBySecurityAnswerAndPhone API
		
        Returns:
            Response containing Definition of Validation data and access token
        10.3.2
        """
        if(reset_password_by_security_answer_and_phone_model is None):
            raise Exception(self._lr_object.get_validation_message("reset_password_by_security_answer_and_phone_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/password/securityanswer"
        return self._lr_object.execute("PUT", resource_path, query_parameters, reset_password_by_security_answer_and_phone_model)

    def reset_password_by_security_answer_and_user_name(self, reset_password_by_security_answer_and_user_name_model):
        """This API is used to reset password for the specified account by security question
        
        Args:
            reset_password_by_security_answer_and_user_name_model: Model Class containing Definition of payload for ResetPasswordBySecurityAnswerAndUserName API
		
        Returns:
            Response containing Definition of Validation data and access token
        10.3.3
        """
        if(reset_password_by_security_answer_and_user_name_model is None):
            raise Exception(self._lr_object.get_validation_message("reset_password_by_security_answer_and_user_name_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/password/securityanswer"
        return self._lr_object.execute("PUT", resource_path, query_parameters, reset_password_by_security_answer_and_user_name_model)

    def reset_password_by_reset_token(self, reset_password_by_reset_token_model):
        """This API is used to set a new password for the specified account.
        
        Args:
            reset_password_by_reset_token_model: Model Class containing Definition of payload for ResetToken API
		
        Returns:
            Response containing Definition of Validation data and access token
        10.7.1
        """
        if(reset_password_by_reset_token_model is None):
            raise Exception(self._lr_object.get_validation_message("reset_password_by_reset_token_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/password/reset"
        return self._lr_object.execute("PUT", resource_path, query_parameters, reset_password_by_reset_token_model)

    def reset_password_by_email_otp(self, reset_password_by_email_and_otp_model):
        """This API is used to set a new password for the specified account.
        
        Args:
            reset_password_by_email_and_otp_model: Model Class containing Definition of payload for ResetPasswordByEmailAndOtp API
		
        Returns:
            Response containing Definition of Validation data and access token
        10.7.2
        """
        if(reset_password_by_email_and_otp_model is None):
            raise Exception(self._lr_object.get_validation_message("reset_password_by_email_and_otp_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/password/reset"
        return self._lr_object.execute("PUT", resource_path, query_parameters, reset_password_by_email_and_otp_model)

    def reset_password_by_otp_and_user_name(self, reset_password_by_user_name_model):
        """This API is used to set a new password for the specified account if you are using the username as the unique identifier in your workflow
        
        Args:
            reset_password_by_user_name_model: Model Class containing Definition of payload for ResetPasswordByUserName API
		
        Returns:
            Response containing Definition of Validation data and access token
        10.7.3
        """
        if(reset_password_by_user_name_model is None):
            raise Exception(self._lr_object.get_validation_message("reset_password_by_user_name_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/password/reset"
        return self._lr_object.execute("PUT", resource_path, query_parameters, reset_password_by_user_name_model)

    def change_password(self, access_token, new_password, old_password):
        """This API is used to change the accounts password based on the previous password
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            new_password: New password
            old_password: User's current password
		
        Returns:
            Response containing Definition of Complete Validation data
        10.8
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(new_password)):
            raise Exception(self._lr_object.get_validation_message("new_password"))

        if(self._lr_object.is_null_or_whitespace(old_password)):
            raise Exception(self._lr_object.get_validation_message("old_password"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        body_parameters = {}
        body_parameters["newPassword"] = new_password
        body_parameters["oldPassword"] = old_password

        resource_path = "identity/v2/auth/password/change"
        return self._lr_object.execute("PUT", resource_path, query_parameters, body_parameters)

    def unlink_social_identities(self, access_token, provider, provider_id):
        """This API is used to unlink up a social provider account with the specified account based on the access token and the social providers user access token. The unlinked account will automatically get removed from your database.
        
        Args:
            access_token: Access_Token
            provider: Name of the provider
            provider_id: Unique ID of the linked account
		
        Returns:
            Response containing Definition of Delete Request
        12.2
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(provider)):
            raise Exception(self._lr_object.get_validation_message("provider"))

        if(self._lr_object.is_null_or_whitespace(provider_id)):
            raise Exception(self._lr_object.get_validation_message("provider_id"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        body_parameters = {}
        body_parameters["provider"] = provider
        body_parameters["providerId"] = provider_id

        resource_path = "identity/v2/auth/socialidentity"
        return self._lr_object.execute("DELETE", resource_path, query_parameters, body_parameters)

    def link_social_identities(self, access_token, candidate_token):
        """This API is used to link up a social provider account with an existing LoginRadius account on the basis of access token and the social providers user access token.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            candidate_token: Access token of the account to be linked
		
        Returns:
            Response containing Definition of Complete Validation data
        12.4
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(candidate_token)):
            raise Exception(self._lr_object.get_validation_message("candidate_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        body_parameters = {}
        body_parameters["candidateToken"] = candidate_token

        resource_path = "identity/v2/auth/socialidentity"
        return self._lr_object.execute("POST", resource_path, query_parameters, body_parameters)

    def link_social_identities_by_ping(self, access_token, client_guid):
        """This API is used to link up a social provider account with an existing LoginRadius account on the basis of ping and the social providers user access token.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            client_guid: Unique ID generated by client
		
        Returns:
            Response containing Definition of Complete Validation data
        12.5
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(client_guid)):
            raise Exception(self._lr_object.get_validation_message("client_guid"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        body_parameters = {}
        body_parameters["clientGuid"] = client_guid

        resource_path = "identity/v2/auth/socialidentity"
        return self._lr_object.execute("POST", resource_path, query_parameters, body_parameters)

    def set_or_change_user_name(self, access_token, username):
        """This API is used to set or change UserName by access token.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            username: Username of the user
		
        Returns:
            Response containing Definition of Complete Validation data
        13.1
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(username)):
            raise Exception(self._lr_object.get_validation_message("username"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        body_parameters = {}
        body_parameters["username"] = username

        resource_path = "identity/v2/auth/username"
        return self._lr_object.execute("PUT", resource_path, query_parameters, body_parameters)

    def check_user_name_availability(self, username):
        """This API is used to check the UserName exists or not on your site.
        
        Args:
            username: UserName of the user
		
        Returns:
            Response containing Definition Complete ExistResponse data
        13.2
        """

        if(self._lr_object.is_null_or_whitespace(username)):
            raise Exception(self._lr_object.get_validation_message("username"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["username"] = username

        resource_path = "identity/v2/auth/username"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def accept_privacy_policy(self, access_token, fields=''):
        """This API is used to update the privacy policy stored in the user's profile by providing the access token of the user accepting the privacy policy
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
		
        Returns:
            Response containing Definition for Complete profile data
        15.1
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields

        resource_path = "identity/v2/auth/privacypolicy/accept"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_privacy_policy_history_by_access_token(self, access_token):
        """This API will return all the accepted privacy policies for the user by providing the access token of that user.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
		
        Returns:
            Complete Policy History data
        15.2
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/privacypolicy/history"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def user_registration_by_email(self, auth_user_registration_model, sott, email_template=None,
        fields='', options='', verification_url=None, welcome_email_template=None):
        """This API creates a user in the database as well as sends a verification email to the user.
        
        Args:
            auth_user_registration_model: Model Class containing Definition of payload for Auth User Registration API
            sott: LoginRadius Secured One Time Token
            email_template: Email template name
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            options: PreventVerificationEmail (Specifying this value prevents the verification email from being sent. Only applicable if you have the optional email verification flow)
            verification_url: Email verification url
            welcome_email_template: Name of the welcome email template
		
        Returns:
            Response containing Definition of Complete Validation, UserProfile data and Access Token
        17.1.1
        """
        if(auth_user_registration_model is None):
            raise Exception(self._lr_object.get_validation_message("auth_user_registration_model"))

        if(self._lr_object.is_null_or_whitespace(sott)):
            raise Exception(self._lr_object.get_validation_message("sott"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["sott"] = sott
        if(not self._lr_object.is_null_or_whitespace(email_template)):
            query_parameters["emailTemplate"] = email_template
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(not self._lr_object.is_null_or_whitespace(options)):
            query_parameters["options"] = options
        if(not self._lr_object.is_null_or_whitespace(verification_url)):
            query_parameters["verificationUrl"] = verification_url
        if(not self._lr_object.is_null_or_whitespace(welcome_email_template)):
            query_parameters["welcomeEmailTemplate"] = welcome_email_template

        resource_path = "identity/v2/auth/register"
        return self._lr_object.execute("POST", resource_path, query_parameters, auth_user_registration_model)

    def user_registration_by_captcha(self, auth_user_registration_model_with_captcha, email_template=None, fields='',
        options='', sms_template=None, verification_url=None, welcome_email_template=None):
        """This API creates a user in the database as well as sends a verification email to the user.
        
        Args:
            auth_user_registration_model_with_captcha: Model Class containing Definition of payload for Auth User Registration by Recaptcha API
            email_template: Email template name
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            options: PreventVerificationEmail (Specifying this value prevents the verification email from being sent. Only applicable if you have the optional email verification flow)
            sms_template: SMS Template name
            verification_url: Email verification url
            welcome_email_template: Name of the welcome email template
		
        Returns:
            Response containing Definition of Complete Validation, UserProfile data and Access Token
        17.2
        """
        if(auth_user_registration_model_with_captcha is None):
            raise Exception(self._lr_object.get_validation_message("auth_user_registration_model_with_captcha"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(email_template)):
            query_parameters["emailTemplate"] = email_template
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

        resource_path = "identity/v2/auth/register/captcha"
        return self._lr_object.execute("POST", resource_path, query_parameters, auth_user_registration_model_with_captcha)

    def auth_resend_email_verification(self, email, email_template=None, verification_url=None):
        """This API resends the verification email to the user.
        
        Args:
            email: user's email
            email_template: Email template name
            verification_url: Email verification url
		
        Returns:
            Response containing Definition of Complete Validation data
        17.3
        """

        if(self._lr_object.is_null_or_whitespace(email)):
            raise Exception(self._lr_object.get_validation_message("email"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(email_template)):
            query_parameters["emailTemplate"] = email_template
        if(not self._lr_object.is_null_or_whitespace(verification_url)):
            query_parameters["verificationUrl"] = verification_url

        body_parameters = {}
        body_parameters["email"] = email

        resource_path = "identity/v2/auth/register"
        return self._lr_object.execute("PUT", resource_path, query_parameters, body_parameters)

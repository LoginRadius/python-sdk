# -- coding: utf-8 --
# Created by LoginRadius Development Team
# Copyright 2019 LoginRadius Inc. All rights reserved.
#


class AccountApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    def get_privacy_policy_history_by_uid(self, uid):
        """This API is used to retrieve all of the accepted Policies by the user, associated with their UID.
        
        Args:
            uid: UID, the unified identifier for each user account
		
        Returns:
            Complete Policy History data
        15.1.1
        """

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/account/" + uid + "/privacypolicy/history"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def create_account(self, account_create_model, fields=''):
        """This API is used to create an account in Cloud Storage. This API bypass the normal email verification process and manually creates the user. <br><br>In order to use this API, you need to format a JSON request body with all of the mandatory fields
        
        Args:
            account_create_model: Model Class containing Definition of payload for Account Create API
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
		
        Returns:
            Response containing Definition for Complete profile data
        18.1
        """
        if(account_create_model is None):
            raise Exception(self._lr_object.get_validation_message("account_create_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields

        resource_path = "identity/v2/manage/account"
        return self._lr_object.execute("POST", resource_path, query_parameters, account_create_model)

    def get_account_profile_by_email(self, email, fields=''):
        """This API is used to retrieve all of the profile data, associated with the specified account by email in Cloud Storage.
        
        Args:
            email: Email of the user
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
		
        Returns:
            Response containing Definition for Complete profile data
        18.2
        """

        if(self._lr_object.is_null_or_whitespace(email)):
            raise Exception(self._lr_object.get_validation_message("email"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        query_parameters["email"] = email
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields

        resource_path = "identity/v2/manage/account"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_account_profile_by_user_name(self, user_name, fields=''):
        """This API is used to retrieve all of the profile data associated with the specified account by user name in Cloud Storage.
        
        Args:
            user_name: UserName of the user
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
		
        Returns:
            Response containing Definition for Complete profile data
        18.3
        """

        if(self._lr_object.is_null_or_whitespace(user_name)):
            raise Exception(self._lr_object.get_validation_message("user_name"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        query_parameters["userName"] = user_name
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields

        resource_path = "identity/v2/manage/account"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_account_profile_by_phone(self, phone, fields=''):
        """This API is used to retrieve all of the profile data, associated with the account by phone number in Cloud Storage.
        
        Args:
            phone: The Registered Phone Number
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
		
        Returns:
            Response containing Definition for Complete profile data
        18.4
        """

        if(self._lr_object.is_null_or_whitespace(phone)):
            raise Exception(self._lr_object.get_validation_message("phone"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        query_parameters["phone"] = phone
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields

        resource_path = "identity/v2/manage/account"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_account_profile_by_uid(self, uid, fields=''):
        """This API is used to retrieve all of the profile data, associated with the account by uid in Cloud Storage.
        
        Args:
            uid: UID, the unified identifier for each user account
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
		
        Returns:
            Response containing Definition for Complete profile data
        18.5
        """

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields

        resource_path = "identity/v2/manage/account/" + uid
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def update_account_by_uid(self, account_user_profile_update_model, uid, fields='',
        null_support=None):
        """This API is used to update the information of existing accounts in your Cloud Storage. See our Advanced API Usage section <a href='https://www.loginradius.com/docs/api/v2/customer-identity-api/advanced-api-usage/'>Here</a> for more capabilities.
        
        Args:
            account_user_profile_update_model: Model Class containing Definition of payload for Account Update API
            uid: UID, the unified identifier for each user account
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
            null_support: Boolean, pass true if you wish to update any user profile field with a NULL value, You can get the details
		
        Returns:
            Response containing Definition for Complete profile data
        18.15
        """
        if(account_user_profile_update_model is None):
            raise Exception(self._lr_object.get_validation_message("account_user_profile_update_model"))

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields
        if(null_support is not None):
            query_parameters["nullSupport"] = null_support

        resource_path = "identity/v2/manage/account/" + uid
        return self._lr_object.execute("PUT", resource_path, query_parameters, account_user_profile_update_model)

    def update_phone_id_by_uid(self, phone, uid, fields=''):
        """This API is used to update the PhoneId by using the Uid's. Admin can update the PhoneId's for both the verified and unverified profiles. It will directly replace the PhoneId and bypass the OTP verification process.
        
        Args:
            phone: Phone number
            uid: UID, the unified identifier for each user account
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
		
        Returns:
            Response containing Definition for Complete profile data
        18.16
        """

        if(self._lr_object.is_null_or_whitespace(phone)):
            raise Exception(self._lr_object.get_validation_message("phone"))

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields

        body_parameters = {}
        body_parameters["phone"] = phone

        resource_path = "identity/v2/manage/account/" + uid + "/phoneid"
        return self._lr_object.execute("PUT", resource_path, query_parameters, body_parameters)

    def get_account_password_hash_by_uid(self, uid):
        """This API use to retrive the hashed password of a specified account in Cloud Storage.
        
        Args:
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition for Complete PasswordHash data
        18.17
        """

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/account/" + uid + "/password"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def set_account_password_by_uid(self, password, uid):
        """This API is used to set the password of an account in Cloud Storage.
        
        Args:
            password: New password
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition for Complete PasswordHash data
        18.18
        """

        if(self._lr_object.is_null_or_whitespace(password)):
            raise Exception(self._lr_object.get_validation_message("password"))

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        body_parameters = {}
        body_parameters["password"] = password

        resource_path = "identity/v2/manage/account/" + uid + "/password"
        return self._lr_object.execute("PUT", resource_path, query_parameters, body_parameters)

    def delete_account_by_uid(self, uid):
        """This API deletes the Users account and allows them to re-register for a new account.
        
        Args:
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition of Delete Request
        18.19
        """

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/account/" + uid
        return self._lr_object.execute("DELETE", resource_path, query_parameters, {})

    def invalidate_account_email_verification(self, uid, email_template='', verification_url=''):
        """This API is used to invalidate the Email Verification status on an account.
        
        Args:
            uid: UID, the unified identifier for each user account
            email_template: Email template name
            verification_url: Email verification url
		
        Returns:
            Response containing Definition of Complete Validation data
        18.20
        """

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        if(not self._lr_object.is_null_or_whitespace(email_template)):
            query_parameters["emailTemplate"] = email_template
        if(not self._lr_object.is_null_or_whitespace(verification_url)):
            query_parameters["verificationUrl"] = verification_url

        resource_path = "identity/v2/manage/account/" + uid + "/invalidateemail"
        return self._lr_object.execute("PUT", resource_path, query_parameters, {})

    def get_forgot_password_token(self, email, email_template=None, reset_password_url=None,
        send_email=None):
        """This API Returns a Forgot Password Token it can also be used to send a Forgot Password email to the customer. Note: If you have the UserName workflow enabled, you may replace the 'email' parameter with 'username' in the body.
        
        Args:
            email: user's email
            email_template: Email template name
            reset_password_url: Url to which user should get re-directed to for resetting the password
            send_email: If set to true, the API will also send a Forgot Password email to the customer, bypassing any Bot Protection challenges that they are faced with.
		
        Returns:
            Response containing Definition of Complete Forgot Password data
        18.22
        """

        if(self._lr_object.is_null_or_whitespace(email)):
            raise Exception(self._lr_object.get_validation_message("email"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        if(not self._lr_object.is_null_or_whitespace(email_template)):
            query_parameters["emailTemplate"] = email_template
        if(not self._lr_object.is_null_or_whitespace(reset_password_url)):
            query_parameters["resetPasswordUrl"] = reset_password_url
        if(send_email is not None):
            query_parameters["sendEmail"] = send_email

        body_parameters = {}
        body_parameters["email"] = email

        resource_path = "identity/v2/manage/account/forgot/token"
        return self._lr_object.execute("POST", resource_path, query_parameters, body_parameters)

    def get_email_verification_token(self, email):
        """This API Returns an Email Verification token.
        
        Args:
            email: user's email
		
        Returns:
            Response containing Definition of Complete Verification data
        18.23
        """

        if(self._lr_object.is_null_or_whitespace(email)):
            raise Exception(self._lr_object.get_validation_message("email"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        body_parameters = {}
        body_parameters["email"] = email

        resource_path = "identity/v2/manage/account/verify/token"
        return self._lr_object.execute("POST", resource_path, query_parameters, body_parameters)

    def get_access_token_by_uid(self, uid):
        """The API is used to get LoginRadius access token based on UID.
        
        Args:
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition of Complete Token data
        18.24
        """

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        query_parameters["uid"] = uid

        resource_path = "identity/v2/manage/account/access_token"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def reset_phone_id_verification_by_uid(self, uid, sms_template=''):
        """This API Allows you to reset the phone no verification of an end user’s account.
        
        Args:
            uid: UID, the unified identifier for each user account
            sms_template: SMS Template name
		
        Returns:
            Response containing Definition of Complete Validation data
        18.27
        """

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        if(not self._lr_object.is_null_or_whitespace(sms_template)):
            query_parameters["smsTemplate"] = sms_template

        resource_path = "identity/v2/manage/account/" + uid + "/invalidatephone"
        return self._lr_object.execute("PUT", resource_path, query_parameters, {})

    def upsert_email(self, upsert_email_model, uid, fields=''):
        """This API is used to add/upsert another emails in account profile by different-different email types. If the email type is same then it will simply update the existing email, otherwise it will add a new email in Email array.
        
        Args:
            upsert_email_model: Model Class containing Definition of payload for UpsertEmail Property
            uid: UID, the unified identifier for each user account
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
		
        Returns:
            Response containing Definition for Complete profile data
        18.29
        """
        if(upsert_email_model is None):
            raise Exception(self._lr_object.get_validation_message("upsert_email_model"))

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields

        resource_path = "identity/v2/manage/account/" + uid + "/email"
        return self._lr_object.execute("PUT", resource_path, query_parameters, upsert_email_model)

    def remove_email(self, email, uid, fields=''):
        """Use this API to Remove emails from a user Account
        
        Args:
            email: user's email
            uid: UID, the unified identifier for each user account
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
		
        Returns:
            Response containing Definition for Complete profile data
        18.30
        """

        if(self._lr_object.is_null_or_whitespace(email)):
            raise Exception(self._lr_object.get_validation_message("email"))

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields

        body_parameters = {}
        body_parameters["email"] = email

        resource_path = "identity/v2/manage/account/" + uid + "/email"
        return self._lr_object.execute("DELETE", resource_path, query_parameters, body_parameters)

    def refresh_access_token_by_refresh_token(self, refresh__token):
        """This API is used to refresh an access token via it's associated refresh token.
        
        Args:
            refresh__token: LoginRadius refresh token
		
        Returns:
            Response containing Definition of Complete Token data
        18.31
        """

        if(self._lr_object.is_null_or_whitespace(refresh__token)):
            raise Exception(self._lr_object.get_validation_message("refresh__token"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        query_parameters["refresh_Token"] = refresh__token

        resource_path = "identity/v2/manage/account/access_token/refresh"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def revoke_refresh_token(self, refresh__token):
        """The Revoke Refresh Access Token API is used to revoke a refresh token or the Provider Access Token, revoking an existing refresh token will invalidate the refresh token but the associated access token will work until the expiry.
        
        Args:
            refresh__token: LoginRadius refresh token
		
        Returns:
            Response containing Definition of Delete Request
        18.32
        """

        if(self._lr_object.is_null_or_whitespace(refresh__token)):
            raise Exception(self._lr_object.get_validation_message("refresh__token"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        query_parameters["refresh_Token"] = refresh__token

        resource_path = "identity/v2/manage/account/access_token/refresh/revoke"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_account_identities_by_email(self, email, fields=''):
        """Note: This is intended for specific workflows where an email may be associated to multiple UIDs. This API is used to retrieve all of the identities (UID and Profiles), associated with a specified email in Cloud Storage.
        
        Args:
            email: Email of the user
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
		
        Returns:
            Complete user Identity data
        18.35
        """

        if(self._lr_object.is_null_or_whitespace(email)):
            raise Exception(self._lr_object.get_validation_message("email"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        query_parameters["email"] = email
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields

        resource_path = "identity/v2/manage/account/identities"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def account_delete_by_email(self, email):
        """This API is used to delete all user profiles associated with an Email.
        
        Args:
            email: Email of the user
		
        Returns:
            Response containing Definition of Delete Request
        18.36
        """

        if(self._lr_object.is_null_or_whitespace(email)):
            raise Exception(self._lr_object.get_validation_message("email"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        query_parameters["email"] = email

        resource_path = "identity/v2/manage/account"
        return self._lr_object.execute("DELETE", resource_path, query_parameters, {})

    def account_update_uid(self, update_uid_model, uid):
        """This API is used to update a user's Uid. It will update all profiles, custom objects and consent management logs associated with the Uid.
        
        Args:
            update_uid_model: Payload containing Update UID
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition of Complete Validation data
        18.41
        """
        if(update_uid_model is None):
            raise Exception(self._lr_object.get_validation_message("update_uid_model"))

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        query_parameters["uid"] = uid

        resource_path = "identity/v2/manage/account/uid"
        return self._lr_object.execute("PUT", resource_path, query_parameters, update_uid_model)

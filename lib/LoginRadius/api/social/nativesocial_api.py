# -- coding: utf-8 --
# Created by LoginRadius Development Team
# Copyright 2019 LoginRadius Inc. All rights reserved.
#


class NativeSocialApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    def get_access_token_by_facebook_access_token(self, fb__access__token, social_app_name=None):
        """The API is used to get LoginRadius access token by sending Facebook's access token. It will be valid for the specific duration of time specified in the response.
        
        Args:
            fb__access__token: Facebook Access Token
            social_app_name: Name of Social provider APP
		
        Returns:
            Response containing Definition of Complete Token data
        20.3
        """

        if(self._lr_object.is_null_or_whitespace(fb__access__token)):
            raise Exception(self._lr_object.get_validation_message("fb__access__token"))

        query_parameters = {}
        query_parameters["fb_Access_Token"] = fb__access__token
        query_parameters["key"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(social_app_name)):
            query_parameters["socialAppName"] = social_app_name

        resource_path = "api/v2/access_token/facebook"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_access_token_by_twitter_access_token(self, tw__access__token, tw__token__secret, social_app_name=None):
        """The API is used to get LoginRadius access token by sending Twitter's access token. It will be valid for the specific duration of time specified in the response.
        
        Args:
            tw__access__token: Twitter Access Token
            tw__token__secret: Twitter Token Secret
            social_app_name: Name of Social provider APP
		
        Returns:
            Response containing Definition of Complete Token data
        20.4
        """

        if(self._lr_object.is_null_or_whitespace(tw__access__token)):
            raise Exception(self._lr_object.get_validation_message("tw__access__token"))

        if(self._lr_object.is_null_or_whitespace(tw__token__secret)):
            raise Exception(self._lr_object.get_validation_message("tw__token__secret"))

        query_parameters = {}
        query_parameters["key"] = self._lr_object.get_api_key()
        query_parameters["tw_Access_Token"] = tw__access__token
        query_parameters["tw_Token_Secret"] = tw__token__secret
        if(not self._lr_object.is_null_or_whitespace(social_app_name)):
            query_parameters["socialAppName"] = social_app_name

        resource_path = "api/v2/access_token/twitter"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_access_token_by_google_access_token(self, google__access__token, client_id=None, refresh_token=None,
        social_app_name=None):
        """The API is used to get LoginRadius access token by sending Google's access token. It will be valid for the specific duration of time specified in the response.
        
        Args:
            google__access__token: Google Access Token
            client_id: Google Client ID
            refresh_token: LoginRadius refresh token
            social_app_name: Name of Social provider APP
		
        Returns:
            Response containing Definition of Complete Token data
        20.5
        """

        if(self._lr_object.is_null_or_whitespace(google__access__token)):
            raise Exception(self._lr_object.get_validation_message("google__access__token"))

        query_parameters = {}
        query_parameters["google_Access_Token"] = google__access__token
        query_parameters["key"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(client_id)):
            query_parameters["client_id"] = client_id
        if(not self._lr_object.is_null_or_whitespace(refresh_token)):
            query_parameters["refresh_token"] = refresh_token
        if(not self._lr_object.is_null_or_whitespace(social_app_name)):
            query_parameters["socialAppName"] = social_app_name

        resource_path = "api/v2/access_token/google"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_access_token_by_google_j_w_t_access_token(self, id__token):
        """This API is used to Get LoginRadius Access Token using google jwt id token for google native mobile login/registration.
        
        Args:
            id__token: Google JWT id_token
		
        Returns:
            Response containing Definition of Complete Token data
        20.6
        """

        if(self._lr_object.is_null_or_whitespace(id__token)):
            raise Exception(self._lr_object.get_validation_message("id__token"))

        query_parameters = {}
        query_parameters["id_Token"] = id__token
        query_parameters["key"] = self._lr_object.get_api_key()

        resource_path = "api/v2/access_token/googlejwt"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_access_token_by_linkedin_access_token(self, ln__access__token, social_app_name=None):
        """The API is used to get LoginRadius access token by sending Linkedin's access token. It will be valid for the specific duration of time specified in the response.
        
        Args:
            ln__access__token: Linkedin Access Token
            social_app_name: Name of Social provider APP
		
        Returns:
            Response containing Definition of Complete Token data
        20.7
        """

        if(self._lr_object.is_null_or_whitespace(ln__access__token)):
            raise Exception(self._lr_object.get_validation_message("ln__access__token"))

        query_parameters = {}
        query_parameters["key"] = self._lr_object.get_api_key()
        query_parameters["ln_Access_Token"] = ln__access__token
        if(not self._lr_object.is_null_or_whitespace(social_app_name)):
            query_parameters["socialAppName"] = social_app_name

        resource_path = "api/v2/access_token/linkedin"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_access_token_by_foursquare_access_token(self, fs__access__token):
        """The API is used to get LoginRadius access token by sending Foursquare's access token. It will be valid for the specific duration of time specified in the response.
        
        Args:
            fs__access__token: Foursquare Access Token
		
        Returns:
            Response containing Definition of Complete Token data
        20.8
        """

        if(self._lr_object.is_null_or_whitespace(fs__access__token)):
            raise Exception(self._lr_object.get_validation_message("fs__access__token"))

        query_parameters = {}
        query_parameters["fs_Access_Token"] = fs__access__token
        query_parameters["key"] = self._lr_object.get_api_key()

        resource_path = "api/v2/access_token/foursquare"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_access_token_by_apple_id_code(self, code, social_app_name=None):
        """The API is used to get LoginRadius access token by sending a valid Apple ID OAuth Code. It will be valid for the specific duration of time specified in the response.
        
        Args:
            code: Apple Code
            social_app_name: Name of Social provider APP
		
        Returns:
            Response containing Definition of Complete Token data
        20.12
        """

        if(self._lr_object.is_null_or_whitespace(code)):
            raise Exception(self._lr_object.get_validation_message("code"))

        query_parameters = {}
        query_parameters["code"] = code
        query_parameters["key"] = self._lr_object.get_api_key()
        if(not self._lr_object.is_null_or_whitespace(social_app_name)):
            query_parameters["socialAppName"] = social_app_name

        resource_path = "api/v2/access_token/apple"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_access_token_by_we_chat_code(self, code):
        """This API is used to retrieve a LoginRadius access token by passing in a valid WeChat OAuth Code.
        
        Args:
            code: WeChat Code
		
        Returns:
            Response containing Definition of Complete Token data
        20.13
        """

        if(self._lr_object.is_null_or_whitespace(code)):
            raise Exception(self._lr_object.get_validation_message("code"))

        query_parameters = {}
        query_parameters["code"] = code
        query_parameters["key"] = self._lr_object.get_api_key()

        resource_path = "api/v2/access_token/wechat"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_access_token_by_vkontakte_access_token(self, vk_access_token):
        """The API is used to get LoginRadius access token by sending Vkontakte's access token. It will be valid for the specific duration of time specified in the response.
        
        Args:
            vk_access_token: Vkontakte Access Token
		
        Returns:
            Response containing Definition of Complete Token data
        20.15
        """

        if(self._lr_object.is_null_or_whitespace(vk_access_token)):
            raise Exception(self._lr_object.get_validation_message("vk_access_token"))

        query_parameters = {}
        query_parameters["key"] = self._lr_object.get_api_key()
        query_parameters["vk_access_token"] = vk_access_token

        resource_path = "api/v2/access_token/vkontakte"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_access_token_by_google_auth_code(self, google_authcode, social_app_name=None):
        """The API is used to get LoginRadius access token by sending Google's AuthCode. It will be valid for the specific duration of time specified in the response.
        
        Args:
            google_authcode: Google AuthCode
            social_app_name: Name of Social provider APP
		
        Returns:
            Response containing Definition of Complete Token data
        20.16
        """

        if(self._lr_object.is_null_or_whitespace(google_authcode)):
            raise Exception(self._lr_object.get_validation_message("google_authcode"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["google_authcode"] = google_authcode
        if(not self._lr_object.is_null_or_whitespace(social_app_name)):
            query_parameters["socialAppName"] = social_app_name

        resource_path = "api/v2/access_token/google"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

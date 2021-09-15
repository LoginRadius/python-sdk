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

    def get_albums(self, access_token):
        """<b>Supported Providers:</b> Facebook, Google, Live, Vkontakte.<br><br> This API returns the photo albums associated with the passed in access tokens Social Profile.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
		
        Returns:
            Response Containing List of Album Data
        22.2.1
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token

        resource_path = "api/v2/album"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_albums_with_cursor(self, access_token, next_cursor):
        """<b>Supported Providers:</b> Facebook, Google, Live, Vkontakte.<br><br> This API returns the photo albums associated with the passed in access tokens Social Profile.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            next_cursor: Cursor value if not all contacts can be retrieved once.
		
        Returns:
            Response Model containing Albums with next cursor
        22.2.2
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(next_cursor)):
            raise Exception(self._lr_object.get_validation_message("next_cursor"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["nextCursor"] = next_cursor

        resource_path = "api/v2/album"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_audios(self, access_token):
        """The Audio API is used to get audio files data from the user's social account.<br><br><b>Supported Providers:</b> Live, Vkontakte
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
		
        Returns:
            Response Containing List of Audio Data
        24.2.1
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token

        resource_path = "api/v2/audio"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_audios_with_cursor(self, access_token, next_cursor):
        """The Audio API is used to get audio files data from the user's social account.<br><br><b>Supported Providers:</b> Live, Vkontakte
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            next_cursor: Cursor value if not all contacts can be retrieved once.
		
        Returns:
            Response Model containing Audio with next cursor
        24.2.2
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(next_cursor)):
            raise Exception(self._lr_object.get_validation_message("next_cursor"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["nextCursor"] = next_cursor

        resource_path = "api/v2/audio"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_check_ins(self, access_token):
        """The Check In API is used to get check Ins data from the user's social account.<br><br><b>Supported Providers:</b> Facebook, Foursquare, Vkontakte
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
		
        Returns:
            Response Containing List of CheckIn Data
        25.2.1
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token

        resource_path = "api/v2/checkin"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_check_ins_with_cursor(self, access_token, next_cursor):
        """The Check In API is used to get check Ins data from the user's social account.<br><br><b>Supported Providers:</b> Facebook, Foursquare, Vkontakte
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            next_cursor: Cursor value if not all contacts can be retrieved once.
		
        Returns:
            Response Model containing Checkins with next cursor
        25.2.2
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(next_cursor)):
            raise Exception(self._lr_object.get_validation_message("next_cursor"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["nextCursor"] = next_cursor

        resource_path = "api/v2/checkin"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_contacts(self, access_token, next_cursor=''):
        """The Contact API is used to get contacts/friends/connections data from the user's social account.This is one of the APIs that makes up the LoginRadius Friend Invite System. The data will normalized into LoginRadius' standard data format. This API requires setting permissions in your LoginRadius Dashboard. <br><br><b>Note:</b> Facebook restricts access to the list of friends that is returned. When using the Contacts API with Facebook you will only receive friends that have accepted some permissions with your app. <br><br><b>Supported Providers:</b> Facebook, Foursquare, Google, LinkedIn, Live, Twitter, Vkontakte, Yahoo
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            next_cursor: Cursor value if not all contacts can be retrieved once.
		
        Returns:
            Response containing Definition of Contact Data with Cursor
        27.1
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        if(not self._lr_object.is_null_or_whitespace(next_cursor)):
            query_parameters["nextCursor"] = next_cursor

        resource_path = "api/v2/contact"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_events(self, access_token):
        """The Event API is used to get the event data from the user's social account.<br><br><b>Supported Providers:</b> Facebook, Live
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
		
        Returns:
            Response Containing List of Events Data
        28.2.1
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token

        resource_path = "api/v2/event"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_events_with_cursor(self, access_token, next_cursor):
        """The Event API is used to get the event data from the user's social account.<br><br><b>Supported Providers:</b> Facebook, Live
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            next_cursor: Cursor value if not all contacts can be retrieved once.
		
        Returns:
            Response Model containing Events with next cursor
        28.2.2
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(next_cursor)):
            raise Exception(self._lr_object.get_validation_message("next_cursor"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["nextCursor"] = next_cursor

        resource_path = "api/v2/event"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_followings(self, access_token):
        """Get the following user list from the user's social account.<br><br><b>Supported Providers:</b> Twitter
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
		
        Returns:
            Response Containing List of Contacts Data
        29.2.1
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token

        resource_path = "api/v2/following"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_followings_with_cursor(self, access_token, next_cursor):
        """Get the following user list from the user's social account.<br><br><b>Supported Providers:</b> Twitter
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            next_cursor: Cursor value if not all contacts can be retrieved once.
		
        Returns:
            Response containing Definition of Contact Data with Cursor
        29.2.2
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(next_cursor)):
            raise Exception(self._lr_object.get_validation_message("next_cursor"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["nextCursor"] = next_cursor

        resource_path = "api/v2/following"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_groups(self, access_token):
        """The Group API is used to get group data from the user's social account.<br><br><b>Supported Providers:</b> Facebook, Vkontakte
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
		
        Returns:
            Response Containing List of Groups Data
        30.2.1
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token

        resource_path = "api/v2/group"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_groups_with_cursor(self, access_token, next_cursor):
        """The Group API is used to get group data from the user's social account.<br><br><b>Supported Providers:</b> Facebook, Vkontakte
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            next_cursor: Cursor value if not all contacts can be retrieved once.
		
        Returns:
            Response Model containing Groups with next cursor
        30.2.2
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(next_cursor)):
            raise Exception(self._lr_object.get_validation_message("next_cursor"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["nextCursor"] = next_cursor

        resource_path = "api/v2/group"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_likes(self, access_token):
        """The Like API is used to get likes data from the user's social account.<br><br><b>Supported Providers:</b> Facebook
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
		
        Returns:
            Response Containing List of Likes Data
        31.2.1
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token

        resource_path = "api/v2/like"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_likes_with_cursor(self, access_token, next_cursor):
        """The Like API is used to get likes data from the user's social account.<br><br><b>Supported Providers:</b> Facebook
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            next_cursor: Cursor value if not all contacts can be retrieved once.
		
        Returns:
            Response Model containing Likes with next cursor
        31.2.2
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(next_cursor)):
            raise Exception(self._lr_object.get_validation_message("next_cursor"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["nextCursor"] = next_cursor

        resource_path = "api/v2/like"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_mentions(self, access_token):
        """The Mention API is used to get mentions data from the user's social account.<br><br><b>Supported Providers:</b> Twitter
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
		
        Returns:
            Response Containing List of Status Data
        32.1
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token

        resource_path = "api/v2/mention"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def post_message(self, access_token, message, subject,
        to):
        """Post Message API is used to post messages to the user's contacts.<br><br><b>Supported Providers:</b> Twitter, LinkedIn <br><br>The Message API is used to post messages to the user?s contacts. This is one of the APIs that makes up the LoginRadius Friend Invite System. After using the Contact API, you can send messages to the retrieved contacts. This API requires setting permissions in your LoginRadius Dashboard.<br><br>GET & POST Message API work the same way except the API method is different
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            message: Body of your message
            subject: Subject of your message
            to: Recipient's social provider's id
		
        Returns:
            Response containing Definition for Complete Validation data
        33.1
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(message)):
            raise Exception(self._lr_object.get_validation_message("message"))

        if(self._lr_object.is_null_or_whitespace(subject)):
            raise Exception(self._lr_object.get_validation_message("subject"))

        if(self._lr_object.is_null_or_whitespace(to)):
            raise Exception(self._lr_object.get_validation_message("to"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["message"] = message
        query_parameters["subject"] = subject
        query_parameters["to"] = to

        resource_path = "api/v2/message"
        return self._lr_object.execute("POST", resource_path, query_parameters, {})

    def get_page(self, access_token, page_name):
        """The Page API is used to get the page data from the user's social account.<br><br><b>Supported Providers:</b>  Facebook, LinkedIn
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            page_name: Name of the page you want to retrieve info from
		
        Returns:
            Response containing Definition of Complete page data
        34.1
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(page_name)):
            raise Exception(self._lr_object.get_validation_message("page_name"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["pageName"] = page_name

        resource_path = "api/v2/page"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_photos(self, access_token, album_id):
        """The Photo API is used to get photo data from the user's social account.<br><br><b>Supported Providers:</b>  Facebook, Foursquare, Google, Live, Vkontakte
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            album_id: The id of the album you want to retrieve info from
		
        Returns:
            Response Containing List of Photos Data
        35.1
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(album_id)):
            raise Exception(self._lr_object.get_validation_message("album_id"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["albumId"] = album_id

        resource_path = "api/v2/photo"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_posts(self, access_token):
        """The Post API is used to get post message data from the user's social account.<br><br><b>Supported Providers:</b>  Facebook
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
		
        Returns:
            Response Containing List of Posts Data
        36.1
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token

        resource_path = "api/v2/post"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def status_posting(self, access_token, caption, description,
        imageurl, status, title, url,
        shorturl='0'):
        """The Status API is used to update the status on the user's wall.<br><br><b>Supported Providers:</b>  Facebook, Twitter, LinkedIn
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            caption: Message displayed below the description(Requires URL, Under 70 Characters).
            description: Description of the displayed URL and Image(Requires URL)
            imageurl: Image to be displayed in the share(Requires URL).
            status: Main body of the Status update.
            title: Title of Linked URL
            url: URL to be included when clicking on the share.
            shorturl: short url
		
        Returns:
            Response conatining Definition of Validation and Short URL data
        37.2
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(caption)):
            raise Exception(self._lr_object.get_validation_message("caption"))

        if(self._lr_object.is_null_or_whitespace(description)):
            raise Exception(self._lr_object.get_validation_message("description"))

        if(self._lr_object.is_null_or_whitespace(imageurl)):
            raise Exception(self._lr_object.get_validation_message("imageurl"))

        if(self._lr_object.is_null_or_whitespace(status)):
            raise Exception(self._lr_object.get_validation_message("status"))

        if(self._lr_object.is_null_or_whitespace(title)):
            raise Exception(self._lr_object.get_validation_message("title"))

        if(self._lr_object.is_null_or_whitespace(url)):
            raise Exception(self._lr_object.get_validation_message("url"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["caption"] = caption
        query_parameters["description"] = description
        query_parameters["imageurl"] = imageurl
        query_parameters["status"] = status
        query_parameters["title"] = title
        query_parameters["url"] = url
        if(not self._lr_object.is_null_or_whitespace(shorturl)):
            query_parameters["shorturl"] = shorturl

        resource_path = "api/v2/status"
        return self._lr_object.execute("POST", resource_path, query_parameters, {})

    def trackable_status_posting(self, access_token, status_model):
        """The Trackable status API works very similar to the Status API but it returns a Post id that you can use to track the stats(shares, likes, comments) for a specific share/post/status update. This API requires setting permissions in your LoginRadius Dashboard.<br><br> The Trackable Status API is used to update the status on the user's wall and return an Post ID value. It is commonly referred to as Permission based sharing or Push notifications.<br><br> POST Input Parameter Format: application/x-www-form-urlencoded
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            status_model: Model Class containing Definition of payload for Status API
		
        Returns:
            Response containing Definition for Complete status data
        37.6
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))
        if(status_model is None):
            raise Exception(self._lr_object.get_validation_message("status_model"))

        query_parameters = {}
        query_parameters["access_token"] = access_token

        resource_path = "api/v2/status/trackable"
        return self._lr_object.execute("POST", resource_path, query_parameters, status_model)

    def get_trackable_status_stats(self, access_token, caption, description,
        imageurl, status, title, url):
        """The Trackable status API works very similar to the Status API but it returns a Post id that you can use to track the stats(shares, likes, comments) for a specific share/post/status update. This API requires setting permissions in your LoginRadius Dashboard.<br><br> The Trackable Status API is used to update the status on the user's wall and return an Post ID value. It is commonly referred to as Permission based sharing or Push notifications.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            caption: Message displayed below the description(Requires URL, Under 70 Characters).
            description: Description of the displayed URL and Image(Requires URL)
            imageurl: Image to be displayed in the share(Requires URL).
            status: Main body of the Status update.
            title: Title of Linked URL
            url: URL to be included when clicking on the share.
		
        Returns:
            Response containing Definition for Complete status data
        37.7
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(caption)):
            raise Exception(self._lr_object.get_validation_message("caption"))

        if(self._lr_object.is_null_or_whitespace(description)):
            raise Exception(self._lr_object.get_validation_message("description"))

        if(self._lr_object.is_null_or_whitespace(imageurl)):
            raise Exception(self._lr_object.get_validation_message("imageurl"))

        if(self._lr_object.is_null_or_whitespace(status)):
            raise Exception(self._lr_object.get_validation_message("status"))

        if(self._lr_object.is_null_or_whitespace(title)):
            raise Exception(self._lr_object.get_validation_message("title"))

        if(self._lr_object.is_null_or_whitespace(url)):
            raise Exception(self._lr_object.get_validation_message("url"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["caption"] = caption
        query_parameters["description"] = description
        query_parameters["imageurl"] = imageurl
        query_parameters["status"] = status
        query_parameters["title"] = title
        query_parameters["url"] = url

        resource_path = "api/v2/status/trackable/js"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def trackable_status_fetching(self, post_id):
        """The Trackable status API works very similar to the Status API but it returns a Post id that you can use to track the stats(shares, likes, comments) for a specific share/post/status update. This API requires setting permissions in your LoginRadius Dashboard.<br><br> This API is used to retrieve a tracked post based on the passed in post ID value. This API requires setting permissions in your LoginRadius Dashboard.<br><br> <b>Note:</b> To utilize this API you need to find the ID for the post you want to track, which might require using Trackable Status Posting API first.
        
        Args:
            post_id: Post ID value
		
        Returns:
            Response containing Definition of Complete Status Update data
        37.8
        """

        if(self._lr_object.is_null_or_whitespace(post_id)):
            raise Exception(self._lr_object.get_validation_message("post_id"))

        query_parameters = {}
        query_parameters["postId"] = post_id
        query_parameters["secret"] = self._lr_object.get_api_secret()

        resource_path = "api/v2/status/trackable"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_refreshed_social_user_profile(self, access_token, fields=''):
        """The User Profile API is used to get the latest updated social profile data from the user's social account after authentication. The social profile will be retrieved via oAuth and OpenID protocols. The data is normalized into LoginRadius' standard data format. This API should be called using the access token retrieved from the refresh access token API.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            fields: The fields parameter filters the API response so that the response only includes a specific set of fields
		
        Returns:
            Response containing Definition for Complete UserProfile data
        38.2
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        if(not self._lr_object.is_null_or_whitespace(fields)):
            query_parameters["fields"] = fields

        resource_path = "api/v2/userprofile/refresh"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_videos(self, access_token, next_cursor):
        """The Video API is used to get video files data from the user's social account.<br><br><b>Supported Providers:</b>   Facebook, Google, Live, Vkontakte
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            next_cursor: Cursor value if not all contacts can be retrieved once.
		
        Returns:
            Response containing Definition of Video Data with Cursor
        39.2
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(next_cursor)):
            raise Exception(self._lr_object.get_validation_message("next_cursor"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["nextCursor"] = next_cursor

        resource_path = "api/v2/video"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

#!/usr/bin/python
#################################################
# Class for Social Authentication               #
#################################################
# This is the main class to communicate with    #
# LoginRadius' Unified Social API. It contains  #
# functions for Social Authentication with User #
# Profile Data (Basic and Extended).            #
#                                               #
# Please note that some API calls are for       #
# premium or enterprise members only.           #
# In which case, an exception will be raised.   #
#################################################
# Copyright 2017-2018 LoginRadius Inc.          #
# - www.LoginRadius.com                         #
#################################################
# This file is part of the LoginRadius SDK      #
# package.                                      #
#################################################

SECURE_API_URL = "https://api.loginradius.com/"
socialLoginEndpoint ="/api/v2/";

class SocialLogin():
    """Where all the API commands can be invoked locally."""

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    #
    # Read permissions
    #

    def get_refresh_user_profile(self, access_token):
        # Refresh User Profile (GET)
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "userprofile/refresh"
        return self._lr_object._get_json(url, payload)

    def get_user_profile(self, access_token):
        """Retrieve basic profile information."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint +"userprofile/"
        return self._lr_object._get_json(url, payload)

    def get_user_profile_raw(self, access_token):
        """Retrieve basic profile information but unformatted based on the provider."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "userprofile/raw/"
        return self._lr_object._get_json(url, payload)

    def get_photo(self, access_token, album_id=''):
        """Get photos based on the album_id retrieved."""
        payload = {'access_token': access_token, 'albumid': album_id}
        url = SECURE_API_URL + socialLoginEndpoint + "photo/"
        return self._lr_object._get_json(url, payload)

    def get_photo_raw(self, access_token, album_id=''):
        """Get photos based on the album_id retrieved but unformatted based on the provider."""
        payload = {'access_token': access_token, 'albumid': album_id}
        url = SECURE_API_URL + socialLoginEndpoint + "photo/raw/"
        return self._lr_object._get_json(url, payload)

    def get_checkin(self, access_token):
        """Get check ins from profile."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "checkin/"
        return self._lr_object._get_json(url, payload)

    def get_checkin_raw(self, access_token):
        """Get check ins but in raw format based on provider."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "checkin/raw/"
        return self._lr_object._get_json(url, payload)

    def get_album(self, access_token):
        """Get albums from profile."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "album/"
        return self._lr_object._get_json(url, payload)

    def get_album_raw(self, access_token):
        """Get albums from profile but in raw format based on provider."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "album/raw/"
        return self._lr_object._get_json(url, payload)

    def get_audio(self, access_token):
        """Get audio from the profile."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "audio/"
        return self._lr_object._get_json(url, payload)

    def get_audio_raw(self, access_token):
        """Get audio from the profile but in raw format based on provider."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "audio/raw/"
        return self._lr_object._get_json(url, payload)

    def get_video(self, access_token):
        """Get videos from the profile."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "video/"
        return self._lr_object._get_json(url, payload)

    def get_video_raw(self, access_token):
        """Get videos from the profile but in raw format based on provider."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "video/raw/"
        return self._lr_object._get_json(url, payload)

    def get_contacts(self, access_token, next_cursor=''):
        """Get a list of contacts from the profile."""
        payload = {'access_token': access_token, 'nextcursor': next_cursor}
        url = SECURE_API_URL + socialLoginEndpoint + "contact/"
        return self._lr_object._get_json(url, payload)

    def get_contacts_raw(self, access_token, next_cursor=''):
        """Get a list of contacts from the profile but in raw format based on provider."""
        payload = {'access_token': access_token, 'nextcursor': next_cursor}
        url = SECURE_API_URL + socialLoginEndpoint + "contact/raw/"
        return self._lr_object._get_json(url, payload)

    def get_status(self, access_token):
        """Get status updates from profile."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "status/"
        return self._lr_object._get_json(url, payload)

    def get_status_raw(self, access_token):
        """Get status updates from profile but in raw format based on provider."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "status/raw/"
        return self._lr_object._get_json(url, payload)

    def get_group(self, access_token):
        """Get group data from profile."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "group/"
        return self._lr_object._get_json(url, payload)

    def get_group_raw(self, access_token):
        """Get group data from profile but in raw format based on provider."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "group/raw/"
        return self._lr_object._get_json(url, payload)

    def get_post(self, access_token):
        """Get posts from profile."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "post/"
        return self._lr_object._get_json(url, payload)

    def get_post_raw(self, access_token):
        """Get posts from profile but in raw format based on provider."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "post/raw/"
        return self._lr_object._get_json(url, payload)

    def get_event(self, access_token):
        """Get events from profile."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "event/"
        return self._lr_object._get_json(url, payload)

    def get_event_raw(self, access_token):
        """Get events from profile but in raw format based on provider."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "event/raw/"
        return self._lr_object._get_json(url, payload)

    def get_mention(self, access_token):
        """Get mentions from profile."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "mention/"
        return self._lr_object._get_json(url, payload)

    def get_mention_raw(self, access_token):
        """Get mentions from profile but in raw format based on provider."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "mention/raw/"
        return self._lr_object._get_json(url, payload)

    def get_company(self, access_token):
        """Get company from profile."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "company/"
        return self._lr_object._get_json(url, payload)

    def get_company_raw(self, access_token):
        """Get company from profile but in raw format based on provider."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "company/raw/"
        return self._lr_object._get_json(url, payload)

    def get_following(self, access_token):
        """Get following/followers from profile."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "following/"
        return self._lr_object._get_json(url, payload)

    def get_following_raw(self, access_token):
        """Get following/followers from profile but in raw format based on provider."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "following/raw/"
        return self._lr_object._get_json(url, payload)

    def get_activity(self, access_token):
        """Get activity from profile."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "activity/"
        return self._lr_object._get_json(url, payload)

    def get_activity_raw(self, access_token):
        """Get activity from profile but in raw format based on provider."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "activity/raw/"
        return self._lr_object._get_json(url, payload)

    def get_page(self, access_token, page_name):
        """Get page information from profile."""
        payload = {'access_token': access_token, 'pagename': page_name}
        url = SECURE_API_URL + socialLoginEndpoint + "page/"
        return self._lr_object._get_json(url, payload)

    def get_page_raw(self, access_token, page_name):
        """Get page information from profile but in raw format based on provider."""
        payload = {'access_token': access_token, 'pagename': page_name}
        url = SECURE_API_URL + socialLoginEndpoint + "page/raw/"
        return self._lr_object._get_json(url, payload)

    def get_like(self, access_token):
        """Get likes from profile."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "like/"
        return self._lr_object._get_json(url, payload)

    def get_like_raw(self, access_token):
        """Get likes from profile but in raw format based on provider."""
        payload = {'access_token': access_token}
        url = SECURE_API_URL + socialLoginEndpoint + "like/raw/"
        return self._lr_object._get_json(url, payload)
    
    def get_message(self, access_token, to, subject, message):
        """Get messages from profile."""
        payload = {'access_token': access_token, 'to':to,'subject':subject,'message':message}
        url = SECURE_API_URL + socialLoginEndpoint + "message/js/"
        return self._lr_object._get_json(url, payload)

    def get_status_update(self, access_token, status, title='', url='', imageurl='', caption='', description=''):
        """
        Perform a status update on the profile on behalf of the user.
        Some of these arguments may be ignored depending on the provider.
        For what is and is not supported, please refer to:
        http://www.loginradius.com/datapoints
        """
        payload = '?access_token='+ access_token + '&status='+ status + '&title='+ title + '&url=' + url + '&imageurl=' + imageurl + '&caption=' + caption + '&description=' + description
        url = SECURE_API_URL + socialLoginEndpoint + "status/js"
        return self._lr_object._get_json(url+payload, {})

    #
    #Write Permissions
    #

    def status_update(self, access_token, status, title='', url='', imageurl='', caption='', description=''):
        """
        Perform a status update on the profile on behalf of the user.
        Some of these arguments may be ignored depending on the provider.
        For what is and is not supported, please refer to:
        http://www.loginradius.com/datapoints
        """
        payload = '?access_token='+ access_token + '&status='+ status + '&title='+ title + '&url=' + url + '&imageurl=' + imageurl + '&caption=' + caption + '&description=' + description
        url = SECURE_API_URL + socialLoginEndpoint + "status/"
        return self._lr_object._post_json(url+payload, {})

    def direct_message(self, access_token, to, subject, message):
        """Direct message another user on behalf of this user."""
        payload = '?access_token=' + access_token + '&to=' + to + '&subject=' + subject + '&message=' + message
        url = SECURE_API_URL + socialLoginEndpoint + "message/"
        return self._lr_object._post_json(url+payload, {})



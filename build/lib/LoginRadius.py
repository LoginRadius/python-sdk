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
# Copyright 2013-2014 LoginRadius Inc.          #
# - www.LoginRadius.com                         #
#################################################
# This file is part of the LoginRadius SDK      #
# package.                                      #
#################################################
from datetime import datetime

#Requires Python 2.6>
from collections import namedtuple
#Requires Python 2.7>
from importlib import import_module

__author__ = "LoginRadius"
__copyright__ = "Copyright 2013-2014, LoginRadius"
__email__ = "developers@loginradius.com"
__status__ = "Production"
__version__ = "2.0"

SECURE_API_URL = "https://api.loginradius.com/"
HEADERS = {'Accept': "application/json"}


class LoginRadius():
    """
    LoginRadius Class. Use this to obtain social data and other information
    from the LoginRadius API. Requires Python 2.7 or greater.
    """

    API_SECRET = None
    LIBRARY = None

    def __init__(self, token):
        """
        Constructed when you want to retrieve social data with respect to the acquired token.
        :param token: token from LoginRadius Callback.
        :raise Exceptions.NoAPISecret: Raised if you did not set an API_SECRET.
        """
        self.user = None
        self.error = {}
        if not self.API_SECRET:
            raise Exceptions.NoAPISecret

        #Token from the POST request.
        self.token = token

        #Namedtuple for settings for each request and the api functions.
        self.settings = namedtuple("Settings", ['library', 'urllib', 'urllib2', 'json', 'requests'])
        self.api = LoginRadiusAPI(self)

        #We prefer to use requests with the updated urllib3 module.
        try:
            from distutils.version import StrictVersion
            import requests

            if StrictVersion(requests.__version__) < StrictVersion("2.0"):
                raise Exceptions.RequestsLibraryDated(requests.__version__)
            else:
                self._settings("requests")

        #However, we can use urllib if there is no requests or it is outdated.
        except (ImportError, Exceptions.RequestsLibraryDated):
            self._settings("urllib2")

        #Well, something went wrong here.
        except:
            raise

        else:
            #Namedtuples for access, api, and user.
            self.access = self._get_access_tuple()
            self.user = self._get_user_tuple()

    #
    # Internal private functions
    #

    def _settings(self, library):
        """This sets the name tuple settings to whatever library you want. You may change this as you wish."""
        if LoginRadius.LIBRARY is not None:
            if LoginRadius.LIBRARY == "requests":
                self._set_requests()
            elif LoginRadius.LIBRARY == "urllib2":
                self._set_urllib2()
            else:
                raise Exceptions.InvalidLibrary(LoginRadius.LIBRARY)
        else:
            if library == "requests":
                self._set_requests()
            elif library == "urllib2":
                self._set_urllib2()
            else:
                raise Exceptions.InvalidLibrary(library)

    def _set_requests(self):
        """Change to the requests library to use."""
        self.settings.library = "requests"
        self.settings.requests = import_module("requests")
        self.settings.urllib2 = False

    def _set_urllib2(self):
        """Change to the requests urllib2 library to use."""
        self.settings.library = "urllib2"
        self.settings.requests = False
        self.settings.urllib2 = import_module("urllib2")
        self.settings.urllib = import_module("urllib")
        self.settings.json = import_module("json")

    def _get_user_tuple(self):
        """All the functions relative to the user with the token."""
        user = namedtuple("User", ['profile', 'photo', 'check_in', 'audio', 'album', 'video',
                                   'contacts', 'status', 'group', 'post', 'event', 'mention',
                                   'company', 'following', 'activity', 'page', 'like',
                                   'status_update', 'direct_message'])

        #Lazy get methods
        user.profile = UserProfileLazyLoad(self)
        user.photo = PhotoLazyLoad(self)
        user.check_in = CheckInLazyLoad(self)
        user.album = AlbumLazyLoad(self)
        user.audio = AudioLazyLoad(self)
        user.video = VideoLazyLoad(self)
        user.contacts = ContactsLazyLoad(self)
        user.status = StatusLazyLoad(self)
        user.group = GroupLazyLoad(self)
        user.event = EventLazyLoad(self)
        user.mention = MentionLazyLoad(self)
        user.activity = ActivityLazyLoad(self)
        user.following = FollowingLazyLoad(self)
        user.page = PageLazyLoad(self)
        user.like = LikeLazyLoad(self)

        #Post methods
        user.status_update = self.api.status_update
        user.direct_message = self.api.direct_message

        return user

    #Get access token
    def _get_access_tuple(self):
        """Access information like token and expire."""
        payload = {'token': self.token, 'secret': self.API_SECRET}
        url = SECURE_API_URL + "api/v2/access_token"
        results = self._get_json(url, payload)
        access = namedtuple("Access", ['token', 'expire', 'raw', 'valid'])
        access.raw = results

        if 'access_token' in results:
            access.token = results['access_token']
        else:
            raise Exceptions.MissingJsonResponseParameter('access_token', raw=access.raw)

        if 'expires_in' in results:
            access.expire = results['expires_in']
        else:
            raise Exceptions.MissingJsonResponseParameter('expires_in', raw=access.raw)

        access.valid = self._validate_token

        return access

    def _get_json(self, url, payload):
        """Get JSON from LoginRadius"""
        if self.settings.requests:
            r = self.settings.requests.get(url, params=payload, headers=HEADERS)
            return self._process_result(r.json())
        else:
            payload = self.settings.urllib.urlencode(payload)
            r = self.settings.urllib2.Request(url + "?" + payload)
            r.add_header('Accept', HEADERS['Accept'])

            try:
                data = self.settings.urllib2.urlopen(r)
            except self.settings.urllib2.HTTPError:
                raise
            return self._process_result(self.settings.json.load(data))

    def _post_json(self, url, payload):
        """Post JSON to LoginRadius"""
        if self.settings.requests:
            import json

            data = json.dumps(payload)
            r = self.settings.requests.post(url + "?" + data, params=payload, headers=HEADERS)
            return self._process_result(r.json())

        else:
            payload = self.settings.urllib.urlencode(payload)
            r = self.settings.urllib2.Request(url + "?" + payload, '', {'Content-Type': 'application/json'})
            for key, value in HEADERS.items():
                r.add_header(key, value)
            try:
                data = self.settings.urllib2.urlopen(r)
            except self.settings.urllib2.HTTPError:
                raise
            return self._process_result(self.settings.json.load(data))

    def _process_result(self, result):
        """Anything we need to parse or look for. In this case, just the errorCode"""
        if "errorCode" in result:
            self._process_error(result)
        else:
            return result

    def _process_error(self, result):
        """If there is an errorCode, let's figure out which one and raise the corresponding exception."""
        self.error = result
        if result['errorCode'] == 901:
            raise Exceptions.APIKeyInvalid
        elif result['errorCode'] == 902:
            raise Exceptions.APISecretInvalid
        elif result['errorCode'] == 903:
            raise Exceptions.InvalidRequestToken
        elif result['errorCode'] == 904:
            raise Exceptions.RequestTokenExpired
        elif result['errorCode'] == 905:
            raise Exceptions.InvalidAccessToken
        elif result['errorCode'] == 906:
            raise Exceptions.TokenExpired(self.access.expire)
        elif result['errorCode'] == 907:
            raise Exceptions.ParameterMissing
        elif result['errorCode'] == 908:
            raise Exceptions.ParameterNotFormatted
        elif result['errorCode'] == 909:
            raise Exceptions.FeatureNotSupported
        elif result['errorCode'] == 910:
            raise Exceptions.EndPointNotSupported
        else:
            raise Exceptions.UnknownJsonError(result)

    def _validate_token(self):
        """UTC time relative for checking if our token is still valid."""
        expire = datetime.strptime(self.access.expire, "%Y-%m-%dT%H:%M:%S.%fZ")
        if expire > datetime.utcnow():
            return True
        else:
            return False

    #
    # Public functions
    #

    def change_library(self, library):
        self._settings(library)


class LoginRadiusAPI(object):
    """Where all the API commands can be invoked locally."""

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    #
    # Read permissions
    #

    def get_user_profile(self):
        """Retrieve basic profile information."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/userprofile/"
        return self._lr_object._get_json(url, payload)

    def get_user_profile_raw(self):
        """Retrieve basic profile information but unformatted based on the provider."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/userprofile/raw/"
        return self._lr_object._get_json(url, payload)

    def get_photo(self, album_id=''):
        """Get photos based on the album_id retrieved."""
        payload = {'access_token': self._lr_object.access.token, 'albumid': album_id}
        url = SECURE_API_URL + "api/v2/photo/"
        return self._lr_object._get_json(url, payload)

    def get_photo_raw(self, album_id=''):
        """Get photos based on the album_id retrieved but unformatted based on the provider."""
        payload = {'access_token': self._lr_object.access.token, 'albumid': album_id}
        url = SECURE_API_URL + "api/v2/photo/raw/"
        return self._lr_object._get_json(url, payload)

    def get_checkin(self):
        """Get check ins from profile."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/checkin/"
        return self._lr_object._get_json(url, payload)

    def get_checkin_raw(self):
        """Get check ins but in raw format based on provider."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/checkin/raw/"
        return self._lr_object._get_json(url, payload)

    def get_album(self):
        """Get albums from profile."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/album/"
        return self._lr_object._get_json(url, payload)

    def get_album_raw(self):
        """Get albums from profile but in raw format based on provider."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/album/raw/"
        return self._lr_object._get_json(url, payload)

    def get_audio(self):
        """Get audio from the profile."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/audio/"
        return self._lr_object._get_json(url, payload)

    def get_audio_raw(self):
        """Get audio from the profile but in raw format based on provider."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/audio/raw/"
        return self._lr_object._get_json(url, payload)

    def get_video(self):
        """Get videos from the profile."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/video/"
        return self._lr_object._get_json(url, payload)

    def get_video_raw(self):
        """Get videos from the profile but in raw format based on provider."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/video/raw/"
        return self._lr_object._get_json(url, payload)

    def get_contacts(self, next_cursor=''):
        """Get a list of contacts from the profile."""
        payload = {'access_token': self._lr_object.access.token, 'nextcursor': next_cursor}
        url = SECURE_API_URL + "api/v2/contact/"
        return self._lr_object._get_json(url, payload)

    def get_contacts_raw(self, next_cursor=''):
        """Get a list of contacts from the profile but in raw format based on provider."""
        payload = {'access_token': self._lr_object.access.token, 'nextcursor': next_cursor}
        url = SECURE_API_URL + "api/v2/contact/raw/"
        return self._lr_object._get_json(url, payload)

    def get_status(self):
        """Get status updates from profile."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/status/"
        return self._lr_object._get_json(url, payload)

    def get_status_raw(self):
        """Get status updates from profile but in raw format based on provider."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/status/raw/"
        return self._lr_object._get_json(url, payload)

    def get_group(self):
        """Get group data from profile."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/group/"
        return self._lr_object._get_json(url, payload)

    def get_group_raw(self):
        """Get group data from profile but in raw format based on provider."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/group/raw/"
        return self._lr_object._get_json(url, payload)

    def get_post(self):
        """Get posts from profile."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/post/"
        return self._lr_object._get_json(url, payload)

    def get_post_raw(self):
        """Get posts from profile but in raw format based on provider."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/post/raw/"
        return self._lr_object._get_json(url, payload)

    def get_event(self):
        """Get events from profile."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/event/"
        return self._lr_object._get_json(url, payload)

    def get_event_raw(self):
        """Get events from profile but in raw format based on provider."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/event/raw/"
        return self._lr_object._get_json(url, payload)

    def get_mention(self):
        """Get mentions from profile."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/mention/"
        return self._lr_object._get_json(url, payload)

    def get_mention_raw(self):
        """Get mentions from profile but in raw format based on provider."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/mention/raw/"
        return self._lr_object._get_json(url, payload)

    def get_company(self):
        """Get company from profile."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/company/"
        return self._lr_object._get_json(url, payload)

    def get_company_raw(self):
        """Get company from profile but in raw format based on provider."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/company/raw/"
        return self._lr_object._get_json(url, payload)

    def get_following(self):
        """Get following/followers from profile."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/following/"
        return self._lr_object._get_json(url, payload)

    def get_following_raw(self):
        """Get following/followers from profile but in raw format based on provider."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/following/raw/"
        return self._lr_object._get_json(url, payload)

    def get_activity(self):
        """Get activity from profile."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/activity/"
        return self._lr_object._get_json(url, payload)

    def get_activity_raw(self):
        """Get activity from profile but in raw format based on provider."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/activity/raw/"
        return self._lr_object._get_json(url, payload)

    def get_page(self, page_name):
        """Get page information from profile."""
        payload = {'access_token': self._lr_object.access.token, 'pagename': page_name}
        url = SECURE_API_URL + "api/v2/page/"
        return self._lr_object._get_json(url, payload)

    def get_page_raw(self, page_name):
        """Get page information from profile but in raw format based on provider."""
        payload = {'access_token': self._lr_object.access.token, 'pagename': page_name}
        url = SECURE_API_URL + "api/v2/page/raw/"
        return self._lr_object._get_json(url, payload)

    def get_like(self):
        """Get likes from profile."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/like/"
        return self._lr_object._get_json(url, payload)

    def get_like_raw(self):
        """Get likes from profile but in raw format based on provider."""
        payload = {'access_token': self._lr_object.access.token}
        url = SECURE_API_URL + "api/v2/like/raw/"
        return self._lr_object._get_json(url, payload)

    #
    #Write Permissions
    #

    def status_update(self, status, title='', url='', imageurl='', caption='', description=''):
        """
        Perform a status update on the profile on behalf of the user.
        Some of these arguments may be ignored depending on the provider.
        For what is and is not supported, please refer to:
        http://www.loginradius.com/datapoints
        """
        payload = {'access_token': self._lr_object.access.token, 'status': status, 'title': title, 'url': url, 'imageurl': imageurl,
                   'caption': caption, 'description': description}
        url = SECURE_API_URL + "api/v2/status/"
        return self._lr_object._post_json(url, payload)

    def direct_message(self, to, subject, message):
        """Direct message another user on behalf of this user."""
        payload = {'access_token': self._lr_object.access.token, 'to': to, 'subject': subject, 'message': message}
        url = SECURE_API_URL + "api/v2/message/"
        return self._lr_object._post_json(url, payload)


class LazyLoad(object):
    """"lazy load" the details when needed. This methodology is inspired by SQLAlchemy."""

    def __init__(self, lr_object, raw=False):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        :param raw: This determines whether or not we should ask the API for provider independent data.
        """

        self._lr_object = lr_object
        self.data = None
        self.raw = raw

    def __str__(self):
        """
        Return the string equivalent of the dictionary.
        """
        self._check()
        return str(self.data)

    def load(self):
        """
        Promptly load the data instead of loading it on first access.
        """
        self.data = self.get()

    def get(self):
        """
        This will get the JSON API and return it as a dictionary.
        """
        if not self.data:
            return self._get()
        else:
            return self.data

    def _get(self):
        """
        Override this method when inheriting.
        This will get the JSON API and return it as a dictionary.
        """
        pass

    def flush(self):
        """
        Clears the local data stored so that the next request doesn't default to the local cache and instead grabs it
        from the LoginRadius servers.
        """
        self.data = None

    def set_raw(self, state):
        """
        Change the state of the raw parameter to determine what data set is grabbed from the provider.
        """
        if isinstance(state, bool):
            self.raw = state
        else:
            raise TypeError

    def __repr__(self):
        """
        General explanation of what type of object for debugging.
        """
        return "LoginRadius LazyLoad Object"

    def __getitem__(self, item):
        """
        Get item from the dictionary.
        """
        self._check()
        return self.data[item]

    def __setitem__(self, key, value):
        """
        Allow the user to set the items in the dictionary as well.
        """
        self._check()
        self.data[key] = value

    def _check(self):
        """
        Simple check to see if we already got the data for this Lazy Load. If not, get it.
        """
        if not self.data:
            self.data = self.get()


class UserProfileLazyLoad(LazyLoad):
    def __init__(self, lr_object, raw=False):
        super(UserProfileLazyLoad, self).__init__(lr_object, raw=raw)

    def _get(self):
        if not self.raw:
            return self._lr_object.api.get_user_profile()
        else:
            return self._lr_object.api.get_user_profile_raw()


class PhotoLazyLoad(LazyLoad):
    def __init__(self, lr_object, raw=False, album_id=''):
        self.album_id = album_id
        super(PhotoLazyLoad, self).__init__(lr_object, raw=raw)

    def _get(self):
        if not self.raw:
            return self._lr_object.api.get_photo(album_id=self.album_id)
        else:
            return self._lr_object.api.get_photo_raw(album_id=self.album_id)


class CheckInLazyLoad(LazyLoad):
    def __init__(self, lr_object, raw=False):
        super(CheckInLazyLoad, self).__init__(lr_object, raw=raw)

    def _get(self):
        if not self.raw:
            return self._lr_object.api.get_checkin()
        else:
            return self._lr_object.api.get_checkin_raw()


class AlbumLazyLoad(LazyLoad):
    def __init__(self, lr_object, raw=False):
        super(AlbumLazyLoad, self).__init__(lr_object, raw=raw)

    def _get(self):
        if not self.raw:
            return self._lr_object.api.get_album()
        else:
            return self._lr_object.api.get_album_raw()


class AudioLazyLoad(LazyLoad):
    def __init__(self, lr_object, raw=False):
        super(AudioLazyLoad, self).__init__(lr_object, raw=raw)

    def _get(self):
        if not self.raw:
            return self._lr_object.api.get_audio()
        else:
            return self._lr_object.api.get_audio_raw()


class VideoLazyLoad(LazyLoad):
    def __init__(self, lr_object, raw=False):
        super(VideoLazyLoad, self).__init__(lr_object, raw=raw)

    def _get(self):
        if not self.raw:
            return self._lr_object.api.get_video()
        else:
            return self._lr_object.api.get_video_raw()


class ContactsLazyLoad(LazyLoad):
    def __init__(self, lr_object, raw=False, next_cursor=''):
        self.next_cursor = next_cursor
        super(ContactsLazyLoad, self).__init__(lr_object, raw=raw)

    def _get(self):
        if not self.raw:
            return self._lr_object.api.get_contacts(next_cursor=self.next_cursor)
        else:
            return self._lr_object.api.get_contacts_raw(next_cursor=self.next_cursor)


class StatusLazyLoad(LazyLoad):
    def __init__(self, lr_object, raw=False):
        super(StatusLazyLoad, self).__init__(lr_object, raw=raw)

    def _get(self):
        if not self.raw:
            return self._lr_object.api.get_status()
        else:
            return self._lr_object.api.get_status_raw()


class GroupLazyLoad(LazyLoad):
    def __init__(self, lr_object, raw=False):
        super(GroupLazyLoad, self).__init__(lr_object, raw=raw)

    def _get(self):
        if not self.raw:
            return self._lr_object.api.get_group()
        else:
            return self._lr_object.api.get_group_raw()


class PostLazyLoad(LazyLoad):
    def __init__(self, lr_object, raw=False):
        super(PostLazyLoad, self).__init__(lr_object, raw=raw)

    def _get(self):
        if not self.raw:
            return self._lr_object.api.get_post()
        else:
            return self._lr_object.api.get_post_raw()


class EventLazyLoad(LazyLoad):
    def __init__(self, lr_object, raw=False):
        super(EventLazyLoad, self).__init__(lr_object, raw=raw)

    def _get(self):
        if not self.raw:
            return self._lr_object.api.get_event()
        else:
            return self._lr_object.api.get_event_raw()


class MentionLazyLoad(LazyLoad):
    def __init__(self, lr_object, raw=False):
        super(MentionLazyLoad, self).__init__(lr_object, raw=raw)

    def _get(self):
        if not self.raw:
            return self._lr_object.api.get_mention()
        else:
            return self._lr_object.api.get_mention_raw()


class CompanyLazyLoad(LazyLoad):
    def __init__(self, lr_object, raw=False):
        super(CompanyLazyLoad, self).__init__(lr_object, raw=raw)

    def _get(self):
        if not self.raw:
            return self._lr_object.api.get_company()
        else:
            return self._lr_object.api.get_company_raw()


class FollowingLazyLoad(LazyLoad):
    def __init__(self, lr_object, raw=False):
        super(FollowingLazyLoad, self).__init__(lr_object, raw=raw)

    def _get(self):
        if not self.raw:
            return self._lr_object.api.get_following()
        else:
            return self._lr_object.api.get_following_raw()


class ActivityLazyLoad(LazyLoad):
    def __init__(self, lr_object, raw=False):
        super(ActivityLazyLoad, self).__init__(lr_object, raw=raw)

    def _get(self):
        if not self.raw:
            return self._lr_object.api.get_activity()
        else:
            return self._lr_object.api.get_activity_raw()


class PageLazyLoad(LazyLoad):
    def __init__(self, lr_object, page_name='', raw=False):
        self.page_name = page_name
        super(PageLazyLoad, self).__init__(lr_object, raw=raw)

    def _get(self):
        if not self.raw:
            return self._lr_object.api.get_page(self.page_name)
        else:
            return self._lr_object.api.get_page_raw(self.page_name)


class LikeLazyLoad(LazyLoad):
    def __init__(self, lr_object, raw=False):
        super(LikeLazyLoad, self).__init__(lr_object, raw=raw)

    def _get(self):
        if not self.raw:
            return self._lr_object.api.get_like()
        else:
            return self._lr_object.api.get_like_raw()


class LoginRadiusExceptions(Exception):
    """
    This is the base for all LoginRadius Exceptions. Makes dealing with exceptions easy!
    """

    def __init__(self):
        pass

    def __str__(self):
        return ""


class Exceptions:
    """
    Common exceptions used by LoginRadius.
    """

    def __init__(self):
        pass

    class RequestsLibraryDated(LoginRadiusExceptions):
        """
        Raise exception if module requests is outdated.
        By default 0.12 is included in Python. We need at least version 2.0
        """

        def __init__(self, version):
            self.version = str(version)

        def __str__(self):
            return "LoginRadius needs at least requests 2.0, found: " \
                   + self.version + "\nPlease upgrade to the latest version."

    class InvalidLibrary(LoginRadiusExceptions):
        """
        Raised on trying to change library to through _settings on invalid library argument.
        """

        def __init__(self, library):
            self.library = library

        def __str__(self):
            return "Invalid library string given. Got: " + str(self.library) + ". Valid cases: 'requests' or " + \
                "'urllib2'"

    class NoAPISecret(LoginRadiusExceptions):
        """
        Raised on construction of the LoginRadius object,
        if no API_SECRET has been set for the class.
        """

        def __init__(self, version):
            self.version = str(version)

        def __str__(self):
            return "No API_SECRET set. Please initialize a API_SECRET first.\n" \
                   + "ie. LoginRadius.API_SECRET = \"Really_Secret_Key\""

    class MissingJsonResponseParameter(LoginRadiusExceptions):
        """
        Raised if construction of namedtuple would fail
        because missing expected response from LoginRadius API.
        """

        def __init__(self, missing_parameter, raw=None):
            self.missing_parameter = missing_parameter
            self.raw = raw

        def __str__(self):
            exception_string = "Expected parameter from JSON response does not exist." + \
                " Expected: " + self.missing_parameter + " but was not in" + \
                " the dictionary."
            if self.raw:
                exception_string += " Instead, we got: " + str(self.raw)
                return exception_string

    class TokenExpired(LoginRadiusExceptions):
        """
        Raised if the request cannot be completed because the access token has expired.
        """
        def __init__(self, time):
            self.time = time

        def __str__(self):
            return "The request cannot be completed because the token has expired. " + \
                "The token expired on: " + self.time

    class FeatureNotSupported(LoginRadiusExceptions):
        """
        Raised if the request cannot be completed because your account/API access does not include this.
        """
        def __init__(self):
            pass

        def __str__(self):
            return "Your LoginRadius site doesn't have permission to access this endpoint, please contact " +\
                   "LoginRadius support if you need more information."

    class UnknownJsonError(LoginRadiusExceptions):
        """
        Raised if cannot determine error number from Json
        """
        def __init__(self, result):
            self.result = result

        def __str__(self):
            return "The request cannot be completed because LoginRadius raised an unknown error in the API request." + \
                   " More information can be found in the error attribute or in this raw data: " + str(self.result)

    class APIKeyInvalid(LoginRadiusExceptions):
        """
        Raised if you entered your API wrong, or not at all.
        """
        def __init__(self):
            pass

        def __str__(self):
            return "The LoginRadius API Key is not valid, please double check your account."

    class APISecretInvalid(LoginRadiusExceptions):
        """
        Raised if you your API Secret is invalid.
        """
        def __init__(self):
            pass

        def __str__(self):
            return "The LoginRadius API Secret is not valid, please double check your account."

    class InvalidRequestToken(LoginRadiusExceptions):
        """
        Raised if you your request token is invalid from the POST request.
        """
        def __init__(self):
            pass

        def __str__(self):
            return "The LoginRadius Request Token is invalid, please verify the authentication response."

    class RequestTokenExpired(LoginRadiusExceptions):
        """
        Raised if you your request token has expired from the POST request.
        """
        def __init__(self):
            pass

        def __str__(self):
            return "The LoginRadius Request Token has expired, please verify the authentication response."

    class InvalidAccessToken(LoginRadiusExceptions):
        """
        Raised if you access token is invalid.
        """
        def __init__(self):
            pass

        def __str__(self):
            return "The LoginRadius Access Token has expired, please get a new token from the LoginRadius API."

    class ParameterMissing(LoginRadiusExceptions):
        """
        Raised if a parameter in the GET or POST request is missing.
        """
        def __init__(self):
            pass

        def __str__(self):
            return "A parameter is missing in the request, please check all parameters in the API call."

    class ParameterNotFormatted(LoginRadiusExceptions):
        """
        Raised if a parameter in the GET or POST request is not formatted properly for the provider.
        """
        def __init__(self):
            pass

        def __str__(self):
            return "A parameter is not formatted well in the request, please check all the parameters in the API call."

    class EndPointNotSupported(LoginRadiusExceptions):
        """
        Raised if a the endpoint is not supported by the provider which correlates to the token.
        """
        def __init__(self):
            pass

        def __str__(self):
            return "The requested endpoint is not supported by the current ID provider, " + \
                   "please check the API support page at http://www.loginradius.com/datapoints"
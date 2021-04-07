LoginRadius offers a complete social infrastructure solution combining 30 major social platforms into one unified API.
With LoginRadius, websites and mobile apps can integrate social login, enable social sharing, capture user profiles and
social data, create a single sign-on experience for their users, and get comprehensive social analytics.
Our social solution helps websites engage, understand, and leverage their users.

This module provides a wrapper for urllib2 or the requests library to easily access the API from
https://docs.loginradius.com/ in a more "pythonic" way. Providing easier access to essential data in a few lines of code.
This will work with 2.0 API specifications.

For more information, visit: http://loginradius.com/

Prerequisites
========

You will need at least Python - 2.7 or greater. LoginRadius module utilizes the namedtuple from the collections library
and the import_module from importlib.

From Package
=========

Using pip

```
 pip install loginradius-v2==11.1.0
```

or with easy_install

```
 easy_install loginradius-v2==11.1.0
```

Changelog
======

11.1.0
-----------
Release on **March 23,2021**

## Enhancements:
 - Added X-Origin-IP header support.
 - Added 429 error code handling for "Too Many Request in a particular time frame".
 - urllib3 support
 - Fixed Delete API issue

## Added new multiple APIs for better user experience:
 - Get Profile By Ping.
 - Passwordless Login Verification By Email And OTP.
 - Passwordless Login Verification By User Name And OTP.


11.0.0
-----------
Release on **July 24,2020**

## Enhancements:
- Added a parameter isWeb in "RefreshAccessToken" API.
- Added a parameter SocialAppName in "getAccessTokenByFacebookAccessToken,  getAccessTokenByTwitterAccessToken,
  getAccessTokenByGoogleAccessToken, getAccessTokenByLinkedinAccessToken, getAccessTokenByAppleIdCode, 
  getAccessTokenByGoogleAuthCode" Native Social login APIs.

## Added new multiple APIs for better user experience:
- Added linkSocialIdentites(POST) API.
- Added linkSocialIdentitiesByPing(POST) API.
- Added getAccessTokenByAppleIdCode API.
- Added getAccessTokenByWeChatCode API.

## Removed APIs:
 - linkSocialIdentity API(PUT)
 - getSocialIdentity API(GET)

10.0.1
-----------
Release on **October 10,2019**

### Enhancements
This full version release includes major breaking changes with several improvements and optimizations :

 - Enhanced the coding standards of SDK to follow industry programming styles and best practices.
 - Enhanced security standards of SDK.
 - Reduced code between the business layer and persistence layer for optimization of SDK performance.
 - Added internal parameter validations in the API function.
 - ApiKey and ApiSecret usage redundancy removed.
 - All LoginRadius related features need to be defined once only and SDK will handle them automatically.
 - Improved the naming conventions of API functions for better readability.
 - Better Exception Handling for LoginRadius API Response in SDK.
 - Revamped complete SDK and restructured it with latest API function names and parameters.
 - Added detailed description to API functions and parameters for better understanding.
 - Updated the demo according to latest SDK changes.
 - Implemented API Region Feature.
 - Added PIN Authentication feature APIs.
 - Added Consent Management feature APIs.
 - Added Local SOTT generation


### Added new multiple APIs for better user experience

 - Update Phone ID by UID
 - Upsert Email
 - Role Context profile
 - MFA Resend OTP
 - User Registration By Captcha
 - Get Access Token via Linkedin Token
 - Get Access Token By Foursquare Access Token
 - Get Active Session By Account Id
 - Get Active Session By Profile Id
 - Delete User Profiles By Email
 - Verify Multifactor OTP Authentication
 - Verify Multifactor Password Authentication
 - Verify Multifactor PIN Authentication
 - Update UID
 - MFA Re-authentication by PIN
 - PIN Login
 - Forgot PIN By Email
 - Forgot PIN By UserName
 - Reset PIN By ResetToken
 - Reset PIN By SecurityAnswer And Email
 - Reset PIN By SecurityAnswer And Username
 - Reset PIN By SecurityAnswer And Phone
 - Forgot PIN By Phone
 - Change PIN By Token
 - Reset PIN by Phone and OTP
 - Reset PIN by Email and OTP
 - Reset PIN by Username and OTP
 - Set PIN By PinAuthToken
 - Invalidate PIN Session Token
 - Submit Consent By ConsentToken
 - Get Consent Logs
 - Submit Consent By AccessToken
 - Verify Consent By AccessToken
 - Update Consent Profile By AccessToken
 - Get Consent Logs By Uid
 - Album With Cursor
 - Audio With Cursor
 - Check In With Cursor
 - Event With Cursor
 - Following With Cursor
 - Group With Cursor
 - Like With Cursor


### Removed APIs:

 - GetCompanies API
 - Getstatus API


10.0.0-beta
-----------
### This beta version release includes major changes with several improvements and optimizations :
  - Enhanced the coding standards of SDK to follow industry programming styles and best practices.
  - Enhanced security standards of SDK.
  - Reduced code between the business layer and persistence layer for optimization of SDK performance.
  - Added internal parameter validations in the API function
  - ApiKey and ApiSecret usage redundancy removed
  - All LoginRadius related features need to be defined once only and SDK will handle them automatically
  - Improved the naming conventions of API functions for better readability.
  - Better Error and Exception Handling for LoginRadius API Response in SDK
  - Revamped complete SDK and restructured it with latest API function names and parameters
  - Added detailed description to API functions and parameters for better understanding
  - Updated the demo according to latest SDK changes
  - Implemented API Region Feature

### Added new multiple APIs for better user experience
  - Update Phone ID by UID
  - Upsert Email
  - Role Context profile
  - MFA Resend OTP
  - User Registration By Captcha
  - Get Access Token via Linkedin Token
  - Get Access Token By Foursquare Access Token
  - Get Active Session By Account Id
  - Get Active Session By Profile Id

### Removed APIs:
  - GetCompanies API

3.2.0
-----

### Enhancements

-   Updated demo with new UI and features.
-   Unit tests.
-   Bug fixes.
-   New V2 API's:
    -   Auth Privacy Policy Accept
    -   Auth Send Welcome Email
    -   Auth Verify Email by OTP
    -   Auth Delete Account
    -   Account Email Delete
    -   Phone Login Using OTP
    -   Phone Send OTP
    -   Remove Phone ID by Access Token
    -   2FA Validate Google Auth Code
    -   2FA Validate OTP
    -   Validate Backup Code
    -   Update MFA by Access Token
    -   Update MFA Setting
    -   One Touch Verify OTP by Email
    -   Get Active Session Details
    -   Access Token via Vkontakte Token
    -   Access Token via Google Token
    -   Refresh User Profile
    -   Refresh Token
    -   Delete All Records by Datasource

### Breaking Changes

-   Replaced deprecated  [pycrypto package](https://pypi.org/project/pycrypto/)  with  [cryptography package](https://pypi.org/project/cryptography/)  for SOTT generation
-   Updated some existing API's:
    -   Get Roles by UID: moved to role class
    -   Assign Roles by UID: moved role class
    -   One Touch Login: moved to authentication.login class
    -   Get Backup Code by Access Token: moved to authentication.TwoFactor class
    -   Reset Backup Code by Access Token: moved to authentication.TwoFactor class
    -   Get Backup Code by UID: moved to account.TwoFactor class
    -   Reset Backup Code by UID: moved to account.TwoFactor class
	
	
3.0.1
-----

* Added Readme and History file

3.0.0
-----

* Added Latest V2 APIs.
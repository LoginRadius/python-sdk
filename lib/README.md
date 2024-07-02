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
 pip install loginradius-v2==11.6.0
```

or with easy_install

```
 easy_install loginradius-v2==11.6.0
```

Changelog
======


# Version 11.6.0

Release on **July 02, 2024**

## Added following APIs:
- `MFAValidateAuthenticatorCode`
- `MFAVerifyAuthenticatorCode`
- `RevokeAllRefreshToken `
- `MultipurposeEmailTokenGeneration`
- `MultipurposeSMSOTPGeneration`
- `MFAReAuthenticateByAuthenticatorCode`
- `AuthSendVerificationEmailForLinkingSocialProfiles `
- `SlidingAccessToken`
- `AccessTokenViaCustomJWTToken`
- `MFAResetAuthenticatorByToken`
- `MFAResetAuthenticatorByUid`

## Enhancements
- Added `isVoiceOtp` parameter in `ResetPhoneIDVerificationByUid` API
- Added `isVoiceOtp` parameter in `MFAConfigureByAccessToken` API
- Added `isVoiceOtp` and `options` parameter in `MFAUpdatePhoneNumberByToken` API
- Added `isVoiceOtp`, `emailTemplate2FA` and `options` parameter in `MFALoginByEmail` API
- Added `isVoiceOtp` and `emailTemplate2FA` parameter in `MFALoginByUserName` API
- Added `isVoiceOtp` , `emailTemplate2FA` and `options` parameter in `MFALoginByPhone` API
- Added `isVoiceOtp` and `options` parameter in `MFAUpdatePhoneNumber` API
- Added `isVoiceOtp` parameter in `MFAResendOTP` API
- Added `isVoiceOtp` parameter in `MFAReAuthenticate` API
- Added `isVoiceOtp` and `options` parameter in `UpdateProfileByAccessToken` API
- Added `isVoiceOtp` parameter in `UserRegistrationByEmail` API
- Added `isVoiceOtp` parameter in `UserRegistrationByCaptcha` API
- Added `isVoiceOtp` parameter in `OneTouchLoginByPhone` API
- Added `isVoiceOtp` parameter in `PasswordlessLoginPhoneVerification` API
- Added `isVoiceOtp` parameter in `PasswordlessLoginByPhone` API
- Added `isVoiceOtp` parameter in `ForgotPasswordByPhoneOTP` API
- Added `isVoiceOtp` parameter in `PhoneVerificationByOTP` API
- Added `isVoiceOtp` parameter in `PhoneVerificationOTPByAccessToken` API
- Added `isVoiceOtp` parameter in `PhoneResendVerificationOTP` API
- Added `isVoiceOtp` parameter in `UpdatePhoneNumber` API
- Added `isVoiceOtp` and `emailTemplate` parameter in `UserRegistrationByPhone` API
- Added `isVoiceOtp` parameter in `SendForgotPINSMSByPhone` API
- Added `uuid` parameter in `VerifyEmail` API

## Removed the following parameter

-`smsTemplate2FA` parameter in `MFAConfigureByAccessToken` API



## Removed (Deprecated) APIs:
- `MFAValidateGoogleAuthCode`
- `MFAReAuthenticateByGoogleAuth`
- `MFAResetGoogleAuthByToken `
- `MFAResetGoogleAuthenticatorByUid`
- `MFAUpdateByAccessToken`

11.5.0
-----------
Release on **January 20, 2023**

## Enhancements

- Added `email_template` parameter in `user_registration_by_phone` Api

## Removed (Deprecated) APIs:
- `auth_get_registration_data`
- `validate_registration_data_code`
- `get_registration_data`
- `add_registration_data`
- `update_registration_data`
- `delete_registration_data`
- `delete_all_records_by_data_source`
- `get_access_token_by_vkontakte_access_token`
- `get_albums`
- `get_albums_with_cursor`
- `get_audios`
- `get_audios_with_cursor`
- `get_check_ins`
- `get_check_ins_with_cursor`
- `get_contacts`
- `get_events`
- `get_events_with_cursor`
- `get_followings`
- `get_followings_with_cursor`
- `get_groups`
- `get_groups_with_cursor`
- `get_likes`
- `get_likes_with_cursor`
- `get_mentions`
- `post_message`
- `get_page`
- `get_photos`
- `get_posts`
- `status_posting`
- `trackable_status_posting`
- `get_trackable_status_stats`
- `trackable_status_fetching`
- `get_videos`
- `get_refreshed_social_user_profile`



11.4.0
-----------
Release on **June 3, 2022**
## Enhancements

- Added additional parameter `startTime` and `endTime`  in LoginRadius manual SOTT generation method `get_sott()`.
- Enhancement in `README.md` file.
- Code optimization for better performance.


11.3.0
-----------
Release on **January 31, 2022**
## Enhancements

- Added a feature to add ApiKey and ApiSecret directly in LoginRadius manual SOTT generation method.
- Code optimization for better performance.
- Added Licence and Contribution Guideline files.

## Breaking Changes

For developers migrating from v11.2.0, there will be 1 minor breaking change in terms of SDK implementation. In this version, we have added a feature to add ApiKey & ApiSecret directly into the manual SOTT generation method `get_sott()`.

11.2.0
-----------
Release on **September 15, 2021**

## Enhancements

- Updated Jquery with latest version(3.6.0) in SDK Demo


## Added new multiple APIs for better user experience

- MFAEmailOtpByAccessToken
- MFAValidateEmailOtpByAccessToken
- MFAResetEmailOtpAuthenticatorByAccessToken
- MFASecurityQuestionAnswerByAccessToken
- MFAResetSecurityQuestionAuthenticatorByAccessToken
- MFAEmailOTP
- MFAValidateEmailOtp
- MFASecurityQuestionAnswer
- MFASecurityQuestionAnswerVerification
- MFAResetEmailOtpAuthenticatorByUid
- MFAResetSecurityQuestionAuthenticatorByUid
- ReAuthValidateEmailOtp
- ReAuthSendEmailOtp
- ReAuthBySecurityQuestion
- 
## Removed (Deprecated) API:
- GetSocialUserProfile

Added `EmailTemplate2FA` parameter in the following API

- MFALoginByEmail
- MFALoginByUserName
- MFALoginByPhone


Added `RbaBrowserEmailTemplate`, `RbaCityEmailTemplate` ,`RbaCountryEmailTemplate` , `RbaIpEmailTemplate` parameter in the following API

- MFAValidateOTPByPhone
- MFAValidateGoogleAuthCode
- MFAValidateBackupCode

Added `emailTemplate`, `verificationUrl` ,`welcomeEmailTemplate`  parameter in the following API

- GetProfileByAccessToken

#### Removed `smsTemplate2FA ` parameter from the following API 
- mfaValidateGoogleAuthCode


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

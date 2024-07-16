# LoginRadius Python SDK Change Log

# Version 11.6.0

Release on **July 16, 2024**

## Added following APIs:
- `mfa_validate_authenticator_code`
- `mfa_verify_authenticator_code`
- `revoke_all_refresh_token `
- `multipurpose_email_token_generation`
- `multipurpose_sms_otp_generation`
- `mfa_re_authenticate_by_authenticator_code`
- `auth_send_verification_email_for_linking_social_profiles `
- `sliding_access_token`
- `access_token_via_custom_j_w_t_token`
- `mfa_reset_authenticator_by_token`
- `mfa_reset_authenticator_by_uid`

## Enhancements
- Added `is_voice_otp` parameter in `reset_phone_id_verification_by_uid` API
- Added `is_voice_otp` parameter in `mfa_configure_by_access_token` API
- Added `is_voice_otp` and `options` parameter in `mfa_update_phone_number_by_token` API
- Added `is_voice_otp`, `email_template2_f_a` and `options` parameter in `mfa_login_by_email` API
- Added `is_voice_otp` and `email_template2_f_a` parameter in `mfa_login_by_user_name` API
- Added `is_voice_otp` , `email_template2_f_a` and `options` parameter in `mfa_login_by_phone` API
- Added `is_voice_otp` and `options` parameter in `mfa_update_phone_number` API
- Added `is_voice_otp` parameter in `mfa_resend_otp` API
- Added `is_voice_otp` parameter in `mfa_re_authenticate` API
- Added `is_voice_otp` and `options` parameter in `update_profile_by_access_token` API
- Added `is_voice_otp` parameter in `user_registration_by_email` API
- Added `is_voice_otp` parameter in `user_registration_by_captcha` API
- Added `is_voice_otp` parameter in `one_touch_login_by_phone` API
- Added `is_voice_otp` parameter in `passwordless_login_phone_verification` API
- Added `is_voice_otp` parameter in `passwordless_login_by_phone` API
- Added `is_voice_otp` parameter in `forgot_password_by_phone_otp` API
- Added `is_voice_otp` parameter in `phone_verification_by_otp` API
- Added `is_voice_otp` parameter in `phone_verification_otp_by_access_token` API
- Added `is_voice_otp` parameter in `phone_resend_verification_otp` API
- Added `is_voice_otp` parameter in `update_phone_number` API
- Added `is_voice_otp` and `email_template` parameter in `user_registration_by_phone` API
- Added `is_voice_otp` parameter in `send_forgot_pin_sms_by_phone` API
- Added `uuid` parameter in `verify_email` API

## Removed the following parameter

-`sms_template` parameter in `mfa_configure_by_access_token` API



## Removed (Deprecated) APIs:
- `mfa_validate_google_auth_code`
- `mfa_re_authenticate_by_google_auth`
- `mfa_reset_google_auth_by_token `
- `mfa_reset_google_authenticator_by_uid`
- `mfa_update_by_access_token`

# Version 11.5.0

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


# Version 11.4.0

## Enhancements

- Added additional parameter `startTime` and `endTime`  in LoginRadius manual SOTT generation method `get_sott()`.
- Enhancement in `README.md` file.
- Code optimization for better performance.


# Version 11.3.0

## Enhancements

- Added a feature to add ApiKey and ApiSecret directly in LoginRadius manual SOTT generation method.
- Code optimization for better performance.
- Added Licence and Contribution Guideline files.

## Breaking Changes

For developers migrating from v11.2.0, there will be 1 minor breaking change in terms of SDK implementation. In this version, we have added a feature to add ApiKey & ApiSecret directly into the manual SOTT generation method `get_sott()`.

# Version 11.2.0

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

# Version 11.1.0

## Enhancements:
 - Added X-Origin-IP header support.
 - Added 429 error code handling for "Too Many Request in a particular time frame".
 - urllib3 support
 - Fixed Delete API issue

## Added new multiple APIs for better user experience:
 - Get Profile By Ping.
 - Passwordless Login Verification By Email And OTP.
 - Passwordless Login Verification By User Name And OTP.



# Version 11.0.0

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

# Version 10.0.0
## This full version release includes major changes with several improvements and optimizations :
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
  - Added Consent Management feature
  - Added PIN Authentication feature 

# Version 10.0.0-beta
## This beta version release includes major changes with several improvements and optimizations :
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

## Added new multiple APIs for better user experience
  - Update Phone ID by UID
  - Upsert Email
  - Role Context profile
  - MFA Resend OTP
  - User Registration By Captcha
  - Get Access Token via Linkedin Token
  - Get Access Token By Foursquare Access Token
  - Get Active Session By Account Id
  - Get Active Session By Profile Id

## Removed APIs:
  - GetCompanies API

# Version 3.3.1
## Bug Fixed
  - Handling Exception for NoAPIKey and NoSecretKey
  - Fixed some bugs and standardised SDK

# Version 3.3.0
## Enhancements
  - Enabled Support for gzip compression

# Version 3.2.0
## Enhancements
  - Updated demo with new UI and features.
  - Unit tests.
  - Bug fixes.
  - New V2 API's:     
      - Auth Privacy Policy Accept   
      - Auth Send Welcome Email   
      - Auth Verify Email by OTP    
      - Auth Delete Account    
      - Account Email Delete    
      - Phone Login Using OTP   
      - Phone Send OTP   
      - Remove Phone ID by Access Token   
      - 2FA Validate Google Auth Code   
      - 2FA Validate OTP   
      - Validate Backup Code   
      - Update MFA by Access Token   
      - Update MFA Setting   
      - One Touch Verify OTP by Email   
      - Get Active Session Details   
      - Access Token via Vkontakte Token   
      - Access Token via Google Token   
      - Refresh User Profile   
      - Refresh Token   
      - Delete All Records by Datasource   

###Breaking Changes
  - Replaced deprecated [pycrypto package](https://pypi.org/project/pycrypto/) with [cryptography package](https://pypi.org/project/cryptography/) for SOTT generation
  - Updated some existing API's:    
      - Get Roles by UID: moved to role class    
      - Assign Roles by UID: moved role class    
      - One Touch Login: moved to authentication.login class   
      - Get Backup Code by Access Token: moved to authentication.TwoFactor class   
      - Reset Backup Code by Access Token: moved to authentication.TwoFactor class   
      - Get Backup Code by UID: moved to account.TwoFactor class   
      - Reset Backup Code by UID: moved to account.TwoFactor class

# Version 3.1.1
## Bug Fixed
  - Fixed HTTP method request bug.

# Version 3.1.0
## Enhancements
  - Passed API key and Secret key in herader for management API's.
  - Passed SOTT In header.
  - Added Management API to generate a SOTT.
  - Implemented ability to support proxy server.
  - Supported NULL and projection in fields.
  - Added new V2 API's.

# Version 3.0
## Enhancements
  - Added Latest V2 APIs.
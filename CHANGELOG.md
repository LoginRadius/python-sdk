# LoginRadius Python SDK Change Log

# Version 11.0.0
Released on **August 11,2020**
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

# Version 10.0.1
Released on **Oct 24,2019**
## Enhancements
  - Fixed the pip installation issue

# Version 10.0.0
Released on **September 30,2019**

## Enhancements
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


## Removed APIs:

 - GetCompanies API
 - Getstatus API

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

### Breaking Changes
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
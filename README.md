# Python-SDK

Customer Identity public repo for Python SDK, based on LoginRadius V2 APIs.

![Home Image](http://docs.lrcontent.com/resources/github/banner-1544x500.png)


## Introduction ##

LoginRadius Python SDK Customer Registration wrapper provides access to LoginRadius Identity Management Platform API.

This SDK provides a wrapper for urllib2 or the requests library to easily access the API from
https://www.loginradius.com/docs/ in a more "pythonic" way. Providing easier access to essential data in a few lines of code.
This will work with 2.0 API specifications.

LoginRadius is an Identity Management Platform that simplifies user registration while securing data. LoginRadius Platform simplifies and secures your user registration process, increases conversion with Social Login that combines 30 major social platforms, and offers a full solution with Traditional User Registration. You can gather a wealth of user profile data from Social Login or Traditional User Registration.

## Documentation

-------
>Disclaimer:<br>
This library is meant to help you with a quick implementation of the LoginRadius platform and also to serve as a reference point for the LoginRadius API. Keep in mind that it is an open source library, which means you are free to download and customize the library functions based on your specific application needs.


### Prerequisites
You will need at least Python - 2.7 or greater. LoginRadius module utilizes the [namedtuple](https://docs.python.org/2/library/collections.html#collections.namedtuple) from the collections library and the [import_module](https://docs.python.org/2/library/importlib.html) from importlib.

### Install From Package
Using pip

```
 pip install loginradius-v2==11.2.0
```

or with easy_install

```
 easy_install loginradius-v2==11.2.0
```

### Install From Source
You can download the latest version from PyPI

- Unzip/untar the files.
- Browse to the directory that you extracted the files to.
- Run ```python setup.py install``` to install the LoginRadius module.


## Initialize SDK
Import the class

```
 from LoginRadius import LoginRadius as LR
```
When you initialize your application, you will need to set your API Key and  Secret. This can be found in your [here](https://www.loginradius.com/docs/api/v2/admin-console/platform-security/api-key-and-secret).

When your Python application initializes, set your API Key and Secret

```
 LR.API_KEY = "<API-KEY>"
 LR.API_SECRET = "<API-SECRET>"
 loginradius = LR()
```

### Custom Domain
When initializing the SDK, optionally specify a custom domain.

```
LR.CUSTOM_DOMAIN = "<CUSTOM-DOMAIN>"
```

### API Request Signing
To enable API request signing, set the value of 'API_REQUEST_SIGNING' to True

```
LR.API_REQUEST_SIGNING = True
```
### X-Origin-IP
LoginRadius allows you to add X-Origin-IP in your headers and it determines the IP address of the client's request,this can also be useful to overcome analytics discrepancies where the analytics depend on header data.

```
LR.ORIGIN_IP = "<Client-Ip-Address>"
```

### Authentication API


List of APIs in this Section:<br>

* PUT : [Auth Update Profile by Token](#UpdateProfileByAccessToken-put-)<br>
* PUT : [Auth Unlock Account by Access Token](#UnlockAccountByToken-put-)<br>
* PUT : [Auth Verify Email By OTP](#VerifyEmailByOTP-put-)<br>
* PUT : [Auth Reset Password by Security Answer and Email](#ResetPasswordBySecurityAnswerAndEmail-put-)<br>
* PUT : [Auth Reset Password by Security Answer and Phone](#ResetPasswordBySecurityAnswerAndPhone-put-)<br>
* PUT : [Auth Reset Password by Security Answer and UserName](#ResetPasswordBySecurityAnswerAndUserName-put-)<br>
* PUT : [Auth Reset Password by Reset Token](#ResetPasswordByResetToken-put-)<br>
* PUT : [Auth Reset Password by OTP](#ResetPasswordByEmailOTP-put-)<br>
* PUT : [Auth Reset Password by OTP and UserName](#ResetPasswordByOTPAndUserName-put-)<br>
* PUT : [Auth Change Password](#ChangePassword-put-)<br>
* PUT : [Auth Set or Change UserName](#SetOrChangeUserName-put-)<br>
* PUT : [Auth Resend Email Verification](#AuthResendEmailVerification-put-)<br>
* POST : [Auth Add Email](#AddEmail-post-)<br>
* POST : [Auth Login by Email](#LoginByEmail-post-)<br>
* POST : [Auth Login by Username](#LoginByUserName-post-)<br>
* POST : [Auth Forgot Password](#ForgotPassword-post-)<br>
* POST : [Auth Link Social Identities](#LinkSocialIdentities-post-)<br>
* POST : [Auth Link Social Identities By Ping](#LinkSocialIdentitiesByPing-post-)<br>
* POST : [Auth User Registration by Email](#UserRegistrationByEmail-post-)<br>
* POST : [Auth User Registration By Captcha](#UserRegistrationByCaptcha-post-)<br>
* GET : [Get Security Questions By Email](#GetSecurityQuestionsByEmail-get-)<br>
* GET : [Get Security Questions By UserName](#GetSecurityQuestionsByUserName-get-)<br>
* GET : [Get Security Questions By Phone](#GetSecurityQuestionsByPhone-get-)<br>
* GET : [Get Security Questions By Access Token](#GetSecurityQuestionsByAccessToken-get-)<br>
* GET : [Auth Validate Access token](#AuthValidateAccessToken-get-)<br>
* GET : [Access Token Invalidate](#AuthInValidateAccessToken-get-)<br>
* GET : [Access Token Info](#GetAccessTokenInfo-get-)<br>
* GET : [Auth Read all Profiles by Token](#GetProfileByAccessToken-get-)<br>
* GET : [Auth Send Welcome Email](#SendWelcomeEmail-get-)<br>
* GET : [Auth Delete Account](#DeleteAccountByDeleteToken-get-)<br>
* GET : [Get Profile By Ping](#GetProfileByPing-get-)<br>
* GET : [Auth Check Email Availability](#CheckEmailAvailability-get-)<br>
* GET : [Auth Verify Email](#VerifyEmail-get-)<br>
* GET : [Auth Check UserName Availability](#CheckUserNameAvailability-get-)<br>
* GET : [Auth Privacy Policy Accept](#AcceptPrivacyPolicy-get-)<br>
* GET : [Auth Privacy Policy History By Access Token](#GetPrivacyPolicyHistoryByAccessToken-get-)<br>
* DELETE : [Auth Delete Account with Email Confirmation](#DeleteAccountWithEmailConfirmation-delete-)<br>
* DELETE : [Auth Remove Email](#RemoveEmail-delete-)<br>
* DELETE : [Auth Unlink Social Identities](#UnlinkSocialIdentities-delete-)<br>




<h6 id="UpdateProfileByAccessToken-put-"> Auth Update Profile by Token (PUT)</h6>

 This API is used to update the user's profile by passing the access token.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-update-profile-by-token/)

 ```

access_token = "<access_token>" #Required
user_profile_update_model = {
"firstName" : "<firstName>",
"lastName" : "<lastName>"
}  #Required
email_template = "<email_template>" #Optional
fields = "<fields>" #Optional
null_support = "True" #Optional
sms_template = "<sms_template>" #Optional
verification_url = "<verification_url>" #Optional

result = loginradius.authentication.update_profile_by_access_token(access_token, user_profile_update_model, email_template, fields, null_support, sms_template, verification_url)
 ```




<h6 id="UnlockAccountByToken-put-"> Auth Unlock Account by Access Token (PUT)</h6>

 This API is used to allow a customer with a valid access token to unlock their account provided that they successfully pass the prompted Bot Protection challenges. The Block or Suspend block types are not applicable for this API. For additional details see our Auth Security Configuration documentation.You are only required to pass the Post Parameters that correspond to the prompted challenges.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-unlock-account-by-access-token/)

 ```

access_token = "<access_token>" #Required
unlock_profile_model = {
"g-recaptcha-response" : "<g-recaptcha-response>"
}  #Required

result = loginradius.authentication.unlock_account_by_token(access_token, unlock_profile_model)
 ```




<h6 id="VerifyEmailByOTP-put-"> Auth Verify Email By OTP (PUT)</h6>

 This API is used to verify the email of user when the OTP Email verification flow is enabled, please note that you must contact LoginRadius to have this feature enabled.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-verify-email-by-otp/)

 ```

email_verification_by_otp_model = {
"email" : "<email>",
"otp" : "<otp>"
}  #Required
fields = "<fields>" #Optional
url = "<url>" #Optional
welcome_email_template = "<welcome_email_template>" #Optional

result = loginradius.authentication.verify_email_by_otp(email_verification_by_otp_model, fields, url, welcome_email_template)
 ```




<h6 id="ResetPasswordBySecurityAnswerAndEmail-put-"> Auth Reset Password by Security Answer and Email (PUT)</h6>

 This API is used to reset password for the specified account by security question  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-reset-password-by-email)

 ```

reset_password_by_security_answer_and_email_model = {
"email" : "<email>",
"password" : "<password>",
"securityAnswer" : {"QuestionID":"Answer"}
}  #Required

result = loginradius.authentication.reset_password_by_security_answer_and_email(reset_password_by_security_answer_and_email_model)
 ```




<h6 id="ResetPasswordBySecurityAnswerAndPhone-put-"> Auth Reset Password by Security Answer and Phone (PUT)</h6>

 This API is used to reset password for the specified account by security question  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-reset-password-by-phone)

 ```

reset_password_by_security_answer_and_phone_model = {
"password" : "<password>",
"phone" : "<phone>",
"securityAnswer" : {"QuestionID":"Answer"}
}  #Required

result = loginradius.authentication.reset_password_by_security_answer_and_phone(reset_password_by_security_answer_and_phone_model)
 ```




<h6 id="ResetPasswordBySecurityAnswerAndUserName-put-"> Auth Reset Password by Security Answer and UserName (PUT)</h6>

 This API is used to reset password for the specified account by security question  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-reset-password-by-username)

 ```

reset_password_by_security_answer_and_user_name_model = {
"password" : "<password>",
"securityAnswer" : {"QuestionID":"Answer"},
"userName" : "<userName>"
}  #Required

result = loginradius.authentication.reset_password_by_security_answer_and_user_name(reset_password_by_security_answer_and_user_name_model)
 ```




<h6 id="ResetPasswordByResetToken-put-"> Auth Reset Password by Reset Token (PUT)</h6>

 This API is used to set a new password for the specified account.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-reset-password-by-reset-token)

 ```

reset_password_by_reset_token_model = {
"password" : "<password>",
"resetToken" : "<resetToken>"
}  #Required

result = loginradius.authentication.reset_password_by_reset_token(reset_password_by_reset_token_model)
 ```




<h6 id="ResetPasswordByEmailOTP-put-"> Auth Reset Password by OTP (PUT)</h6>

 This API is used to set a new password for the specified account.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-reset-password-by-otp)

 ```

reset_password_by_email_and_otp_model = {
"email" : "<email>",
"otp" : "<otp>",
"password" : "<password>"
}  #Required

result = loginradius.authentication.reset_password_by_email_otp(reset_password_by_email_and_otp_model)
 ```




<h6 id="ResetPasswordByOTPAndUserName-put-"> Auth Reset Password by OTP and UserName (PUT)</h6>

 This API is used to set a new password for the specified account if you are using the username as the unique identifier in your workflow  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-reset-password-by-otp-and-username/)

 ```

reset_password_by_user_name_model = {
"otp" : "<otp>",
"password" : "<password>",
"userName" : "<userName>"
}  #Required

result = loginradius.authentication.reset_password_by_otp_and_user_name(reset_password_by_user_name_model)
 ```




<h6 id="ChangePassword-put-"> Auth Change Password (PUT)</h6>

 This API is used to change the accounts password based on the previous password  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-change-password)

 ```

access_token = "<access_token>" #Required
new_password = "<new_password>" #Required
old_password = "<old_password>" #Required

result = loginradius.authentication.change_password(access_token, new_password, old_password)
 ```




<h6 id="SetOrChangeUserName-put-"> Auth Set or Change UserName (PUT)</h6>

 This API is used to set or change UserName by access token.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-set-or-change-user-name/)

 ```

access_token = "<access_token>" #Required
username = "<username>" #Required

result = loginradius.authentication.set_or_change_user_name(access_token, username)
 ```




<h6 id="AuthResendEmailVerification-put-"> Auth Resend Email Verification (PUT)</h6>

 This API resends the verification email to the user.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-resend-email-verification/)

 ```

email = "<email>" #Required
email_template = "<email_template>" #Optional
verification_url = "<verification_url>" #Optional

result = loginradius.authentication.auth_resend_email_verification(email, email_template, verification_url)
 ```




<h6 id="AddEmail-post-"> Auth Add Email (POST)</h6>

 This API is used to add additional emails to a user's account.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-add-email)

 ```

access_token = "<access_token>" #Required
email = "<email>" #Required
type = "<type>" #Required
email_template = "<email_template>" #Optional
verification_url = "<verification_url>" #Optional

result = loginradius.authentication.add_email(access_token, email, type, email_template, verification_url)
 ```




<h6 id="LoginByEmail-post-"> Auth Login by Email (POST)</h6>

 This API retrieves a copy of the user data based on the Email  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-login-by-email)

 ```

email_authentication_model = {
"email" : "<email>",
"password" : "<password>"
}  #Required
email_template = "<email_template>" #Optional
fields = "<fields>" #Optional
login_url = "<login_url>" #Optional
verification_url = "<verification_url>" #Optional

result = loginradius.authentication.login_by_email(email_authentication_model, email_template, fields, login_url, verification_url)
 ```




<h6 id="LoginByUserName-post-"> Auth Login by Username (POST)</h6>

 This API retrieves a copy of the user data based on the Username  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-login-by-username)

 ```

user_name_authentication_model = {
"password" : "<password>",
"username" : "<username>"
}  #Required
email_template = "<email_template>" #Optional
fields = "<fields>" #Optional
login_url = "<login_url>" #Optional
verification_url = "<verification_url>" #Optional

result = loginradius.authentication.login_by_user_name(user_name_authentication_model, email_template, fields, login_url, verification_url)
 ```




<h6 id="ForgotPassword-post-"> Auth Forgot Password (POST)</h6>

 This API is used to send the reset password url to a specified account. Note: If you have the UserName workflow enabled, you may replace the 'email' parameter with 'username'  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-forgot-password)

 ```

email = "<email>" #Required
reset_password_url = "<reset_password_url>" #Required
email_template = "<email_template>" #Optional

result = loginradius.authentication.forgot_password(email, reset_password_url, email_template)
 ```




<h6 id="LinkSocialIdentities-post-"> Auth Link Social Identities (POST)</h6>

 This API is used to link up a social provider account with an existing LoginRadius account on the basis of access token and the social providers user access token.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-link-social-identities)

 ```

access_token = "<access_token>" #Required
candidate_token = "<candidate_token>" #Required

result = loginradius.authentication.link_social_identities(access_token, candidate_token)
 ```




<h6 id="LinkSocialIdentitiesByPing-post-"> Auth Link Social Identities By Ping (POST)</h6>

 This API is used to link up a social provider account with an existing LoginRadius account on the basis of ping and the social providers user access token.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-link-social-identities-by-ping)

 ```

access_token = "<access_token>" #Required
client_guid = "<client_guid>" #Required

result = loginradius.authentication.link_social_identities_by_ping(access_token, client_guid)
 ```




<h6 id="UserRegistrationByEmail-post-"> Auth User Registration by Email (POST)</h6>

 This API creates a user in the database as well as sends a verification email to the user.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-user-registration-by-email)

 ```

auth_user_registration_model = {
"email" : [   {
 "type" : "<type>"  ,
 "value" : "<value>"   
}  ] ,
"firstName" : "<firstName>",
"lastName" : "<lastName>",
"password" : "<password>"
}  #Required
sott = "<sott>" #Required
email_template = "<email_template>" #Optional
fields = "<fields>" #Optional
options = "<options>" #Optional
verification_url = "<verification_url>" #Optional
welcome_email_template = "<welcome_email_template>" #Optional

result = loginradius.authentication.user_registration_by_email(auth_user_registration_model, sott, email_template, fields, options, verification_url, welcome_email_template)
 ```




<h6 id="UserRegistrationByCaptcha-post-"> Auth User Registration By Captcha (POST)</h6>

 This API creates a user in the database as well as sends a verification email to the user.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-user-registration-by-recaptcha)

 ```

auth_user_registration_model_with_captcha = {
"email" : [   {
 "type" : "<type>"  ,
 "value" : "<value>"   
}  ] ,
"firstName" : "<firstName>",
"g-recaptcha-response" : "<g-recaptcha-response>",
"lastName" : "<lastName>",
"password" : "<password>"
}  #Required
email_template = "<email_template>" #Optional
fields = "<fields>" #Optional
options = "<options>" #Optional
sms_template = "<sms_template>" #Optional
verification_url = "<verification_url>" #Optional
welcome_email_template = "<welcome_email_template>" #Optional

result = loginradius.authentication.user_registration_by_captcha(auth_user_registration_model_with_captcha, email_template, fields, options, sms_template, verification_url, welcome_email_template)
 ```




<h6 id="GetSecurityQuestionsByEmail-get-"> Get Security Questions By Email (GET)</h6>

 This API is used to retrieve the list of questions that are configured on the respective LoginRadius site.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/security-questions-by-email/)

 ```

email = "<email>" #Required

result = loginradius.authentication.get_security_questions_by_email(email)
 ```




<h6 id="GetSecurityQuestionsByUserName-get-"> Get Security Questions By UserName (GET)</h6>

 This API is used to retrieve the list of questions that are configured on the respective LoginRadius site.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/security-questions-by-user-name/)

 ```

user_name = "<user_name>" #Required

result = loginradius.authentication.get_security_questions_by_user_name(user_name)
 ```




<h6 id="GetSecurityQuestionsByPhone-get-"> Get Security Questions By Phone (GET)</h6>

 This API is used to retrieve the list of questions that are configured on the respective LoginRadius site.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/security-questions-by-phone/)

 ```

phone = "<phone>" #Required

result = loginradius.authentication.get_security_questions_by_phone(phone)
 ```




<h6 id="GetSecurityQuestionsByAccessToken-get-"> Get Security Questions By Access Token (GET)</h6>

 This API is used to retrieve the list of questions that are configured on the respective LoginRadius site.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/security-questions-by-access-token/)

 ```

access_token = "<access_token>" #Required

result = loginradius.authentication.get_security_questions_by_access_token(access_token)
 ```




<h6 id="AuthValidateAccessToken-get-"> Auth Validate Access token (GET)</h6>

 This api validates access token, if valid then returns a response with its expiry otherwise error.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-validate-access-token/)

 ```

access_token = "<access_token>" #Required

result = loginradius.authentication.auth_validate_access_token(access_token)
 ```




<h6 id="AuthInValidateAccessToken-get-"> Access Token Invalidate (GET)</h6>

 This api call invalidates the active access token or expires an access token's validity.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-invalidate-access-token/)

 ```

access_token = "<access_token>" #Required
prevent_refresh = "True" #Optional

result = loginradius.authentication.auth_in_validate_access_token(access_token, prevent_refresh)
 ```




<h6 id="GetAccessTokenInfo-get-"> Access Token Info (GET)</h6>

 This api call provide the active access token Information  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-access-token-info/)

 ```

access_token = "<access_token>" #Required

result = loginradius.authentication.get_access_token_info(access_token)
 ```




<h6 id="GetProfileByAccessToken-get-"> Auth Read all Profiles by Token (GET)</h6>

 This API retrieves a copy of the user data based on the access token.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-read-profiles-by-token/)

 ```

access_token = "<access_token>" #Required
fields = "<fields>" #Optional
email_template = "<email_template>" #Optional
verification_url = "<verification_url>" #Optional
welcome_email_template = "<welcome_email_template>" #Optional

result = loginradius.authentication.get_profile_by_access_token(access_token, fields,email_template, verification_url, welcome_email_template)
 ```




<h6 id="SendWelcomeEmail-get-"> Auth Send Welcome Email (GET)</h6>

 This API sends a welcome email  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-send-welcome-email/)

 ```

access_token = "<access_token>" #Required
welcome_email_template = "<welcome_email_template>" #Optional

result = loginradius.authentication.send_welcome_email(access_token, welcome_email_template)
 ```




<h6 id="DeleteAccountByDeleteToken-get-"> Auth Delete Account (GET)</h6>

 This API is used to delete an account by passing it a delete token.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-delete-account/)

 ```

deletetoken = "<deletetoken>" #Required

result = loginradius.authentication.delete_account_by_delete_token(deletetoken)
 ```


<h6 id="GetProfileByPing-get-">Get Profile By Ping  (GET)</h6>

This API is used to get a user's profile using the clientGuid parameter if no callback feature enabled.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/social-login-by-ping/)

 ```

client_guid = "<client_guid>" #Required
email_template = "<email_template>" #Optional
fields = "<fields>" #Optional
verification_url = "<verification_url>" #Optional
welcome_email_template = "<welcome_email_template>" #Optional

result = loginradius.authentication.get_profile_by_ping(client_guid, email_template, fields, verification_url, welcome_email_template)
 ```




<h6 id="CheckEmailAvailability-get-"> Auth Check Email Availability (GET)</h6>

 This API is used to check the email exists or not on your site.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-email-availability/)

 ```

email = "<email>" #Required

result = loginradius.authentication.check_email_availability(email)
 ```




<h6 id="VerifyEmail-get-"> Auth Verify Email (GET)</h6>

 This API is used to verify the email of user. Note: This API will only return the full profile if you have 'Enable auto login after email verification' set in your LoginRadius Admin Console's Email Workflow settings under 'Verification Email'.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-verify-email/)

 ```

verification_token = "<verification_token>" #Required
fields = "<fields>" #Optional
url = "<url>" #Optional
welcome_email_template = "<welcome_email_template>" #Optional

result = loginradius.authentication.verify_email(verification_token, fields, url, welcome_email_template)
 ```




<h6 id="CheckUserNameAvailability-get-"> Auth Check UserName Availability (GET)</h6>

 This API is used to check the UserName exists or not on your site.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-username-availability/)

 ```

username = "<username>" #Required

result = loginradius.authentication.check_user_name_availability(username)
 ```




<h6 id="AcceptPrivacyPolicy-get-"> Auth Privacy Policy Accept (GET)</h6>

 This API is used to update the privacy policy stored in the user's profile by providing the access token of the user accepting the privacy policy  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-privacy-policy-accept)

 ```

access_token = "<access_token>" #Required
fields = "<fields>" #Optional

result = loginradius.authentication.accept_privacy_policy(access_token, fields)
 ```




<h6 id="GetPrivacyPolicyHistoryByAccessToken-get-"> Auth Privacy Policy History By Access Token (GET)</h6>

 This API will return all the accepted privacy policies for the user by providing the access token of that user.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/privacy-policy-history-by-access-token/)

 ```

access_token = "<access_token>" #Required

result = loginradius.authentication.get_privacy_policy_history_by_access_token(access_token)
 ```




<h6 id="DeleteAccountWithEmailConfirmation-delete-"> Auth Delete Account with Email Confirmation (DELETE)</h6>

 This API will send a confirmation email for account deletion to the customer's email when passed the customer's access token  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-delete-account-with-email-confirmation/)

 ```

access_token = "<access_token>" #Required
delete_url = "<delete_url>" #Optional
email_template = "<email_template>" #Optional

result = loginradius.authentication.delete_account_with_email_confirmation(access_token, delete_url, email_template)
 ```




<h6 id="RemoveEmail-delete-"> Auth Remove Email (DELETE)</h6>

 This API is used to remove additional emails from a user's account.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-remove-email)

 ```

access_token = "<access_token>" #Required
email = "<email>" #Required

result = loginradius.authentication.remove_email(access_token, email)
 ```




<h6 id="UnlinkSocialIdentities-delete-"> Auth Unlink Social Identities (DELETE)</h6>

 This API is used to unlink up a social provider account with the specified account based on the access token and the social providers user access token. The unlinked account will automatically get removed from your database.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-unlink-social-identities)

 ```

access_token = "<access_token>" #Required
provider = "<provider>" #Required
provider_id = "<provider_id>" #Required

result = loginradius.authentication.unlink_social_identities(access_token, provider, provider_id)
 ```






### Account API


List of APIs in this Section:<br>

* PUT : [Account Update](#UpdateAccountByUid-put-)<br>
* PUT : [Update Phone ID by UID](#UpdatePhoneIDByUid-put-)<br>
* PUT : [Account Set Password](#SetAccountPasswordByUid-put-)<br>
* PUT : [Account Invalidate Verification Email](#InvalidateAccountEmailVerification-put-)<br>
* PUT : [Reset phone ID verification](#ResetPhoneIDVerificationByUid-put-)<br>
* PUT : [Upsert Email](#UpsertEmail-put-)<br>
* PUT : [Update UID](#AccountUpdateUid-put-)<br>
* POST : [Account Create](#CreateAccount-post-)<br>
* POST : [Forgot Password token](#GetForgotPasswordToken-post-)<br>
* POST : [Email Verification token](#GetEmailVerificationToken-post-)<br>
* GET : [Get Privacy Policy History By Uid](#GetPrivacyPolicyHistoryByUid-get-)<br>
* GET : [Account Profiles by Email](#GetAccountProfileByEmail-get-)<br>
* GET : [Account Profiles by Username](#GetAccountProfileByUserName-get-)<br>
* GET : [Account Profile by Phone ID](#GetAccountProfileByPhone-get-)<br>
* GET : [Account Profiles by UID](#GetAccountProfileByUid-get-)<br>
* GET : [Account Password](#GetAccountPasswordHashByUid-get-)<br>
* GET : [Access Token based on UID or User impersonation API](#GetAccessTokenByUid-get-)<br>
* GET : [Refresh Access Token by Refresh Token](#RefreshAccessTokenByRefreshToken-get-)<br>
* GET : [Revoke Refresh Token](#RevokeRefreshToken-get-)<br>
* GET : [Account Identities by Email](#GetAccountIdentitiesByEmail-get-)<br>
* DELETE : [Account Delete](#DeleteAccountByUid-delete-)<br>
* DELETE : [Account Remove Email](#RemoveEmail-delete-)<br>
* DELETE : [Delete User Profiles By Email](#AccountDeleteByEmail-delete-)<br>




<h6 id="UpdateAccountByUid-put-"> Account Update (PUT)</h6>

 This API is used to update the information of existing accounts in your Cloud Storage. See our Advanced API Usage section <a href='https://www.loginradius.com/docs/api/v2/customer-identity-api/advanced-api-usage/'>Here</a> for more capabilities.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/account/account-update)

 ```

account_user_profile_update_model = {
"firstName" : "<firstName>",
"lastName" : "<lastName>"
}  #Required
uid = "<uid>" #Required
fields = "<fields>" #Optional
null_support = "True" #Optional

result = loginradius.account.update_account_by_uid(account_user_profile_update_model, uid, fields, null_support)
 ```




<h6 id="UpdatePhoneIDByUid-put-"> Update Phone ID by UID (PUT)</h6>

 This API is used to update the PhoneId by using the Uid's. Admin can update the PhoneId's for both the verified and unverified profiles. It will directly replace the PhoneId and bypass the OTP verification process.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/account/update-phoneid-by-uid)

 ```

phone = "<phone>" #Required
uid = "<uid>" #Required
fields = "<fields>" #Optional

result = loginradius.account.update_phone_id_by_uid(phone, uid, fields)
 ```




<h6 id="SetAccountPasswordByUid-put-"> Account Set Password (PUT)</h6>

 This API is used to set the password of an account in Cloud Storage.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/account/account-set-password)

 ```

password = "<password>" #Required
uid = "<uid>" #Required

result = loginradius.account.set_account_password_by_uid(password, uid)
 ```




<h6 id="InvalidateAccountEmailVerification-put-"> Account Invalidate Verification Email (PUT)</h6>

 This API is used to invalidate the Email Verification status on an account.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/account/account-invalidate-verification-email)

 ```

uid = "<uid>" #Required
email_template = "<email_template>" #Optional
verification_url = "<verification_url>" #Optional

result = loginradius.account.invalidate_account_email_verification(uid, email_template, verification_url)
 ```




<h6 id="ResetPhoneIDVerificationByUid-put-"> Reset phone ID verification (PUT)</h6>

 This API Allows you to reset the phone no verification of an end user’s account.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/phone-authentication/reset-phone-id-verification)

 ```

uid = "<uid>" #Required
sms_template = "<sms_template>" #Optional

result = loginradius.account.reset_phone_id_verification_by_uid(uid, sms_template)
 ```




<h6 id="UpsertEmail-put-"> Upsert Email (PUT)</h6>

 This API is used to add/upsert another emails in account profile by different-different email types. If the email type is same then it will simply update the existing email, otherwise it will add a new email in Email array.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/account/upsert-email)

 ```

upsert_email_model = {
"email" : [   {
 "type" : "<type>"  ,
 "value" : "<value>"   
}  ]
}  #Required
uid = "<uid>" #Required
fields = "<fields>" #Optional

result = loginradius.account.upsert_email(upsert_email_model, uid, fields)
 ```




<h6 id="AccountUpdateUid-put-"> Update UID (PUT)</h6>

 This API is used to update a user's Uid. It will update all profiles, custom objects and consent management logs associated with the Uid.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/account/account-update/)

 ```

update_uid_model = {
"newUid" : "<newUid>"
}  #Required
uid = "<uid>" #Required

result = loginradius.account.account_update_uid(update_uid_model, uid)
 ```




<h6 id="CreateAccount-post-"> Account Create (POST)</h6>

 This API is used to create an account in Cloud Storage. This API bypass the normal email verification process and manually creates the user. <br><br>In order to use this API, you need to format a JSON request body with all of the mandatory fields  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/account/account-create)

 ```

account_create_model = {
"email" : [   {
 "type" : "<type>"  ,
 "value" : "<value>"   
}  ] ,
"firstName" : "<firstName>",
"lastName" : "<lastName>",
"password" : "<password>"
}  #Required
fields = "<fields>" #Optional

result = loginradius.account.create_account(account_create_model, fields)
 ```




<h6 id="GetForgotPasswordToken-post-"> Forgot Password token (POST)</h6>

 This API Returns a Forgot Password Token it can also be used to send a Forgot Password email to the customer. Note: If you have the UserName workflow enabled, you may replace the 'email' parameter with 'username' in the body.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/account/get-forgot-password-token)

 ```

email = "<email>" #Required
email_template = "<email_template>" #Optional
reset_password_url = "<reset_password_url>" #Optional
send_email = "True" #Optional

result = loginradius.account.get_forgot_password_token(email, email_template, reset_password_url, send_email)
 ```




<h6 id="GetEmailVerificationToken-post-"> Email Verification token (POST)</h6>

 This API Returns an Email Verification token.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/account/get-email-verification-token)

 ```

email = "<email>" #Required

result = loginradius.account.get_email_verification_token(email)
 ```




<h6 id="GetPrivacyPolicyHistoryByUid-get-"> Get Privacy Policy History By Uid (GET)</h6>

 This API is used to retrieve all of the accepted Policies by the user, associated with their UID.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/account/privacy-policy-history-by-uid/)

 ```

uid = "<uid>" #Required

result = loginradius.account.get_privacy_policy_history_by_uid(uid)
 ```




<h6 id="GetAccountProfileByEmail-get-"> Account Profiles by Email (GET)</h6>

 This API is used to retrieve all of the profile data, associated with the specified account by email in Cloud Storage.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/account/account-profiles-by-email)

 ```

email = "<email>" #Required
fields = "<fields>" #Optional

result = loginradius.account.get_account_profile_by_email(email, fields)
 ```




<h6 id="GetAccountProfileByUserName-get-"> Account Profiles by Username (GET)</h6>

 This API is used to retrieve all of the profile data associated with the specified account by user name in Cloud Storage.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/account/account-profiles-by-user-name)

 ```

user_name = "<user_name>" #Required
fields = "<fields>" #Optional

result = loginradius.account.get_account_profile_by_user_name(user_name, fields)
 ```




<h6 id="GetAccountProfileByPhone-get-"> Account Profile by Phone ID (GET)</h6>

 This API is used to retrieve all of the profile data, associated with the account by phone number in Cloud Storage.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/account/account-profiles-by-phone-id/)

 ```

phone = "<phone>" #Required
fields = "<fields>" #Optional

result = loginradius.account.get_account_profile_by_phone(phone, fields)
 ```




<h6 id="GetAccountProfileByUid-get-"> Account Profiles by UID (GET)</h6>

 This API is used to retrieve all of the profile data, associated with the account by uid in Cloud Storage.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/account/account-profiles-by-uid)

 ```

uid = "<uid>" #Required
fields = "<fields>" #Optional

result = loginradius.account.get_account_profile_by_uid(uid, fields)
 ```




<h6 id="GetAccountPasswordHashByUid-get-"> Account Password (GET)</h6>

 This API use to retrive the hashed password of a specified account in Cloud Storage.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/account/account-password)

 ```

uid = "<uid>" #Required

result = loginradius.account.get_account_password_hash_by_uid(uid)
 ```




<h6 id="GetAccessTokenByUid-get-"> Access Token based on UID or User impersonation API (GET)</h6>

 The API is used to get LoginRadius access token based on UID.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/account/account-impersonation-api)

 ```

uid = "<uid>" #Required

result = loginradius.account.get_access_token_by_uid(uid)
 ```




<h6 id="RefreshAccessTokenByRefreshToken-get-"> Refresh Access Token by Refresh Token (GET)</h6>

 This API is used to refresh an access token via it's associated refresh token.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/refresh-token/refresh-access-token-by-refresh-token)

 ```

refresh_token = "<refresh_token>" #Required

result = loginradius.account.refresh_access_token_by_refresh_token(refresh_token)
 ```




<h6 id="RevokeRefreshToken-get-"> Revoke Refresh Token (GET)</h6>

 The Revoke Refresh Access Token API is used to revoke a refresh token or the Provider Access Token, revoking an existing refresh token will invalidate the refresh token but the associated access token will work until the expiry.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/refresh-token/revoke-refresh-token)

 ```

refresh_token = "<refresh_token>" #Required

result = loginradius.account.revoke_refresh_token(refresh_token)
 ```




<h6 id="GetAccountIdentitiesByEmail-get-"> Account Identities by Email (GET)</h6>

 Note: This is intended for specific workflows where an email may be associated to multiple UIDs. This API is used to retrieve all of the identities (UID and Profiles), associated with a specified email in Cloud Storage.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/account/account-identities-by-email)

 ```

email = "<email>" #Required
fields = "<fields>" #Optional

result = loginradius.account.get_account_identities_by_email(email, fields)
 ```




<h6 id="DeleteAccountByUid-delete-"> Account Delete (DELETE)</h6>

 This API deletes the Users account and allows them to re-register for a new account.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/account/account-delete)

 ```

uid = "<uid>" #Required

result = loginradius.account.delete_account_by_uid(uid)
 ```




<h6 id="RemoveEmail-delete-"> Account Remove Email (DELETE)</h6>

 Use this API to Remove emails from a user Account  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/account/account-email-delete)

 ```

email = "<email>" #Required
uid = "<uid>" #Required
fields = "<fields>" #Optional

result = loginradius.account.remove_email(email, uid, fields)
 ```




<h6 id="AccountDeleteByEmail-delete-"> Delete User Profiles By Email (DELETE)</h6>

 This API is used to delete all user profiles associated with an Email.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/account/account-email-delete/)

 ```

email = "<email>" #Required

result = loginradius.account.account_delete_by_email(email)
 ```






### Social API


List of APIs in this Section:<br>

* POST : [Post Message API](#PostMessage-post-)<br>
* POST : [Status Posting ](#StatusPosting-post-)<br>
* POST : [Trackable Status Posting](#TrackableStatusPosting-post-)<br>
* GET : [Access Token](#ExchangeAccessToken-get-)<br>
* GET : [Refresh Token](#RefreshAccessToken-get-)<br>
* GET : [Token Validate](#ValidateAccessToken-get-)<br>
* GET : [Access Token Invalidate](#InValidateAccessToken-get-)<br>
* GET : [Get Active Session Details](#GetActiveSession-get-)<br>
* GET : [Get Active Session By Account Id](#GetActiveSessionByAccountID-get-)<br>
* GET : [Get Active Session By Profile Id](#GetActiveSessionByProfileID-get-)<br>
* GET : [Album](#GetAlbums-get-)<br>
* GET : [Get Albums with cursor](#GetAlbumsWithCursor-get-)<br>
* GET : [Audio](#GetAudios-get-)<br>
* GET : [Get Audio With Cursor](#GetAudiosWithCursor-get-)<br>
* GET : [Check In](#GetCheckIns-get-)<br>
* GET : [Get CheckIns With Cursor](#GetCheckInsWithCursor-get-)<br>
* GET : [Contact](#GetContacts-get-)<br>
* GET : [Event](#GetEvents-get-)<br>
* GET : [Get Events With Cursor](#GetEventsWithCursor-get-)<br>
* GET : [Following](#GetFollowings-get-)<br>
* GET : [Get Followings With Cursor](#GetFollowingsWithCursor-get-)<br>
* GET : [Group](#GetGroups-get-)<br>
* GET : [Get Groups With Cursor](#GetGroupsWithCursor-get-)<br>
* GET : [Like](#GetLikes-get-)<br>
* GET : [Get Likes With Cursor](#GetLikesWithCursor-get-)<br>
* GET : [Mention](#GetMentions-get-)<br>
* GET : [Page](#GetPage-get-)<br>
* GET : [Photo](#GetPhotos-get-)<br>
* GET : [Get Post](#GetPosts-get-)<br>
* GET : [Get Trackable Status Stats](#GetTrackableStatusStats-get-)<br>
* GET : [Trackable Status Fetching](#TrackableStatusFetching-get-)<br>
* GET : [Refresh User Profile](#GetRefreshedSocialUserProfile-get-)<br>
* GET : [Video](#GetVideos-get-)<br>




<h6 id="PostMessage-post-"> Post Message API (POST)</h6>

 Post Message API is used to post messages to the user's contacts.<br><br><b>Supported Providers:</b> Twitter, LinkedIn <br><br>The Message API is used to post messages to the user?s contacts. This is one of the APIs that makes up the LoginRadius Friend Invite System. After using the Contact API, you can send messages to the retrieved contacts. This API requires setting permissions in your LoginRadius Dashboard.<br><br>GET & POST Message API work the same way except the API method is different  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/post-message-api)

 ```

access_token = "<access_token>" #Required
message = "<message>" #Required
subject = "<subject>" #Required
to = "<to>" #Required

result = loginradius.social.post_message(access_token, message, subject, to)
 ```




<h6 id="StatusPosting-post-"> Status Posting  (POST)</h6>

 The Status API is used to update the status on the user's wall.<br><br><b>Supported Providers:</b>  Facebook, Twitter, LinkedIn  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/status-posting/)

 ```

access_token = "<access_token>" #Required
caption = "<caption>" #Required
description = "<description>" #Required
imageurl = "<imageurl>" #Required
status = "<status>" #Required
title = "<title>" #Required
url = "<url>" #Required
shorturl = "<shorturl>" #Optional

result = loginradius.social.status_posting(access_token, caption, description, imageurl, status, title, url, shorturl)
 ```




<h6 id="TrackableStatusPosting-post-"> Trackable Status Posting (POST)</h6>

 The Trackable status API works very similar to the Status API but it returns a Post id that you can use to track the stats(shares, likes, comments) for a specific share/post/status update. This API requires setting permissions in your LoginRadius Dashboard.<br><br> The Trackable Status API is used to update the status on the user's wall and return an Post ID value. It is commonly referred to as Permission based sharing or Push notifications.<br><br> POST Input Parameter Format: application/x-www-form-urlencoded  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/trackable-status-posting/)

 ```

access_token = "<access_token>" #Required
status_model = {
"caption" : "<caption>",
"description" : "<description>",
"imageurl" : "<imageurl>",
"status" : "<status>",
"title" : "<title>",
"url" : "<url>"
}  #Required

result = loginradius.social.trackable_status_posting(access_token, status_model)
 ```




<h6 id="ExchangeAccessToken-get-"> Access Token (GET)</h6>

 This API Is used to translate the Request Token returned during authentication into an Access Token that can be used with other API calls.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/access-token)

 ```

token = "<token>" #Required

result = loginradius.social.exchange_access_token(token)
 ```




<h6 id="RefreshAccessToken-get-"> Refresh Token (GET)</h6>

 The Refresh Access Token API is used to refresh the provider access token after authentication. It will be valid for up to 60 days on LoginRadius depending on the provider. In order to use the access token in other APIs, always refresh the token using this API.<br><br><b>Supported Providers :</b> Facebook,Yahoo,Google,Twitter, Linkedin.<br><br> Contact LoginRadius support team to enable this API.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/refresh-token/refresh-token)

 ```

access_token = "<access_token>" #Required
expires_in = 0 #Optional
is_web = "True" #Optional

result = loginradius.social.refresh_access_token(access_token, expires_in, is_web)
 ```




<h6 id="ValidateAccessToken-get-"> Token Validate (GET)</h6>

 This API validates access token, if valid then returns a response with its expiry otherwise error.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/validate-access-token)

 ```

access_token = "<access_token>" #Required

result = loginradius.social.validate_access_token(access_token)
 ```




<h6 id="InValidateAccessToken-get-"> Access Token Invalidate (GET)</h6>

 This api invalidates the active access token or expires an access token validity.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/invalidate-access-token)

 ```

access_token = "<access_token>" #Required

result = loginradius.social.in_validate_access_token(access_token)
 ```




<h6 id="GetActiveSession-get-"> Get Active Session Details (GET)</h6>

 This api is use to get all active session by Access Token.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/get-active-session-details)

 ```

token = "<token>" #Required

result = loginradius.social.get_active_session(token)
 ```




<h6 id="GetActiveSessionByAccountID-get-"> Get Active Session By Account Id (GET)</h6>

 This api is used to get all active sessions by AccountID(UID).  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/active-session-by-account-id/)

 ```

account_id = "<account_id>" #Required

result = loginradius.social.get_active_session_by_account_id(account_id)
 ```




<h6 id="GetActiveSessionByProfileID-get-"> Get Active Session By Profile Id (GET)</h6>

 This api is used to get all active sessions by ProfileId.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/active-session-by-profile-id/)

 ```

profile_id = "<profile_id>" #Required

result = loginradius.social.get_active_session_by_profile_id(profile_id)
 ```




<h6 id="GetAlbums-get-"> Album (GET)</h6>

 <b>Supported Providers:</b> Facebook, Google, Live, Vkontakte.<br><br> This API returns the photo albums associated with the passed in access tokens Social Profile.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/album/)

 ```

access_token = "<access_token>" #Required

result = loginradius.social.get_albums(access_token)
 ```




<h6 id="GetAlbumsWithCursor-get-"> Get Albums with cursor (GET)</h6>

 <b>Supported Providers:</b> Facebook, Google, Live, Vkontakte.<br><br> This API returns the photo albums associated with the passed in access tokens Social Profile.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/album/)

 ```

access_token = "<access_token>" #Required
next_cursor = "<next_cursor>" #Required

result = loginradius.social.get_albums_with_cursor(access_token, next_cursor)
 ```




<h6 id="GetAudios-get-"> Audio (GET)</h6>

 The Audio API is used to get audio files data from the user's social account.<br><br><b>Supported Providers:</b> Live, Vkontakte  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/audio)

 ```

access_token = "<access_token>" #Required

result = loginradius.social.get_audios(access_token)
 ```




<h6 id="GetAudiosWithCursor-get-"> Get Audio With Cursor (GET)</h6>

 The Audio API is used to get audio files data from the user's social account.<br><br><b>Supported Providers:</b> Live, Vkontakte  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/audio)

 ```

access_token = "<access_token>" #Required
next_cursor = "<next_cursor>" #Required

result = loginradius.social.get_audios_with_cursor(access_token, next_cursor)
 ```




<h6 id="GetCheckIns-get-"> Check In (GET)</h6>

 The Check In API is used to get check Ins data from the user's social account.<br><br><b>Supported Providers:</b> Facebook, Foursquare, Vkontakte  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/check-in)

 ```

access_token = "<access_token>" #Required

result = loginradius.social.get_check_ins(access_token)
 ```




<h6 id="GetCheckInsWithCursor-get-"> Get CheckIns With Cursor (GET)</h6>

 The Check In API is used to get check Ins data from the user's social account.<br><br><b>Supported Providers:</b> Facebook, Foursquare, Vkontakte  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/check-in)

 ```

access_token = "<access_token>" #Required
next_cursor = "<next_cursor>" #Required

result = loginradius.social.get_check_ins_with_cursor(access_token, next_cursor)
 ```




<h6 id="GetContacts-get-"> Contact (GET)</h6>

 The Contact API is used to get contacts/friends/connections data from the user's social account.This is one of the APIs that makes up the LoginRadius Friend Invite System. The data will normalized into LoginRadius' standard data format. This API requires setting permissions in your LoginRadius Dashboard. <br><br><b>Note:</b> Facebook restricts access to the list of friends that is returned. When using the Contacts API with Facebook you will only receive friends that have accepted some permissions with your app. <br><br><b>Supported Providers:</b> Facebook, Foursquare, Google, LinkedIn, Live, Twitter, Vkontakte, Yahoo  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/contact)

 ```

access_token = "<access_token>" #Required
next_cursor = "<next_cursor>" #Optional

result = loginradius.social.get_contacts(access_token, next_cursor)
 ```




<h6 id="GetEvents-get-"> Event (GET)</h6>

 The Event API is used to get the event data from the user's social account.<br><br><b>Supported Providers:</b> Facebook, Live  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/event)

 ```

access_token = "<access_token>" #Required

result = loginradius.social.get_events(access_token)
 ```




<h6 id="GetEventsWithCursor-get-"> Get Events With Cursor (GET)</h6>

 The Event API is used to get the event data from the user's social account.<br><br><b>Supported Providers:</b> Facebook, Live  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/event)

 ```

access_token = "<access_token>" #Required
next_cursor = "<next_cursor>" #Required

result = loginradius.social.get_events_with_cursor(access_token, next_cursor)
 ```




<h6 id="GetFollowings-get-"> Following (GET)</h6>

 Get the following user list from the user's social account.<br><br><b>Supported Providers:</b> Twitter  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/following)

 ```

access_token = "<access_token>" #Required

result = loginradius.social.get_followings(access_token)
 ```




<h6 id="GetFollowingsWithCursor-get-"> Get Followings With Cursor (GET)</h6>

 Get the following user list from the user's social account.<br><br><b>Supported Providers:</b> Twitter  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/following)

 ```

access_token = "<access_token>" #Required
next_cursor = "<next_cursor>" #Required

result = loginradius.social.get_followings_with_cursor(access_token, next_cursor)
 ```




<h6 id="GetGroups-get-"> Group (GET)</h6>

 The Group API is used to get group data from the user's social account.<br><br><b>Supported Providers:</b> Facebook, Vkontakte  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/group)

 ```

access_token = "<access_token>" #Required

result = loginradius.social.get_groups(access_token)
 ```




<h6 id="GetGroupsWithCursor-get-"> Get Groups With Cursor (GET)</h6>

 The Group API is used to get group data from the user's social account.<br><br><b>Supported Providers:</b> Facebook, Vkontakte  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/group)

 ```

access_token = "<access_token>" #Required
next_cursor = "<next_cursor>" #Required

result = loginradius.social.get_groups_with_cursor(access_token, next_cursor)
 ```




<h6 id="GetLikes-get-"> Like (GET)</h6>

 The Like API is used to get likes data from the user's social account.<br><br><b>Supported Providers:</b> Facebook  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/like)

 ```

access_token = "<access_token>" #Required

result = loginradius.social.get_likes(access_token)
 ```




<h6 id="GetLikesWithCursor-get-"> Get Likes With Cursor (GET)</h6>

 The Like API is used to get likes data from the user's social account.<br><br><b>Supported Providers:</b> Facebook  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/like)

 ```

access_token = "<access_token>" #Required
next_cursor = "<next_cursor>" #Required

result = loginradius.social.get_likes_with_cursor(access_token, next_cursor)
 ```




<h6 id="GetMentions-get-"> Mention (GET)</h6>

 The Mention API is used to get mentions data from the user's social account.<br><br><b>Supported Providers:</b> Twitter  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/mention)

 ```

access_token = "<access_token>" #Required

result = loginradius.social.get_mentions(access_token)
 ```




<h6 id="GetPage-get-"> Page (GET)</h6>

 The Page API is used to get the page data from the user's social account.<br><br><b>Supported Providers:</b>  Facebook, LinkedIn  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/page)

 ```

access_token = "<access_token>" #Required
page_name = "<page_name>" #Required

result = loginradius.social.get_page(access_token, page_name)
 ```




<h6 id="GetPhotos-get-"> Photo (GET)</h6>

 The Photo API is used to get photo data from the user's social account.<br><br><b>Supported Providers:</b>  Facebook, Foursquare, Google, Live, Vkontakte  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/photo)

 ```

access_token = "<access_token>" #Required
album_id = "<album_id>" #Required

result = loginradius.social.get_photos(access_token, album_id)
 ```




<h6 id="GetPosts-get-"> Get Post (GET)</h6>

 The Post API is used to get post message data from the user's social account.<br><br><b>Supported Providers:</b>  Facebook  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/post)

 ```

access_token = "<access_token>" #Required

result = loginradius.social.get_posts(access_token)
 ```




<h6 id="GetTrackableStatusStats-get-"> Get Trackable Status Stats (GET)</h6>

 The Trackable status API works very similar to the Status API but it returns a Post id that you can use to track the stats(shares, likes, comments) for a specific share/post/status update. This API requires setting permissions in your LoginRadius Dashboard.<br><br> The Trackable Status API is used to update the status on the user's wall and return an Post ID value. It is commonly referred to as Permission based sharing or Push notifications.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/get-trackable-status-stats/)

 ```

access_token = "<access_token>" #Required
caption = "<caption>" #Required
description = "<description>" #Required
imageurl = "<imageurl>" #Required
status = "<status>" #Required
title = "<title>" #Required
url = "<url>" #Required

result = loginradius.social.get_trackable_status_stats(access_token, caption, description, imageurl, status, title, url)
 ```




<h6 id="TrackableStatusFetching-get-"> Trackable Status Fetching (GET)</h6>

 The Trackable status API works very similar to the Status API but it returns a Post id that you can use to track the stats(shares, likes, comments) for a specific share/post/status update. This API requires setting permissions in your LoginRadius Dashboard.<br><br> This API is used to retrieve a tracked post based on the passed in post ID value. This API requires setting permissions in your LoginRadius Dashboard.<br><br> <b>Note:</b> To utilize this API you need to find the ID for the post you want to track, which might require using Trackable Status Posting API first.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/trackable-status-fetching/)

 ```

post_id = "<post_id>" #Required

result = loginradius.social.trackable_status_fetching(post_id)
 ```





<h6 id="GetRefreshedSocialUserProfile-get-"> Refresh User Profile (GET)</h6>

 The User Profile API is used to get the latest updated social profile data from the user's social account after authentication. The social profile will be retrieved via oAuth and OpenID protocols. The data is normalized into LoginRadius' standard data format. This API should be called using the access token retrieved from the refresh access token API.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/refresh-token/refresh-user-profile)

 ```

access_token = "<access_token>" #Required
fields = "<fields>" #Optional

result = loginradius.social.get_refreshed_social_user_profile(access_token, fields)
 ```




<h6 id="GetVideos-get-"> Video (GET)</h6>

 The Video API is used to get video files data from the user's social account.<br><br><b>Supported Providers:</b>   Facebook, Google, Live, Vkontakte  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/advanced-social-api/video)

 ```

access_token = "<access_token>" #Required
next_cursor = "<next_cursor>" #Required

result = loginradius.social.get_videos(access_token, next_cursor)
 ```






### CustomObject API


List of APIs in this Section:<br>

* PUT : [Custom Object Update by Access Token](#UpdateCustomObjectByToken-put-)<br>
* PUT : [Custom Object Update by UID](#UpdateCustomObjectByUid-put-)<br>
* POST : [Create Custom Object by Token](#CreateCustomObjectByToken-post-)<br>
* POST : [Create Custom Object by UID](#CreateCustomObjectByUid-post-)<br>
* GET : [Custom Object by Token](#GetCustomObjectByToken-get-)<br>
* GET : [Custom Object by ObjectRecordId and Token](#GetCustomObjectByRecordIDAndToken-get-)<br>
* GET : [Custom Object By UID](#GetCustomObjectByUid-get-)<br>
* GET : [Custom Object by ObjectRecordId and UID](#GetCustomObjectByRecordID-get-)<br>
* DELETE : [Custom Object Delete by Record Id And Token](#DeleteCustomObjectByToken-delete-)<br>
* DELETE : [Account Delete Custom Object by ObjectRecordId](#DeleteCustomObjectByRecordID-delete-)<br>




<h6 id="UpdateCustomObjectByToken-put-"> Custom Object Update by Access Token (PUT)</h6>

 This API is used to update the specified custom object data of the specified account. If the value of updatetype is 'replace' then it will fully replace custom object with the new custom object and if the value of updatetype is 'partialreplace' then it will perform an upsert type operation  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/custom-object/custom-object-update-by-objectrecordid-and-token)

 ```

access_token = "<access_token>" #Required
object_name = "<object_name>" #Required
object_record_id = "<object_record_id>" #Required
object = { "customdata1": "Store my customdata1 value"}  #Required
update_type = "<update_type>" #Optional

result = loginradius.custom_object.update_custom_object_by_token(access_token, object_name, object_record_id, object, update_type)
 ```




<h6 id="UpdateCustomObjectByUid-put-"> Custom Object Update by UID (PUT)</h6>

 This API is used to update the specified custom object data of a specified account. If the value of updatetype is 'replace' then it will fully replace custom object with new custom object and if the value of updatetype is partialreplace then it will perform an upsert type operation.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/custom-object/custom-object-update-by-objectrecordid-and-uid)

 ```

object_name = "<object_name>" #Required
object_record_id = "<object_record_id>" #Required
object = { "customdata1": "Store my customdata1 value"}  #Required
uid = "<uid>" #Required
update_type = "<update_type>" #Optional

result = loginradius.custom_object.update_custom_object_by_uid(object_name, object_record_id, object, uid, update_type)
 ```




<h6 id="CreateCustomObjectByToken-post-"> Create Custom Object by Token (POST)</h6>

 This API is used to write information in JSON format to the custom object for the specified account.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/custom-object/create-custom-object-by-token)

 ```

access_token = "<access_token>" #Required
object_name = "<object_name>" #Required
object = { "customdata1": "Store my customdata1 value"}  #Required

result = loginradius.custom_object.create_custom_object_by_token(access_token, object_name, object)
 ```




<h6 id="CreateCustomObjectByUid-post-"> Create Custom Object by UID (POST)</h6>

 This API is used to write information in JSON format to the custom object for the specified account.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/custom-object/create-custom-object-by-uid)

 ```

object_name = "<object_name>" #Required
object = { "customdata1": "Store my customdata1 value"}  #Required
uid = "<uid>" #Required

result = loginradius.custom_object.create_custom_object_by_uid(object_name, object, uid)
 ```




<h6 id="GetCustomObjectByToken-get-"> Custom Object by Token (GET)</h6>

 This API is used to retrieve the specified Custom Object data for the specified account.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/custom-object/custom-object-by-token)

 ```

access_token = "<access_token>" #Required
object_name = "<object_name>" #Required

result = loginradius.custom_object.get_custom_object_by_token(access_token, object_name)
 ```




<h6 id="GetCustomObjectByRecordIDAndToken-get-"> Custom Object by ObjectRecordId and Token (GET)</h6>

 This API is used to retrieve the Custom Object data for the specified account.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/custom-object/custom-object-by-objectrecordid-and-token)

 ```

access_token = "<access_token>" #Required
object_name = "<object_name>" #Required
object_record_id = "<object_record_id>" #Required

result = loginradius.custom_object.get_custom_object_by_record_id_and_token(access_token, object_name, object_record_id)
 ```




<h6 id="GetCustomObjectByUid-get-"> Custom Object By UID (GET)</h6>

 This API is used to retrieve all the custom objects by UID from cloud storage.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/custom-object/custom-object-by-uid)

 ```

object_name = "<object_name>" #Required
uid = "<uid>" #Required

result = loginradius.custom_object.get_custom_object_by_uid(object_name, uid)
 ```




<h6 id="GetCustomObjectByRecordID-get-"> Custom Object by ObjectRecordId and UID (GET)</h6>

 This API is used to retrieve the Custom Object data for the specified account.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/custom-object/custom-object-by-objectrecordid-and-uid)

 ```

object_name = "<object_name>" #Required
object_record_id = "<object_record_id>" #Required
uid = "<uid>" #Required

result = loginradius.custom_object.get_custom_object_by_record_id(object_name, object_record_id, uid)
 ```




<h6 id="DeleteCustomObjectByToken-delete-"> Custom Object Delete by Record Id And Token (DELETE)</h6>

 This API is used to remove the specified Custom Object data using ObjectRecordId of a specified account.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/custom-object/custom-object-delete-by-objectrecordid-and-token)

 ```

access_token = "<access_token>" #Required
object_name = "<object_name>" #Required
object_record_id = "<object_record_id>" #Required

result = loginradius.custom_object.delete_custom_object_by_token(access_token, object_name, object_record_id)
 ```




<h6 id="DeleteCustomObjectByRecordID-delete-"> Account Delete Custom Object by ObjectRecordId (DELETE)</h6>

 This API is used to remove the specified Custom Object data using ObjectRecordId of specified account.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/custom-object/custom-object-delete-by-objectrecordid-and-uid)

 ```

object_name = "<object_name>" #Required
object_record_id = "<object_record_id>" #Required
uid = "<uid>" #Required

result = loginradius.custom_object.delete_custom_object_by_record_id(object_name, object_record_id, uid)
 ```






### PhoneAuthentication API


List of APIs in this Section:<br>

* PUT : [Phone Reset Password by OTP](#ResetPasswordByPhoneOTP-put-)<br>
* PUT : [Phone Verification OTP](#PhoneVerificationByOTP-put-)<br>
* PUT : [Phone Verification OTP by Token](#PhoneVerificationOTPByAccessToken-put-)<br>
* PUT : [Phone Number Update](#UpdatePhoneNumber-put-)<br>
* POST : [Phone Login](#LoginByPhone-post-)<br>
* POST : [Phone Forgot Password by OTP](#ForgotPasswordByPhoneOTP-post-)<br>
* POST : [Phone Resend Verification OTP](#PhoneResendVerificationOTP-post-)<br>
* POST : [Phone Resend Verification OTP By Token](#PhoneResendVerificationOTPByToken-post-)<br>
* POST : [Phone User Registration by SMS](#UserRegistrationByPhone-post-)<br>
* GET : [Phone Number Availability](#CheckPhoneNumberAvailability-get-)<br>
* DELETE : [Remove Phone ID by Access Token](#RemovePhoneIDByAccessToken-delete-)<br>




<h6 id="ResetPasswordByPhoneOTP-put-"> Phone Reset Password by OTP (PUT)</h6>

 This API is used to reset the password  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/phone-authentication/phone-reset-password-by-otp)

 ```

reset_password_by_otp_model = {
"otp" : "<otp>",
"password" : "<password>",
"phone" : "<phone>"
}  #Required

result = loginradius.phone_authentication.reset_password_by_phone_otp(reset_password_by_otp_model)
 ```




<h6 id="PhoneVerificationByOTP-put-"> Phone Verification OTP (PUT)</h6>

 This API is used to validate the verification code sent to verify a user's phone number  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/phone-authentication/phone-verify-otp)

 ```

otp = "<otp>" #Required
phone = "<phone>" #Required
fields = "<fields>" #Optional
sms_template = "<sms_template>" #Optional

result = loginradius.phone_authentication.phone_verification_by_otp(otp, phone, fields, sms_template)
 ```




<h6 id="PhoneVerificationOTPByAccessToken-put-"> Phone Verification OTP by Token (PUT)</h6>

 This API is used to consume the verification code sent to verify a user's phone number. Use this call for front-end purposes in cases where the user is already logged in by passing the user's access token.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/phone-authentication/phone-verify-otp-by-token)

 ```

access_token = "<access_token>" #Required
otp = "<otp>" #Required
sms_template = "<sms_template>" #Optional

result = loginradius.phone_authentication.phone_verification_otp_by_access_token(access_token, otp, sms_template)
 ```




<h6 id="UpdatePhoneNumber-put-"> Phone Number Update (PUT)</h6>

 This API is used to update the login Phone Number of users  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/phone-authentication/phone-number-update)

 ```

access_token = "<access_token>" #Required
phone = "<phone>" #Required
sms_template = "<sms_template>" #Optional

result = loginradius.phone_authentication.update_phone_number(access_token, phone, sms_template)
 ```




<h6 id="LoginByPhone-post-"> Phone Login (POST)</h6>

 This API retrieves a copy of the user data based on the Phone  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/phone-authentication/phone-login)

 ```

phone_authentication_model = {
"password" : "<password>",
"phone" : "<phone>"
}  #Required
fields = "<fields>" #Optional
login_url = "<login_url>" #Optional
sms_template = "<sms_template>" #Optional

result = loginradius.phone_authentication.login_by_phone(phone_authentication_model, fields, login_url, sms_template)
 ```




<h6 id="ForgotPasswordByPhoneOTP-post-"> Phone Forgot Password by OTP (POST)</h6>

 This API is used to send the OTP to reset the account password.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/phone-authentication/phone-forgot-password-by-otp)

 ```

phone = "<phone>" #Required
sms_template = "<sms_template>" #Optional

result = loginradius.phone_authentication.forgot_password_by_phone_otp(phone, sms_template)
 ```




<h6 id="PhoneResendVerificationOTP-post-"> Phone Resend Verification OTP (POST)</h6>

 This API is used to resend a verification OTP to verify a user's Phone Number. The user will receive a verification code that they will need to input  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/phone-authentication/phone-resend-otp)

 ```

phone = "<phone>" #Required
sms_template = "<sms_template>" #Optional

result = loginradius.phone_authentication.phone_resend_verification_otp(phone, sms_template)
 ```




<h6 id="PhoneResendVerificationOTPByToken-post-"> Phone Resend Verification OTP By Token (POST)</h6>

 This API is used to resend a verification OTP to verify a user's Phone Number in cases in which an active token already exists  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/phone-authentication/phone-resend-otp-by-token)

 ```

access_token = "<access_token>" #Required
phone = "<phone>" #Required
sms_template = "<sms_template>" #Optional

result = loginradius.phone_authentication.phone_resend_verification_otp_by_token(access_token, phone, sms_template)
 ```




<h6 id="UserRegistrationByPhone-post-"> Phone User Registration by SMS (POST)</h6>

 This API registers the new users into your Cloud Storage and triggers the phone verification process.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/phone-authentication/phone-user-registration-by-sms)

 ```

auth_user_registration_model = {
"firstName" : "<firstName>",
"lastName" : "<lastName>",
"password" : "<password>",
"phoneId" : "<phoneId>"
}  #Required
sott = "<sott>" #Required
fields = "<fields>" #Optional
options = "<options>" #Optional
sms_template = "<sms_template>" #Optional
verification_url = "<verification_url>" #Optional
welcome_email_template = "<welcome_email_template>" #Optional

result = loginradius.phone_authentication.user_registration_by_phone(auth_user_registration_model, sott, fields, options, sms_template, verification_url, welcome_email_template)
 ```




<h6 id="CheckPhoneNumberAvailability-get-"> Phone Number Availability (GET)</h6>

 This API is used to check the Phone Number exists or not on your site.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/phone-authentication/phone-number-availability)

 ```

phone = "<phone>" #Required

result = loginradius.phone_authentication.check_phone_number_availability(phone)
 ```




<h6 id="RemovePhoneIDByAccessToken-delete-"> Remove Phone ID by Access Token (DELETE)</h6>

 This API is used to delete the Phone ID on a user's account via the access token  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/phone-authentication/remove-phone-id-by-access-token)

 ```

access_token = "<access_token>" #Required

result = loginradius.phone_authentication.remove_phone_id_by_access_token(access_token)
 ```






### MultiFactorAuthentication API


List of APIs in this Section:<br>

* PUT : [Update MFA Setting](#MFAUpdateSetting-put-)<br>
* PUT : [Update MFA by Access Token](#MFAUpdateByAccessToken-put-)<br>
* PUT : [MFA Update Phone Number by Token](#MFAUpdatePhoneNumberByToken-put-)<br>
* PUT : [Verify MFA Email OTP by Access Token](#MFAValidateEmailOtpByAccessToken-put-)<br>
* PUT : [Update MFA Security Question by Access Token](#MFASecurityQuestionAnswerByAccessToken-put-)<br>
* PUT : [MFA Validate OTP](#MFAValidateOTPByPhone-put-)<br>
* PUT : [MFA Validate Google Auth Code](#MFAValidateGoogleAuthCode-put-)<br>
* PUT : [MFA Validate Backup code](#MFAValidateBackupCode-put-)<br>
* PUT : [MFA Update Phone Number](#MFAUpdatePhoneNumber-put-)<br>
* PUT : [Verify MFA Email OTP by MFA Token](#MFAValidateEmailOtp-put-)<br>
* PUT : [Update MFA Security Question by MFA Token](#MFASecurityQuestionAnswer-put-)<br>
* POST : [MFA Email Login](#MFALoginByEmail-post-)<br>
* POST : [MFA UserName Login](#MFALoginByUserName-post-)<br>
* POST : [MFA Phone Login](#MFALoginByPhone-post-)<br>
* POST : [Send MFA Email OTP by MFA Token](#MFAEmailOTP-post-)<br>
* POST : [Verify MFA Security Question by MFA Token](#MFASecurityQuestionAnswerVerification-post-)<br>
* GET : [MFA Validate Access Token](#MFAConfigureByAccessToken-get-)<br>
* GET : [MFA Backup Code by Access Token](#MFABackupCodeByAccessToken-get-)<br>
* GET : [Reset Backup Code by Access Token](#MFAResetBackupCodeByAccessToken-get-)<br>
* GET : [Send MFA Email OTP by Access Token](#MFAEmailOtpByAccessToken-get-)<br>
* GET : [MFA Resend Otp](#MFAResendOTP-get-)<br>
* GET : [MFA Backup Code by UID](#MFABackupCodeByUid-get-)<br>
* GET : [MFA Reset Backup Code by UID](#MFAResetBackupCodeByUid-get-)<br>
* DELETE : [MFA Reset Google Authenticator by Token](#MFAResetGoogleAuthByToken-delete-)<br>
* DELETE : [MFA Reset SMS Authenticator by Token](#MFAResetSMSAuthByToken-delete-)<br>
* DELETE : [Reset MFA Email OTP Authenticator By Access Token](#MFAResetEmailOtpAuthenticatorByAccessToken-delete-)<br>
* DELETE : [MFA Reset Security Question Authenticator By Access Token](#MFAResetSecurityQuestionAuthenticatorByAccessToken-delete-)<br>
* DELETE : [MFA Reset SMS Authenticator By UID](#MFAResetSMSAuthenticatorByUid-delete-)<br>
* DELETE : [MFA Reset Google Authenticator By UID](#MFAResetGoogleAuthenticatorByUid-delete-)<br>
* DELETE : [Reset MFA Email OTP Authenticator Settings by Uid](#MFAResetEmailOtpAuthenticatorByUid-delete-)<br>
* DELETE : [Reset MFA Security Question Authenticator Settings by Uid](#MFAResetSecurityQuestionAuthenticatorByUid-delete-)<br>




<h6 id="MFAUpdateSetting-put-"> Update MFA Setting (PUT)</h6>

 This API is used to trigger the Multi-factor authentication settings after login for secure actions  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/sms-authenticator/update-mfa-setting/)

 ```

access_token = "<access_token>" #Required
multi_factor_auth_model_with_lockout = {
"otp" : "<otp>"
}  #Required
fields = "<fields>" #Optional

result = loginradius.mfa.mfa_update_setting(access_token, multi_factor_auth_model_with_lockout, fields)
 ```




<h6 id="MFAUpdateByAccessToken-put-"> Update MFA by Access Token (PUT)</h6>

 This API is used to Enable Multi-factor authentication by access token on user login  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/google-authenticator/update-mfa-by-access-token/)

 ```

access_token = "<access_token>" #Required
multi_factor_auth_model_by_google_authenticator_code = {
"googleAuthenticatorCode" : "<googleAuthenticatorCode>"
}  #Required
fields = "<fields>" #Optional
sms_template = "<sms_template>" #Optional

result = loginradius.mfa.mfa_update_by_access_token(access_token, multi_factor_auth_model_by_google_authenticator_code, fields, sms_template)
 ```




<h6 id="MFAUpdatePhoneNumberByToken-put-"> MFA Update Phone Number by Token (PUT)</h6>

 This API is used to update the Multi-factor authentication phone number by sending the verification OTP to the provided phone number  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/sms-authenticator/mfa-update-phone-number-by-token/)

 ```

access_token = "<access_token>" #Required
phone_no2_f_a = "<phone_no2_f_a>" #Required
sms_template2_f_a = "<sms_template2_f_a>" #Optional

result = loginradius.mfa.mfa_update_phone_number_by_token(access_token, phone_no2_f_a, sms_template2_f_a)
 ```




<h6 id="MFAValidateEmailOtpByAccessToken-put-"> Verify MFA Email OTP by Access Token (PUT)</h6>

 This API is used to set up MFA Email OTP authenticator on profile after login.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/verify-mfa-otp-by-access-token/)

 ```

access_token = "<access_token>" #Required
multi_factor_auth_model_by_email_otp_with_lockout = {
"EmailId":"emailId",
"Otp":"otp"
}  #Required

result = loginradius.mfa.mfa_validate_email_otp_by_access_token(access_token, multi_factor_auth_model_by_email_otp_with_lockout)
 ```




<h6 id="MFASecurityQuestionAnswerByAccessToken-put-"> Update MFA Security Question by Access Token (PUT)</h6>

 This API is used to set up MFA Security Question authenticator on profile after login.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/update-mfa-security-question-by-access-token)

 ```

access_token = "<access_token>" #Required
security_question_answer_model_by_access_token = {
   "securityquestionanswer": [
        {
            "QuestionId": "db7****8a73e4******bd9****8c20",
            "Answer": "<answer>"
        }
    ],
     "ReplaceSecurityQuestionAnswer":"True"
}  #Required

result = loginradius.mfa.mfa_security_question_answer_by_access_token(access_token, security_question_answer_model_by_access_token)
 ```




<h6 id="MFAValidateOTPByPhone-put-"> MFA Validate OTP (PUT)</h6>

 This API is used to login via Multi-factor authentication by passing the One Time Password received via SMS  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/sms-authenticator/mfa-validate-otp/)

 ```

multi_factor_auth_model_with_lockout = {
"otp" : "<otp>"
}  #Required
second_factor_authentication_token = "<second_factor_authentication_token>" #Required
fields = "<fields>" #Optional
sms_template2_f_a = "<sms_template2_f_a>" #Optional
rba_browser_email_template = "<rba_browser_email_template>" #Optional
rba_city_email_template = "<rba_city_email_template>" #Optional
rba_country_email_template = "<rba_country_email_template>" #Optional
rba_ip_email_template = "<rba_ip_email_template>" #Optional

result = loginradius.mfa.mfa_validate_otp_by_phone(multi_factor_auth_model_with_lockout, second_factor_authentication_token, fields,sms_template2_f_a, rba_browser_email_template, rba_city_email_template, rba_country_email_template, rba_ip_email_template)
 ```




<h6 id="MFAValidateGoogleAuthCode-put-"> MFA Validate Google Auth Code (PUT)</h6>

 This API is used to login via Multi-factor-authentication by passing the google authenticator code.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/google-authenticator/mfa-validate-google-auth-code/)

 ```

google_authenticator_code = "<google_authenticator_code>" #Required
second_factor_authentication_token = "<second_factor_authentication_token>" #Required
fields = "<fields>" #Optional
rba_browser_email_template = "<rba_browser_email_template>" #Optional
rba_city_email_template = "<rba_city_email_template>" #Optional
rba_country_email_template = "<rba_country_email_template>" #Optional
rba_ip_email_template = "<rba_ip_email_template>" #Optional

result = loginradius.mfa.mfa_validate_google_auth_code(google_authenticator_code, second_factor_authentication_token, fields, rba_browser_email_template, rba_city_email_template, rba_country_email_template, rba_ip_email_template)
 ```




<h6 id="MFAValidateBackupCode-put-"> MFA Validate Backup code (PUT)</h6>

 This API is used to validate the backup code provided by the user and if valid, we return an access token allowing the user to login incases where Multi-factor authentication (MFA) is enabled and the secondary factor is unavailable. When a user initially downloads the Backup codes, We generate 10 codes, each code can only be consumed once. if any user attempts to go over the number of invalid login attempts configured in the Dashboard then the account gets blocked automatically  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/backup-codes/mfa-validate-backup-code/)

 ```

multi_factor_auth_model_by_backup_code = {
"backupCode" : "<backupCode>"
}  #Required
second_factor_authentication_token = "<second_factor_authentication_token>" #Required
fields = "<fields>" #Optional
rba_browser_email_template = "<rba_browser_email_template>" #Optional
rba_city_email_template = "<rba_city_email_template>" #Optional
rba_country_email_template = "<rba_country_email_template>" #Optional
rba_ip_email_template = "<rba_ip_email_template>" #Optional

result = loginradius.mfa.mfa_validate_backup_code(multi_factor_auth_model_by_backup_code, second_factor_authentication_token, fields, rba_browser_email_template, rba_city_email_template, rba_country_email_template, rba_ip_email_template)
 ```




<h6 id="MFAUpdatePhoneNumber-put-"> MFA Update Phone Number (PUT)</h6>

 This API is used to update (if configured) the phone number used for Multi-factor authentication by sending the verification OTP to the provided phone number  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/sms-authenticator/mfa-update-phone-number/)

 ```

phone_no2_f_a = "<phone_no2_f_a>" #Required
second_factor_authentication_token = "<second_factor_authentication_token>" #Required
sms_template2_f_a = "<sms_template2_f_a>" #Optional

result = loginradius.mfa.mfa_update_phone_number(phone_no2_f_a, second_factor_authentication_token, sms_template2_f_a)
 ```




<h6 id="MFAValidateEmailOtp-put-"> Verify MFA Email OTP by MFA Token (PUT)</h6>

 This API is used to Verify MFA Email OTP by MFA Token  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/verify-mfa-email-otp-by-mfa-token/)

 ```

multi_factor_auth_model_by_email_otp = {

    "EmailId":"email",
    "Otp":"otp"
}  #Required
second_factor_authentication_token = "<second_factor_authentication_token>" #Required
rba_browser_email_template = "<rba_browser_email_template>" #Optional
rba_city_email_template = "<rba_city_email_template>" #Optional
rba_country_email_template = "<rba_country_email_template>" #Optional
rba_ip_email_template = "<rba_ip_email_template>" #Optional

result = loginradius.mfa.mfa_validate_email_otp(multi_factor_auth_model_by_email_otp, second_factor_authentication_token, rba_browser_email_template, rba_city_email_template, rba_country_email_template, rba_ip_email_template)
 ```




<h6 id="MFASecurityQuestionAnswer-put-"> Update MFA Security Question by MFA Token (PUT)</h6>

 This API is used to set the security questions on the profile with the MFA token when MFA flow is required.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/update-mfa-security-question-by-mfa-token/)

 ```

security_question_answer_update_model = {
   "securityquestionanswer": [
        {
            "QuestionId": "db7****8a73e4******bd9****8c20",
            "Answer": "<answer>"
        }
    ]
}  #Required
second_factor_authentication_token = "<second_factor_authentication_token>" #Required

result = loginradius.mfa.mfa_security_question_answer(security_question_answer_update_model, second_factor_authentication_token)
 ```




<h6 id="MFALoginByEmail-post-"> MFA Email Login (POST)</h6>

 This API can be used to login by emailid on a Multi-factor authentication enabled LoginRadius site.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/mfa-email-login)

 ```

email = "<email>" #Required
password = "<password>" #Required
email_template = "<email_template>" #Optional
fields = "<fields>" #Optional
login_url = "<login_url>" #Optional
sms_template = "<sms_template>" #Optional
sms_template2_f_a = "<sms_template2_f_a>" #Optional
verification_url = "<verification_url>" #Optional
email_template2_f_a = "<email_template2_f_a>" #Optional


result = loginradius.mfa.mfa_login_by_email(email, password, email_template, fields, login_url, sms_template, sms_template2_f_a, verification_url,email_template2_f_a)
 ```




<h6 id="MFALoginByUserName-post-"> MFA UserName Login (POST)</h6>

 This API can be used to login by username on a Multi-factor authentication enabled LoginRadius site.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/mfa-user-name-login)

 ```

password = "<password>" #Required
username = "<username>" #Required
email_template = "<email_template>" #Optional
fields = "<fields>" #Optional
login_url = "<login_url>" #Optional
sms_template = "<sms_template>" #Optional
sms_template2_f_a = "<sms_template2_f_a>" #Optional
verification_url = "<verification_url>" #Optional
email_template2_f_a = "<email_template2_f_a>" #Optional


result = loginradius.mfa.mfa_login_by_user_name(password, username, email_template, fields, login_url, sms_template, sms_template2_f_a, verification_url,email_template2_f_a)
 ```




<h6 id="MFALoginByPhone-post-"> MFA Phone Login (POST)</h6>

 This API can be used to login by Phone on a Multi-factor authentication enabled LoginRadius site.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/mfa-phone-login)

 ```

password = "<password>" #Required
phone = "<phone>" #Required
email_template = "<email_template>" #Optional
fields = "<fields>" #Optional
login_url = "<login_url>" #Optional
sms_template = "<sms_template>" #Optional
sms_template2_f_a = "<sms_template2_f_a>" #Optional
verification_url = "<verification_url>" #Optional
email_template2_f_a = "<email_template2_f_a>" #Optional


result = loginradius.mfa.mfa_login_by_phone(password, phone, email_template, fields, login_url, sms_template, sms_template2_f_a, verification_url,email_template2_f_a)
 ```




<h6 id="MFAEmailOTP-post-"> Send MFA Email OTP by MFA Token (POST)</h6>

 An API designed to send the MFA Email OTP to the email.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/send-mfa-email-otp-by-mfa-token/)

 ```

email_id_model = {
  "EmailId":"email"
 }  #Required
second_factor_authentication_token = "<second_factor_authentication_token>" #Required
email_template2_f_a = "<email_template2_f_a>" #Optional

result = loginradius.mfa.mfa_email_otp(email_id_model, second_factor_authentication_token, email_template2_f_a)
 ```




<h6 id="MFASecurityQuestionAnswerVerification-post-"> Verify MFA Security Question by MFA Token (POST)</h6>

 This API is used to resending the verification OTP to the provided phone number  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/verify-mfa-security-question-by-mfa-token/)

 ```

security_question_answer_update_model = {
   "securityquestionanswer": [
        {
            "QuestionId": "db7****8a73e4******bd9****8c20",
            "Answer": "<answer>"
        }
    ]
 }  #Required
second_factor_authentication_token = "<second_factor_authentication_token>" #Required
rba_browser_email_template = "<rba_browser_email_template>" #Optional
rba_city_email_template = "<rba_city_email_template>" #Optional
rba_country_email_template = "<rba_country_email_template>" #Optional
rba_ip_email_template = "<rba_ip_email_template>" #Optional

result = loginradius.mfa.mfa_security_question_answer_verification(security_question_answer_update_model, second_factor_authentication_token, rba_browser_email_template, rba_city_email_template, rba_country_email_template, rba_ip_email_template)
 ```




<h6 id="MFAConfigureByAccessToken-get-"> MFA Validate Access Token (GET)</h6>

 This API is used to configure the Multi-factor authentication after login by using the access token when MFA is set as optional on the LoginRadius site.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/mfa-validate-access-token/)

 ```

access_token = "<access_token>" #Required
sms_template2_f_a = "<sms_template2_f_a>" #Optional

result = loginradius.mfa.mfa_configure_by_access_token(access_token, sms_template2_f_a)
 ```




<h6 id="MFABackupCodeByAccessToken-get-"> MFA Backup Code by Access Token (GET)</h6>

 This API is used to get a set of backup codes via access token to allow the user login on a site that has Multi-factor Authentication enabled in the event that the user does not have a secondary factor available. We generate 10 codes, each code can only be consumed once. If any user attempts to go over the number of invalid login attempts configured in the Dashboard then the account gets blocked automatically  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/backup-codes/mfa-backup-code-by-access-token/)

 ```

access_token = "<access_token>" #Required

result = loginradius.mfa.mfa_backup_code_by_access_token(access_token)
 ```




<h6 id="MFAResetBackupCodeByAccessToken-get-"> Reset Backup Code by Access Token (GET)</h6>

 API is used to reset the backup codes on a given account via the access token. This API call will generate 10 new codes, each code can only be consumed once  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/backup-codes/mfa-reset-backup-code-by-access-token/)

 ```

access_token = "<access_token>" #Required

result = loginradius.mfa.mfa_reset_backup_code_by_access_token(access_token)
 ```




<h6 id="MFAEmailOtpByAccessToken-get-"> Send MFA Email OTP by Access Token (GET)</h6>

 This API is created to send the OTP to the email if email OTP authenticator is enabled in app's MFA configuration.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/send-mfa-email-otp-by-access-token/)

 ```

access_token = "<access_token>" #Required
email_id = "<email_id>" #Required
email_template2_f_a = "<email_template2_f_a>" #Optional

result = loginradius.mfa.mfa_email_otp_by_access_token(access_token, email_id, email_template2_f_a)
 ```




<h6 id="MFAResendOTP-get-"> MFA Resend Otp (GET)</h6>

 This API is used to resending the verification OTP to the provided phone number  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/resend-twofactorauthentication-otp/)

 ```

second_factor_authentication_token = "<second_factor_authentication_token>" #Required
sms_template2_f_a = "<sms_template2_f_a>" #Optional

result = loginradius.mfa.mfa_resend_otp(second_factor_authentication_token, sms_template2_f_a)
 ```




<h6 id="MFABackupCodeByUid-get-"> MFA Backup Code by UID (GET)</h6>

 This API is used to reset the backup codes on a given account via the UID. This API call will generate 10 new codes, each code can only be consumed once.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/backup-codes/mfa-backup-code-by-uid/)

 ```

uid = "<uid>" #Required

result = loginradius.mfa.mfa_backup_code_by_uid(uid)
 ```




<h6 id="MFAResetBackupCodeByUid-get-"> MFA Reset Backup Code by UID (GET)</h6>

 This API is used to reset the backup codes on a given account via the UID. This API call will generate 10 new codes, each code can only be consumed once.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/backup-codes/mfa-reset-backup-code-by-uid/)

 ```

uid = "<uid>" #Required

result = loginradius.mfa.mfa_reset_backup_code_by_uid(uid)
 ```




<h6 id="MFAResetGoogleAuthByToken-delete-"> MFA Reset Google Authenticator by Token (DELETE)</h6>

 This API Resets the Google Authenticator configurations on a given account via the access token  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/google-authenticator/mfa-reset-google-authenticator-by-token/)

 ```

access_token = "<access_token>" #Required
googleauthenticator = "True" #Required

result = loginradius.mfa.mfa_reset_google_auth_by_token(access_token, googleauthenticator)
 ```




<h6 id="MFAResetSMSAuthByToken-delete-"> MFA Reset SMS Authenticator by Token (DELETE)</h6>

 This API resets the SMS Authenticator configurations on a given account via the access token.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/sms-authenticator/mfa-reset-sms-authenticator-by-token/)

 ```

access_token = "<access_token>" #Required
otpauthenticator = "True" #Required

result = loginradius.mfa.mfa_reset_sms_auth_by_token(access_token, otpauthenticator)
 ```




<h6 id="MFAResetEmailOtpAuthenticatorByAccessToken-delete-"> Reset MFA Email OTP Authenticator By Access Token (DELETE)</h6>

 This API is used to reset the Email OTP Authenticator settings for an MFA-enabled user  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/reset-mfa-email-otp-authenticator-access-token/)

 ```

access_token = "<access_token>" #Required

result = loginradius.mfa.mfa_reset_email_otp_authenticator_by_access_token(access_token)
 ```




<h6 id="MFAResetSecurityQuestionAuthenticatorByAccessToken-delete-"> MFA Reset Security Question Authenticator By Access Token (DELETE)</h6>

 This API is used to Reset MFA Security Question Authenticator By Access Token  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/reset-mfa-security-question-by-access-token/)

 ```

access_token = "<access_token>" #Required

result = loginradius.mfa.mfa_reset_security_question_authenticator_by_access_token(access_token)
 ```




<h6 id="MFAResetSMSAuthenticatorByUid-delete-"> MFA Reset SMS Authenticator By UID (DELETE)</h6>

 This API resets the SMS Authenticator configurations on a given account via the UID.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/sms-authenticator/mfa-reset-sms-authenticator-by-uid/)

 ```

otpauthenticator = "True" #Required
uid = "<uid>" #Required

result = loginradius.mfa.mfa_reset_sms_authenticator_by_uid(otpauthenticator, uid)
 ```




<h6 id="MFAResetGoogleAuthenticatorByUid-delete-"> MFA Reset Google Authenticator By UID (DELETE)</h6>

 This API resets the Google Authenticator configurations on a given account via the UID.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/google-authenticator/mfa-reset-google-authenticator-by-uid/)

 ```

googleauthenticator = "True" #Required
uid = "<uid>" #Required

result = loginradius.mfa.mfa_reset_google_authenticator_by_uid(googleauthenticator, uid)
 ```




<h6 id="MFAResetEmailOtpAuthenticatorByUid-delete-"> Reset MFA Email OTP Authenticator Settings by Uid (DELETE)</h6>

 This API is used to reset the Email OTP Authenticator settings for an MFA-enabled user.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/backup-codes/reset-mfa-email-otp-authenticator-settings-by-uid/)

 ```

uid = "<uid>" #Required

result = loginradius.mfa.mfa_reset_email_otp_authenticator_by_uid(uid)
 ```




<h6 id="MFAResetSecurityQuestionAuthenticatorByUid-delete-"> Reset MFA Security Question Authenticator Settings by Uid (DELETE)</h6>

 This API is used to reset the Security Question Authenticator settings for an MFA-enabled user.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/backup-codes/reset-mfa-security-question-authenticator-settings-by-uid/)

 ```

uid = "<uid>" #Required

result = loginradius.mfa.mfa_reset_security_question_authenticator_by_uid(uid)
 ```






### PINAuthentication API


List of APIs in this Section:<br>

* PUT : [Reset PIN By ResetToken](#ResetPINByResetToken-put-)<br>
* PUT : [Reset PIN By SecurityAnswer And Email](#ResetPINByEmailAndSecurityAnswer-put-)<br>
* PUT : [Reset PIN By SecurityAnswer And Username](#ResetPINByUsernameAndSecurityAnswer-put-)<br>
* PUT : [Reset PIN By SecurityAnswer And Phone](#ResetPINByPhoneAndSecurityAnswer-put-)<br>
* PUT : [Change PIN By Token](#ChangePINByAccessToken-put-)<br>
* PUT : [Reset PIN by Phone and OTP](#ResetPINByPhoneAndOtp-put-)<br>
* PUT : [Reset PIN by Email and OTP](#ResetPINByEmailAndOtp-put-)<br>
* PUT : [Reset PIN by Username and OTP](#ResetPINByUsernameAndOtp-put-)<br>
* POST : [PIN Login](#PINLogin-post-)<br>
* POST : [Forgot PIN By Email](#SendForgotPINEmailByEmail-post-)<br>
* POST : [Forgot PIN By UserName](#SendForgotPINEmailByUsername-post-)<br>
* POST : [Forgot PIN By Phone](#SendForgotPINSMSByPhone-post-)<br>
* POST : [Set PIN By PinAuthToken](#SetPINByPinAuthToken-post-)<br>
* GET : [Invalidate PIN Session Token](#InValidatePinSessionToken-get-)<br>




<h6 id="ResetPINByResetToken-put-"> Reset PIN By ResetToken (PUT)</h6>

 This API is used to reset pin using reset token.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/pin-authentication/reset-pin-by-resettoken/)

 ```

reset_pin_by_reset_token = {
"pin" : "<pin>",
"resetToken" : "<resetToken>"
}  #Required

result = loginradius.pin_authentication.reset_pin_by_reset_token(reset_pin_by_reset_token)
 ```




<h6 id="ResetPINByEmailAndSecurityAnswer-put-"> Reset PIN By SecurityAnswer And Email (PUT)</h6>

 This API is used to reset pin using security question answer and email.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/pin-authentication/reset-pin-by-securityanswer-and-email/)

 ```

reset_pin_by_security_question_answer_and_email_model = {
"email" : "<email>",
"pin" : "<pin>",
"securityAnswer" : {"QuestionID":"Answer"}
}  #Required

result = loginradius.pin_authentication.reset_pin_by_email_and_security_answer(reset_pin_by_security_question_answer_and_email_model)
 ```




<h6 id="ResetPINByUsernameAndSecurityAnswer-put-"> Reset PIN By SecurityAnswer And Username (PUT)</h6>

 This API is used to reset pin using security question answer and username.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/pin-authentication/reset-pin-by-securityanswer-and-username/)

 ```

reset_pin_by_security_question_answer_and_username_model = {
"pin" : "<pin>",
"securityAnswer" : {"QuestionID":"Answer"},
"username" : "<username>"
}  #Required

result = loginradius.pin_authentication.reset_pin_by_username_and_security_answer(reset_pin_by_security_question_answer_and_username_model)
 ```




<h6 id="ResetPINByPhoneAndSecurityAnswer-put-"> Reset PIN By SecurityAnswer And Phone (PUT)</h6>

 This API is used to reset pin using security question answer and phone.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/pin-authentication/reset-pin-by-securityanswer-and-phone/)

 ```

reset_pin_by_security_question_answer_and_phone_model = {
"phone" : "<phone>",
"pin" : "<pin>",
"securityAnswer" : {"QuestionID":"Answer"}
}  #Required

result = loginradius.pin_authentication.reset_pin_by_phone_and_security_answer(reset_pin_by_security_question_answer_and_phone_model)
 ```




<h6 id="ChangePINByAccessToken-put-"> Change PIN By Token (PUT)</h6>

 This API is used to change a user's PIN using access token.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/pin-authentication/change-pin-by-access-token/)

 ```

access_token = "<access_token>" #Required
change_pin_model = {
"newPIN" : "<newPIN>",
"oldPIN" : "<oldPIN>"
}  #Required

result = loginradius.pin_authentication.change_pin_by_access_token(access_token, change_pin_model)
 ```




<h6 id="ResetPINByPhoneAndOtp-put-"> Reset PIN by Phone and OTP (PUT)</h6>

 This API is used to reset pin using phoneId and OTP.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/pin-authentication/reset-pin-by-phone-and-otp/)

 ```

reset_pin_by_phone_and_otp_model = {
"otp" : "<otp>",
"phone" : "<phone>",
"pin" : "<pin>"
}  #Required

result = loginradius.pin_authentication.reset_pin_by_phone_and_otp(reset_pin_by_phone_and_otp_model)
 ```




<h6 id="ResetPINByEmailAndOtp-put-"> Reset PIN by Email and OTP (PUT)</h6>

 This API is used to reset pin using email and OTP.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/pin-authentication/reset-pin-by-email-and-otp/)

 ```

reset_pin_by_email_and_otp_model = {
"email" : "<email>",
"otp" : "<otp>",
"pin" : "<pin>"
}  #Required

result = loginradius.pin_authentication.reset_pin_by_email_and_otp(reset_pin_by_email_and_otp_model)
 ```




<h6 id="ResetPINByUsernameAndOtp-put-"> Reset PIN by Username and OTP (PUT)</h6>

 This API is used to reset pin using username and OTP.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/pin-authentication/reset-pin-by-username-and-otp/)

 ```

reset_pin_by_username_and_otp_model = {
"otp" : "<otp>",
"pin" : "<pin>",
"username" : "<username>"
}  #Required

result = loginradius.pin_authentication.reset_pin_by_username_and_otp(reset_pin_by_username_and_otp_model)
 ```




<h6 id="PINLogin-post-"> PIN Login (POST)</h6>

 This API is used to login a user by pin and session token.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/pin-authentication/login-by-pin/)

 ```

login_by_pin_model = {
"pin" : "<pin>"
}  #Required
session_token = "<session_token>" #Required

result = loginradius.pin_authentication.pin_login(login_by_pin_model, session_token)
 ```




<h6 id="SendForgotPINEmailByEmail-post-"> Forgot PIN By Email (POST)</h6>

 This API sends the reset pin email to specified email address.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/pin-authentication/forgot-pin-by-email/)

 ```

forgot_pin_link_by_email_model = {
"email" : "<email>"
}  #Required
email_template = "<email_template>" #Optional
reset_pin_url = "<reset_pin_url>" #Optional

result = loginradius.pin_authentication.send_forgot_pin_email_by_email(forgot_pin_link_by_email_model, email_template, reset_pin_url)
 ```




<h6 id="SendForgotPINEmailByUsername-post-"> Forgot PIN By UserName (POST)</h6>

 This API sends the reset pin email using username.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/pin-authentication/forgot-pin-by-username/)

 ```

forgot_pin_link_by_user_name_model = {
"userName" : "<userName>"
}  #Required
email_template = "<email_template>" #Optional
reset_pin_url = "<reset_pin_url>" #Optional

result = loginradius.pin_authentication.send_forgot_pin_email_by_username(forgot_pin_link_by_user_name_model, email_template, reset_pin_url)
 ```




<h6 id="SendForgotPINSMSByPhone-post-"> Forgot PIN By Phone (POST)</h6>

 This API sends the OTP to specified phone number  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/pin-authentication/forgot-pin-by-phone/)

 ```

forgot_pin_otp_by_phone_model = {
"phone" : "<phone>"
}  #Required
sms_template = "<sms_template>" #Optional

result = loginradius.pin_authentication.send_forgot_pin_sms_by_phone(forgot_pin_otp_by_phone_model, sms_template)
 ```




<h6 id="SetPINByPinAuthToken-post-"> Set PIN By PinAuthToken (POST)</h6>

 This API is used to change a user's PIN using Pin Auth token.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/pin-authentication/set-pin-by-pinauthtoken/)

 ```

pin_required_model = {
"pin" : "<pin>"
}  #Required
pin_auth_token = "<pin_auth_token>" #Required

result = loginradius.pin_authentication.set_pin_by_pin_auth_token(pin_required_model, pin_auth_token)
 ```




<h6 id="InValidatePinSessionToken-get-"> Invalidate PIN Session Token (GET)</h6>

 This API is used to invalidate pin session token.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/pin-authentication/invalidate-pin-session-token/)

 ```

session_token = "<session_token>" #Required

result = loginradius.pin_authentication.in_validate_pin_session_token(session_token)
 ```






### ReAuthentication API


List of APIs in this Section:<br>

* PUT : [Validate MFA by OTP](#MFAReAuthenticateByOTP-put-)<br>
* PUT : [Validate MFA by Backup Code](#MFAReAuthenticateByBackupCode-put-)<br>
* PUT : [Validate MFA by Google Authenticator Code](#MFAReAuthenticateByGoogleAuth-put-)<br>
* PUT : [Validate MFA by Password](#MFAReAuthenticateByPassword-put-)<br>
* PUT : [MFA Re-authentication by PIN](#VerifyPINAuthentication-put-)<br>
* PUT : [MFA Re-authentication by Email OTP](#ReAuthValidateEmailOtp-put-)<br>
* POST : [Verify Multifactor OTP Authentication](#VerifyMultiFactorOtpReauthentication-post-)<br>
* POST : [Verify Multifactor Password Authentication](#VerifyMultiFactorPasswordReauthentication-post-)<br>
* POST : [Verify Multifactor PIN Authentication](#VerifyMultiFactorPINReauthentication-post-)<br>
* POST : [MFA Re-authentication by Security Question](#ReAuthBySecurityQuestion-post-)<br>
* GET : [Multi Factor Re-Authenticate](#MFAReAuthenticate-get-)<br>
* GET : [Send MFA Re-auth Email OTP by Access Token](#ReAuthSendEmailOtp-get-)<br>




<h6 id="MFAReAuthenticateByOTP-put-"> Validate MFA by OTP (PUT)</h6>

 This API is used to re-authenticate via Multi-factor authentication by passing the One Time Password received via SMS  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/re-authentication/mfa/re-auth-by-otp/)

 ```

access_token = "<access_token>" #Required
reauth_by_otp_model = {
"otp" : "<otp>"
}  #Required

result = loginradius.re_authentication.mfa_re_authenticate_by_otp(access_token, reauth_by_otp_model)
 ```




<h6 id="MFAReAuthenticateByBackupCode-put-"> Validate MFA by Backup Code (PUT)</h6>

 This API is used to re-authenticate by set of backup codes via access token on the site that has Multi-factor authentication enabled in re-authentication for the user that does not have the device  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/re-authentication/mfa/re-auth-by-backup-code/)

 ```

access_token = "<access_token>" #Required
reauth_by_backup_code_model = {
"backupCode" : "<backupCode>"
}  #Required

result = loginradius.re_authentication.mfa_re_authenticate_by_backup_code(access_token, reauth_by_backup_code_model)
 ```




<h6 id="MFAReAuthenticateByGoogleAuth-put-"> Validate MFA by Google Authenticator Code (PUT)</h6>

 This API is used to re-authenticate via Multi-factor-authentication by passing the google authenticator code  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/re-authentication/re-auth-by-google-authenticator-code)

 ```

access_token = "<access_token>" #Required
reauth_by_google_authenticator_code_model = {
"googleAuthenticatorCode" : "<googleAuthenticatorCode>"
}  #Required

result = loginradius.re_authentication.mfa_re_authenticate_by_google_auth(access_token, reauth_by_google_authenticator_code_model)
 ```




<h6 id="MFAReAuthenticateByPassword-put-"> Validate MFA by Password (PUT)</h6>

 This API is used to re-authenticate via Multi-factor-authentication by passing the password  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/re-authentication/re-auth-by-password)

 ```

access_token = "<access_token>" #Required
password_event_based_auth_model_with_lockout = {
"password" : "<password>"
}  #Required
sms_template2_f_a = "<sms_template2_f_a>" #Optional

result = loginradius.re_authentication.mfa_re_authenticate_by_password(access_token, password_event_based_auth_model_with_lockout, sms_template2_f_a)
 ```




<h6 id="VerifyPINAuthentication-put-"> MFA Re-authentication by PIN (PUT)</h6>

 This API is used to validate the triggered MFA authentication flow with a password.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/re-authentication/pin/re-auth-by-pin/)

 ```

access_token = "<access_token>" #Required
pin_auth_event_based_auth_model_with_lockout = {
"pin" : "<pin>"
}  #Required
sms_template2_f_a = "<sms_template2_f_a>" #Optional

result = loginradius.re_authentication.verify_pin_authentication(access_token, pin_auth_event_based_auth_model_with_lockout, sms_template2_f_a)
 ```




<h6 id="ReAuthValidateEmailOtp-put-"> MFA Re-authentication by Email OTP (PUT)</h6>

 This API is used to validate the triggered MFA authentication flow with an Email OTP.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/re-authentication/mfa-re-auth-by-email-otp/)

 ```

access_token = "<access_token>" #Required
reauth_by_email_otp_model = {
  "EmailId":"email",
  "otp": "otp"
}  #Required

result = loginradius.re_authentication.re_auth_validate_email_otp(access_token, reauth_by_email_otp_model)
 ```




<h6 id="VerifyMultiFactorOtpReauthentication-post-"> Verify Multifactor OTP Authentication (POST)</h6>

 This API is used on the server-side to validate and verify the re-authentication token created by the MFA re-authentication API. This API checks re-authentications created by OTP.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/re-authentication/mfa/re-auth-validate-mfa/)

 ```

event_based_multi_factor_token = {
"secondFactorValidationToken" : "<secondFactorValidationToken>"
}  #Required
uid = "<uid>" #Required

result = loginradius.re_authentication.verify_multi_factor_otp_reauthentication(event_based_multi_factor_token, uid)
 ```




<h6 id="VerifyMultiFactorPasswordReauthentication-post-"> Verify Multifactor Password Authentication (POST)</h6>

 This API is used on the server-side to validate and verify the re-authentication token created by the MFA re-authentication API. This API checks re-authentications created by password.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/re-authentication/re-auth-validate-password/)

 ```

event_based_multi_factor_token = {
"secondFactorValidationToken" : "<secondFactorValidationToken>"
}  #Required
uid = "<uid>" #Required

result = loginradius.re_authentication.verify_multi_factor_password_reauthentication(event_based_multi_factor_token, uid)
 ```




<h6 id="VerifyMultiFactorPINReauthentication-post-"> Verify Multifactor PIN Authentication (POST)</h6>

 This API is used on the server-side to validate and verify the re-authentication token created by the MFA re-authentication API. This API checks re-authentications created by PIN.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/re-authentication/pin/re-auth-validate-pin/)

 ```

event_based_multi_factor_token = {
"secondFactorValidationToken" : "<secondFactorValidationToken>"
}  #Required
uid = "<uid>" #Required

result = loginradius.re_authentication.verify_multi_factor_pin_reauthentication(event_based_multi_factor_token, uid)
 ```




<h6 id="ReAuthBySecurityQuestion-post-"> MFA Re-authentication by Security Question (POST)</h6>

 This API is used to validate the triggered MFA re-authentication flow with security questions answers.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/re-authentication/mfa-re-authentication-by-security-question/)

 ```

access_token = "<access_token>" #Required
security_question_answer_update_model = {
   "securityquestionanswer": [
        {
            "QuestionId": "db7****8a73e4******bd9****8c20",
            "Answer": "<answer>"
        }
    ]
}  #Required

result = loginradius.re_authentication.re_auth_by_security_question(access_token, security_question_answer_update_model)
 ```




<h6 id="MFAReAuthenticate-get-"> Multi Factor Re-Authenticate (GET)</h6>

 This API is used to trigger the Multi-Factor Autentication workflow for the provided access token  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/re-authentication/re-auth-trigger/)

 ```

access_token = "<access_token>" #Required
sms_template2_f_a = "<sms_template2_f_a>" #Optional

result = loginradius.re_authentication.mfa_re_authenticate(access_token, sms_template2_f_a)
 ```




<h6 id="ReAuthSendEmailOtp-get-"> Send MFA Re-auth Email OTP by Access Token (GET)</h6>

 This API is used to send the MFA Email OTP to the email for Re-authentication  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/multi-factor-authentication/re-authentication/send-mfa-re-auth-email-otp-by-access-token/)

 ```

access_token = "<access_token>" #Required
email_id = "<email_id>" #Required
email_template2_f_a = "<email_template2_f_a>" #Optional

result = loginradius.re_authentication.re_auth_send_email_otp(access_token, email_id, email_template2_f_a)
 ```






### ConsentManagement API


List of APIs in this Section:<br>

* PUT : [Update Consent By Access Token](#UpdateConsentProfileByAccessToken-put-)<br>
* POST : [Consent By ConsentToken](#SubmitConsentByConsentToken-post-)<br>
* POST : [Post Consent By Access Token](#SubmitConsentByAccessToken-post-)<br>
* GET : [Get Consent Logs By Uid](#GetConsentLogsByUid-get-)<br>
* GET : [Get Consent Log by Access Token](#GetConsentLogs-get-)<br>
* GET : [Get Verify Consent By Access Token](#VerifyConsentByAccessToken-get-)<br>




<h6 id="UpdateConsentProfileByAccessToken-put-"> Update Consent By Access Token (PUT)</h6>

 This API is to update consents using access token.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/consent-management/update-consent-by-access-token/)

 ```

access_token = "<access_token>" #Required
consent_update_model = {
"consents" : [   {
 "consentOptionId" : "<consentOptionId>"  ,
"isAccepted" : "True"  
}  ]
}  #Required

result = loginradius.consent_management.update_consent_profile_by_access_token(access_token, consent_update_model)
 ```




<h6 id="SubmitConsentByConsentToken-post-"> Consent By ConsentToken (POST)</h6>

 This API is to submit consent form using consent token.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/consent-management/consent-by-consent-token/)

 ```

consent_token = "<consent_token>" #Required
consent_submit_model = {
"data" : [   {
 "consentOptionId" : "<consentOptionId>"  ,
"isAccepted" : "True"  
}  ] ,
"events" : [   {
 "event" : "<event>"  ,
"isCustom" : "True"  
}  ]
}  #Required

result = loginradius.consent_management.submit_consent_by_consent_token(consent_token, consent_submit_model)
 ```




<h6 id="SubmitConsentByAccessToken-post-"> Post Consent By Access Token (POST)</h6>

 API to provide a way to end user to submit a consent form for particular event type.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/consent-management/consent-by-access-token/)

 ```

access_token = "<access_token>" #Required
consent_submit_model = {
"data" : [   {
 "consentOptionId" : "<consentOptionId>"  ,
"isAccepted" : "True"  
}  ] ,
"events" : [   {
 "event" : "<event>"  ,
"isCustom" : "True"  
}  ]
}  #Required

result = loginradius.consent_management.submit_consent_by_access_token(access_token, consent_submit_model)
 ```




<h6 id="GetConsentLogsByUid-get-"> Get Consent Logs By Uid (GET)</h6>

 This API is used to get the Consent logs of the user.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/consent-management/consent-log-by-uid/)

 ```

uid = "<uid>" #Required

result = loginradius.consent_management.get_consent_logs_by_uid(uid)
 ```




<h6 id="GetConsentLogs-get-"> Get Consent Log by Access Token (GET)</h6>

 This API is used to fetch consent logs.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/consent-management/consent-log-by-access-token/)

 ```

access_token = "<access_token>" #Required

result = loginradius.consent_management.get_consent_logs(access_token)
 ```




<h6 id="VerifyConsentByAccessToken-get-"> Get Verify Consent By Access Token (GET)</h6>

 This API is used to check if consent is submitted for a particular event or not.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/consent-management/verify-consent-by-access-token/)

 ```

access_token = "<access_token>" #Required
event = "<event>" #Required
is_custom = "True" #Required

result = loginradius.consent_management.verify_consent_by_access_token(access_token, event, is_custom)
 ```






### SmartLogin API


List of APIs in this Section:<br>

* GET : [Smart Login Verify Token](#SmartLoginTokenVerification-get-)<br>
* GET : [Smart Login By Email](#SmartLoginByEmail-get-)<br>
* GET : [Smart Login By Username](#SmartLoginByUserName-get-)<br>
* GET : [Smart Login Ping](#SmartLoginPing-get-)<br>




<h6 id="SmartLoginTokenVerification-get-"> Smart Login Verify Token (GET)</h6>

 This API verifies the provided token for Smart Login  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/smart-login/smart-login-verify-token/)

 ```

verification_token = "<verification_token>" #Required
welcome_email_template = "<welcome_email_template>" #Optional

result = loginradius.smart_login.smart_login_token_verification(verification_token, welcome_email_template)
 ```




<h6 id="SmartLoginByEmail-get-"> Smart Login By Email (GET)</h6>

 This API sends a Smart Login link to the user's Email Id.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/smart-login/smart-login-by-email)

 ```

client_guid = "<client_guid>" #Required
email = "<email>" #Required
redirect_url = "<redirect_url>" #Optional
smart_login_email_template = "<smart_login_email_template>" #Optional
welcome_email_template = "<welcome_email_template>" #Optional

result = loginradius.smart_login.smart_login_by_email(client_guid, email, redirect_url, smart_login_email_template, welcome_email_template)
 ```




<h6 id="SmartLoginByUserName-get-"> Smart Login By Username (GET)</h6>

 This API sends a Smart Login link to the user's Email Id.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/smart-login/smart-login-by-username)

 ```

client_guid = "<client_guid>" #Required
username = "<username>" #Required
redirect_url = "<redirect_url>" #Optional
smart_login_email_template = "<smart_login_email_template>" #Optional
welcome_email_template = "<welcome_email_template>" #Optional

result = loginradius.smart_login.smart_login_by_user_name(client_guid, username, redirect_url, smart_login_email_template, welcome_email_template)
 ```




<h6 id="SmartLoginPing-get-"> Smart Login Ping (GET)</h6>

 This API is used to check if the Smart Login link has been clicked or not  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/smart-login/smart-login-ping)

 ```

client_guid = "<client_guid>" #Required
fields = "<fields>" #Optional

result = loginradius.smart_login.smart_login_ping(client_guid, fields)
 ```






### OneTouchLogin API


List of APIs in this Section:<br>

* PUT : [One Touch OTP Verification](#OneTouchLoginOTPVerification-put-)<br>
* POST : [One Touch Login by Email](#OneTouchLoginByEmail-post-)<br>
* POST : [One Touch Login by Phone](#OneTouchLoginByPhone-post-)<br>
* GET : [One Touch Email Verification](#OneTouchEmailVerification-get-)<br>
* GET : [One Touch Login Ping](#OneTouchLoginPing-get-)<br>




<h6 id="OneTouchLoginOTPVerification-put-"> One Touch OTP Verification (PUT)</h6>

 This API is used to verify the otp for One Touch Login.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/one-touch-login/one-touch-otp-verification/)

 ```

otp = "<otp>" #Required
phone = "<phone>" #Required
fields = "<fields>" #Optional
sms_template = "<sms_template>" #Optional

result = loginradius.one_touch_login.one_touch_login_otp_verification(otp, phone, fields, sms_template)
 ```




<h6 id="OneTouchLoginByEmail-post-"> One Touch Login by Email (POST)</h6>

 This API is used to send a link to a specified email for a frictionless login/registration  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/one-touch-login/one-touch-login-by-email-captcha/)

 ```

one_touch_login_by_email_model = {
"clientguid" : "<clientguid>",
"email" : "<email>",
"g-recaptcha-response" : "<g-recaptcha-response>"
}  #Required
one_touch_login_email_template = "<one_touch_login_email_template>" #Optional
redirecturl = "<redirecturl>" #Optional
welcomeemailtemplate = "<welcomeemailtemplate>" #Optional

result = loginradius.one_touch_login.one_touch_login_by_email(one_touch_login_by_email_model, one_touch_login_email_template, redirecturl, welcomeemailtemplate)
 ```




<h6 id="OneTouchLoginByPhone-post-"> One Touch Login by Phone (POST)</h6>

 This API is used to send one time password to a given phone number for a frictionless login/registration.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/one-touch-login/one-touch-login-by-phone-captcha/)

 ```

one_touch_login_by_phone_model = {
"g-recaptcha-response" : "<g-recaptcha-response>",
"phone" : "<phone>"
}  #Required
sms_template = "<sms_template>" #Optional

result = loginradius.one_touch_login.one_touch_login_by_phone(one_touch_login_by_phone_model, sms_template)
 ```




<h6 id="OneTouchEmailVerification-get-"> One Touch Email Verification (GET)</h6>

 This API verifies the provided token for One Touch Login  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/one-touch-login/one-touch-email-verification)

 ```

verification_token = "<verification_token>" #Required
welcome_email_template = "<welcome_email_template>" #Optional

result = loginradius.one_touch_login.one_touch_email_verification(verification_token, welcome_email_template)
 ```




<h6 id="OneTouchLoginPing-get-"> One Touch Login Ping (GET)</h6>

 This API is used to check if the One Touch Login link has been clicked or not.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/one-touch-login/one-touch-login-ping/)

 ```

client_guid = "<client_guid>" #Required
fields = "<fields>" #Optional

result = loginradius.one_touch_login.one_touch_login_ping(client_guid, fields)
 ```






### PasswordLessLogin API


List of APIs in this Section:<br>

* PUT : [Passwordless Login Phone Verification](#PasswordlessLoginPhoneVerification-put-)<br>
* POST :[Passwordless Login Verification By Email And OTP](#PasswordlessLoginVerificationByEmailAndOTP-post-)<br>
* POST :[Passwordless Login Verification By User Name And OTP](#PasswordlessLoginVerificationByUserNameAndOTP-post-)<br>
* GET : [Passwordless Login by Phone](#PasswordlessLoginByPhone-get-)<br>
* GET : [Passwordless Login By Email](#PasswordlessLoginByEmail-get-)<br>
* GET : [Passwordless Login By UserName](#PasswordlessLoginByUserName-get-)<br>
* GET : [Passwordless Login Verification](#PasswordlessLoginVerification-get-)<br>




<h6 id="PasswordlessLoginPhoneVerification-put-"> Passwordless Login Phone Verification (PUT)</h6>

 This API verifies an account by OTP and allows the customer to login.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/passwordless-login/passwordless-login-phone-verification)

 ```

password_less_login_otp_model = {
"otp" : "<otp>",
"phone" : "<phone>"
}  #Required
fields = "<fields>" #Optional
sms_template = "<sms_template>" #Optional

result = loginradius.password_less_login.passwordless_login_phone_verification(password_less_login_otp_model, fields, sms_template)
 ```


<h6 id="PasswordlessLoginVerificationByEmailAndOTP-post-">Passwordless Login Verification By Email And OTP (POST)</h6>

 This API is used to verify the otp sent to the email when doing a passwordless login.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/passwordless-login/passwordless-login-verify-by-email-and-otp/)

 ```

password_less_login_by_email_and_otp_model = {
  "email": "<email>",
  "otp": "<otp>",
  "welcomeemailtemplate": "<welcome_email_template>"
}  #Required
fields = "<fields>" #Optional

result = loginradius.password_less_login.passwordless_login_verification_by_email_and_otp(password_less_login_by_email_and_otp_model, fields)
 ```



<h6 id="PasswordlessLoginVerificationByUserNameAndOTP-post-">Passwordless Login Verification By User Name And OTP (POST)</h6>

This API is used to verify the otp sent to the email when doing a passwordless login.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/passwordless-login/passwordless-login-verify-by-username-and-otp/)

 ```

password_less_login_by_user_name_and_otp_model = {
  "username": "<User name>",
  "otp": "<otp>",
  "welcomeemailtemplate": "<welcome_email_template>"
}  #Required
fields = "<fields>" #Optional

result = loginradius.password_less_login.passwordless_login_verification_by_user_name_and_otp(password_less_login_by_user_name_and_otp_model, fields)
 ```



<h6 id="PasswordlessLoginByPhone-get-"> Passwordless Login by Phone (GET)</h6>

 API can be used to send a One-time Passcode (OTP) provided that the account has a verified PhoneID  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/passwordless-login/passwordless-login-by-phone)

 ```

phone = "<phone>" #Required
sms_template = "<sms_template>" #Optional

result = loginradius.password_less_login.passwordless_login_by_phone(phone, sms_template)
 ```




<h6 id="PasswordlessLoginByEmail-get-"> Passwordless Login By Email (GET)</h6>

 This API is used to send a Passwordless Login verification link to the provided Email ID  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/passwordless-login/passwordless-login-by-email)

 ```

email = "<email>" #Required
password_less_login_template = "<password_less_login_template>" #Optional
verification_url = "<verification_url>" #Optional

result = loginradius.password_less_login.passwordless_login_by_email(email, password_less_login_template, verification_url)
 ```




<h6 id="PasswordlessLoginByUserName-get-"> Passwordless Login By UserName (GET)</h6>

 This API is used to send a Passwordless Login Verification Link to a customer by providing their UserName  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/passwordless-login/passwordless-login-by-username)

 ```

username = "<username>" #Required
password_less_login_template = "<password_less_login_template>" #Optional
verification_url = "<verification_url>" #Optional

result = loginradius.password_less_login.passwordless_login_by_user_name(username, password_less_login_template, verification_url)
 ```




<h6 id="PasswordlessLoginVerification-get-"> Passwordless Login Verification (GET)</h6>

 This API is used to verify the Passwordless Login verification link. Note: If you are using Passwordless Login by Phone you will need to use the Passwordless Login Phone Verification API  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/passwordless-login/passwordless-login-verification)

 ```

verification_token = "<verification_token>" #Required
fields = "<fields>" #Optional
welcome_email_template = "<welcome_email_template>" #Optional

result = loginradius.password_less_login.passwordless_login_verification(verification_token, fields, welcome_email_template)
 ```






### Configuration API


List of APIs in this Section:<br>

* GET : [Get Server Time](#GetServerInfo-get-)<br>
* GET : [Get Configurations](#GetConfigurations-get-)<br>



<h6 id="GetServerInfo-get-"> Get Server Time (GET)</h6>

 This API allows you to query your LoginRadius account for basic server information and server time information which is useful when generating an SOTT token.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/configuration/get-server-time/)

 ```

time_difference = 0 #Optional

result = loginradius.configuration.get_server_info(time_difference)
 ```
 <h6 id="GetConfigurations-get-"> Get Configuration (GET)</h6>

 This API is used to get the configurations which are set in the LoginRadius Admin Console for a particular LoginRadius site/environment. [More info](https://www.loginradius.com/docs/api/v2/customer-identity-api/configuration/get-configurations)

  ```
result = loginradius.configuration.get_configurations()
```



### Role API


List of APIs in this Section:<br>

* PUT : [Assign Roles by UID](#AssignRolesByUid-put-)<br>
* PUT : [Upsert Context](#UpdateRoleContextByUid-put-)<br>
* PUT : [Add Permissions to Role](#AddRolePermissions-put-)<br>
* POST : [Roles Create](#CreateRoles-post-)<br>
* GET : [Roles by UID](#GetRolesByUid-get-)<br>
* GET : [Get Context with Roles and Permissions](#GetRoleContextByUid-get-)<br>
* GET : [Role Context profile](#GetRoleContextByContextName-get-)<br>
* GET : [Roles List](#GetRolesList-get-)<br>
* DELETE : [Unassign Roles by UID](#UnassignRolesByUid-delete-)<br>
* DELETE : [Delete Role Context](#DeleteRoleContextByUid-delete-)<br>
* DELETE : [Delete Role from Context](#DeleteRolesFromRoleContextByUid-delete-)<br>
* DELETE : [Delete Additional Permission from Context](#DeleteAdditionalPermissionFromRoleContextByUid-delete-)<br>
* DELETE : [Account Delete Role](#DeleteRole-delete-)<br>
* DELETE : [Remove Permissions](#RemoveRolePermissions-delete-)<br>




<h6 id="AssignRolesByUid-put-"> Assign Roles by UID (PUT)</h6>

 This API is used to assign your desired roles to a given user.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/roles-management/assign-roles-by-uid/)

 ```

account_roles_model = {
"roles" : [  "roles" ]
}  #Required
uid = "<uid>" #Required

result = loginradius.role.assign_roles_by_uid(account_roles_model, uid)
 ```




<h6 id="UpdateRoleContextByUid-put-"> Upsert Context (PUT)</h6>

 This API creates a Context with a set of Roles  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/roles-management/upsert-context)

 ```

account_role_context_model = {
"roleContext" : [   {
  "additionalPermissions" : ["<additionalPermissions>" ] ,
 "context" : "<context>"  ,
 "expiration" : "<expiration>"  ,
  "roles" : ["<roles>" ]  
}  ]
}  #Required
uid = "<uid>" #Required

result = loginradius.role.update_role_context_by_uid(account_role_context_model, uid)
 ```




<h6 id="AddRolePermissions-put-"> Add Permissions to Role (PUT)</h6>

 This API is used to add permissions to a given role.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/roles-management/add-permissions-to-role)

 ```

permissions_model = {
"permissions" : [  "permissions" ]
}  #Required
role = "<role>" #Required

result = loginradius.role.add_role_permissions(permissions_model, role)
 ```




<h6 id="CreateRoles-post-"> Roles Create (POST)</h6>

 This API creates a role with permissions.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/roles-management/roles-create)

 ```

roles_model = {
"roles" : [   {
 "name" : "<name>"  ,
"permissions" : {"Permission_name" : "True"}  
}  ]
}  #Required

result = loginradius.role.create_roles(roles_model)
 ```




<h6 id="GetRolesByUid-get-"> Roles by UID (GET)</h6>

 API is used to retrieve all the assigned roles of a particular User.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/roles-management/get-roles-by-uid)

 ```

uid = "<uid>" #Required

result = loginradius.role.get_roles_by_uid(uid)
 ```




<h6 id="GetRoleContextByUid-get-"> Get Context with Roles and Permissions (GET)</h6>

 This API Gets the contexts that have been configured and the associated roles and permissions.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/roles-management/get-context)

 ```

uid = "<uid>" #Required

result = loginradius.role.get_role_context_by_uid(uid)
 ```




<h6 id="GetRoleContextByContextName-get-"> Role Context profile (GET)</h6>

 The API is used to retrieve role context by the context name.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/roles-management/role-context-profile/)

 ```

context_name = "<context_name>" #Required

result = loginradius.role.get_role_context_by_context_name(context_name)
 ```




<h6 id="GetRolesList-get-"> Roles List (GET)</h6>

 This API retrieves the complete list of created roles with permissions of your app.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/roles-management/roles-list)

 ```


result = loginradius.role.get_roles_list()
 ```




<h6 id="UnassignRolesByUid-delete-"> Unassign Roles by UID (DELETE)</h6>

 This API is used to unassign roles from a user.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/roles-management/unassign-roles-by-uid)

 ```

account_roles_model = {
"roles" : [  "roles" ]
}  #Required
uid = "<uid>" #Required

result = loginradius.role.unassign_roles_by_uid(account_roles_model, uid)
 ```




<h6 id="DeleteRoleContextByUid-delete-"> Delete Role Context (DELETE)</h6>

 This API Deletes the specified Role Context  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/roles-management/delete-context)

 ```

context_name = "<context_name>" #Required
uid = "<uid>" #Required

result = loginradius.role.delete_role_context_by_uid(context_name, uid)
 ```




<h6 id="DeleteRolesFromRoleContextByUid-delete-"> Delete Role from Context (DELETE)</h6>

 This API Deletes the specified Role from a Context.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/roles-management/delete-role-from-context/)

 ```

context_name = "<context_name>" #Required
role_context_remove_role_model = {
"roles" : [  "roles" ]
}  #Required
uid = "<uid>" #Required

result = loginradius.role.delete_roles_from_role_context_by_uid(context_name, role_context_remove_role_model, uid)
 ```




<h6 id="DeleteAdditionalPermissionFromRoleContextByUid-delete-"> Delete Additional Permission from Context (DELETE)</h6>

 This API Deletes Additional Permissions from Context.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/roles-management/delete-permissions-from-context)

 ```

context_name = "<context_name>" #Required
role_context_additional_permission_remove_role_model = {
"additionalPermissions" : [  "additionalPermissions" ]
}  #Required
uid = "<uid>" #Required

result = loginradius.role.delete_additional_permission_from_role_context_by_uid(context_name, role_context_additional_permission_remove_role_model, uid)
 ```




<h6 id="DeleteRole-delete-"> Account Delete Role (DELETE)</h6>

 This API is used to delete the role.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/roles-management/delete-role)

 ```

role = "<role>" #Required

result = loginradius.role.delete_role(role)
 ```




<h6 id="RemoveRolePermissions-delete-"> Remove Permissions (DELETE)</h6>

 API is used to remove permissions from a role.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/roles-management/remove-permissions)

 ```

permissions_model = {
"permissions" : [  "permissions" ]
}  #Required
role = "<role>" #Required

result = loginradius.role.remove_role_permissions(permissions_model, role)
 ```






### CustomRegistrationData API


List of APIs in this Section:<br>

* PUT : [Update Registration Data](#UpdateRegistrationData-put-)<br>
* POST : [Validate secret code](#ValidateRegistrationDataCode-post-)<br>
* POST : [Add Registration Data](#AddRegistrationData-post-)<br>
* GET : [Auth Get Registration Data Server](#AuthGetRegistrationData-get-)<br>
* GET : [Get Registration Data](#GetRegistrationData-get-)<br>
* DELETE : [Delete Registration Data](#DeleteRegistrationData-delete-)<br>
* DELETE : [Delete All Records by Datasource](#DeleteAllRecordsByDataSource-delete-)<br>




<h6 id="UpdateRegistrationData-put-"> Update Registration Data (PUT)</h6>

 This API allows you to update a dropdown item  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/custom-registration-data/update-registration-data)

 ```

registration_data_update_model = {
"isActive" : "True",
"key" : "<key>",
"type" : "<type>",
"value" : "<value>"
}  #Required
record_id = "<record_id>" #Required

result = loginradius.custom_registration_data.update_registration_data(registration_data_update_model, record_id)
 ```




<h6 id="ValidateRegistrationDataCode-post-"> Validate secret code (POST)</h6>

 This API allows you to validate code for a particular dropdown member.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/custom-registration-data/validate-code)

 ```

code = "<code>" #Required
record_id = "<record_id>" #Required

result = loginradius.custom_registration_data.validate_registration_data_code(code, record_id)
 ```




<h6 id="AddRegistrationData-post-"> Add Registration Data (POST)</h6>

 This API allows you to fill data into a dropdown list which you have created for user Registration. For more details on how to use this API please see our Custom Registration Data Overview  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/custom-registration-data/add-registration-data)

 ```

registration_data_create_model_list = {
"data" : [   {
 "code" : "<code>"  ,
"isActive" : "True" ,
 "key" : "<key>"  ,
 "parentId" : "<parentId>"  ,
 "type" : "<type>"  ,
 "value" : "<value>"   
}  ]
}  #Required

result = loginradius.custom_registration_data.add_registration_data(registration_data_create_model_list)
 ```




<h6 id="AuthGetRegistrationData-get-"> Auth Get Registration Data Server (GET)</h6>

 This API is used to retrieve dropdown data.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/custom-registration-data/auth-get-registration-data)

 ```

type = "<type>" #Required
limit = 0 #Optional
parent_id = "<parent_id>" #Optional
skip = 0 #Optional

result = loginradius.custom_registration_data.auth_get_registration_data(type, limit, parent_id, skip)
 ```




<h6 id="GetRegistrationData-get-"> Get Registration Data (GET)</h6>

 This API is used to retrieve dropdown data.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/custom-registration-data/get-registration-data)

 ```

type = "<type>" #Required
limit = 0 #Optional
parent_id = "<parent_id>" #Optional
skip = 0 #Optional

result = loginradius.custom_registration_data.get_registration_data(type, limit, parent_id, skip)
 ```




<h6 id="DeleteRegistrationData-delete-"> Delete Registration Data (DELETE)</h6>

 This API allows you to delete an item from a dropdown list.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/custom-registration-data/delete-registration-data)

 ```

record_id = "<record_id>" #Required

result = loginradius.custom_registration_data.delete_registration_data(record_id)
 ```




<h6 id="DeleteAllRecordsByDataSource-delete-"> Delete All Records by Datasource (DELETE)</h6>

 This API allows you to delete all records contained in a datasource.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/custom-registration-data/delete-all-records-by-datasource)

 ```

type = "<type>" #Required

result = loginradius.custom_registration_data.delete_all_records_by_data_source(type)
 ```






### RiskBasedAuthentication API


List of APIs in this Section:<br>

* POST : [Risk Based Authentication Login by Email](#RBALoginByEmail-post-)<br>
* POST : [Risk Based Authentication Login by Username](#RBALoginByUserName-post-)<br>
* POST : [Risk Based Authentication Phone Login](#RBALoginByPhone-post-)<br>




<h6 id="RBALoginByEmail-post-"> Risk Based Authentication Login by Email (POST)</h6>

 This API retrieves a copy of the user data based on the Email  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-login-by-email)

 ```

email_authentication_model = {
"email" : "<email>",
"password" : "<password>"
}  #Required
email_template = "<email_template>" #Optional
fields = "<fields>" #Optional
login_url = "<login_url>" #Optional
password_delegation = "True" #Optional
password_delegation_app = "<password_delegation_app>" #Optional
rba_browser_email_template = "<rba_browser_email_template>" #Optional
rba_browser_sms_template = "<rba_browser_sms_template>" #Optional
rba_city_email_template = "<rba_city_email_template>" #Optional
rba_city_sms_template = "<rba_city_sms_template>" #Optional
rba_country_email_template = "<rba_country_email_template>" #Optional
rba_country_sms_template = "<rba_country_sms_template>" #Optional
rba_ip_email_template = "<rba_ip_email_template>" #Optional
rba_ip_sms_template = "<rba_ip_sms_template>" #Optional
rba_oneclick_email_template = "<rba_oneclick_email_template>" #Optional
rba_otp_sms_template = "<rba_otp_sms_template>" #Optional
sms_template = "<sms_template>" #Optional
verification_url = "<verification_url>" #Optional

result = loginradius.risk_based_authentication.rba_login_by_email(email_authentication_model, email_template, fields, login_url, password_delegation, password_delegation_app, rba_browser_email_template, rba_browser_sms_template, rba_city_email_template, rba_city_sms_template, rba_country_email_template, rba_country_sms_template, rba_ip_email_template, rba_ip_sms_template, rba_oneclick_email_template, rba_otp_sms_template, sms_template, verification_url)
 ```




<h6 id="RBALoginByUserName-post-"> Risk Based Authentication Login by Username (POST)</h6>

 This API retrieves a copy of the user data based on the Username  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/authentication/auth-login-by-username)

 ```

user_name_authentication_model = {
"password" : "<password>",
"username" : "<username>"
}  #Required
email_template = "<email_template>" #Optional
fields = "<fields>" #Optional
login_url = "<login_url>" #Optional
password_delegation = "True" #Optional
password_delegation_app = "<password_delegation_app>" #Optional
rba_browser_email_template = "<rba_browser_email_template>" #Optional
rba_browser_sms_template = "<rba_browser_sms_template>" #Optional
rba_city_email_template = "<rba_city_email_template>" #Optional
rba_city_sms_template = "<rba_city_sms_template>" #Optional
rba_country_email_template = "<rba_country_email_template>" #Optional
rba_country_sms_template = "<rba_country_sms_template>" #Optional
rba_ip_email_template = "<rba_ip_email_template>" #Optional
rba_ip_sms_template = "<rba_ip_sms_template>" #Optional
rba_oneclick_email_template = "<rba_oneclick_email_template>" #Optional
rba_otp_sms_template = "<rba_otp_sms_template>" #Optional
sms_template = "<sms_template>" #Optional
verification_url = "<verification_url>" #Optional

result = loginradius.risk_based_authentication.rba_login_by_user_name(user_name_authentication_model, email_template, fields, login_url, password_delegation, password_delegation_app, rba_browser_email_template, rba_browser_sms_template, rba_city_email_template, rba_city_sms_template, rba_country_email_template, rba_country_sms_template, rba_ip_email_template, rba_ip_sms_template, rba_oneclick_email_template, rba_otp_sms_template, sms_template, verification_url)
 ```




<h6 id="RBALoginByPhone-post-"> Risk Based Authentication Phone Login (POST)</h6>

 This API retrieves a copy of the user data based on the Phone  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/phone-authentication/phone-login)

 ```

phone_authentication_model = {
"password" : "<password>",
"phone" : "<phone>"
}  #Required
email_template = "<email_template>" #Optional
fields = "<fields>" #Optional
login_url = "<login_url>" #Optional
password_delegation = "True" #Optional
password_delegation_app = "<password_delegation_app>" #Optional
rba_browser_email_template = "<rba_browser_email_template>" #Optional
rba_browser_sms_template = "<rba_browser_sms_template>" #Optional
rba_city_email_template = "<rba_city_email_template>" #Optional
rba_city_sms_template = "<rba_city_sms_template>" #Optional
rba_country_email_template = "<rba_country_email_template>" #Optional
rba_country_sms_template = "<rba_country_sms_template>" #Optional
rba_ip_email_template = "<rba_ip_email_template>" #Optional
rba_ip_sms_template = "<rba_ip_sms_template>" #Optional
rba_oneclick_email_template = "<rba_oneclick_email_template>" #Optional
rba_otp_sms_template = "<rba_otp_sms_template>" #Optional
sms_template = "<sms_template>" #Optional
verification_url = "<verification_url>" #Optional

result = loginradius.risk_based_authentication.rba_login_by_phone(phone_authentication_model, email_template, fields, login_url, password_delegation, password_delegation_app, rba_browser_email_template, rba_browser_sms_template, rba_city_email_template, rba_city_sms_template, rba_country_email_template, rba_country_sms_template, rba_ip_email_template, rba_ip_sms_template, rba_oneclick_email_template, rba_otp_sms_template, sms_template, verification_url)
 ```






### Sott API


List of APIs in this Section:<br>

* GET : [Generate SOTT](#GenerateSott-get-)<br>




<h6 id="GenerateSott-get-"> Generate SOTT (GET)</h6>

 This API allows you to generate SOTT with a given expiration time.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/session/generate-sott-token)

 ```

time_difference = 0 #Optional

result = loginradius.sott.generate_sott(time_difference)
 ```






### NativeSocial API


List of APIs in this Section:<br>

* GET : [Access Token via Facebook Token](#GetAccessTokenByFacebookAccessToken-get-)<br>
* GET : [Access Token via Twitter Token](#GetAccessTokenByTwitterAccessToken-get-)<br>
* GET : [Access Token via Google Token](#GetAccessTokenByGoogleAccessToken-get-)<br>
* GET : [Access Token using google JWT token for Native Mobile Login](#GetAccessTokenByGoogleJWTAccessToken-get-)<br>
* GET : [Access Token via Linkedin Token](#GetAccessTokenByLinkedinAccessToken-get-)<br>
* GET : [Get Access Token By Foursquare Access Token](#GetAccessTokenByFoursquareAccessToken-get-)<br>
* GET : [Access Token via Apple Id Code](#GetAccessTokenByAppleIdCode-get-)<br>
* GET : [Access Token via WeChat Code](#GetAccessTokenByWeChatCode-get-)<br>
* GET : [Access Token via Vkontakte Token](#GetAccessTokenByVkontakteAccessToken-get-)<br>
* GET : [Access Token via Google AuthCode](#GetAccessTokenByGoogleAuthCode-get-)<br>




<h6 id="GetAccessTokenByFacebookAccessToken-get-"> Access Token via Facebook Token (GET)</h6>

 The API is used to get LoginRadius access token by sending Facebook's access token. It will be valid for the specific duration of time specified in the response.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/native-social-login-api/access-token-via-facebook-token/)

 ```

fb_access_token = "<fb_access_token>" #Required
social_app_name = "<social_app_name>" #Optional

result = loginradius.native_social.get_access_token_by_facebook_access_token(fb_access_token, social_app_name)
 ```




<h6 id="GetAccessTokenByTwitterAccessToken-get-"> Access Token via Twitter Token (GET)</h6>

 The API is used to get LoginRadius access token by sending Twitter's access token. It will be valid for the specific duration of time specified in the response.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/native-social-login-api/access-token-via-twitter-token)

 ```

tw_access_token = "<tw_access_token>" #Required
tw_token_secret = "<tw_token_secret>" #Required
social_app_name = "<social_app_name>" #Optional

result = loginradius.native_social.get_access_token_by_twitter_access_token(tw_access_token, tw_token_secret, social_app_name)
 ```




<h6 id="GetAccessTokenByGoogleAccessToken-get-"> Access Token via Google Token (GET)</h6>

 The API is used to get LoginRadius access token by sending Google's access token. It will be valid for the specific duration of time specified in the response.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/native-social-login-api/access-token-via-google-token)

 ```

google_access_token = "<google_access_token>" #Required
client_id = "<client_id>" #Optional
refresh_token = "<refresh_token>" #Optional
social_app_name = "<social_app_name>" #Optional

result = loginradius.native_social.get_access_token_by_google_access_token(google_access_token, client_id, refresh_token, social_app_name)
 ```




<h6 id="GetAccessTokenByGoogleJWTAccessToken-get-"> Access Token using google JWT token for Native Mobile Login (GET)</h6>

 This API is used to Get LoginRadius Access Token using google jwt id token for google native mobile login/registration.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/native-social-login-api/access-token-via-googlejwt)

 ```

id_token = "<id_token>" #Required

result = loginradius.native_social.get_access_token_by_google_j_w_t_access_token(id_token)
 ```




<h6 id="GetAccessTokenByLinkedinAccessToken-get-"> Access Token via Linkedin Token (GET)</h6>

 The API is used to get LoginRadius access token by sending Linkedin's access token. It will be valid for the specific duration of time specified in the response.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/native-social-login-api/access-token-via-linkedin-token/)

 ```

ln_access_token = "<ln_access_token>" #Required
social_app_name = "<social_app_name>" #Optional

result = loginradius.native_social.get_access_token_by_linkedin_access_token(ln_access_token, social_app_name)
 ```




<h6 id="GetAccessTokenByFoursquareAccessToken-get-"> Get Access Token By Foursquare Access Token (GET)</h6>

 The API is used to get LoginRadius access token by sending Foursquare's access token. It will be valid for the specific duration of time specified in the response.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/native-social-login-api/access-token-via-foursquare-token/)

 ```

fs_access_token = "<fs_access_token>" #Required

result = loginradius.native_social.get_access_token_by_foursquare_access_token(fs_access_token)
 ```




<h6 id="GetAccessTokenByAppleIdCode-get-"> Access Token via Apple Id Code (GET)</h6>

 The API is used to get LoginRadius access token by sending a valid Apple ID OAuth Code. It will be valid for the specific duration of time specified in the response.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/native-social-login-api/access-token-via-apple-id-code)

 ```

code = "<code>" #Required
social_app_name = "<social_app_name>" #Optional

result = loginradius.native_social.get_access_token_by_apple_id_code(code, social_app_name)
 ```




<h6 id="GetAccessTokenByWeChatCode-get-"> Access Token via WeChat Code (GET)</h6>

 This API is used to retrieve a LoginRadius access token by passing in a valid WeChat OAuth Code.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/native-social-login-api/access-token-via-wechat-code)

 ```

code = "<code>" #Required

result = loginradius.native_social.get_access_token_by_we_chat_code(code)
 ```




<h6 id="GetAccessTokenByVkontakteAccessToken-get-"> Access Token via Vkontakte Token (GET)</h6>

 The API is used to get LoginRadius access token by sending Vkontakte's access token. It will be valid for the specific duration of time specified in the response.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/native-social-login-api/access-token-via-vkontakte-token)

 ```

vk_access_token = "<vk_access_token>" #Required

result = loginradius.native_social.get_access_token_by_vkontakte_access_token(vk_access_token)
 ```




<h6 id="GetAccessTokenByGoogleAuthCode-get-"> Access Token via Google AuthCode (GET)</h6>

 The API is used to get LoginRadius access token by sending Google's AuthCode. It will be valid for the specific duration of time specified in the response.  [More Info](https://www.loginradius.com/docs/api/v2/customer-identity-api/social-login/native-social-login-api/access-token-via-google-auth-code)

 ```

google_authcode = "<google_authcode>" #Required
social_app_name = "<social_app_name>" #Optional

result = loginradius.native_social.get_access_token_by_google_auth_code(google_authcode, social_app_name)
 ```






### WebHook API


List of APIs in this Section:<br>

* POST : [Webhook Subscribe](#WebHookSubscribe-post-)<br>
* GET : [Webhook Subscribed URLs](#GetWebHookSubscribedURLs-get-)<br>
* GET : [Webhook Test](#WebhookTest-get-)<br>
* DELETE : [WebHook Unsubscribe](#WebHookUnsubscribe-delete-)<br>




<h6 id="WebHookSubscribe-post-"> Webhook Subscribe (POST)</h6>

 API can be used to configure a WebHook on your LoginRadius site. Webhooks also work on subscribe and notification model, subscribe your hook and get a notification. Equivalent to RESThook but these provide security on basis of signature and RESThook work on unique URL. Following are the events that are allowed by LoginRadius to trigger a WebHook service call.  [More Info](https://www.loginradius.com/docs/api/v2/integrations/webhooks/webhook-subscribe)

 ```

web_hook_subscribe_model = {
"event" : "<event>",
"targetUrl" : "<targetUrl>"
}  #Required

result = loginradius.web_hook.web_hook_subscribe(web_hook_subscribe_model)
 ```




<h6 id="GetWebHookSubscribedURLs-get-"> Webhook Subscribed URLs (GET)</h6>

 This API is used to fatch all the subscribed URLs, for particular event  [More Info](https://www.loginradius.com/docs/api/v2/integrations/webhooks/webhook-subscribed-urls)

 ```

event = "<event>" #Required

result = loginradius.web_hook.get_web_hook_subscribed_u_r_ls(event)
 ```




<h6 id="WebhookTest-get-"> Webhook Test (GET)</h6>

 API can be used to test a subscribed WebHook.  [More Info](https://www.loginradius.com/docs/api/v2/integrations/webhooks/webhook-test)

 ```


result = loginradius.web_hook.webhook_test()
 ```




<h6 id="WebHookUnsubscribe-delete-"> WebHook Unsubscribe (DELETE)</h6>

 API can be used to unsubscribe a WebHook configured on your LoginRadius site.  [More Info](https://www.loginradius.com/docs/api/v2/integrations/webhooks/webhook-unsubscribe)

 ```

web_hook_subscribe_model = {
"event" : "<event>",
"targetUrl" : "<targetUrl>"
}  #Required

result = loginradius.web_hook.web_hook_unsubscribe(web_hook_subscribe_model)
 ```






#### Error Handling
If the request fails, it can be handled in the following way:

```
if result.get('ErrorCode') is not None:
    print(result.get('Description'))
else:
    print(result)
```

<br>
## Demo
We have a demo web application using the Python SDK, which includes the following features:

* Traditional email login
* Multi-Factor login
* Passwordless login
* Social login
* Register
* Email verification
* Forgot password
* Reset password
* Change password
* Set password
* Update account
* Account linking
* Custom object management
* Roles management

You can get a copy of our demo project at [GitHub](https://github.com/LoginRadius/python-sdk).

<br>

### Configuration

1.Have  Flask, requests, pbkdf2, cryptography installed or you can install the required dependency using the following command:

```pip install -r requirements.txt``` <br>

2.Fill in credentials in ```lr.py``` and ```static/js/options.js```

3.Navigate to demo directory and run: ```python app.py```

4.Demo will appear on ```http://localhost:5000```

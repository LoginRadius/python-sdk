import unittest, env, sys, time
from LoginRadius import LoginRadius as LR
from helpers import setUp, tearDown

@unittest.skipIf(env.IS_MFA_ENABLED == True, 'disabled mfa required')
class TestAuthentication(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('~~~~TestAuthentication::setUpClass~~~~')

        LR.API_KEY = env.API_KEY
        LR.API_SECRET = env.API_SECRET
        LR.LIBRARY = 'requests'
        cls.loginradius = LR()
        cls.set = setUp(cls.loginradius)
        cls.tear = tearDown(cls.loginradius)

    # Add Email (POST)
    def test_post_addEmail(self):
        account = ''
        try:
            account = self.set.account(True)
            login = self.set.login(account.email)
            res = self.loginradius.authentication.addEmail(login.token, 'lr-pysdk' + str(time.time()) + '@mailinator.com', 'Secondary')
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Forgot Password (POST)
    def test_post_forgotPassword(self):
        account = ''
        try:
            account = self.set.account(True)
            res = self.loginradius.authentication.forgotPassword(account.email, 'loginradius.com')
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # User Registration by Email (POST)
    def test_post_register(self):
        try:
            email = 'lr-pysdk' + str(time.time()) + '@mailinator.com'
            payload = {
                'Email': [{
                    'Type': 'Primary',
                    'Value': email
                }],
                'Password': email
            }
            res = self.loginradius.authentication.register(payload, '', '', True)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                # get uid -> delete acc
                token = self.loginradius.account.getEmailVerificationToken(email)['VerificationToken']
                self.loginradius.authentication.getVerifyEmail(token)
                profile = self.loginradius.authentication.login.byEmail({'email': email, 'password': email})['Profile']
                self.tear.account(profile['Uid'])
        except Exception as e:
            self.fail(e)

    # Login by Email (POST)
    def test_post_loginByEmail(self):
        account = ''
        try:
            account = self.set.account(True)
            payload = {
                'email': account.email,
                'password': account.email
            }
            res = self.loginradius.authentication.login.byEmail(payload)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Login by UserName (POST)
    def test_post_loginByUsername(self):
        account = ''
        try:
            account = self.set.account(True)
            payload = {
                'username': account.username,
                'password': account.email
            }
            res = self.loginradius.authentication.login.byUsername(payload)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Check Email Availability (GET)
    def test_get_emailAvailability(self):
        try:
            res = self.loginradius.authentication.getCheckEmail('lr-pysdk@mailinator.com')
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Check Username Availability (GET)
    def test_get_usernameAvailability(self):
        try:
            res = self.loginradius.authentication.checkUsername('lr-pysdk')
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Read all Profiles by Token (GET)
    def test_get_readProfileByToken(self):
        account = ''
        try:
            account = self.set.account(True)
            login = self.set.login(account.email)
            res = self.loginradius.authentication.profile.getByToken(login.token)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Privacy Policy Accept (GET)
    def test_get_acceptPrivacyPolicy(self):
        account = ''
        try:
            account = self.set.account(True)
            login = self.set.login(account.email)
            res = self.loginradius.authentication.privacyPolicyAccept(login.token)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Send Welcome Email (GET)
    def test_get_sendWelcomeEmail(self):
        account = ''
        try:
            account = self.set.account(True)
            login = self.set.login(account.email)
            res = self.loginradius.authentication.sendWelcomeEmail(login.token)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Social Identity (GET)
    def test_get_socialidentity(self):
        account = ''
        try:
            account = self.set.account(True)
            login = self.set.login(account.email)
            res = self.loginradius.authentication.getSocialProfile(login.token)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Validate Access token (GET)
    def test_get_tokenValidate(self):
        account = ''
        try:
            account = self.set.account(True)
            login = self.set.login(account.email)
            res = self.loginradius.authentication.tokenValidate(login.token)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Invalidate Access token (GET)
    def test_get_tokenInvalidate(self):
        account = ''
        try:
            account = self.set.account(True)
            login = self.set.login(account.email)
            res = self.loginradius.authentication.tokenInvalidate(login.token)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Verify Email (GET)
    def test_get_VerifyEmail(self):
        account = ''
        try:
            account = self.set.account()
            token = self.set.email_verification_token(account.email)
            res = self.loginradius.authentication.getVerifyEmail(token)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Delete Account (GET)
    def test_get_deleteAccount(self):
        try:
            self.loginradius.authentication.deleteAccount('99999')
        except Exception as e:
            self.fail(e)

    # Security Questions by Access Token (GET)
    @unittest.skipIf(env.SECURITY_QUESTION_ID == '', 'security_question_id required')
    def test_get_securityQuestionByToken(self):
        account = ''
        try:
            if env.SECURITY_QUESTION_ID != '':
                account = self.set.account(True)
                login = self.set.login(account.email)
                self.set.security_question(login.token, env.SECURITY_QUESTION_ID, 'answer')
                res = self.loginradius.authentication.securityQuestionByToken(login.token)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
                else:
                    self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Security Questions by Email (GET)
    @unittest.skipIf(env.SECURITY_QUESTION_ID == '', 'security_question_id required')
    def test_get_securityQuestionByEmail(self):
        account = ''
        try:
            if env.SECURITY_QUESTION_ID != '':
                account = self.set.account(True)
                login = self.set.login(account.email)
                self.set.security_question(login.token, env.SECURITY_QUESTION_ID, 'answer')
                res = self.loginradius.authentication.securityQuestionByEmail(account.email)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
                else:
                    self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Security Questions by Username (GET)
    @unittest.skipIf(env.SECURITY_QUESTION_ID == '', 'security_question_id required')
    def test_get_securityQuestionByUsername(self):
        account = ''
        try:
            if env.SECURITY_QUESTION_ID != '':
                account = self.set.account(True)
                login = self.set.login(account.email)
                self.set.security_question(login.token, env.SECURITY_QUESTION_ID, 'answer')
                res = self.loginradius.authentication.securityQuestionByUsername(account.username)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
                else:
                    self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Security Questions by Phone (GET)
    @unittest.skipIf(env.SECURITY_QUESTION_ID == '' or env.PHONE_NUM == '', 'security_question_id and phone_num required')
    def test_get_securityQuestionByPhone(self):
        account = ''
        try:
            if env.SECURITY_QUESTION_ID != '' and env.PHONE_NUM != '':
                account = self.set.account(True)
                login = self.set.login(account.email)
                self.set.security_question(login.token, env.SECURITY_QUESTION_ID, 'answer')
                res = self.loginradius.authentication.securityQuestionByPhone(account.phoneid)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
                else:
                    self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Verify Email by OTP (PUT)
    def test_put_verifyEmailbyOTP(self):
        try:
            self.loginradius.authentication.verifyEmailbyOTP({'otp': '99999', 'email': 'lr-pysdk@mailinator.com'})
        except Exception as e:
            self.fail(e)

    # Change Password (PUT)
    def test_put_changePassword(self):
        account = ''
        try:
            account = self.set.account(True)
            login = self.set.login(account.email)
            res = self.loginradius.authentication.changePassword(login.token, account.email, '1234567890')
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Link Social Identities (PUT)
    @unittest.skipIf(env.CANDIDATE_TOKEN == '', 'candidate_token required')
    def test_put_accountLink(self):
        account = ''
        try:
            if env.CANDIDATE_TOKEN != '':
                account = self.set.account(True)
                login = self.set.login(account.email)
                res = self.loginradius.authentication.accountLink(login.token, env.CANDIDATE_TOKEN)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
                else:
                    self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Resend Email Verification (PUT)
    def test_put_resendEmailVerification(self):
        account = ''
        try:
            account = self.set.account()
            res = self.loginradius.authentication.resendEmailVerification(account.email)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Reset Password by Reset Token (PUT)
    def test_put_resetPassword(self):
        account = ''
        try:
            account = self.set.account()
            token = self.set.reset_token(account.email)
            payload = {
                'resettoken': token,
                'password': '1234567890'
            }
            res = self.loginradius.authentication.resetPassword(payload)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Reset Password by OTP (PUT)
    def test_put_resetPasswordByOTP(self):
        account = ''
        try:
            account = self.set.account(False)
            payload = {
                'password': '1234567890',
                'otp': '999999',
                'email': account.email
            }
            self.loginradius.authentication.resetPasswordByOTP(payload)
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Reset Password by Security Answer and Email (PUT)
    @unittest.skipIf(env.SECURITY_QUESTION_ID == '', 'security_question_id required')
    def test_put_resetPasswordBySecurityAnswerAndEmail(self):
        account = ''
        try:
            if env.SECURITY_QUESTION_ID != '':
                account = self.set.account(True)
                login = self.set.login(account.email)
                self.set.security_question(login.token, env.SECURITY_QUESTION_ID, 'answer')
                res = self.loginradius.authentication.resetPasswordBySecurityAnswerAndEmail({env.SECURITY_QUESTION_ID: 'answer'}, account.email, '1234567890')
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
                else:
                    self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Reset Password by Security Answer and Phone (PUT)
    @unittest.skipIf(env.SECURITY_QUESTION_ID == '' or env.PHONE_NUM == '', 'security_question_id and phone_num required')
    def test_put_resetPasswordBySecurityAnswerAndPhone(self):
        try:
            if env.SECURITY_QUESTION_ID != '' and env.PHONE_NUM != '':
                account = self.set.account(True, True)
                login = self.set.login(account.email)
                self.set.security_question(login.token, env.SECURITY_QUESTION_ID, 'answer')
                res = self.loginradius.authentication.resetPasswordBySecurityAnswerAndPhone({env.SECURITY_QUESTION_ID: 'answer'}, account.phoneid, '1234567890')
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
                else:
                    self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Reset Password by Security Answer and UserName (PUT)
    @unittest.skipIf(env.SECURITY_QUESTION_ID == '', 'security_question_id required')
    def test_put_resetPasswordBySecurityAnswerAndUsername(self):
        try:
            if env.SECURITY_QUESTION_ID != '':
                account = self.set.account(True)
                login = self.set.login(account.email)
                self.set.security_question(login.token, env.SECURITY_QUESTION_ID, 'answer')
                res = self.loginradius.authentication.resetPasswordBySecurityAnswerAndUsername({env.SECURITY_QUESTION_ID: 'answer'}, account.username, '1234567890')
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
                else:
                    self.tear.account(account.uid)
        except Exception as e:
            self.fail(e)

    # Set or Change UserName (PUT)
    def test_put_changeUsername(self):
        account = ''
        try:
            account = self.set.account(True)
            login = self.set.login(account.email)
            res = self.loginradius.authentication.changeUsername(login.token, account.username + '1')
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Update Profile by Token (PUT)
    def test_put_updateByToken(self):
        account = ''
        try:
            account = self.set.account(True)
            login = self.set.login(account.email)
            payload = {
                'FirstName': 'John',
                'LastName': 'Doe',
                'About': 'anything i want'
            }
            res = self.loginradius.authentication.profile.updateByToken(login.token, payload)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Update Security Question by Access token (PUT)
    @unittest.skipIf(env.SECURITY_QUESTION_ID == '', 'security_question_id required')
    def test_put_updateSecurityQuestionByAccessToken(self):
        account = ''
        try:
            account = self.set.account(True)
            login = self.set.login(account.email)
            res = self.loginradius.authentication.updateSecurityQuestionByAccessToken(login.token, {env.SECURITY_QUESTION_ID: 'answer'})
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Delete Account with Email Confirmation (DEL)
    def test_del_deleteAccountByEmailConfirmation(self):
        account = ''
        try:
            account = self.set.account(True)
            login = self.set.login(account.email)
            res = self.loginradius.authentication.deleteAccountByEmailConfirmation(login.token)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Remove Email (DEL)
    def test_del_removeEmail(self):
        account = ''
        try:
            account = self.set.account(True)
            login = self.set.login(account.email)
            self.loginradius.authentication.removeEmail(login.token, 'lr-pysdk@mailinator.com')
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Unlink Social Identities (DEL)
    def test_del_accountUnlink(self):
        account = ''
        try:
            account = self.set.account(True)
            login = self.set.login(account.email)
            self.loginradius.authentication.accountUnlink(login.token, '99999' , '99999')
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

if __name__ == '__main__':
    unittest.main()

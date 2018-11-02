import unittest, env, sys, time
from LoginRadius import LoginRadius as LR
from helpers import setUp, tearDown

@unittest.skipIf(env.IS_MFA_ENABLED == True, 'disabled mfa required')
class TestAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('~~~~TestAccount::setUpClass~~~~')

        LR.API_KEY = env.API_KEY
        LR.API_SECRET = env.API_SECRET
        LR.LIBRARY = 'requests'
        cls.loginradius = LR()
        cls.set = setUp(cls.loginradius)
        cls.tear = tearDown(cls.loginradius)

    # Account Create (POST)
    def test_post_create(self):
        profile = ''
        try:
            email = 'lr-pysdk' + str(time.time()) + '@mailinator.com'
            payload = {
                'Email': [{
                    'Type': 'Primary',
                    'Value': email
                }],
                'Password': email,
                'EmailVerified': True,
            }
            res = self.loginradius.account.create(payload)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                # get uid -> delete acc
                profile = self.loginradius.authentication.login.byEmail({'email': email, 'password': email})['Profile']
                self.tear.account(profile['Uid'])
        except Exception as e:
            self.fail(e)

    # Email Verification Token (POST)
    def test_post_getEmailVerificationToken(self):
        account = ''
        try:
            account = self.set.account()
            res = self.loginradius.account.getEmailVerificationToken(account.email)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Forgot Password Token (POST)
    def test_post_getForgotPasswordToken(self):
        account = ''
        try:
            account = self.set.account()
            res = self.loginradius.account.getForgotPasswordToken(account.email)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Account Identities by Email (GET)
    def test_get_getIdentities(self):
        account = ''
        try:
            account = self.set.account()
            res = self.loginradius.account.getIdentities(account.email)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Access Token based on UID or User impersonation API (GET)
    def test_get_getAccessToken(self):
        account = ''
        try:
            account = self.set.account()
            res = self.loginradius.account.getAccessToken(account.uid)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Account Password (GET)
    def test_get_getPassword(self):
        account = ''
        try:
            account = self.set.account()
            res = self.loginradius.account.getPassword(account.uid)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Account Profiles by Email (GET)
    def test_get_profile_getByEmail(self):
        account = ''
        try:
            account = self.set.account()
            res = self.loginradius.account.profile.getByEmail(account.email)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Account Profiles by Username (GET)
    def test_get_profile_getByUsername(self):
        account = ''
        try:
            account = self.set.account()
            res = self.loginradius.account.profile.getByUsername(account.username)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Account Profile by Phone ID (GET)
    @unittest.skipIf(env.PHONE_NUM == '', 'phone_num required')
    def test_get_profile_getByPhone(self):
        account = ''
        try:
            if env.PHONE_NUM != '':
                account = self.set.account()
                res = self.loginradius.account.profile.getByPhone(account.phoneid)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
                else:
                    self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Account Profiles by UID (GET)
    def test_get_profile_getByUid(self):
        account = ''
        try:
            account = self.set.account()
            res = self.loginradius.account.profile.getByUid(account.uid)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Account Set Password (PUT)
    def test_put_setPassword(self):
        account = ''
        try:
            account = self.set.account()
            res = self.loginradius.account.setPassword(account.uid, '1234567890')
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Account Update (PUT)
    def test_put_setPassword(self):
        account = ''
        try:
            account = self.set.account()
            payload = {
                'FirstName': 'John',
                'LastName': 'Doe',
                'About': 'anything i want'
            }
            res = self.loginradius.account.update(account.uid, payload)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Account Update Security Question Configuration (PUT)
    @unittest.skipIf(env.SECURITY_QUESTION_ID == '', 'security_question_id required')
    def test_put_updateSecurityQuestion(self):
        account = ''
        try:
            if env.SECURITY_QUESTION_ID != '':  
                account = self.set.account()
                payload = {
                    'securityquestionanswer': {
                        env.SECURITY_QUESTION_ID: 'answer'
                    }
                }
                res = self.loginradius.account.updateSecurityQuestion(account.uid, payload)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
                else:
                    self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Account Invalidate Verification Email (PUT)
    def test_put_invalidateVerificationEmail(self):
        account = ''
        try:
            account = self.set.account(True, False)
            res = self.loginradius.account.invalidateVerificationEmail(account.uid)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Account Email Delete (DEL)
    def test_del_removeEmail(self):
        account = ''
        try:
            account = self.set.account()
            res = self.loginradius.account.removeEmail(account.uid, account.secondary_email)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Account Delete (DEL)
    def test_del_remove(self):
        account = ''
        try:
            account = self.set.account()
            res = self.loginradius.account.remove(account.uid)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

if __name__ == '__main__':
    unittest.main()

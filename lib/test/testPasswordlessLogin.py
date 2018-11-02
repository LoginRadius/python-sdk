import unittest, env, sys, time
from LoginRadius import LoginRadius as LR
from helpers import setUp, tearDown

@unittest.skipIf(env.IS_MFA_ENABLED == True, 'disabled mfa required')
class TestPasswordlessLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('~~~~TestPasswordlessLogin::setUpClass~~~~')

        LR.API_KEY = env.API_KEY
        LR.API_SECRET = env.API_SECRET
        LR.LIBRARY = 'requests'
        cls.loginradius = LR()
        cls.set = setUp(cls.loginradius)
        cls.tear = tearDown(cls.loginradius)

    # Passwordless Login By Email (GET)
    def test_get_passwordlessLoginByEmail(self):
        account = ''
        try:
            account = self.set.account(True, True)
            res = self.loginradius.authentication.login.passwordlessLoginByEmail(account.email)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Passwordless Login By UserName (GET)
    def test_get_passwordlessLoginByUsername(self):
        account = ''
        try:
            account = self.set.account(True, True)
            res = self.loginradius.authentication.login.passwordlessLoginByUsername(account.username)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Passwordless Login Verification (GET)
    def test_get_passwordlessLoginVerification(self):
        try:
            self.loginradius.authentication.login.passwordlessLoginVerification('999999')
        except Exception as e:
            self.fail(e)

    # Phone Send One time Passcode (GET)
    @unittest.skipIf(env.PHONE_NUM == '', 'phone_num required')
    def test_get_passwordlessLoginSendOTP(self):
        account = ''
        try:
            account = self.set.account(True, True)
            res = self.loginradius.authentication.login.passwordlessLoginSendOTP(account.phoneid)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Phone Login Using One Time Passcode (PUT)
    def test_put_passwordlessLoginVerifyOTP(self):
        try:
            self.loginradius.authentication.login.passwordlessLoginVerifyOTP({'otp':'99999','phone':'99999'})
        except Exception as e:
            self.fail(e)

if __name__ == '__main__':
    unittest.main()

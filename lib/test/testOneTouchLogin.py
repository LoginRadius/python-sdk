import unittest, env, sys, time
from LoginRadius import LoginRadius as LR
from helpers import setUp, tearDown

@unittest.skipIf(env.IS_MFA_ENABLED == True, 'disabled mfa required')
class TestOneTouchLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('~~~~TestOneTouchLogin::setUpClass~~~~')

        LR.API_KEY = env.API_KEY
        LR.API_SECRET = env.API_SECRET
        LR.LIBRARY = 'requests'
        cls.loginradius = LR()
        cls.set = setUp(cls.loginradius)
        cls.tear = tearDown(cls.loginradius)

    # One Touch Login by Email (GET)
    def test_get_oneTouchLoginByEmail(self):
        account = ''
        try:
            account = self.set.account(True, True)
            res = self.loginradius.authentication.login.oneTouchLoginByEmail(account.email, account.uid)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # One Touch Login by Phone (GET)
    @unittest.skipIf(env.PHONE_NUM == '', 'phone_num required')
    def test_get_oneTouchLoginByPhone(self):
        account = ''
        try:
            account = self.set.account(True, True)
            res = self.loginradius.authentication.login.oneTouchLoginByPhone(account.phoneid, account.uid)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # One Touch Email Verification (GET)
    def test_get_oneTouchEmailVerification(self):
        try:
            self.loginradius.authentication.login.oneTouchEmailVerification('999999')
        except Exception as e:
            self.fail(e)

    # One Touch Login Ping (GET)
    def test_get_oneTouchPing(self):
        try:
            self.loginradius.authentication.login.smartLoginPing('99999')
        except Exception as e:
            self.fail(e)

    # One Touch OTP Verification (PUT)
    def test_put_oneTouchOtpVerification(self):
        try:
            self.loginradius.authentication.login.oneTouchOtpVerification('999999', '999999')
        except Exception as e:
            self.fail(e)

if __name__ == '__main__':
    unittest.main()

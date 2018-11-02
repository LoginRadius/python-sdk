import unittest, env, sys, time
from LoginRadius import LoginRadius as LR
from helpers import setUp, tearDown

@unittest.skipIf(env.IS_MFA_ENABLED == True, 'disabled mfa required')
class TestSmartLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('~~~~TestSmartLogin::setUpClass~~~~')

        LR.API_KEY = env.API_KEY
        LR.API_SECRET = env.API_SECRET
        LR.LIBRARY = 'requests'
        cls.loginradius = LR()
        cls.set = setUp(cls.loginradius)
        cls.tear = tearDown(cls.loginradius)

    # Smart Login By Email (GET)
    def test_get_smartLoginByEmail(self):
        account = ''
        try:
            account = self.set.account(True, True)
            res = self.loginradius.authentication.login.smartLoginByEmail(account.email, account.uid)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Smart Login By Username (GET)
    def test_get_smartLoginByUsername(self):
        account = ''
        try:
            account = self.set.account(True, True)
            res = self.loginradius.authentication.login.smartLoginByUsername(account.username, account.uid)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Smart Login Ping (GET)
    def test_get_smartLoginPing(self):
        try:
            self.loginradius.authentication.login.smartLoginPing('999999')
        except Exception as e:
            self.fail(e)

    # Smart Login Verify Token (GET)
    def test_get_smartLoginVerifyToken(self):
        try:
            self.loginradius.authentication.login.smartLoginVerifyToken('999999')
        except Exception as e:
            self.fail(e)

if __name__ == '__main__':
    unittest.main()

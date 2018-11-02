import unittest, env, sys, time
from LoginRadius import LoginRadius as LR
from helpers import setUp, tearDown

@unittest.skipIf(env.IS_MFA_ENABLED == True, 'disabled mfa required')
class TestInfrastructure(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('~~~~TestInfrastructure::setUpClass~~~~')

        LR.API_KEY = env.API_KEY
        LR.API_SECRET = env.API_SECRET
        LR.LIBRARY = 'requests'
        cls.loginradius = LR()
        cls.set = setUp(cls.loginradius)
        cls.tear = tearDown(cls.loginradius)

    # Get Configurations (GET)
    def test_get_config(self):
        try:
            res = self.loginradius.config.getConfiguration()
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Get Server Time (GET)
    def test_get_servertime(self):
        try:
            res = self.loginradius.authentication.getServerTime()
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Generate SOTT (GET)
    def test_get_generateSott(self):
        try:
            res = self.loginradius.account.generateSott()
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Get Active Session Details (GET)
    def test_get_activeSessionDetails(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            res = self.loginradius.accesstoken.activeSessionDetails(login.token)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

if __name__ == '__main__':
    unittest.main()

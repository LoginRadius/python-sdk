import unittest, env, sys, time
from LoginRadius import LoginRadius as LR
from helpers import setUp, tearDown

@unittest.skipIf(env.IS_MFA_ENABLED == True, 'disabled mfa required')
class TestTokenManagement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('~~~~TestTokenManagement::setUpClass~~~~')

        LR.API_KEY = env.API_KEY
        LR.API_SECRET = env.API_SECRET
        LR.LIBRARY = 'requests'
        cls.loginradius = LR()
        cls.set = setUp(cls.loginradius)
        cls.tear = tearDown(cls.loginradius)

    # Access Token via Facebook Token (GET)
    @unittest.skipIf(env.FACEBOOK_TOKEN == '', 'facebook_token required')
    def test_get_fbtoken(self):
        try:
            if env.FACEBOOK_TOKEN != '':
                res = self.loginradius.accesstoken.getFacebookToken(env.FACEBOOK_TOKEN)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Access Token via Twitter Token (GET)
    @unittest.skipIf(env.TWITTER_TOKEN == '' or env.TWITTER_SECRET == '', 'twitter_token and twitter_secret required')
    def test_get_twtoken(self):
        try:
            if env.TWITTER_TOKEN != '' and env.TWITTER_SECRET != '':
                res = self.loginradius.accesstoken.getTwitterToken(env.TWITTER_TOKEN, env.TWITTER_SECRET)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Access Token via Vkontakte Token (GET)
    @unittest.skipIf(env.VKONTAKTE_TOKEN == '', 'vk_token required')
    def test_get_vktoken(self):
        try:
            if env.VKONTAKTE_TOKEN != '':
                res = self.loginradius.accesstoken.getVkontakteToken(env.VKONTAKTE_TOKEN)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Access Token via Google JWT (GET)
    @unittest.skipIf(env.GOOGLE_TOKEN == '', 'google_token required')
    def test_get_gtoken(self):
        try:
            if env.GOOGLE_TOKEN != '':
                res = self.loginradius.accesstoken.getGoogleToken(env.GOOGLE_TOKEN)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Refresh User Profile (GET)
    def test_get_refresh_profile(self):
        account = ''
        try:
            account = self.set.account(True)
            login = self.set.login(account.email)
            res = self.loginradius.sociallogin.refresh_profile(login.token)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Refresh Token (GET)
    def test_get_refresh(self):
        account = ''
        try:
            account = self.set.account(True)
            login = self.set.login(account.email)
            res = self.loginradius.accesstoken.refresh(login.token)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

if __name__ == '__main__':
    unittest.main()

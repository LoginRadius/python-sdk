import unittest, env, sys, time
from LoginRadius import LoginRadius as LR
from helpers import setUp, tearDown

@unittest.skipIf(env.IS_MFA_ENABLED == True, 'disabled mfa required')
class TestWebhooks(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('~~~~TestWebhooks::setUpClass~~~~')

        LR.API_KEY = env.API_KEY
        LR.API_SECRET = env.API_SECRET
        LR.LIBRARY = 'requests'
        cls.loginradius = LR()
        cls.set = setUp(cls.loginradius)
        cls.tear = tearDown(cls.loginradius)

    # WebHook Subscribe API (POST)
    def test_post_subscribe(self):
        try:
            res = self.loginradius.webhook.subscribe('https://www.google.ca', 'Register')
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Webhook Test (GET)
    def test_get_test(self):
        try:
            res = self.loginradius.webhook.test()
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Webhook Subscribed URLs (GET)
    def test_get_getSubscribed(self):
        try:
            res = self.loginradius.webhook.getSubscribed('Register')
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # WebHook Unsubscribe (DEL)
    def test_del_unsubscribe(self):
        try:
            res = self.loginradius.webhook.unsubscribe('https://www.google.ca', 'Register')
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

if __name__ == '__main__':
    unittest.main()

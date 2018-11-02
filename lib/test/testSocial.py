import unittest, env, sys, time
from LoginRadius import LoginRadius as LR
from helpers import setUp, tearDown

@unittest.skipIf(env.IS_MFA_ENABLED == True, 'disabled mfa required')
class TestSocial(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('~~~~TestSocial::setUpClass~~~~')

        LR.API_KEY = env.API_KEY
        LR.API_SECRET = env.API_SECRET
        LR.LIBRARY = 'requests'
        cls.loginradius = LR()
        cls.set = setUp(cls.loginradius)
        cls.tear = tearDown(cls.loginradius)

    # Post Message (POST)
    def test_post_direct_message(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            res = self.loginradius.sociallogin.direct_message(login.token, '', '', '')
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Status Posting (POST)
    def test_post_status_update(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            res = self.loginradius.sociallogin.status_update(login.token, '')
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Access Token (GET)
    def test_get_exchange(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            res = self.loginradius.accesstoken.exchange(login.token)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Token Validate (GET)
    def test_get_validate(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            res = self.loginradius.accesstoken.validate(login.token)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Access Token Invalidate (GET)
    def test_get_invalidate(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            res = self.loginradius.accesstoken.invalidate(login.token)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # User Profile (GET)
    def test_get_user_profile(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            res = self.loginradius.sociallogin.profile(login.token)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Album (GET)
    def test_get_album(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            self.loginradius.sociallogin.album(login.token)
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Audio (GET)
    def test_get_audio(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            self.loginradius.sociallogin.audio(login.token)
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Check In (GET)
    def test_get_checkin(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            self.loginradius.sociallogin.check_in(login.token)
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Company (GET)
    def test_get_company(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            self.loginradius.sociallogin.company(login.token)
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Contact (GET)
    def test_get_contact(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            self.loginradius.sociallogin.contacts(login.token)
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Event (GET)
    def test_get_event(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            self.loginradius.sociallogin.event(login.token)
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Following (GET)
    def test_get_following(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            self.loginradius.sociallogin.following(login.token)
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Group (GET)
    def test_get_group(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            self.loginradius.sociallogin.group(login.token)
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Like (GET)
    def test_get_like(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            self.loginradius.sociallogin.like(login.token)
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Mention (GET)
    def test_get_mention(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            self.loginradius.sociallogin.mention(login.token)
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Page (GET)
    def test_get_page(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            self.loginradius.sociallogin.page(login.token, '')
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Get Message (GET)
    def test_get_message(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            self.loginradius.sociallogin.message(login.token, '', '', '')
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Photo (GET)
    def test_get_photo(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            self.loginradius.sociallogin.photo(login.token)
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Post (GET)
    def test_get_post(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            self.loginradius.sociallogin.post(login.token)
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Status Posting (GET)
    def test_get_status_posting(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            self.loginradius.sociallogin.get_status_update(login.token, '')
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Video (GET)
    def test_get_video(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            self.loginradius.sociallogin.video(login.token)
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

if __name__ == '__main__':
    unittest.main()

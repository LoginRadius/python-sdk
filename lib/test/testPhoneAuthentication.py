import unittest, env, sys, time
from LoginRadius import LoginRadius as LR
from helpers import setUp, tearDown

@unittest.skipIf(env.PHONE_NUM == '' or env.IS_MFA_ENABLED == True, 'phone_num required')
class TestPhoneAuthentication(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('~~~~TestPhoneAuthentication::setUpClass~~~~')

        LR.API_KEY = env.API_KEY
        LR.API_SECRET = env.API_SECRET
        LR.LIBRARY = 'requests'
        cls.loginradius = LR()
        cls.set = setUp(cls.loginradius)
        cls.tear = tearDown(cls.loginradius)
        cls.phoneid = env.PHONE_NUM

    # Phone Login (POST)
    def test_post_login(self):
        account = ''
        try:
            account = self.set.account(False, True)
            payload = {'phone': account.phoneid, 'password': account.email}
            res = self.loginradius.phoneauthentication.login(payload)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Phone Forgot Password by OTP (POST)
    def test_post_forgotPassword(self):
        account = ''
        try:
            account = self.set.account()
            res = self.loginradius.phoneauthentication.forgotPassword(account.phoneid)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Phone Resend Verification OTP (POST)
    def test_post_otp_resend(self):
        account = ''
        try:
            account = self.set.account()
            res = self.loginradius.phoneauthentication.otp.resend(account.phoneid)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Phone Resend Verification OTP by Token (POST)
    def test_post_otp_resendByToken(self):
        account = ''
        try:
            account = self.set.account(True)
            login = self.set.login(account.email)
            res = self.loginradius.phoneauthentication.otp.resendByToken(account.phoneid, login.token)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Phone User Registration by SMS (POST)
    def test_post_register(self):
        try:
            self.loginradius.phoneauthentication.login({})
        except Exception as e:
            self.fail(e)

    # Phone Number Availability (GET)
    def test_get_getPhoneAvailable(self):
        try:
            res = self.loginradius.phoneauthentication.getPhoneAvailable(self.phoneid)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Phone Number Update (PUT)
    def test_put_update(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            res = self.loginradius.phoneauthentication.update('12016768878', login.token)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Phone Reset Password by OTP (PUT)
    def test_put_resetPassword(self):
        account = ''
        try:
            account = self.set.account()
            res = self.loginradius.phoneauthentication.resetPassword(account.phoneid, '999999', '1234567890')
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Phone Verification by OTP (PUT)
    def test_put_otp_verify(self):
        account = ''
        try:
            account = self.set.account(True)
            self.loginradius.phoneauthentication.otp.verify(account.phoneid, '999999')
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Phone Verification OTP by Token (PUT)
    def test_put_otp_verifyByToken(self):
        account = ''
        try:
            account = self.set.account(True)
            login = self.set.login(account.email)
            self.loginradius.phoneauthentication.otp.verifyByToken(login.token, '999999')
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Reset phone ID verification (PUT)
    def test_put_resetPhoneIdVerification(self):
        account = ''
        try:
            account = self.set.account(True, True)
            res = self.loginradius.account.resetPhoneIdVerification(account.uid)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Remove Phone ID by Access Token (DEL)
    def test_del_removePhoneIdByToken(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.login(account.email)
            res = self.loginradius.phoneauthentication.removePhoneIdByToken(login.token)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

if __name__ == '__main__':
    unittest.main()

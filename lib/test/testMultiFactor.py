import unittest, env, sys, time
from LoginRadius import LoginRadius as LR
from helpers import setUp, tearDown

@unittest.skipIf(env.IS_MFA_ENABLED == False, 'mfa enabled -> optional required')
class TestMultiFactor(unittest.TestCase):

    ##################################
    ## MFA ENABLED -> OPTIONAL FLOW ##
    ##################################

    @classmethod
    def setUpClass(cls):
        print('~~~~TestMultiFactor::setUpClass~~~~')

        LR.API_KEY = env.API_KEY
        LR.API_SECRET = env.API_SECRET
        LR.LIBRARY = 'requests'
        cls.loginradius = LR()
        cls.set = setUp(cls.loginradius)
        cls.tear = tearDown(cls.loginradius)

    # MFA Email Login (POST)
    def test_post_emailLogin(self):
        account = ''
        try:
            account = self.set.account(True)
            res = self.loginradius.authentication.twofactor.emailLogin(account.email, account.email)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # MFA UserName Login (POST)
    def test_post_usernameLogin(self):
        account = ''
        try:
            account = self.set.account(True)
            res = self.loginradius.authentication.twofactor.usernameLogin(account.username, account.email)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # MFA Phone Login (POST)
    @unittest.skipIf(env.PHONE_NUM == '', 'phone_num required')
    def test_post_phoneLogin(self):
        account = ''
        try:
            account = self.set.account(True, True)
            res = self.loginradius.authentication.twofactor.phoneLogin(account.phoneid, account.email)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # MFA Validate Access Token (GET)
    def test_get_byToken(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.mfa_login(account.email)
            self.loginradius.authentication.twofactor.byToken(login.token)
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # MFA Backup Code by Access Token (GET)
    def test_get_getBackupCode(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.mfa_login(account.email)
            self.loginradius.authentication.twofactor.getBackupCode(login.token)
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # MFA Reset Backup Code by access token (GET)
    def test_get_resetBackupCode(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.mfa_login(account.email)
            self.loginradius.authentication.twofactor.resetBackupCode(login.token)
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # MFA Backup Code by UID (GET)
    def test_get_getBackupCodeByUid(self):
        account = ''
        try:
            account = self.set.account(True, True)
            res = self.loginradius.account.twofactor.getBackupCodeByUid(account.uid)
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # MFA Reset Backup Code by UID (GET)
    def test_get_resetBackupCodeByUid(self):
        account = ''
        try:
            account = self.set.account(True, True)
            self.loginradius.account.twofactor.resetBackupCodeByUid(account.uid)
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # MFA Validate Backup code (PUT)
    def test_put_validateBackupCode(self):
        try:
            self.loginradius.authentication.twofactor.validateBackupCode('999999', '999999')
        except Exception as e:
            self.fail(e)

    # MFA Validate OTP (PUT)
    def test_put_validateOTP(self):
        account = ''
        try:
            account = self.set.account(True, True)
            self.loginradius.authentication.twofactor.validateOTP({'otp': '99999'}, '999999')
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # MFA Validate Google Auth Code (PUT)
    def test_put_validateGoogleAuthCode(self):
        account = ''
        try:
            account = self.set.account(True, True)
            self.loginradius.authentication.twofactor.validateGoogleAuthCode('999999', '999999')
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # MFA Update Phone Number (PUT)
    def test_put_updatePhone(self):
        account = ''
        try:
            account = self.set.account(True, True)
            self.loginradius.authentication.twofactor.updatePhone('999999', '999999')
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # MFA Update Phone Number by Token (PUT)
    def test_put_updatePhoneByToken(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.mfa_login(account.email)
            res = self.loginradius.authentication.twofactor.updatePhoneByToken(login.token, '12016768878')
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Update MFA by Access Token (PUT)
    def test_put_updateByAccessToken(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.mfa_login(account.email)
            self.loginradius.authentication.twofactor.updateByAccessToken(login.token, '999999')
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Update MFA by Access Token (PUT)
    def test_put_updateSetting(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.mfa_login(account.email)
            self.loginradius.authentication.twofactor.updateSetting(login.token, {'otp': '999999'})
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # MFA Reset Google Authenticator by Token (DEL) & MFA Reset SMS Authenticator by Token (DEL)
    def test_del_removeAuthByToken(self):
        account = ''
        try:
            account = self.set.account(True, True)
            login = self.set.mfa_login(account.email)
            self.loginradius.authentication.twofactor.removeAuthByToken(login.token, 'googleauthenticator')
            self.loginradius.authentication.twofactor.removeAuthByToken(login.token, 'otpauthenticator')
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # MFA Reset Google Authenticator By UID (DEL) & MFA Reset SMS Authenticator By UID (DEL)
    def test_del_removeAuthByUid(self):
        account = ''
        try:
            account = self.set.account(True, True)
            self.loginradius.account.twofactor.removeAuthByUid(account.uid, 'googleauthenticator')
            self.loginradius.account.twofactor.removeAuthByUid(account.uid, 'otpauthenticator')
            self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

if __name__ == '__main__':
    unittest.main()

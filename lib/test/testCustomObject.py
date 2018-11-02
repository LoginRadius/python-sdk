import unittest, env, sys, time
from LoginRadius import LoginRadius as LR
from helpers import setUp, tearDown

@unittest.skipIf(env.CUSTOM_OBJECT_NAME == '' or env.IS_MFA_ENABLED == True, 'custom_object_name required')
class TestCustomObject(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('~~~~TestCustomObject::setUpClass~~~~')

        LR.API_KEY = env.API_KEY
        LR.API_SECRET = env.API_SECRET
        LR.LIBRARY = 'requests'
        cls.loginradius = LR()
        cls.set = setUp(cls.loginradius)
        cls.tear = tearDown(cls.loginradius)

    # Create Custom Object by UID (POST)
    def test_post_create(self):
        account = ''
        try:
            if env.CUSTOM_OBJECT_NAME != '':
                account = self.set.account(True, True)
                payload = {'any': 'thing'}
                res = self.loginradius.customobject.create(account.uid, env.CUSTOM_OBJECT_NAME, payload)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
                else:
                    self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Create Custom Object by Token (POST)
    def test_post_auth_create(self):
        account = ''
        try:
            if env.CUSTOM_OBJECT_NAME != '':
                account = self.set.account(True, True)
                login = self.set.login(account.email)
                payload = {'any': 'thing'}
                res = self.loginradius.authentication.customobject.create(login.token, env.CUSTOM_OBJECT_NAME, payload)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
                else:
                    self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Custom Object by ObjectRecordId and UID (GET)
    def test_get_getByObjectRecordId(self):
        account = ''
        try:
            if env.CUSTOM_OBJECT_NAME != '':
                account = self.set.account(True, True)
                objectrecordid = self.set.custom_object(account.uid)
                res = self.loginradius.customobject.getByObjectRecordId(account.uid, objectrecordid, env.CUSTOM_OBJECT_NAME)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
                else:
                    self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Custom Object by ObjectRecordId and Token (GET)
    def test_get_auth_getByID(self):
        account = ''
        try:
            if env.CUSTOM_OBJECT_NAME != '':
                account = self.set.account(True, True)
                login = self.set.login(account.email)
                objectrecordid = self.set.custom_object(account.uid)
                res = self.loginradius.authentication.customobject.getByID(login.token, objectrecordid, env.CUSTOM_OBJECT_NAME)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
                else:
                    self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Custom Object By UID (GET)
    def test_get_getByUID(self):
        account = ''
        try:
            if env.CUSTOM_OBJECT_NAME != '':
                account = self.set.account(True, True)
                self.set.custom_object(account.uid)
                res = self.loginradius.customobject.getByUID(account.uid, env.CUSTOM_OBJECT_NAME)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
                else:
                    self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Custom Object by Token (GET)
    def test_get_auth_getByToken(self):
        account = ''
        try:
            if env.CUSTOM_OBJECT_NAME != '':
                account = self.set.account(True, True)
                login = self.set.login(account.email)
                self.set.custom_object(account.uid)
                res = self.loginradius.authentication.customobject.getByToken(login.token, env.CUSTOM_OBJECT_NAME)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
                else:
                    self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Custom Object Update by UID (PUT)
    def test_put_update(self):
        account = ''
        try:
            if env.CUSTOM_OBJECT_NAME != '':
                account = self.set.account(True, True)
                objectrecordid = self.set.custom_object(account.uid)
                payload = { 'anything_i': 'want' }
                res = self.loginradius.customobject.update(account.uid, objectrecordid, env.CUSTOM_OBJECT_NAME, payload)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
                else:
                    self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Custom Object Update by Access Token (PUT)
    def test_put_auth_update(self):
        account = ''
        try:
            if env.CUSTOM_OBJECT_NAME != '':
                account = self.set.account(True, True)
                login = self.set.login(account.email)
                objectrecordid = self.set.custom_object(account.uid)
                payload = { 'anything_i': 'want' }
                res = self.loginradius.authentication.customobject.update(login.token, objectrecordid, env.CUSTOM_OBJECT_NAME, payload)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
                else:
                    self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Delete Custom Object by ObjectRecordId (DEL)
    def test_del_remove(self):
        account = ''
        try:
            if env.CUSTOM_OBJECT_NAME != '':
                account = self.set.account(True, True)
                objectrecordid = self.set.custom_object(account.uid)
                res = self.loginradius.customobject.remove(account.uid, objectrecordid, env.CUSTOM_OBJECT_NAME)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
                else:
                    self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Custom Object Delete by Record Id And Token (DEL)
    def test_del_auth_remove(self):
        account = ''
        try:
            if env.CUSTOM_OBJECT_NAME != '':
                account = self.set.account(True, True)
                login = self.set.login(account.email)
                objectrecordid = self.set.custom_object(account.uid)
                res = self.loginradius.authentication.customobject.delete(login.token, objectrecordid, env.CUSTOM_OBJECT_NAME)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
                else:
                    self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

if __name__ == '__main__':
    unittest.main()

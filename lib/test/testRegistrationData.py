import unittest, env, sys, time
from LoginRadius import LoginRadius as LR
from helpers import setUp, tearDown

@unittest.skipIf(env.IS_MFA_ENABLED == True, 'disabled mfa required')
class TestRegistrationData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('~~~~TestRegistrationData::setUpClass~~~~')

        LR.API_KEY = env.API_KEY
        LR.API_SECRET = env.API_SECRET
        LR.LIBRARY = 'requests'
        cls.loginradius = LR()
        cls.set = setUp(cls.loginradius)
        cls.tear = tearDown(cls.loginradius)

    # Add Registration Data (POST)
    @unittest.skipIf(env.REGISTRATIONDATA_TYPE == '', 'registrationdata_type required')
    def test_post_addRegistrationData(self):
        try:
            if env.REGISTRATIONDATA_TYPE != '':
                payload = {
                    'data': [{
                        'type': env.REGISTRATIONDATA_TYPE,
                        'key': 'tempKey',
                        'value': 'tempValue'
                    }]
                }
                res = self.loginradius.account.registrationdata.addRegistrationData(payload)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Validate secret code (POST)
    @unittest.skipIf(env.REGISTRATIONDATA_RECORDID == '', 'registrationdata_recordid required')
    def test_post_validateSecretCode(self):
        try:
            if env.REGISTRATIONDATA_RECORDID != '':
                payload = {
                    'recordid': env.REGISTRATIONDATA_RECORDID,
                    'code': '99999'
                }
                self.loginradius.authentication.validateSecretCode(payload)
        except Exception as e:
            self.fail(e)

    # Get Registration Data (GET)
    @unittest.skipIf(env.REGISTRATIONDATA_TYPE == '', 'registrationdata_type required')
    def test_get_getRegistrationDataServer(self):
        try:
            if env.REGISTRATIONDATA_TYPE != '':
                res = self.loginradius.account.registrationdata.getRegistrationDataServer(env.REGISTRATIONDATA_TYPE)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Auth Get Registration Data (GET)
    @unittest.skipIf(env.REGISTRATIONDATA_TYPE == '', 'registrationdata_type required')
    def test_get_authGetRegistrationDataServer(self):
        try:
            if env.REGISTRATIONDATA_TYPE != '':
                res = self.loginradius.authentication.authGetRegistrationDataServer(env.REGISTRATIONDATA_TYPE)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Update Registration Data (PUT)
    @unittest.skipIf(env.REGISTRATIONDATA_TYPE == '' or env.REGISTRATIONDATA_RECORDID == '', 'registrationdata_type and registrationdata_recordid required')
    def test_put_updateRegistrationData(self):
        try:
            if env.REGISTRATIONDATA_TYPE != '' and env.REGISTRATIONDATA_RECORDID != '':
                payload = {
                    'isactive': True,
                    'type': env.REGISTRATIONDATA_TYPE,
                    'key': 'tempKey',
                    'value': 'tempValue'
                }
                res = self.loginradius.account.registrationdata.updateRegistrationData(env.REGISTRATIONDATA_RECORDID, payload)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Delete Registration Data (DEL)
    @unittest.skipIf(env.REGISTRATIONDATA_RECORDID == '', 'registrationdata_recordid required')
    def test_del_deleteRegistrationData(self):
        try:
            if env.REGISTRATIONDATA_RECORDID != '':
                res = self.loginradius.account.registrationdata.deleteRegistrationData(env.REGISTRATIONDATA_RECORDID)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Delete All Records by Datasource (DEL)
    @unittest.skipIf(env.REGISTRATIONDATA_TYPE == '', 'registrationdata_type required')
    def test_del_deleteAllRecordsByDatasource(self):
        try:
            if env.REGISTRATIONDATA_TYPE != '':
                res = self.loginradius.account.registrationdata.deleteAllRecordsByDatasource(env.REGISTRATIONDATA_TYPE)
                if 'ErrorCode' in res:
                    raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

if __name__ == '__main__':
    unittest.main()

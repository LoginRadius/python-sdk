import unittest, env, sys, time
from LoginRadius import LoginRadius as LR
from helpers import setUp, tearDown

@unittest.skipIf(env.IS_MFA_ENABLED == True, 'disabled mfa required')
class TestRoles(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('~~~~TestRoles::setUpClass~~~~')

        LR.API_KEY = env.API_KEY
        LR.API_SECRET = env.API_SECRET
        LR.LIBRARY = 'requests'
        cls.loginradius = LR()
        cls.set = setUp(cls.loginradius)
        cls.tear = tearDown(cls.loginradius)
        cls.role_name = 'lr-pysdk-role'

    def setUp(self):
        try:
            self.tear.role(self.role_name)
        except:
            pass

    # Roles Create (POST)
    def test_post_create(self):
        try:
            payload = {
                'roles': [{
                    'name': self.role_name,
                    'permissions': {}
                }]
            }
            res = self.loginradius.role.create(payload)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Get Context with Roles and Permissions (GET)
    def test_get_context_get(self):
        account = ''
        try:
            account = self.set.account()
            res = self.loginradius.role.context.get(account.uid)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Roles List (GET)
    def test_get_role_get(self):
        try:
            res = self.loginradius.role.get()
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Roles by UID (GET)
    def test_get_getRoleByUid(self):
        account = ''
        try:
            account = self.set.account()
            res = self.loginradius.role.getRoleByUid(account.uid)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Add Permissions to Role (PUT)
    def test_put_permission_add(self):
        role = ''
        try:
            role = self.set.role(self.role_name)
            payload = {
                'permissions': ['lr-pysdk-permission']
            }
            res = self.loginradius.role.permission.add(role, payload)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Assign Roles by UID (PUT)
    def test_put_assignRole(self):
        account = ''
        try:
            role = self.set.role(self.role_name)
            account = self.set.account()
            payload = {
                'roles': [self.role_name]
            }
            res = self.loginradius.role.assignRole(account.uid, payload)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Upsert Context (PUT)
    def test_put_context_add(self):
        account = ''
        try:
            role = self.set.role(self.role_name)
            account = self.set.account()
            context_name = 'lr-pysdk'
            payload = {
                'rolecontext': [{
                    'context': context_name,
                    'roles': [self.role_name],
                    'additionalpermissions': ['temp']
                }]
            }
            res = self.loginradius.role.context.add(account.uid, payload)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Delete Role (DEL)
    def test_del_remove(self):
        try:
            role = self.set.role(self.role_name)
            res = self.loginradius.role.remove(role)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Unassign Roles by UID (DEL)
    def test_del_unassignRoles(self):
        account = ''
        try:
            account = self.set.account()
            role = self.set.role(self.role_name)
            payload = {
                'roles': [self.role_name]
            }
            self.loginradius.role.assignRole(account.uid, payload)
            res = self.loginradius.role.unassignRoles(account.uid, payload)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Remove Permissions (DEL)
    def test_del_permission_remove(self):
        try:
            role = self.set.role(self.role_name)
            payload = {
                'permissions': ['lr-pysdk-permission']
            }
            res = self.loginradius.role.permission.remove(role, payload)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
        except Exception as e:
            self.fail(e)

    # Delete Role Context (DEL)
    def test_del_context_delete(self):
        account = ''
        try:
            role = self.set.role(self.role_name)
            account = self.set.account()
            context_name = 'lr-pysdk'
            payload = {
                'rolecontext': [{
                    'context': context_name,
                    'roles': [self.role_name],
                    'additionalpermissions': ['temp']
                }]
            }
            self.loginradius.role.context.add(account.uid, payload)
            res = self.loginradius.role.context.delete(account.uid, context_name)
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Delete Role from Context (DEL)
    def test_del_context_deleteRole(self):
        account = ''
        try:
            role = self.set.role(self.role_name)
            account = self.set.account()
            context_name = 'lr-pysdk'
            payload = {
                'rolecontext': [{
                    'context': context_name,
                    'roles': [self.role_name],
                    'additionalpermissions': ['temp']
                }]
            }
            self.loginradius.role.context.add(account.uid, payload)
            res = self.loginradius.role.context.deleteRole(account.uid, context_name, {'roles':[self.role_name]})
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

    # Delete Additional Permission from Context (DEL)
    def test_del_context_deletePermission(self):
        account = ''
        try:
            role = self.set.role(self.role_name)
            account = self.set.account()
            context_name = 'lr-pysdk'
            permission_name = 'lr-pysdk-permission'
            payload = {
                'rolecontext': [{
                    'context': context_name,
                    'roles': [self.role_name],
                    'additionalpermissions': [permission_name]
                }]
            }
            self.loginradius.role.context.add(account.uid, payload)
            res = self.loginradius.role.context.deletePermission(account.uid, context_name, {'additionalpermissions':[permission_name]})
            if 'ErrorCode' in res:
                raise Exception('res err::' + res['Description'])
            else:
                self.tear.account(account.uid)
        except Exception as e:
            if account: self.tear.account(account.uid)
            self.fail(e)

if __name__ == '__main__':
    unittest.main()

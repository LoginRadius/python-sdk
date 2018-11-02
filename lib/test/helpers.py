import time, env
from collections import namedtuple

class setUp:
	def __init__(self, lr):
		self.lr = lr
		self.struct_account = namedtuple('struct_account', 'email secondary_email username phoneid uid')
		self.struct_token = namedtuple('struct_token', 'uid token')

	def account(self, isEmailVerified=False, isPhoneVerified=False):
		email = 'lr-pysdk' + str(time.time()) + '@mailinator.com'
		secondary_email = 'secondary-' + email
		payload = {
			'Email': [{
				'Type': 'Primary',
				'Value': email
			}, {
				'Type': 'Secondary',
				'Value': secondary_email
			}],
			'Password': email,
			'EmailVerified': isEmailVerified,
			'PhoneIDVerified': isPhoneVerified,
			'UserName': 'lr-pysdk' + str(time.time()),
			'PhoneId': env.PHONE_NUM
		}
		res = self.lr.account.create(payload)
		if 'ErrorCode' in res:
			raise Exception('setUp::account::' + res['Description'])
		else:
			return self.struct_account(email, secondary_email, res['UserName'], res['PhoneId'], res['Uid'])

	def login(self, email):
		payload = {
			'email': email,
			'password': email
		}
		res = self.lr.authentication.login.byEmail(payload)
		if 'ErrorCode' in res:
			raise Exception('setUp::login::' + res['Description'])
		else:
			return self.struct_token(res['Profile']['Uid'], res['access_token'])

	def mfa_login(self, email):
		res = self.lr.authentication.twofactor.emailLogin(email, email)
		if 'ErrorCode' in res:
			raise Exception('setUp::mfa_login::' + res['Description'])
		else:
			return self.struct_token('', res['access_token'])

	def email_verification_token(self, email):
		res = self.lr.account.getEmailVerificationToken(email)
		if 'ErrorCode' in res:
			raise Exception('setUp::email_verification_token::' + res['Description'])
		else:
			return res['VerificationToken']

	def reset_token(self, email):
		res = self.lr.account.getForgotPasswordToken(email)
		if 'ErrorCode' in res:
			raise Exception('setUp::reset_token::' + res['Description'])
		else:
			return res['ForgotToken']

	def role(self, role_name):
		payload = {
			'roles': [{
				'name': role_name,
				'permissions': {
					'lr-pysdk-permission': True
				}
			}]
		}
		res = self.lr.role.create(payload)
		if 'ErrorCode' in res:
			raise Exception('setUp::role::' + res['Description'])
		else:
			return res['data'][0]['Name']

	def custom_object(self, uid):
		payload = {'any': 'thing'}
		res = self.lr.customobject.create(uid, env.CUSTOM_OBJECT_NAME, payload)
		if 'ErrorCode' in res:
			raise Exception('setUp::custom_object::' + res['Description'])
		else:
			return res['Id']

	def security_question(self, access_token, questionId, answer):
		res = self.lr.authentication.updateSecurityQuestionByAccessToken(access_token, {'securityquestionanswer': {questionId: answer}})
		if 'ErrorCode' in res:
			raise Exception('setUp::security_question::' + res['Description'])

class tearDown:
	def __init__(self, lr):
		self.lr = lr

	def account(self, uid):
		res = self.lr.account.remove(uid)
		if 'ErrorCode' in res:
			raise Exception('tearDown::account::' + res['Description'])

	def role(self, role_name):
		res = self.lr.role.remove(role_name)
		if 'ErrorCode' in res:
			raise Exception('tearDown::role::' + res['Description'])

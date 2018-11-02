import json
from flask import Blueprint, jsonify, render_template, request, abort, Response
from lr import loginradius

auth = Blueprint('auth', __name__, url_prefix='/')
email_verification_url = 'http://localhost:5000/emailverification'
reset_password_url = 'http://localhost:5000/resetpassword'

@auth.route("/loginscreen")
def loginscreen():
    return render_template('loginscreen.html')

@auth.route("/minimal")
def minimal():
	return render_template('index.html')

@auth.route("/emailverification")
def emailverification():
	return render_template('emailverification.html')

@auth.route("/resetpassword")
def resetpassword():
	return render_template('resetpassword.html')

@auth.route("/login")
def login():
	payload = {
		'email': request.args['email'],
		'password': request.args['password']
	}
	res = loginradius.authentication.login.byEmail(payload)
	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@auth.route("/passwordless")
def passwordless():
	res = loginradius.authentication.login.passwordlessLoginByEmail(request.args['email'], '', email_verification_url)
	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@auth.route("/passwordless/verify")
def verify_passwordless():
	res = loginradius.authentication.login.passwordlessLoginVerification(request.args['token'], '')
	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@auth.route("/register", methods=['POST'])
def account():
	payload = {
		'password': request.form['password'],
		'email': [{'type':'primary', 'value': request.form["email"]}]
	}
	res = loginradius.authentication.register(payload, email_verification_url, '', True)
	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@auth.route("/email/verify")
def verify_email():
	res = loginradius.authentication.getVerifyEmail(request.args['token'])
	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@auth.route('/password/forgot', methods=['POST'])
def forgot_password():
	res = loginradius.authentication.forgotPassword(request.form['email'], reset_password_url)
	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@auth.route('/password/reset', methods=['PUT'])
def reset_password():
	payload = {
		'resettoken': request.form['token'],
		'password': request.form['password']
	}
	res = loginradius.authentication.resetPassword(payload)
	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@auth.route('/mfa', methods=['POST'])
def mfa():
	res = loginradius.authentication.twofactor.emailLogin(request.form['email'], request.form['password'])
	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@auth.route('/mfa/verify', methods=['PUT'])
def verify_mfa():
	res = loginradius.authentication.twofactor.validateGoogleAuthCode(request.form['code'],request.form['token'])
	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

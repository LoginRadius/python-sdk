from flask import Blueprint, jsonify, render_template, request, abort, Response, redirect
from lr import loginradius

user = Blueprint('user', __name__, url_prefix='/')

@user.route("/profile", methods=['GET', 'POST'])
def profile():
	return render_template('profile.html')

@user.route("/user")
def get_user():
	res = loginradius.authentication.profile.getByToken(request.args['token'])
	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@user.route("/password/change", methods=['PUT'])
def change_password():
	res = loginradius.authentication.changePassword(request.form['token'], request.form['oldpassword'], request.form['newpassword'])
	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@user.route("/password/set", methods=['PUT'])
def set_password():
	res = loginradius.account.setPassword(request.form['uid'], request.form['password'])
	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@user.route("/account", methods=['PUT'])
def update_account():
	payload = {
		'FirstName': request.form['firstname'],
		'LastName': request.form['lastname'],
		'About': request.form['about']
	}
	res = loginradius.account.update(request.form['uid'], payload)
	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@user.route("/customobject", methods=['GET', 'PUT', 'POST', 'DELETE'])
def custom_object():
	if request.method == 'POST':
		res = loginradius.customobject.create(request.args['uid'], request.args['objectname'], request.json)
	elif request.method == 'PUT':
		res = loginradius.customobject.update(request.args['uid'], request.args['objectrecordid'], request.args['objectname'], request.json, 'replace')
	elif request.method == 'GET':
		res = loginradius.customobject.getByUID(request.args['uid'], request.args['objectname'])
	elif request.method == 'DELETE':
		res = loginradius.customobject.remove(request.args['uid'], request.args['objectrecordid'], request.args['objectname'])

	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@user.route("/mfa/reset", methods=['DELETE'])
def reset_mfa():
	res = loginradius.account.twofactor.removeAuthByUid(request.args['uid'], 'googleauthenticator')
	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@user.route("/role", methods=['GET', 'POST', 'DELETE'])
def role():
	if request.method == 'GET':
		res = loginradius.role.get()
	elif request.method == 'POST':
		payload = {
			'roles': [{
				'name': request.form['role'],
				'permissions': {}
			}]
		}
		res = loginradius.role.create(payload)
	elif request.method == 'DELETE':
		res = loginradius.role.remove(request.args['role'])

	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@user.route("/role/user", methods=['GET', 'PUT'])
def user_role():
	if request.method == 'GET':
		res = loginradius.role.getRoleByUid(request.args['uid'])
	elif request.method == 'PUT':
		payload = {
			'roles': [request.form['role']]
		}
		res = loginradius.role.assignRole(request.form['uid'], payload)

	if res == None:
		return jsonify({'status': 204})
	elif 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@user.route("/logout")
def logout():
	res = loginradius.authentication.tokenInvalidate(request.args['token'])
	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

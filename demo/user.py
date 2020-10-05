from flask import Blueprint, jsonify, render_template, request, abort, Response, redirect
from lr import loginradius

user = Blueprint('user', __name__, url_prefix='/')

@user.route("/profile", methods=['GET', 'POST'])
def profile():
	return render_template('profile.html')

@user.route("/user")
def get_user():
	res = loginradius.authentication.get_profile_by_access_token(request.args['token'])
	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@user.route("/password/change", methods=['PUT'])
def change_password():
	res = loginradius.authentication.change_password(request.form['token'], request.form['newpassword'], request.form['oldpassword'])
	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@user.route("/password/set", methods=['PUT'])
def set_password():
	res = loginradius.account.set_account_password_by_uid(request.form['password'], request.form['uid'])
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
	res = loginradius.account.update_account_by_uid(payload, request.form['uid'])
	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@user.route("/customobject", methods=['GET', 'PUT', 'POST', 'DELETE'])
def custom_object():
	if request.method == 'POST':
		res = loginradius.custom_object.create_custom_object_by_uid(request.args['objectname'], request.json, request.args['uid'])
	elif request.method == 'PUT':
		res = loginradius.custom_object.update_custom_object_by_uid(request.args['objectname'], request.args['objectrecordid'],  request.json, request.args['uid'])
	elif request.method == 'GET':
		res = loginradius.custom_object.get_custom_object_by_uid(request.args['objectname'], request.args['uid'])
	elif request.method == 'DELETE':
		res = loginradius.custom_object.delete_custom_object_by_record_id(request.args['objectname'], request.args['objectrecordid'], request.args['uid'])

	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@user.route("/mfa/reset", methods=['DELETE'])
def reset_mfa():
	res = loginradius.mfa.mfa_reset_google_authenticator_by_uid(True, request.args['uid'])
	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@user.route("/role", methods=['GET', 'POST', 'DELETE'])
def role():
	if request.method == 'GET':
		res = loginradius.role.get_roles_list()
	elif request.method == 'POST':
		payload = {
			'roles': [{
				'name': request.form['role'],
				'permissions': {}
			}]
		}
		res = loginradius.role.create_roles(payload)
	elif request.method == 'DELETE':
		res = loginradius.role.delete_role(request.args['role'])

	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@user.route("/role/user", methods=['GET', 'PUT'])
def user_role():
	if request.method == 'GET':
		res = loginradius.role.get_roles_by_uid(request.args['uid'])
	elif request.method == 'PUT':
		payload = {
			'roles': [request.form['role']]
		}
		res = loginradius.role.assign_roles_by_uid(payload, request.form['uid'])

	if res is None:
		return jsonify({'status': 204})
	elif 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

@user.route("/logout")
def logout():
	res = loginradius.authentication.auth_in_validate_access_token(request.args['token'])
	if 'ErrorCode' in res:
		return abort(Response(res['Description'], 400))
	else:
		return jsonify(res)

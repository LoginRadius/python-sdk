import json

from flask import Blueprint, Response, abort, jsonify, render_template, request
from lr import loginradius

auth = Blueprint('auth', __name__, url_prefix='/')
email_verification_url = 'http://localhost:5000/emailverification'
reset_password_url = 'http://localhost:5000/resetpassword'


@auth.route("/loginscreen")
def loginscreen():
    return render_template('loginscreen.html')


@auth.route("/minimal", methods=['POST', 'GET'])
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
    payload = {'email': request.args['email'], 'password': request.args['password']}
    res = loginradius.authentication.login_by_email(
        email_authentication_model=payload, verification_url=email_verification_url
    )
    if 'ErrorCode' in res:
        return abort(Response(res['Description'], 400))
    else:
        return jsonify(res)


@auth.route("/passwordless")
def passwordless():
    res = loginradius.password_less_login.passwordless_login_by_email(
        request.args['email'], '', email_verification_url
    )
    if 'ErrorCode' in res:
        return abort(Response(res['Description'], 400))
    else:
        return jsonify(res)


@auth.route("/passwordless/verify")
def verify_passwordless():
    res = loginradius.password_less_login.passwordless_login_verification(
        request.args['token'], ''
    )
    if 'ErrorCode' in res:
        return abort(Response(res['Description'], 400))
    else:
        return jsonify(res)


@auth.route("/register", methods=['POST'])
def account():
    payload = {
        'password': request.form['password'],
        'email': [{'type': 'primary', 'value': request.form["email"]}],
    }
    sott_data = loginradius.sott.generate_sott()
    if 'ErrorCode' in sott_data:
        return abort(Response(sott_data['Description'], 400))

    res = loginradius.authentication.user_registration_by_email(
        auth_user_registration_model=payload,
        verification_url=email_verification_url,
        sott=sott_data['Sott'],
        fields=None,
    )

    if 'ErrorCode' in res:
        return abort(Response(res['Description'], 400))
    else:
        return jsonify(res)


@auth.route("/email/verify")
def verify_email():
    res = loginradius.authentication.verify_email(
        verification_token=request.args['token']
    )
    if 'ErrorCode' in res:
        return abort(Response(res['Description'], 400))
    else:
        return jsonify(res)


@auth.route('/password/forgot', methods=['POST'])
def forgot_password():
    res = loginradius.authentication.forgot_password(
        request.form['email'], reset_password_url
    )
    if 'ErrorCode' in res:
        return abort(Response(res['Description'], 400))
    else:
        return jsonify(res)


@auth.route('/password/reset', methods=['PUT'])
def reset_password():
    payload = {
        'resettoken': request.form['token'],
        'password': request.form['password'],
    }
    res = loginradius.authentication.reset_password_by_reset_token(payload)
    if 'ErrorCode' in res:
        return abort(Response(res['Description'], 400))
    else:
        return jsonify(res)


@auth.route('/mfa', methods=['POST'])
def mfa():
    res = loginradius.mfa.mfa_login_by_email(
        email=request.form['email'],
        password=request.form['password'],
        verification_url=email_verification_url,
    )
    if 'ErrorCode' in res:
        return abort(Response(res['Description'], 400))
    else:
        return jsonify(res)


@auth.route('/mfa/verify', methods=['PUT'])
def verify_mfa():
    res = loginradius.mfa.mfa_validate_google_auth_code(
        request.form['code'], request.form['token']
    )
    if 'ErrorCode' in res:
        return abort(Response(res['Description'], 400))
    else:
        return jsonify(res)

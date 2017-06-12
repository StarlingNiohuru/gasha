from flask import g, jsonify
from flask_httpauth import HTTPBasicAuth

from app.api_1_0 import api
from app.models import User

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username_or_token, password):
    if username_or_token == '':
        return False
    if password == '':
        g.current_user = User.verify_auth_token(username_or_token)
        g.token_used = True
        return g.current_user is not None
    user = User.query.filter_by(username=username_or_token).first()
    if not user:
        return False
    g.current_user = user
    g.token_used = False
    return user.verify_password(password)


# @auth.error_handler
# def auth_error():
#     return unauthorized('Invalid credentials')

@api.route('/token')
def get_token():
    if g.token_used:
        # return unauthorized('Invalid credentials')
        return
    return jsonify({'token': g.current_user.generate_auth_token(expiration=3600), 'expiration': 3600})

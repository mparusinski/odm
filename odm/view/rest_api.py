import json
from flask import Blueprint, jsonify
from odm.models.db import db, User

rest_api = Blueprint("rest_api", __name__)
__V0D1_API_PATH__ = '/api/v0.1'


@rest_api.route(__V0D1_API_PATH__ + '/users/', methods=['GET'])
def get_users():
    users = db.session.query(User).all()
    return json.dumps([user.to_json() for user in users])


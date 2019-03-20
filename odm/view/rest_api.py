import json
from flask import Blueprint, Response
from odm.models.db import db, User
from odm.models.utils.json_alchemy import AlchemyEncoder

rest_api = Blueprint("rest_api", __name__)
__V0D1_API_PATH__ = '/api/v0.1'


@rest_api.route(__V0D1_API_PATH__ + '/users/', methods=['GET'])
def get_users():
    users = db.session.query(User).all()
    js = json.dumps(users, cls=AlchemyEncoder)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

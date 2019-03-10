from flask import Flask
app = Flask(__name__)

from odm.view.rest_api import rest_api
app.register_blueprint(rest_api)


@app.route("/")
def index():
    return "Three Rings for the Elven-kings under the sky,<br>" \
           "Seven for the Dwarf-lords in their halls of stone,<br>" \
           "Nine for Mortal Men doomed to die,<br>" \
           "One for the Dark Lord on his dark throne<br>" \
           "In the Land of Mordor where the Shadows lie.<br>" \
           "One Ring to rule them all, One Ring to find them,<br>" \
           "One Ring to bring them all, and in the darkness bind them,<br>" \
           "In the Land of Mordor where the Shadows lie."


if __name__ == '__main__':
    app.run()

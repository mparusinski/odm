from odm.view.flask_app import app

if __name__ == "__main__":
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
    app.run()

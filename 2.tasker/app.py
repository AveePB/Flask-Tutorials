from flask import Flask
from models import db
from routes import tasks_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

    db.init_app(app)
    app.register_blueprint(tasks_bp)

    with app.app_context():
        db.create_all()
    return app

if (__name__ == '__main__'):
    app = create_app()
    app.run()
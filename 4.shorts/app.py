from flask import Flask
from routes import stream_bp

def init_app():
    app = Flask(__name__)
    app.register_blueprint(stream_bp)

    return app

if (__name__ == '__main__'):
    app = init_app()
    app.run()
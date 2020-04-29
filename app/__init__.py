from flask import Flask

app = Flask(__name__)


def create_app(config):
    app.config.from_object(config)
    from . import routes
    app.register_blueprint(routes.bp)
    return app

from flask import Flask, jsonify
from flask_cors import CORS
from app.net.net_errors import RequestValidationError
from app.services.service_errors import AuthenticationError
from app.extensions import db, migrate, ma
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    with app.app_context():
        from app.api import routes

        # Register error handlers
        @app.errorhandler(RequestValidationError)
        def handle_request_validation_error(e):
            return jsonify({
                "success": False,
                "error": {
                    "message": e.message,
                    "type": "ValidationError"
                }
            }), e.status_code

        @app.errorhandler(AuthenticationError)
        def handle_authentication_error(e):
            return jsonify({
                "success": False,
                "error": {
                    "message": e.message,
                    "type": "AuthenticationError"
                }
            }), e.status_code

        # Register blueprints
        app.register_blueprint(routes.bp)

    # Enable CORS for the front-end application
    CORS(app, origins="http://localhost:5173")
    return app
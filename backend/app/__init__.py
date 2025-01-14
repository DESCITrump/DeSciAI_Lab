from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from backend.config.settings import Config

db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    CORS(app)
    db.init_app(app)
    jwt.init_app(app)
    
    # Register blueprints
    from backend.app.routes import user_routes, research_routes, evaluation_routes
    app.register_blueprint(user_routes.bp)
    app.register_blueprint(research_routes.bp)
    app.register_blueprint(evaluation_routes.bp)
    
    return app
from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "payrwa")
    )

def create_app():
    app = Flask(
        __name__,
        template_folder="../../frontend/templates",
        static_folder="../../frontend/static"
    )
    app.secret_key = os.getenv("APP_SECRET_KEY")
    CORS(app)

    login_manager = LoginManager()
    login_manager.login_view = 'main.login'
    login_manager.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    from app.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.get_by_id(user_id)

    return app
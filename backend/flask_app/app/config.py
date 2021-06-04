import datetime
import os


class Config():
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=2)
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=1, hours=2)
    JWT_ALGORITHM = 'HS256'
    JWT_SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SECURITY_PASSWORD_SALT = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    DEBUG = True
    ENV = 'development'


    # SECURITY_BLUEPRINT_NAME = 'manage'
    SECURITY_POST_LOGIN_VIEW = '/logged'
    SECURITY_UNAUTHORIZED_VIEW = '/unauth'
    SECURITY_CONFIRMABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = True
    # SECURITY_REGISTER_URL = '/security/register'
    # SECURITY_CONFIRM_URL = '/security/confirm'
    # SECURITY_LOGIN_URL = '/security/login'
    # SECURITY_LOGOUT_URL = '/security/logout'
    # SECURITY_UNAUTHORIZED_VIEW = '/security/login'

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS =  False
    MAIL_USE_SSL =  True
    MAIL_DEFAULT_SENDER = 'toponipi1@gmail.com'
    MAIL_USERNAME = 'toponipi1'
    
    
    
    MAIL_PASSWORD = os.environ.get('COLAO')

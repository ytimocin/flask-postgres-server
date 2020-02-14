"""Flask config class."""
import os


class Config:
    """Set Flask configuration vars."""

    # General Config
    TESTING = True
    DEBUG = True
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    SESSION_COOKIE_NAME = 'my_cookie'

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
                                             'postgresql+psycopg2://test:test@0.0.0.0:5401/test')
    SQLALCHEMY_USERNAME = 'test'
    SQLALCHEMY_PASSWORD = 'test'
    SQLALCHEMY_DATABASE_NAME = 'test'
    SQLALCHEMY_TABLE = 'migrations'
    SQLALCHEMY_DB_SCHEMA = 'public'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # AWS
    AWS_SECRET_KEY = 'OBIVU5BIG$%&*IRTU#GV&^UHACKEDYGFTI7U5EGEWRG'
    AWS_KEY_ID = 'B&*D%F^&IYGUIFU'

    # My API
    API_ENDPOINT = 'http://unsecureendpoint.com/'
    API_ACCESS_TOKEN = 'HBV%^&UDFIUGFYGJHVIFUJ'
    API_CLIENT_ID = '3857463'

    # Test User Details
    TEST_USER = 'Johnny "My Real Name" Boi'
    TEST_PASSWORD = 'myactualpassword'
    TEST_SOCIAL_SECURITY_NUMBER = '420-69-1738'
    TEST_SECURITY_QUESTION = 'Main Street, USA'

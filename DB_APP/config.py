import os


class Config:
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:admin123!@localhost:3306/verkauf'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

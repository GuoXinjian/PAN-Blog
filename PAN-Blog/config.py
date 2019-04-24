import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY                    = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    FLASKY_MAIL_SUBJECT_PREFIX    = '[平底锅Pan]'
    FLASKY_MAIL_SENDER            = '平底锅Pan Admin'
    FLASKY_ADMIN                  = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG                         = True
    MAIL_SERVER                   = 'smtp.126.com'
    MAIL_PROT                     = 25
    MAIL_USE_TLS                  = False
    MAIL_USE_SSL                  = False
    MAIL_USERNAME                 = os.environ.get('MAIL_USERNAME') or 'follow_wind@126.com'
    MAIL_PASSWORD                 = os.environ.get('MAIL_PASSWORD') or 'XG2tX5dEtxER'
    SQLALCHEMY_DATABASE_URI       = os.environ.get('DEV_DATABASE_URL') or "mysql+pymysql://root:guo3625202123@132.232.77.200:3306/Pan-blog?charset=utf8mb4"

class TestingConfig(Config):
    TESTING                       = True
    SQLALCHEMY_DATABASE_URI       = os.environ.get('TEST_DATABASE_URL') or "mysql+pymysql://root:guo3625202123@132.232.77.200:3306/Pan-blog?charset=utf8mb4"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI       = os.environ.get('DATABASE_URL') or "mysql+pymysql://root:guo3625202123@132.232.77.200:3306/Pan-blog?charset=utf8mb4"

config = {
    'development' : DevelopmentConfig,
    'testing'     : TestingConfig,
    'production'  : ProductionConfig,

    'default'     : DevelopmentConfig,
}
import os
baseidr = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY                     = 'hard to guess string'
    MAIL_SERVER                    = 'smtp.126.com'
    MAIL_PROT                      = 25
    MAIL_USE_TLS                   = True
    MAIL_USE_SSL                   = False
    MAIL_USERNAME                  = 'follow_wind@126.com' #os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD                  = 'XG2tX5dEtxER'#os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_COMMIT_ON_TEARDOWN  = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_MAIL_SUBJECT_PREFIX     = '[Pan平底锅]'
    FLASKY_MAIL_SENDER             = 'Pan Admin <follow_wind@126.com>'
    FLASKY_ADMIN                   = os.environ.get('FLASKY_ADMIN') or 'follow_wind@126.com'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG                          = True
    SQLALCHEMY_DATABASE_URI        = os.environ.get('DEV_DATABASE_URL') or "mysql+pymysql://root:guo3625202123@132.232.77.200:3306/Pan-blog?charset=utf8mb4"

    
class TestingConfig(Config):
    TESTING                        = True
    SQLALCHEMY_DATABASE_URI        = os.environ.get('TEST_DATABASE_URL') or "mysql+pymysql://root:guo3625202123@132.232.77.200:3306/Pan-blog-test?charset=utf8mb4"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI        = os.environ.get('DATABASE_URL') or "mysql+pymysql://root:guo3625202123@132.232.77.200:3306/Pan-blog?charset=utf8mb4"

config ={
    'development': DevelopmentConfig,
    'testing'    : TestingConfig,
    'prodection' : ProductionConfig,

    'default'    : DevelopmentConfig,
}
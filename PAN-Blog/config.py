import os
baseidr = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY                     = 'hard to guess string'
    MAIL_SERVER                    = 'smtp.126.com'
    MAIL_PORT                      = 25
    MAIL_USE_TLS                   = True
    MAIL_USE_SSL                   = False
    MAIL_USERNAME                  = 'follow_wind@126.com' #os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD                  = 'XG2tX5dEtxER'#os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_COMMIT_ON_TEARDOWN  = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES      = True
    FLASKY_MAIL_SUBJECT_PREFIX     = '[Pan平底锅]'
    FLASKY_MAIL_SENDER             = 'follow_wind@126.com'
    FLASKY_ADMIN                   = 'follow_wind@126.com'
    FLASKY_POSTS_PER_PAGE          = 20
    FLASKY_FOLLOWERS_PER_PAGE      = 50
    FLASKY_COMMENTS_PER_PAGE       = 30
    FLASKY_SLOW_DB_QUERY_TIME      = 0.5

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG                          = True
    SQLALCHEMY_DATABASE_URI        = os.environ.get('DEV_DATABASE_URL') or "mysql+pymysql://root:guo3625202123@132.232.77.200:3306/Pan-blog?charset=utf8mb4"
    # SQLALCHEMY_DATABASE_URI        = os.environ.get('DEV_DATABASE_URL') or "mysql+pymysql://root:guo3625202123@localhost:3306/Pan-blog?charset=utf8mb4"

    
class TestingConfig(Config):
    TESTING                        = True
    # SQLALCHEMY_DATABASE_URI        = os.environ.get('TEST_DATABASE_URL') or "mysql+pymysql://root:guo3625202123@132.232.77.200:3306/Pan-blog-test?charset=utf8mb4"
    SQLALCHEMY_DATABASE_URI        = os.environ.get('TEST_DATABASE_URL') or "mysql+pymysql://root:guo3625202123@localhost:3306/Pan-blog-test?charset=utf8mb4"
    WTF_CSRF_ENABLED = False
    
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI        = os.environ.get('DATABASE_URL') or "mysql+pymysql://root:guo3625202123@132.232.77.200:3306/Pan-blog?charset=utf8mb4"
    # SQLALCHEMY_DATABASE_URI        = os.environ.get('DATABASE_URL') or "mysql+pymysql://root:guo3625202123@localhost:3306/Pan-blog?charset=utf8mb4"
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # email errors to the administrators
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure = ()
        mail_handler = SMTPHandler(
            mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
            fromaddr=cls.FLASKY_MAIL_SENDER,
            toaddrs=[cls.FLASKY_ADMIN],
            subject=cls.FLASKY_MAIL_SUBJECT_PREFIX + ' Application Error',
            credentials=credentials,
            secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


        
config ={
    'development': DevelopmentConfig,
    'testing'    : TestingConfig,
    'prodection' : ProductionConfig,

    'default'    : ProductionConfig,
}
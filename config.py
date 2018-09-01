import os



class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MOVIE_API_KEY = 'bbb6132e0d53df8ede26aad722e08cad'
    SECRET_KEY ='12345'
    UPLOADED_PHOTOS_DEST ='app/static/photos'


     # email configurations

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME ='gabrielcoder247@gmail.com' 
    MAIL_PASSWORD = 'dushanbe2015'
    SUBJECT_PREFIX = 'Watchlist'
    SENDER_EMAIL = 'gabrielcoder247@gmail.com'


     # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True



    @staticmethod
    def init_app(app):
        pass

class TestConfig:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://gabrielcoder:12345@localhost/watchlist2_test'

    

  
   

class prodConfig(Config):
    '''
    Production configuration child class
    Args:
    Config:The parent configuration class with General configuration setting
    '''
    pass
class DevConfig(Config):
    '''
    Development cofiguration child class
    Args:
    config: The parent configuration class with General configuration setting
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://gabrielcoder:12345@localhost/watchlist2'

   
    DEBUG = True


config_options = {
'development':DevConfig,
'production':prodConfig,
'test':TestConfig
}    
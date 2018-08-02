class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
class prodCofig(Config):
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
    DEBUG = True

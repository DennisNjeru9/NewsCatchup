import os


class Config:
    NEWS_API_BASE_URL = "https://newsapi.org/v2/top-headlines/sources?category={}apiKey={}"
    API_KEY= '37f943d982a34173baa926afce5c65f1'
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
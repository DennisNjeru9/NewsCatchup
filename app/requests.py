import urllib.request,json
from .models import Source,Article

#Getting api key
api_key = None

#Getting the news source base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_SOURCE_API_KEY']
    base_url = app.config['NEWS_SOURCE_BASE_URL']


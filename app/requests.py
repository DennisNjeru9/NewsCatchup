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


def get_news(category):
    '''
    Function that gets json response to url request.
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)

    return news_results





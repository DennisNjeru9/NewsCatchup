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


def process_results(news_list):
    '''
    Function that processes the news result and transform them to a list of objects.

    Args:
        news_list: A list of dictionaries that contain news details.

    Returns:
        news_results: A list of movie objects.
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        language = news_item.get('language')

        if id:
            news_object = Source(id,name,description,url,language)
            news_results.append(news_object)

    return news_results



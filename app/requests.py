import json
from .models import Source,Article
from newsapi import NewsApiClient


#Getting api key
newsapi = None

#Getting the news source base url
base_url = None

def configure_request(app):
    global base_url,newsapi
    base_url = app.config["NEWS_API_BASE_URL"]
    newsapi = NewsApiClient(api_key=app.config['API_KEY'])



def get_sources(category):
    sources = newsapi.get_sources(category)
    sources_list = sources

    # sources_results = None

    # if get_sources_response[]:
    #     source_results_list = get_sources_response[]
    #     sources_results = process_results(source_results_list)
    return sources_list


# def get_sources(category):
#     '''
#     Function that gets json response to url request.
#     '''
#     get_sources_url = base_url.format(category,newsapi)

#     with urllib.request.urlopen(get_sources_url) as url:
#         get_sources_data = url.read()
#         get_sources_response = json.loads(get_sources_data)

#         sources_results = None

#         if get_sources_response['results']:
#             source_results_list = get_sources_response['results']
#             sources_results = process_results(source_results_list)

#     return sources_results


# def get_news_article(title):
#     get_news_details_url = base_url.format(title,newsapi)

#     with urllib.request.urlopen(get_news_details_url) as url:
#         news_details_data = url.read()
#         news_details_response = json.loads(news_details_data)

#         news_article_object = None

#         if news_details_response:
#             author = news_details_response.get('author')
#             title = news_details_response.get('title')
#             description = news_details_response.get('description')
#             path = news_details_response.get('url')
#             poster = news_details_response.get('urlToImage')
#             publishedAt = news_details_response.get('publishedAt')

#             news_article_object = Article(author,title,description,path,poster,publishedAt)
            
#     return news_article_object


def process_results(source_list):
    '''
    Function that processes the news result and transform them to a list of objects.

    Args:
        news_list: A list of dictionaries that contain news details.

    Returns:
        news_results: A list of movie objects.
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        language = source_item.get('language')
        
        source_object = Source(id,name,description,url,language)
        source_results.append(source_object)

    return source_results



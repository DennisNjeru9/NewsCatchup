import requests as rq,json
from .models import Source,Article


#Getting api key
my_api_key = None

#Getting the news source base url
base_url = None

#Getting the article url
article_url = None

def configure_request(app):
    global base_url,my_api_key,article_url
    base_url = app.config["NEWS_API_BASE_URL"]
    my_api_key = app.config['API_KEY']
    article_url = app.config['ARTICLE_URL']


def get_sources():
    '''
    Function that requests for data of all news sources.
    '''
    with rq.get(base_url.format(my_api_key)) as data:
        data = data.json()
        source_list = data.get('sources')
        source_results = []
        for source in source_list:
            id = source.get('id')
            name = source.get('name')
            description = source.get('description')
            url = source.get('url')
            language = source.get('language')

            source_object = Source(id,name,description,url,language)
            source_results.append(source_object)
    return source_results



def get_articles(source):
    '''
    Function that gets a list of articles from a particular source

    Args: 
        source_id: The id of a specific result.
    Returns:
        article_results: list of news articles in the specific news source.
    '''

    with rq.get(article_url.format(source,my_api_key))as data:
        data = data.json()
        article_list =data.get('articles')
        articles_results = []
        for article in article_list:
            author = article.get('author')
            title = article.get('title')
            description = article.get('description')
            url = article.get('url')
            urlToImage = article.get('urlToImage')
            publishedAt = article.get('publishedAt')

    article_object = Article(author,title,description,url,urlToImage,publishedAt)
    articles_results.append(article_object)

    return articles_results

def search_article(q):
    search_article_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    with rq.get(search_article_url.format(q,my_api_key))as data:
        data = data.json()
        search_article_list =data.get('articles')
        search_articles_results = []
        for article in search_article_list:
            author = article.get('author')
            title = article.get('title')
            description = article.get('description')
            url = article.get('url')
            urlToImage = article.get('urlToImage')
            publishedAt = article.get('publishedAt')

    search_article_object = Article(author,title,description,url,urlToImage,publishedAt)
    search_articles_results.append(search_article_object)

    return search_articles_results


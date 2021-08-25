import requests as rq
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



# # def get_top_headlines():
# #     top_headlines = newsapi.get_top_headlines()


# # def process_results(source_list):
# #     source_results = []
# #     for source_item in source_list:
# #         id = source_item.get('id')
# #         name = source_item.get('name')
# #         description = source_item.get('description')
# #         url = source_item.get('url')
# #         language = source_item.get('language')

# #     source_object = Source(id,name,description,url,language)
# #     source_results.append(source_object)

# #     return source_results

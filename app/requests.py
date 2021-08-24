from .models import Source,Article



#Getting api key
api_key = None

#Getting the news source base url
base_url = None

def configure_request(app):
    global base_url,api_key
    base_url = app.config["NEWS_API_BASE_URL"]
    api_key = app.config['API_KEY']


# # def get_sources():
# #     sources = newsapi.get_sources()
# #     return sources



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

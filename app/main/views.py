from flask import render_template,request,redirect
from flask.helpers import url_for
from . import main
from newsapi import NewsApiClient

#Getting api key
my_api_key = None

#Getting the news source base url
#base_url = None

def configure_request(app):
    global my_api_key
    my_api_key = app.config['API_KEY']


#Views
@main.route('/',methods=['GET'])
def index():
    newsapi = NewsApiClient(api_key=my_api_key)
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")

    articles = topheadlines['articles']
    news = []
    desc = []
    img = []

    for i in range(len(articles)):
        my_articles = articles[i]

        news.append(my_articles['title'])
        desc.append(my_articles['description'])
        img.append(my_articles['urlToImage'])

    my_list = zip(news,desc,img)

    title = 'Home - Welcome to the best news catch-up online website'

    return render_template('index.html',title=title, context=my_list)


# @main.route('/news/',methods=['POST'])
# def get_results():
#     newsapi = NewsApiClient(api_key=my_api_key)
#     keyword = request.form['keyword']

#     news= newsapi.get_top_headlines(q=keyword,category="general",language="en")']
#     all_articles=['newsapi.get_everything(q=keyword,language="en",page=1)']
#     # print(news['articles'])
#     # print(all_articles['articles'])
    
#     search_article=request.args.get('keyword')

#     if search_article:
#         return redirect(url_for('search', article_name = search_article))
#     else:
#         return render_template('news.html',all_articles = all_articles('articles'))
from flask import render_template,request,redirect
from . import main
from newsapi import NewsApiClient



#Getting api key
my_api_key = None

#Getting the news source base url
#base_url = None

def configure_request(app):
    global my_api_key
    my_api_key = app.config['API_KEY']


newsapi = NewsApiClient(api_key=my_api_key)


#Views
@main.route('/',methods=['GET'])
def index():
    #sources = newsapi.get_sources()
    title = 'Home - Welcome to the best news catch-up online website'

    return render_template('index.html',title=title)


@main.route('/news/',methods=['POST'])
def get_results():
    keyword = request.form['keyword']

    news = newsapi.get_top_headlines(q=keyword,category='general',language='en')
    all_articles = newsapi.get_everything(q=keyword,language='en',page=1)
    #print(news['articles'])
    #print(all_articles['articles'])
    return render_template('news.html',news=news['articles'], all_articles = all_articles['articles'])
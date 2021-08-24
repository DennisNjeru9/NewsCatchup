from flask import render_template,request,redirect
from . import main
from ..requests import newsapi
from newsapi import NewsApiClient


my_api_key = main.config['NEWS_API_KEY']

newsapi = NewsApiClient(api_key=my_api_key)


#Views
@main.route('/')
def index():
    sources = newsapi.getsources()
    title = 'Home - Welcome to the best news catch-up online website'

    return render_template('index.html',title=title,source=sources['sources'])

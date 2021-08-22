from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_news_article

#Views
@main.route('/')
def index():
    general_news = get_news('general')
    business_news = get_news('business')
    health_news = get_news('health')
    science_news = get_news('science')
    sports_news = get_news('sports')
    technology_news = get_news('technology')
    title = 'Home - Welcome to the best news catch-up website'

    return render_template('index.html', title=title,general=general_news,business=business_news,health=health_news,science=science_news,sports=sports_news,technology=technology_news)
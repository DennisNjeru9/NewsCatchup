from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources

#Views
@main.route('/')
def index():
    general_news = get_sources('general')
    business_news = get_sources('business')
    health_news = get_sources('health')
    science_news = get_sources('science')
    sports_news = get_sources('sports')
    technology_news = get_sources('technology')
    title = 'Home - Welcome to the best news catch-up website'

    return render_template('index.html', title=title,general=general_news,business=business_news,health=health_news,science=science_news,sports=sports_news,technology=technology_news)
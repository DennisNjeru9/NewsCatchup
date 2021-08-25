from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_articles,get_sources


#Views
@main.route('/')
def index():
    sources = get_sources()
    title = 'Home - Welcome to the best news catch-up online website'

    return render_template('index.html',title=title, sources = sources)


@main.route('/news/<source_url>')
def source(source_url):
    pass



@main.route('/news/<source_name>', methods=['POST'])
def news(source_name):
    articles = get_articles(source_name)
    title = 'Here are the search results'
    return render_template('news.html',title=title, articles=articles)
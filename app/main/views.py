from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_articles,get_sources,search_article


#Views
@main.route('/')
def index():
    sources = get_sources()
    title = 'Home - Welcome to the best news catch-up online website'

    search_article = request.args.get('keyword')

    if search_article:
        return redirect(url_for('.search',article_name=search_article))
    else:
        return render_template('index.html',title=title, sources = sources)


@main.route('/search/<q>')
def search(q):
    article_keyword_list = q.split(" ")
    article_keyword_format = "+".join(article_keyword_list)
    searched_articles = search_article(article_keyword_format)
    title = f'search results for {q}'
    return render_template('search.html', title=title,article=searched_articles)

@main.route('/news/<source_id>')
def news(source_id):
    articles = get_articles(source_id)
    title = 'Here are the search results'
    return render_template('news.html',title=title, articles=articles)
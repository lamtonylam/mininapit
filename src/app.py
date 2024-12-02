from flask import render_template, request, redirect
from db_helper import reset_db
from repositories.citation_repository import (
    get_citations,
    create_article,
    create_inproceedings,
    delete_citation_by_id
)
from config import app, test_env

@app.get('/')
def index():
    citations = get_citations()

    return render_template('index.html', citations=citations)

@app.get('/new')
def new():
    return render_template('new.html')

@app.post('/article_new')
def article_new():

    info = {
        "key": request.form['key_article'],
        "author": request.form['author_article'],
        "title": request.form['title_article'],
        "journal": request.form['journal_article'],
        "year": request.form['year_article'],
        "volume": request.form.get('volume_article'),
        "pages": request.form.get('pages_article')
    }

    create_article(info)

    return redirect('/')

@app.post('/inproceedings_new')
def inproceedings_new():

    info = {
        "key": request.form['key_inproceedings'],
        "author": request.form['author_inproceedings'],
        "title": request.form['title_inproceedings'],
        "year": request.form['year_inproceedings'],
        "booktitle": request.form['booktitle_inproceedings']
    }

    create_inproceedings(info)

    return redirect('/')

@app.post('/delete')
def delete_citation():
    cid = request.form['id']
    ctype = request.form['type']
    delete_citation_by_id(cid, ctype)

    return redirect('/')

@app.get('/toggle-bibtex')
def toggle_bibtex():
    citations = get_citations()
    return render_template('index.html', citations=citations, is_bibtex=True)

if test_env:
    @app.get('/reset-db')
    def reset_database():
        reset_db()
        return 'db reset'

    @app.get('/alive')
    def alive():
        return 'yes'

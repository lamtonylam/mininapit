from flask import render_template, request, redirect
from db_helper import reset_db
from repositories.citation_repository import (
    get_citations,
    create_citation,
    delete_citation_by_key,
)
from config import app, test_env

@app.get('/')
def index():
    citations = get_citations()

    return render_template('index.html', citations=citations)

@app.get('/new')
def new():
    return render_template('new.html')

@app.post('/create_new')
def create_new():
    key = request.form['key']
    author = request.form['author']
    title = request.form['title']
    journal = request.form['journal']
    year = request.form['year']
    volume = request.form.get('volume')
    pages = request.form.get('pages')

    create_citation(key, author, title, journal, year, volume, pages)

    return redirect('/')

@app.post('/delete')
def delete_citation():
    key = request.form['key']
    delete_citation_by_key(key)

    return redirect('/')

@app.get('/toggle-bibtex')
def toggle_bibtex():
    citations = get_citations()
    return render_template('index.html', citations=citations, is_bibtex=True)

if test_env:
    @app.get('/reset_db')
    def reset_database():
        reset_db()
        return 'db reset'

    @app.get('/alive')
    def alive():
        return 'yes'

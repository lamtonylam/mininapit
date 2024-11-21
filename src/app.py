from flask import redirect, render_template, request, flash
from db_helper import reset_db
from repositories.citation_repository import get_citations, create_citation
from config import app, test_env
from util import validate_todo

@app.get('/')
def index():
    citations = get_citations()
    return render_template('index.html', citations=citations) 

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/create_new' , methods=['POST'])
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

if test_env:
    @app.route('/reset_db')
    def reset_database():
        reset_db()
        return 'db reset'
    
    @app.get('/alive')
    def alive():
        return 'yes'

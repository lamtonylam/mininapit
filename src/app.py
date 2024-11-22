from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.citation_repository import get_citations, create_todo, set_done, create_citation, generate_bibtex
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

    citations = get_citations()

    return render_template('index.html', citations=citations)

@app.route('/toggle-bibtex')
def toggle_bibtex():
    citations = get_citations()
    bibtex_citations = generate_bibtex(citations)
    return render_template('index.html', citations=bibtex_citations, is_bibtex=True)




# @app.route("/new_todo")
# def new():
#     return render_template("new_todo.html")

# @app.route("/create_todo", methods=["POST"])
# def todo_creation():
#     content = request.form.get("content")
# 
#     try:
#         validate_todo(content)
#         create_todo(content)
#         return redirect("/")
#     except Exception as error:
#         flash(str(error))
#         return  redirect("/new_todo")

# @app.route("/toggle_todo/<todo_id>", methods=["POST"])
# def toggle_todo(todo_id):
#     set_done(todo_id)
#     return redirect("/")

if test_env:
    @app.route('/reset_db')
    def reset_database():
        reset_db()
        return 'db reset'
    
    @app.get('/alive')
    def alive():
        return 'yes'

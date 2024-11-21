from config import db
from sqlalchemy import text

from entities.citation import Article

def get_citations():
    result = db.session.execute(text('SELECT * FROM articles'))
    articles = result.fetchall()

    return [Article(*article) for article in articles]

def create_citation(key, author, title, journal, year, volume, pages):
    sql = text('''INSERT INTO articles (key, author, title, journal, year, volume, pages)
             VALUES (:key, :author, :title, :journal, :year, :volume, :pages)''')

    db.session.execute(sql, {'key': key, 'author': author, 'title': title, 'journal': journal, 'year': year, 'volume': volume, 'pages': pages})
    db.session.commit()
    return

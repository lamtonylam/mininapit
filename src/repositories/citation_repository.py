from sqlalchemy import text
from config import db
from entities.citation import Article, Inproceedings

def get_citations():
    articles = db.session.execute(text('SELECT * FROM articles')).fetchall()
    inproceedings = db.session.execute(text('SELECT * FROM inproceedings')).fetchall()

    return [Article(*art) for art in articles] + [Inproceedings(*ip) for ip in inproceedings]

# let's fix this issue later
def create_citation(key, author, title, journal, year, volume, pages):  # pylint: disable=too-many-arguments, too-many-positional-arguments
    sql = text('''INSERT INTO articles (key, author, title, journal, year, volume, pages)
             VALUES (:key, :author, :title, :journal, :year, :volume, :pages)''')

    db.session.execute(sql, {
        'key': key, 'author': author, 'title': title, 'journal': journal,
        'year': year, 'volume': volume, 'pages': pages
    })
    db.session.commit()

def delete_citation_by_key(key):
    sql = text('DELETE FROM articles WHERE key = :key')
    db.session.execute(sql, {'key': key})
    db.session.commit()

from sqlalchemy import text
from config import db
from entities.citation import Article, Inproceedings, Book

def get_citations():
    articles = db.session.execute(text('SELECT * FROM articles')).fetchall()
    inproceedings = db.session.execute(text('SELECT * FROM inproceedings')).fetchall()
    books = db.session.execute(text('SELECT * FROM books')).fetchall()

    return (
        [Article(*art) for art in articles] +
        [Inproceedings(*ip) for ip in inproceedings] +
        [Book(*bk) for bk in books]
    )

def create_article(info:Article):
    sql = text('''INSERT INTO articles (key, author, title, journal, year, volume, pages)
             VALUES (:key, :author, :title, :journal, :year, :volume, :pages)''')

    db.session.execute(sql, {
        'key': info.key,
        'author': info.author,
        'title': info.title,
        'journal': info.journal,
        'year': info.year,
        'volume': info.volume,
        'pages': info.pages
    })
    db.session.commit()

def create_inproceedings(info:Inproceedings):
    sql = text('''INSERT INTO inproceedings (key, author, title, year, booktitle)
             VALUES (:key, :author, :title, :year, :booktitle)''')

    db.session.execute(sql, {
        'key': info.key,
        'author': info.author,
        'title': info.title,
        'year': info.year,
        'booktitle': info.booktitle
    })
    db.session.commit()

def delete_citation_by_id(cid, ctype):
    # no sql injections
    if not ctype in ('article', 'inproceedings', 'book'):
        return

    # change to plural if needed
    if ctype[-1] != 's':
        ctype += 's'

    sql = text(f'DELETE FROM {ctype} WHERE id = :id')
    db.session.execute(sql, {'id': cid})
    db.session.commit()

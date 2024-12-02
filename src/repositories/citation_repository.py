from sqlalchemy import text
from config import db
from entities.citation import Article, Inproceedings

def get_citations():
    articles = db.session.execute(text('SELECT * FROM articles')).fetchall()
    inproceedings = db.session.execute(text('SELECT * FROM inproceedings')).fetchall()

    return [Article(*art) for art in articles] + [Inproceedings(*ip) for ip in inproceedings]

def create_article(information): 
    sql = text('''INSERT INTO articles (key, author, title, journal, year, volume, pages)
             VALUES (:key, :author, :title, :journal, :year, :volume, :pages)''')

    db.session.execute(sql, {
        'key': information["key"], 'author': information["author"], 'title': information["title"], 'journal': information["journal"],
        'year': information["year"], 'volume': information["volume"], 'pages': information["pages"]
    })
    db.session.commit()

def create_inproceedings(information):  
    sql = text('''INSERT INTO inproceedings (key, author, title, year, booktitle)
             VALUES (:key, :author, :title, :year, :booktitle)''')

    db.session.execute(sql, {
        'key': information["key"], 'author': information["author"], 'title': information["title"],
        'year': information["year"], 'booktitle': information["booktitle"]
    })
    db.session.commit()

def delete_citation_by_id(cid, ctype):
    # no sql injections
    if not ctype in ('article', 'inproceedings'):
        return

    # change to plural if needed
    if ctype[-1] != 's':
        ctype += 's'

    sql = text(f'DELETE FROM {ctype} WHERE id = :id')
    db.session.execute(sql, {'id': cid})
    db.session.commit()

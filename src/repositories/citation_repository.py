from sqlalchemy import text
from config import db
from entities.citation import Article, Inproceedings

def get_citations():
    articles = db.session.execute(text('SELECT * FROM articles')).fetchall()
    inproceedings = db.session.execute(text('SELECT * FROM inproceedings')).fetchall()

    return [Article(*art) for art in articles] + [Inproceedings(*ip) for ip in inproceedings]

# let's fix this issue later
def create_article(key, author, title, journal, year, volume, pages):  # pylint: disable=too-many-arguments, too-many-positional-arguments
    sql = text('''INSERT INTO articles (key, author, title, journal, year, volume, pages)
             VALUES (:key, :author, :title, :journal, :year, :volume, :pages)''')

    db.session.execute(sql, {
        'key': key, 'author': author, 'title': title, 'journal': journal,
        'year': year, 'volume': volume, 'pages': pages
    })
    db.session.commit()

# let's fix this issue later
def create_inproceedings(key, author, title, year, booktitle):  # pylint: disable=too-many-arguments, too-many-positional-arguments
    sql = text('''INSERT INTO inproceedings (key, author, title, year, booktitle)
             VALUES (:key, :author, :title, :year, :booktitle)''')

    db.session.execute(sql, {
        'key': key, 'author': author, 'title': title,
        'year': year, 'booktitle': booktitle
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

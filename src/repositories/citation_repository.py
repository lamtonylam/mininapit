from sqlalchemy import text
from config import db
from entities.citation import Article

def get_citations():
    result = db.session.execute(text('SELECT * FROM articles'))
    articles = result.fetchall()

    return [Article(*article) for article in articles]

# let's fix this issue later
def create_article(key, author, title, journal, year, volume, pages):  # pylint: disable=too-many-arguments, too-many-positional-arguments
    sql = text('''INSERT INTO articles (key, author, title, journal, year, volume, pages)
             VALUES (:key, :author, :title, :journal, :year, :volume, :pages)''')

    db.session.execute(sql, {
        'key': key, 'author': author, 'title': title, 'journal': journal,
        'year': year, 'volume': volume, 'pages': pages
    })
    db.session.commit()

def create_inproceedings(key, author, title, year, booktitle):  # pylint: disable=too-many-arguments, too-many-positional-arguments
    sql = text('''INSERT INTO inproceedings (key, author, title, year, booktitle)
             VALUES (:key, :author, :title, :year, :booktitle)''')

    db.session.execute(sql, {
        'key': key, 'author': author, 'title': title,
        'year': year, 'booktitle': booktitle
    })
    db.session.commit()

def generate_bibtex(citations):
    bibtex_citations = []
    for c in citations:
        # let's fix this issue later
        if type(c) == Article:  # pylint: disable=unidiomatic-typecheck
            bibtex_c = f'@article{{{c.key},\n' \
                           f'    author = {{{c.author}}},\n' \
                           f'    title = {{{c.title}}},\n' \
                           f'    journal = {{{c.journal}}},\n' \
                           f'    year = {{{c.year}}},\n' \
                           f'    volume = {{{c.volume}}},\n' \
                           f'    pages = {{{c.pages}}}\n' \
                           f'}}'
            bibtex_citations.append(bibtex_c)
        # if type(c) == Inproceedings:
        #     print('Inproceedings it is!')
        # if type(c) == Book:
        #     print('Book it is!')
    return bibtex_citations

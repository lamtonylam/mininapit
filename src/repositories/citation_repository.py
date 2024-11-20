from config import db
from sqlalchemy import text

from entities.citation import Article

def get_citations():
    result = db.session.execute(text('select * from articles'))
    articles = result.fetchall()

    return [Article(*article) for article in articles]

def set_done(todo_id):
    return

    sql = text("UPDATE todos SET done = TRUE WHERE id = :id")
    db.session.execute(sql, { "id": todo_id })
    db.session.commit()

def create_todo(content):
    return

    sql = text("INSERT INTO todos (content) VALUES (:content)")
    db.session.execute(sql, { "content": content })
    db.session.commit()

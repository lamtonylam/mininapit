from sqlalchemy import text
from config import db, app

TABLE = 'articles'

def table_exists(name):
    sql_table_existence = text(
      'SELECT EXISTS ('
      '  SELECT 1'
      '  FROM information_schema.tables'
      f' WHERE table_name = \'{name}\''
      ')'
    )

    print(f'Checking if table {name} exists')
    print(sql_table_existence)

    result = db.session.execute(sql_table_existence)
    return result.fetchall()[0][0]

def reset_db():
    print(f'Clearing contents from table {TABLE}')
    sql = text(f'DELETE FROM {TABLE}')
    db.session.execute(sql)
    db.session.commit()

def setup_db():
    if table_exists(TABLE):
        print(f'Table {TABLE} exists, dropping')
        sql = text(f'DROP TABLE {TABLE}')
        db.session.execute(sql)
        db.session.commit()

    print(f'Creating table {TABLE}')
    sql = text(
      f'CREATE TABLE {TABLE} ('
      '  id SERIAL PRIMARY KEY,'
      '  key TEXT UNIQUE NOT NULL,'
      '  author TEXT NOT NULL,'
      '  title TEXT NOT NULL,'
      '  journal TEXT NOT NULL,'
      '  year INT NOT NULL,'
      '  volume TEXT,'
      '  pages TEXT'
      ')'
    )

    db.session.execute(sql)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        setup_db()

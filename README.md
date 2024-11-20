# OhTu-miniproject for managing LaTeX references

The idea of this project is to practice Scrum framework while trying to produce an app that automatically creates BibTeX files from the references in the database

## Running

* Alernative 1: Clone repository with HTTPS

  ```git clone https://github.com/Levottomat-Napit/mininapit.git```

* Alernative 2: Clone repository with SSH

  ```git clone git@github.com:Levottomat-Napit/mininapit.git```

* Install dependencies

  ```poetry install```

* Set up `.env`

```env
DATABASE_URL=postgresql:///databasename
TEST_ENV=boolean
SECRET_KEY=somethingsecret
```

* Set up database

  `python3 src/db_helper.py`

* Start poetry shell

  ```poetry shell```

* Run app

  ```python3 src/index.py```

## Backlog and sprint planning

PLEASE ADD READ-ONLY EXCEL LINK HERE

## Definition of done

A feature can be considered done when it has been planned, coded, tested and integrated. Tests should work automatically and existing features shall not break.

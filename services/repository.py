import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query, params=None):
    cursor = connection.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def create_submission_table():
    path = 'db/submission_db.sqlite3'

    connection = create_connection(path)

    create_table = """
        CREATE TABLE IF NOT EXISTS submissions (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          finish TEXT NOT NULL,
          year INTEGER NOT NULL,
          opponent TEXT NOT NULL,
          weight TEXT NOT NULL,
          competition TEXT NOT NULL
        );
        """

    execute_query(connection, create_table)


def create_submissions(cleaned_submissions):
    path = 'db/submission_db.sqlite3'

    connection = create_connection(path)

    create_submission = """
    INSERT INTO submissions (name, finish, year, opponent, weight, competition)
    VALUES (?, ?, ?, ?, ?, ?)
    """

    for submission in cleaned_submissions:
        execute_query(connection, create_submission, (
            submission['name'],
            submission['finish'],
            submission['year'],
            submission['opponent'],
            submission['weight'],
            submission['competition']
        ))

    connection.close()

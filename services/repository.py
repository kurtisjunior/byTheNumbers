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


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
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


def create_submission_item(submission):
    path = 'db/submission_db.sqlite3'

    connection = create_connection(path)

    # do something to the data to make it ready for inserting
    # iterate over the data and add 1 at a time?
    # add everything at once somehow?

    create_submission = """
    INSERT INTO
      submission_db (name,finish,year,opponent,weight,competition)
    VALUES
      ('name', 'finish', 'year', 'opponent', 'weight', 'competition'),
    """

    execute_query(connection, create_submission)


create_submission_item()

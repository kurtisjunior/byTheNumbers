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
    path = '../db/submission_db.sqlite3'

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


def create_submission_item():
    repo_test_data = [
        {

            'name': 'aaron tex johnson',
            'finish': 'DQ',
            'year': 2021,
            'opponent': 'O. Sanchez',
            'weight': 'Heavyweight',
            'competition': '2021 FloGrappling WNO Championship'
        },
        {
            'name': 'kurtis',
            'finish': 'DQ',
            'year': 2021,
            'opponent': 'O. Sanchez',
            'weight': 'Heavyweight',
            'competition': '2021 FloGrappling WNO Championship'
        }
    ]

    path = 'db/submission_db.sqlite3'

    connection = create_connection(path)

    create_submission = """
    INSERT INTO submission_db (name, finish, year, opponent, weight, competition)
    VALUES (?, ?, ?, ?, ?, ?)
    """

    for submission in repo_test_data:
        execute_query(connection, create_submission, (
            submission['name'],
            submission['finish'],
            submission['year'],
            submission['opponent'],
            submission['weight'],
            submission['competition']
        ))

    connection.close()


def create_single_item():
    single = {
        'name': 'aaron tex johnson',
        'finish': 'DQ',
        'year': 2021,
        'opponent': 'O. Sanchez',
        'weight': 'Heavyweight',
        'competition': '2021 FloGrappling WNO Championship'
    }
    path = '../db/submission_db.sqlite3'
    connection = create_connection(path)

    create_submission = """
    INSERT INTO submissions (name, finish, year, opponent, weight, competition)
    VALUES (?, ?, ?, ?, ?, ?)
    """

    execute_query(connection, create_submission, (
        single['name'],
        single['finish'],
        single['year'],
        single['opponent'],
        single['weight'],
        single['competition']
    ))

    connection.close()


create_submission_table()
create_single_item()

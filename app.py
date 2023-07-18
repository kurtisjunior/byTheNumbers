from flask import Flask
import sqlite3

from services.repository import get_athletes

app = Flask(__name__)


@app.route('/')
def athlete_controller():
    athletes = get_athletes()

    return 'Hello, this is a basic Flask endpoint!'


if __name__ == '__main__':
    app.run(debug=True)

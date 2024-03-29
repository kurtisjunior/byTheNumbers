from flask import Flask

from services.repository import get_athletes

app = Flask(__name__)


@app.route('/')
def athlete_controller():
    athletes = get_athletes()

    athlete_dicts = [
        {
            'name': athlete[1],
            'finish': athlete[2],
            'year': athlete[3],
            'opponent': athlete[4],
            'weight': athlete[5],
            'competition': athlete[6]
        }
        for athlete in athletes
    ]

    print('fired')
    return athlete_dicts


if __name__ == '__main__':
    app.run(debug=True)

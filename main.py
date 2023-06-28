from services.get_data import get_athletes_links, get_name, get_fight_data
from services.repository import save_athlete_data
from services.clean_data import clean_data


def extract():
    athletes_links = get_athletes_links()

    athlete_subs = {}

    for athlete_link in athletes_links:
        athlete_name = get_name(athlete_link)
        athlete_fight_data = get_fight_data(athlete_link)
        athlete_subs[athlete_name] = athlete_fight_data

    return athlete_subs


def transform(athlete_data):
    transformed_data = clean_data(athlete_data)

    return transformed_data


def load():
    save_athlete_data()

from extract import get_athletes_links, get_name, get_fight_data


def extract():
    athletes_links = get_athletes_links()

    athlete_data = {}

    for athlete_link in athletes_links:
        athlete_name = get_name(athlete_link)
        athlete_fight_data = get_fight_data(athlete_link)
        athlete_data[athlete_name] = athlete_fight_data

    return athlete_data


def transform():
    print("hello, world")

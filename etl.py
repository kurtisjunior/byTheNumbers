from services.clean_data import clean_data
from services.get_data import get_athletes_info, get_name, get_fight_data
from services.repository import create_submissions, create_submission_table


def extract():
    athlete_codes = get_athletes_info()
    athlete_subs = {}
    for athlete_code in athlete_codes:
        athlete_name = get_name(athlete_code)
        athlete_fight_data = get_fight_data(athlete_code)
        athlete_subs[athlete_name] = athlete_fight_data

    return athlete_subs


def transform(athlete_submissions):
    transformed_data = clean_data(athlete_submissions)

    return transformed_data


def load(cleaned_submissions):
    create_submission_table()
    create_submissions(cleaned_submissions)


def main():
    athlete_submissions = extract()
    cleaned_submissions = transform(athlete_submissions)
    load(cleaned_submissions)


main()

# run this script when it's deployed

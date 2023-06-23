import requests
from bs4 import BeautifulSoup
import re


def get_athletes_href_links():
    response = requests.get("https://www.flograppling.com/people")
    soup = BeautifulSoup(response.text, "html.parser")
    all_a_tags = soup.find_all('a')

    athlete_href_links = []

    for link in all_a_tags:
        href = link.get('href')
        if isinstance(href, str) and href.startswith('/people/'):
            athlete_href_links.append(href)

    return athlete_href_links


def get_match_data():
    response = requests.get("https://www.flograppling.com/people/5950131-adam-wardzinski")
    soup = BeautifulSoup(response.text, "html.parser")
    # all_a_tags = soup.find('flo-table')

    dates = soup.find_all('h5')
    dates_as_strings = [str(year.string) for year in dates]

    pattern = r"\b\d{4}\b"
    valid_years = [year for year in dates_as_strings if re.match(pattern, year)]

    print(valid_years)


get_match_data()

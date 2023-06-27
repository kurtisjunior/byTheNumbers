import requests
from bs4 import BeautifulSoup
import re


def get_athletes():
    response = requests.get("https://www.flograppling.com/people")
    soup = BeautifulSoup(response.text, "html.parser")
    all_a_tags = soup.find_all('a')

    athlete_href_links = []

    for link in all_a_tags:
        href = link.get('href')
        if isinstance(href, str) and href.startswith('/people/'):
            athlete_href_links.append(href)

    return athlete_href_links


def get_fight_data(athlete_link):
    response = requests.get("https://www.flograppling.com/people/" + athlete_link)
    soup = BeautifulSoup(response.text, "html.parser")

    dates = s¡oup.find_all('h5')
    dates_as_strings = [str(year.string) for year in dates]
    pattern = r"\b\d{4}\b"
    valid_years = [year for year in dates_as_strings if re.match(pattern, year)]

    tables = soup.findAll('tbody')
    sub_results = []
    year_index = 0
    for table in tables:
        rows = table.findAll('tr')
        for row in rows:
            row_elements = row.findAll('td')
            if len(row_elements) > 6:
                if row_elements[1].text == 'W':
                    sub_results.append(
                        row_elements[3].text + "-" + valid_years[year_index] + "-" + row_elements[5].text + "-"
                        + row_elements[6].text)
        year_index += 1

    return sub_results


def extract():
    athletes = get_athletes()
    for athlete in athletes:
        athlete_name = get_name(athlete)


def get_name(athlete_name):
    split_name = athlete_name.split('-')
    del split_name[0]
    return ' '.join(split_name)


get_name()

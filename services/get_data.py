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
            athlete_link = href.replace('/people/', "")
            athlete_href_links.append(athlete_link)

    return athlete_href_links


def get_fight_data(athlete_code):
    response = requests.get("https://www.flograppling.com/people/" + athlete_code)
    soup = BeautifulSoup(response.text, "html.parser")

    dates = soup.find_all('h5')
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
                    athlete_sub_result = {'finish': row_elements[3].text, 'year': valid_years[year_index],
                                          'opponent': row_elements[4].text, 'weight': row_elements[5].text,
                                          'competition': row_elements[6].text}
                    sub_results.append(athlete_sub_result)
        year_index += 1

    return sub_results


def get_name(athlete_name):
    split_name = athlete_name.split('-')
    del split_name[0]
    return ' '.join(split_name)

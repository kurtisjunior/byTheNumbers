import requests
from bs4 import BeautifulSoup


def get_athletes():
    response = requests.get("https://www.flograppling.com/people")
    soup = BeautifulSoup(response.text, "html.parser")
    elements = soup.find_all("h2")
    for element in elements:
        data = element.text
        print(data)


get_athletes()

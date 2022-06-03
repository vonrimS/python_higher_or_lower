import requests
from bs4 import BeautifulSoup


def get_data():
    url = 'https://www.tiobe.com/tiobe-index/'
    result =requests.get(url).text
    doc = BeautifulSoup(result, 'html.parser')

    table = doc.find('tbody').find_all('tr')

    data_dict = dict()

    for row in table:
        columns = row.find_all('td')
        if (columns != []):
            name = columns[4].text
            rating = columns[5].text.replace('%', '')
            data_dict[name] = float(rating)

    return data_dict
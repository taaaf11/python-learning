import requests
import csv
import re
from bs4 import BeautifulSoup
from collections import defaultdict

URL = "https://www.countryaah.com/alphabetical-list-of-cities-and-towns-in-indiana/"
CSV_FILE = "indiana_cities.csv"

try:
    response = requests.get(URL)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    city_elements = soup.select("li")

    cities_by_letter = defaultdict(list)
    pattern = re.compile(r"^(.*?),")

    for city in city_elements:
        city_name = city.text.strip()
        match = pattern.match(city_name)
        if match:
            city_name = match.group(1)
            first_letter = city_name[0].upper()
            cities_by_letter[first_letter].append(city_name)

    sorted_letters = sorted(cities_by_letter.keys())

    max_rows = max(len(cities_by_letter[letter]) for letter in sorted_letters)

    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(sorted_letters)

        for i in range(max_rows):
            row = [cities_by_letter[letter][i] if i < len(cities_by_letter[letter]) else "" for letter in sorted_letters]
            writer.writerow(row)

    print(f"Successfully saved city data in table format to {CSV_FILE}")

except requests.exceptions.RequestException as error:
    print(f"Error fetching data: {error}")

import requests
from bs4 import BeautifulSoup

URL = "https://www.landingfolio.com/"

save_file = "landingfolio.csv"

try:
    response = requests.get(URL)
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    headings = soup.find_all("h3", class_="mt-4 text-base font-bold text-gray-900")
    dates = soup.find_all("p", class_="mt-1.5 text-xs font-medium text-gray-500")

    with open(save_file, "w") as file:
        for headings, dates in zip(headings, dates):
            heading = headings.text.strip()
            date = dates.text.strip()
            file.write(f"{heading},{date}\n")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")


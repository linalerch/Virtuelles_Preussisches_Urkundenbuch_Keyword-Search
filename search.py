#made with AI

import requests
from bs4 import BeautifulSoup

base_url = "https://www.spaetmittelalter.uni-hamburg.de/Urkundenbuch/pub/"
years = list(range(1140, 1526))  # adjust to desired range
search_name = "KEYWORD".lower()  # change to your name / keyword

found = []

for y in years:
    url = f"{base_url}orden{y}.html"
    print(f"Checking {url} ...")
    resp = requests.get(url)

    # some years might not exist — skip if 404
    if resp.status_code != 200:
        continue

    # parse page text
    soup = BeautifulSoup(resp.text, "html.parser")
    text = soup.get_text().lower()

    if search_name in text:
        print(f"Found '{search_name}' in {y}!")
        found.append(y)

print("Done. Matches found in years:", found)

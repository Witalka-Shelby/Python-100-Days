import requests
from bs4 import BeautifulSoup

date_input = "2006-06-17"

url = f"https://www.billboard.com/charts/hot-100/{date_input}/"

# response = requests.get(url)
# website_html = response.text

with open("./day 46/billboard.html") as website:
    website_html = website.read()

soup = BeautifulSoup(website_html, "html.parser")
songs = soup.find_all(name="div", class_="o-chart-results-list-row-container")
# songs = soup.find(name="div", class_="o-chart-results-list-row-container")

for song in songs:
    singer_name = song.select_one(selector="ul li ul li span")
    print(singer_name.text.strip())

    song_name = song.select_one(selector="ul li ul li h3")
    print(song_name.text.strip())

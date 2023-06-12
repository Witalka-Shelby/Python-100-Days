from bs4 import BeautifulSoup
# import requests

with open("./day 45/100.html") as website_html:
    website = website_html.read()

soup = BeautifulSoup(website, "html.parser")

movies = soup.find_all("h3")

with open("./day 45/movies.txt", "w") as file:
    for movie in movies:
        file.write(movie.string)
        file.write("\n")


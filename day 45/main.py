from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
website = response.text

soup = BeautifulSoup(website, "html.parser")

# #\33 6292413 > td:nth-child(3) > span:nth-child(1) > a:nth-child(1)

title = soup.find(name="tr", class_="athing")

link = title.select_one(selector="td span a")

# print(title)

print(link.get("href"))



# with open("./day 45/website.html", encoding="utf8") as html_data:
#     website = html_data.read()

# soup = BeautifulSoup(website, "html.parser")

# # print(soup.title.string)

# # print(soup.find_all(name="a"))

# heading = soup.find(name="h1", id="name")
# # print(heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)
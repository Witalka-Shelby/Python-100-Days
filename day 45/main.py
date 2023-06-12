from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
website = response.text

soup = BeautifulSoup(website, "html.parser")

# #\33 6292413 > td:nth-child(3) > span:nth-child(1) > a:nth-child(1)

titles = soup.find_all(name="tr", class_="athing")

article_text = []
article_links = []
article_points = []


for title in titles:
    title_id = title.get("id")
    points = soup.find(id=f"score_{title_id}")
    link = title.select_one(selector="td span a")

    article_text.append(title.text)
    article_links.append(link.get("href"))
    article_points.append(int(points.text.split(" ")[0]))


highest_points = max(article_points)
index_highest_points = article_points.index(highest_points)

print(article_text[index_highest_points])
print(article_links[index_highest_points])

# with open("./day 45/website.html", encoding="utf8") as html_data:
#     website = html_data.read()

# soup = BeautifulSoup(website, "html.parser")

# # print(soup.title.string)

# # print(soup.find_all(name="a"))

# heading = soup.find(name="h1", id="name")
# # print(heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)
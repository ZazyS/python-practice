import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

titles = soup.find_all("span", class_="titleline")

for title in titles:
    print(title.a.text)
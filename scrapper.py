import requests
from bs4 import BeautifulSoup

file = open("quotes.txt", "w", encoding="utf-8")

for page_number in range (1, 11):
    url = f"https://quotes.toscrape.com/page/{page_number}/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")
    
    for quote, author in zip(quotes, authors):
        file.write(quote.text + "\n")
        file.write("- " + author.text + "\n\n")
        
    print(f"Page {page_number} done")
    
file.close()
print("All saved to quotes.txt")

import requests
from bs4 import BeautifulSoup
import csv

def enter_page():
    base_url = 'https://vc.ru/new'
    html = requests.get(base_url).text
    soup = BeautifulSoup(html, 'lxml')
    news = soup.find_all('div', class_="feed__item")

    urls = []
    with open("C:\\Users\\DiX PC Store\\Desktop\\text.csv", "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Title", "Content"])  # Записываем заголовки столбцов
        for article in news:
            url = article.find("a", class_="content-link")["href"]
            urls.append(url)
            writer.writerow([url])

    return urls

def book(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    news = soup.find_all('div', class_="l-entry")
    with open("C:\\Users\\DiX PC Store\\Desktop\\text.csv", "a", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for article in news:
            title = article.find("h1", class_="content-title").text.strip()
            content_divs = article.find_all("div", class_="l-entry__content")
            content = "\n".join(div.text.strip() for div in content_divs)
            writer.writerow([title, content])

urls = enter_page()
for url in urls:
    book(url)

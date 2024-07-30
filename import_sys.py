import requests
from bs4 import BeautifulSoup
import csv


class views_pages:
    
    base_url = 'https://www.chitai-gorod.ru/catalog/books/komiksy-110063'
    
    
    def number_str(base_url):
        html = requests.get(base_url).text
        soup = BeautifulSoup(html, 'html.parser')
        nums = soup.find_all('span', class_='pagination__text')
        last_nums_pages = None
        
        for nums_links in nums:
            last_nums_pages = nums_links
            nums_pages = last_nums_pages.get_text(strip=True)
            
        return nums_pages
        
    nums_pages = number_str(base_url)
    
    
    def parser_boock(nums_pages, base_url):

        for pages in range(1, int(nums_pages)+1):
            
            base_url_patterns = base_url + '?page=' + str(pages)
            print(base_url_patterns)
            
            html = requests.get(base_url_patterns).text
            soup = BeautifulSoup(html, 'html.parser')
            articls = soup.find_all('article', class_='product-card product-card product')
            
            
            for i, items in enumerate(articls):
                url = items.get("href")
                
                title = soup.find_all('div', class_='product-title__head')[i]
                title_book = title.get_text(strip=True)
                
                img = soup.find_all('img', class_='product-picture__img')[i]
                img_book = img.get('data-srcset')
                if img.get('data-srcset'):
                    img_str = img_book.split('?width=400&height=560&fit=bounds 2x')
                    img_str_link = img_str[0]
                else:
                    img_str = img.get('src')
                    img_str_link = img_str
                
                
                
                old_prices = items.find('div', class_='product-price__old')
                
                if old_prices:
                    old_prices_text = old_prices.get_text(strip=True)
                else:
                    old_prices_text = ''
                    
                sale_prices = items.find('div', class_='product-price__value')
                
                if sale_prices:
                    sale_prices_text = sale_prices.get_text(strip=True)
                else:
                    sale_prices_text = ''
                
                
                
                autor = items.find('div', class_='product-title__author')
                if autor:
                    autor_text = autor.get_text(strip=True)
                else:
                    autor_text = 'Автор не указан'
                
                print(title_book, old_prices_text, sale_prices_text, autor_text)
        
    parser_boock(nums_pages, base_url)
    

from bs4 import BeautifulSoup
from scrapy import Selector

def parse_with_beautifulsoup(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    data = {}
    data['name'] = soup.find('span', {'class': 'name'}).text if soup.find('span', {'class': 'name'}) else None
    data['address'] = soup.find('span', {'class': 'address'}).text if soup.find('span', {'class': 'address'}) else None
    data['deed'] = soup.find('span', {'class': 'deed'}).text if soup.find('span', {'class': 'deed'}) else None
    return data

def parse_with_scrapy(html_content):
    selector = Selector(text=html_content)
    data = {}
    data['email'] = selector.css('span.email::text').get()
    data['phone'] = selector.css('span.phone::text').get()
    return data

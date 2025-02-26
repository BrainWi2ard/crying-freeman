import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from scrapy import Selector
from ratelimit import limits, sleep_and_retry

# Rate limit settings
RATE_LIMIT = 5  # 5 requests
PER_SECOND = 1  # per 1 second

@sleep_and_retry
@limits(calls=RATE_LIMIT, period=PER_SECOND)
def fetch_html_with_requests(url, params=None):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Error fetching data from {url}: {response.status_code}")

@sleep_and_retry
@limits(calls=RATE_LIMIT, period=PER_SECOND)
def fetch_html_with_selenium(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get(url)
    html_content = driver.page_source
    driver.quit()
    return html_content

@sleep_and_retry
@limits(calls=RATE_LIMIT, period=PER_SECOND)
def fetch_html_with_scrapy(url):
    response = requests.get(url)
    if response.status_code == 200):
        selector = Selector(text=response.text)
        return selector
    else:
        raise Exception(f"Error fetching data from {url}: {response.status_code}")

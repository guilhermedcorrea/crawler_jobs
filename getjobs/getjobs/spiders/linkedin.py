import scrapy
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import requests
from random import randint
from dotenv import load_dotenv
import os

secret_key = os.getenv('API_KEY')

SCRAPEOPS_API_KEY = secret_key


def get_headers_list():
  response = requests.get('http://headers.scrapeops.io/v1/browser-headers?api_key=' + SCRAPEOPS_API_KEY)
  json_response = response.json()
  return json_response.get('result', [])

def get_random_header(header_list):
  random_index = randint(0, len(header_list) - 1)
  return header_list[random_index]


class LinkedinSpider(scrapy.Spider):
    name = "linkedin"
    allowed_domains = ["linkedin.com"]
    start_urls = ["https://linkedin.com"]
    
    
    allowed_domains = ["https://linkedin.com"]
    custom_settings = {
        'SCRAPEOPS_API_KEY': f'{secret_key}',
        'SCRAPEOPS_FAKE_HEADERS_ENABLED': True,
        'DOWNLOADER_MIDDLEWARES': {
            'getjobs.middlewares.ScrapeOpsFakeBrowserHeadersMiddleware': 400,
        }
    }
    
    def __init__(self):
        self.option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), 
                            options=self.option)
        
    def start_requests(self):
        header_list = get_headers_list()
        url = "https://linkedin.com"
        yield scrapy.Request(url=url, callback=self.parse,headers=get_random_header(header_list))
    

    def parse(self, response):
        self.driver.get('https://linkedin.com')

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
import urllib.parse

secret_key = os.getenv('API_KEY')

SCRAPEOPS_API_KEY = secret_key


def get_scrapeops_url(url):
    payload = {'api_key': secret_key, 'url': url, 'bypass': 'cloudflare'}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urllib.parse.urlencode(payload)
    return proxy_url

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
    handle_httpstatus_list = [404]
    def __init__(self):
        self.option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), 
                            options=self.option)
        
    def start_requests(self):
        self.driver.implicitly_wait(3)
        header_list = get_headers_list()
        url = "https://www.linkedin.com/?trk=seo-authwall-base_nav-header-logo"
        yield scrapy.Request(url=get_scrapeops_url(url), callback=self.parse)

    def scroll_page(self) -> None:
        lenOfPage = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while(match==False):
            lastCount = lenOfPage
            time.sleep(1)
            lenOfPage = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True
                

    def parse(self, response):
        self.driver.implicitly_wait(3)
        
        self.driver.get('https://www.linkedin.com/?trk=seo-authwall-base_nav-header-logo')
        
        time.sleep(100)
        pass


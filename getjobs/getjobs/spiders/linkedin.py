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
        url = "https://www.linkedin.com/"
        yield scrapy.Request(url=url, callback=self.parse,headers=get_random_header(header_list))
        
         
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

    def login(self):
        self.driver.implicitly_wait(3)
        user = self.driver.find_element(By.XPATH,'/html/body/div/main/div/form/section/div[2]/div[1]/input')
        user.clear()
        user.send_keys('TESTE')
        
        password = self.driver.find_element(By.XPATH,'/html/body/div/main/div/form/section/div[2]/div[2]/input')
        password.clear()
        password.send_keys('senhaaa')

    def parse(self):
       
        self.driver.get('https://www.linkedin.com/?trk=seo-authwall-base_nav-header-logo')
        
        self.driver.implicitly_wait(3)
        
        self.login()
        

        
  
    def get_jobs(self):
        ...
       

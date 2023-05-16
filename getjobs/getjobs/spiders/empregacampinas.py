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
from typing import Any


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


class EmpregacampinasSpider(scrapy.Spider):
    
    name = "empregacampinas"
    allowed_domains = ["empregacampinas.com.br"]
    custom_settings = {
        'SCRAPEOPS_API_KEY': f'{secret_key}',
        'SCRAPEOPS_FAKE_HEADERS_ENABLED': True,
        'DOWNLOADER_MIDDLEWARES': {
            'getjobs.middlewares.ScrapeOpsFakeBrowserHeadersMiddleware': 400,
        }
    }
    
    def __init__(self) -> None:
        self.option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), 
                            options=self.option)
        
    def start_requests(self) -> Any:
        header_list = get_headers_list()
        url = "https://empregacampinas.com.br"
        yield scrapy.Request(url=get_scrapeops_url(url), callback=self.parse,headers=get_random_header(header_list))
        
         
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

    def parse(self) -> None:
       
        self.driver.get('https://empregacampinas.com.br')
        
        self.driver.implicitly_wait(3)
        
        search = self.driver.find_element(
            By.XPATH,'/html/body/header/div/div[2]/form/div/div/input')
        search.clear()
        search.send_keys('Python')
        time.sleep(1)
        
        click = self.driver.find_element(
            By.XPATH,'/html/body/header/div/div[2]/form/input').click()
        
        
    def get_page_items(self) -> None:
        self.scroll_page()
        
        job_urls = self.driver.find_elements(By.XPATH,'//*[@id="article"]/div/div[2]/div[2]/div/a')
        for jobs in job_urls:
            print(jobs.get_attribute("href"))
        
        

        

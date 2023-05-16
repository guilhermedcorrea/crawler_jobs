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
import random


def randoms(ranges):
    ranges = random.randint(3, ranges)
    return ranges


secret_key = os.getenv('secret_key')

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


class GupySpider(scrapy.Spider):
    name = "gupy"
    allowed_domains = ["gupy.io"]
    start_urls = ["https://login.gupy.io"]
    
    def __init__(self):
        self.option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), 
                            options=self.option)
    
    def start_requests(self) ->Any:
        time.sleep(randoms(10))
        self.driver.implicitly_wait(3)
        header_list = get_headers_list()
        url = "https://login.gupy.io/candidates/signin"
        yield scrapy.Request(url=get_scrapeops_url(url), callback=self.parse,headers=get_random_header(header_list))

    def parse(self, response):
        time.sleep(randoms(10))
        self.driver.implicitly_wait(3)
        
        self.driver.get("https://login.gupy.io/candidates/signin")
        
        
        try:
            click = self.driver.find_element(
                By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div[3]/button[1]/span[1]/div/span[1]').click()
            time.sleep(1)
        except Exception as e:
            print(e)
            
        try:
            username = self.driver.find_element(
                By.ID,'username')
            username.click()
            username.clear()
            username.send_keys('')
            
        except Exception as e:
            print(e)

        try:
            password = self.driver.find_element(
                By.ID,'password-input')
            password.click()
            password.clear()
            password.send_keys('')
            
        except Exception as e:
            print(e)
        
        
     


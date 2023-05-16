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

user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
]



secret_key = 'keywords'

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


options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--start-maximized")
options.add_argument('--disable-infobars')
driver = webdriver.Chrome(options=options, executable_path=r"C:\crawler_jobs\chromedriver.exe")


class GupySpider(scrapy.Spider):
    name = "gupy"
    allowed_domains = ["gupy.io"]
    start_urls = ["https://login.gupy.io"]
    
    
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=get_scrapeops_url(url), callback=self.parse,
                        headers={"User-Agent": user_agent_list[random.randint(0, len(user_agent_list)-1)]})
    
   
    def parse(self, response):
        time.sleep(randoms(10))
       
        
        driver.get("https://login.gupy.io/candidates/signin")
        driver.implicitly_wait(10)
        
        try:
            click = driver.find_element(
                By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div[3]/button[1]/span[1]/div/span[1]').click()
            time.sleep(1)
        except Exception as e:
            print(e)
            
        try:
            username = driver.find_element(
                By.ID,'username')
            username.click()
            username.clear()
            username.send_keys('user@user')
            
        except Exception as e:
            print(e)
            
        time.sleep(2)
        try:
            password = driver.find_element(
                By.ID,'password-input')
            password.click()
            password.clear()
            password.send_keys('123')
            
        except Exception as e:
            print(e)
            
        try:
            poup_up = driver.find_element(By.CSS_SELECTOR,'#onetrust-accept-btn-handler').click()
        except Exception as e:
            print(e)
        time.sleep(1)
        
        try:
            button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
                By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/form/button/span[1]")))
            button.click()
        except Exception as e:
            print(e)
    
    def new_jobs(self):
        driver.implicitly_wait(10)
        #search_new_applications > span.jss1434 > div
        try:
            poup_up = driver.find_element(By.CSS_SELECTOR,'#pushConfirmation').click()
        except:
            pass
        
        try:
            new_jb = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
                        By.CSS_SELECTOR, "search_new_applications > span.jss1434 > div")))
            new_jb.click()
        except Exception as e:
            print(e)
        
        try:
            element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, "search_new_applications")))
            time.sleep(5)
            print(element.is_displayed())
        except Exception as e:
            print(e)
            
    def search_job(self):
        driver.implicitly_wait(19)
        
        
        try:
            element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, "__next")))
            time.sleep(5)
            print(element.is_displayed())
        except Exception as e:
            print(e)

        

        
            
    
   
            
            
        
        
        
     


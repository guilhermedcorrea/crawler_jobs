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


class EmprecacampinasSpider(scrapy.Spider):
    
    name = "empregacampinas"
    allowed_domains = ["empregacampinas.com.br"]

    def start_requests(self):
        url = "https://empregacampinas.com.br"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(ChromeDriverManager().install(), 
                            options=option)
        
        driver.get('https://empregacampinas.com.br')
        




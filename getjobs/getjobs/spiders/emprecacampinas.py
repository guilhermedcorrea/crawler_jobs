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
    name = "emprecacampinas"
    allowed_domains = ["empregacampinas.com.br"]
    start_urls = ["https://empregacampinas.com.br"]

    def parse(self, response):
        pass

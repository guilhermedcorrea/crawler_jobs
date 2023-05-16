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


option = webdriver.ChromeOptions()
#option.add_argument('--headless') ## --> comment out to see the browser launch.
#option.add_argument('--no-sandbox')


driver = webdriver.Chrome(ChromeDriverManager().install(), 
                            options=option)                            


def scroll_page() -> None:
    lenOfPage = driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(1)
        lenOfPage = driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True

def get_url():
    driver.implicitly_wait(7)
    driver.get("https://empregacampinas.com.br/")
    
    def search_job():
        driver.implicitly_wait(3)
        
        search = driver.find_element(
            By.XPATH,'/html/body/header/div/div[2]/form/div/div/input')
        search.clear()
        search.send_keys('Python')
        time.sleep(1)
        
        driver.find_element(
            By.XPATH,'/html/body/header/div/div[2]/form/input').click()
        
    
    def get_page_items():
        scroll_page()
        
        job_urls = driver.find_elements(By.XPATH,'//*[@id="article"]/div/div[2]/div[2]/div/a')
        for jobs in job_urls:
            print(jobs.get_attribute("href"))
        
        
        
    search_job()
    get_page_items()
        
get_url()

    


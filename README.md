# Automatize a busca por vagas e envio de curriculos

#Gupy, Linkedin, emprega Campinas, Instagram

#Iniciando projeto

#py -3 -m venv venv
#venv/Scripts/activate
#pip install -r requirements.txt


# cd getjobs
#scrapy startproject getjobs
#scrapy genspider emprecacampinas empregacampinas.com.br
#scrapy crawl linkedin



```Python
def get_scrapeops_url(url) -> str:
    payload = {'api_key': secret_key, 'url': url, 'bypass': 'cloudflare'}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urllib.parse.urlencode(payload)
    return proxy_url

def get_headers_list() -> Any:
  response = requests.get('http://headers.scrapeops.io/v1/browser-headers?api_key=' + SCRAPEOPS_API_KEY)
  json_response = response.json()
  return json_response.get('result', [])

def get_random_header(header_list) -> Any:
  random_index = randint(0, len(header_list) - 1)
  return header_list[random_index]

class LinkedinSpider(scrapy.Spider):
    name = "linkedin"
    allowed_domains = ["linkedin.com"]
    start_urls = ["https://linkedin.com"]
    handle_httpstatus_list = [404]
    def __init__(self) -> None:
        self.option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), 
                            options=self.option)
        
    def start_requests(self) ->Any:
        time.sleep(randoms(10))
        self.driver.implicitly_wait(3)
        header_list = get_headers_list()
        url = "https://www.linkedin.com/?trk=seo-authwall-base_nav-header-logo"
        yield scrapy.Request(url=get_scrapeops_url(url), callback=self.parse,headers=get_random_header(header_list))
```


# Automatize a busca por vagas e envio de curriculos

# Gupy, Linkedin, emprega Campinas, Instagram

# Iniciando projeto

#py -3 -m venv venv
#venv/Scripts/activate
#pip install -r requirements.txt
#cd getjobs
#scrapy startproject getjobs

# Criando e iniciando um novo Spyder
#<b>scrapy genspider emprecacampinas empregacampinas.com.br</b>
#<b>scrapy crawl gupy</b>





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
<b>Criando Headers de modo dinamico com API scrapeops</b>
<b>Proxy scrapeops</b>



```Python
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
```

<b>Criando Headers de modo dinamico com API scrapeops</b>
<b>Ajuste chromeptions</b>


<b>Demais ajustes devem ser feitos no settings.py</b>
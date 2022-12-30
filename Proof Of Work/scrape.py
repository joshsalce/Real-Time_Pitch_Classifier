# Credit: https://www.zenrows.com/blog/scraping-javascript-rendered-web-pages#how-to-scrape-javascript-generated-content

import time 
#import pandas as pd 
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager

# define the options, set to headless mode
options = webdriver.ChromeOptions() 
options.headless = True 

# normally, selenium waits for all resources to download 
# we don't need it as the page also populated with the running javascript code. 
options.page_load_strategy = 'none' 

# returns the path web driver downloaded 
chrome_path = ChromeDriverManager().install() 
chrome_service = Service(chrome_path) 

# pass the defined options and service objects to initialize the web driver 
driver = Chrome(options=options, service=chrome_service) 

driver.maximize_window() # For maximizing window
driver.implicitly_wait(10)


url = "file:///Users/josh/Desktop/Proof%20Of%20Work/RNG.html"
driver.get(url) 

# wait a certain amount of time, by then JavaScript code will be running
time.sleep(3)

content = driver.find_element(By.CSS_SELECTOR, "div[class*='Main'")
metrics_text = content.find_elements(By.TAG_NAME, "tr")[1].text.split(" ")

metrics = [float(i) for i in metrics_text]

print(metrics) 
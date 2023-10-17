from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service # import Service class
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from webdriver_manager.chrome import ChromeDriverManager

import sys
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

service = Service(executable_path=ChromeDriverManager().install()) # create a Service object with executable_path
driver = webdriver.Chrome(options=options, service=service) # 
search_url = str(sys.argv[1])
print(search_url)

driver.get(search_url)

actions = ActionChains(driver)

old_scroll_height = 0 
while(True):    
    body = driver.find_element(By.ID, "content")
    scroll_height = body.get_attribute("scrollHeight")
    actions.key_down(Keys.CONTROL).send_keys(Keys.END).perform()
    time.sleep(3)
    print(scroll_height)
    if int(scroll_height) == int(old_scroll_height):
        break
    old_scroll_height = scroll_height

videos = driver.find_elements(By.ID, "channel-thumbnail")

channel_names = []
channel_dictionary = "var channelDict =  {"

for i in range(len(videos)):
	channel_names.append(videos[i].text)
	channel_dictionary += "\""+ videos[i].text +"\":\""+ videos[i].get_attribute("href") +"\""\
	if i == 1 else ", \""+ videos[i].text +"\":\""+ videos[i].get_attribute("href") +"\""
    
channel_dictionary += "};"

print (channel_dictionary)

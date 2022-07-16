import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import json 
from constants import CHROMEDRIVER_PATH, DISCORD_EMAIL, PASSWORD

"""This is us trying to get all the message IDs / currently open in YOUR discord dms. Nothing is sent anywhere else. This file just makes a browser, logs into discord w/ whatever you type in constants, gets the IDs, puts it in data.txt (in this directory) and exits.
"""

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")


# Open up chrome.
driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=chrome_options)
driver.delete_all_cookies()

# Go to facebook, type in details
driver.get('https://discord.com/login')

#Start users and pass

driver.find_element(By.XPATH, '//*[@name="email"]').send_keys(DISCORD_EMAIL)

inputa = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@name="password"]'))
)
inputa.click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//*[@name="password"]').send_keys(PASSWORD)

inputa = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@type="submit"]'))
)
inputa.click()
time.sleep(3)

driver.get("https://discord.com/channels/@me")

## In DMS.
time.sleep(6)
# myElem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Direct Messages"]')))

dm_class = driver.find_element(By.XPATH, '//*[@aria-label="Direct Messages"]')
options = dm_class.find_elements(By.TAG_NAME, "li")
# print(options)
data = [] 
count = 0 
# It doesn't re-get the options, which I think is the problem.
new_aria = 2
old_aria = 0


while True: 
	new_aria += 1
	try:
		dm = driver.find_element(By.XPATH, f'//*[@aria-posinset="{new_aria}"]'.format(new_aria = new_aria))
		print("DM User: " +dm.text)
	except NoSuchElementException:
		print("Reached the end of your dms!")
		break

	# find li element
	# get id
	# move down
	link_to_channel = dm.find_element(By.TAG_NAME, "a") # Find first <a href> thingy.
	link = link_to_channel.get_attribute("href")
	message_id = link.split('/')[-1] # Gets message id from link.
	
	# Move one message down
	hover = ActionChains(driver).move_to_element(dm)
	hover.perform()
	print(message_id)
	data.append(message_id)

	# old_aria = new_aria # aria pos of this li

# while True:
#     for option in options:
#         print(count)
#         count +=1
#         # # Debugging, see what it's printing and where it is.


#         link_to_channel = option.find_element(By.TAG_NAME, "a") # Find first <a href> thingy.
#         link = link_to_channel.get_attribute("href")
#         message_id = link.split('/')[-1] # Gets message id from link.
        
#         # Move one message down
#         hover = ActionChains(driver).move_to_element(option)
#         hover.perform()

#         print(message_id)
#         data.append(message_id)
#         # print(option.text, option.get_attribute("aria-posinset"))


# Dump the data into data.txt
with open('data.txt', 'w') as f:
  json.dump(data, f, ensure_ascii=False)

driver.close() # Closes the browser



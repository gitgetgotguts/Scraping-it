
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

# Specify the path to the geckodriver executable
service = Service(executable_path='/bin/geckodriver')
driver = webdriver.Firefox(service=service)

# Open a webpage
driver.get("http://quotes.toscrape.com/")
# Close the browser after a few seconds
#import time
#time.sleep(1)
#quotes=driver.find_elements(By.CLASS_NAME,'quote')
#quotess = driver.find_elements_by_classname('quote')
fruit = driver.find_elements(By.CLASS_NAME,"quote")
for element in fruit:
    # Perform actions on each element
    print(element.text)
print(fruit)
driver.close()
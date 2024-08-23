#first attempt  clicking button then looping the elements
import undetected_chromedriver as uc
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

L=[]


# Specify the path to the geckodriver executable
service = Service(executable_path='/bin/geckodriver')
driver = webdriver.Firefox(service=service)
# Open a webpage
driver.get("http://quotes.toscrape.com/")
tquotes=[x.text for x  in driver.find_elements(By.CLASS_NAME,"quote")]
L.append(tquotes)

while 1:
    try:
        btn=driver.find_element(By.CLASS_NAME,'next').find_element(By.TAG_NAME,'a')
        btn.click()
        tquotes=[x.text for x  in driver.find_elements(By.CLASS_NAME,"quote")]
        L.append(tquotes)
        
    except:
        print(L)
        driver.quit()



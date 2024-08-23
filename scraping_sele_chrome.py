#first attempt  clicking button then looping the elements
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = uc.Chrome()
# Open a webpage
driver.get("http://quotes.toscrape.com/")
L=[]

tquotes=[x.text for x  in driver.find_elements(By.CLASS_NAME,"quote")]
L.append(tquotes)
oc=0
while 1:
    try:
        btn=driver.find_element(By.CLASS_NAME,'next').find_element(By.TAG_NAME,'a')
        btn.click()
        tquotes=[x.text for x  in driver.find_elements(By.CLASS_NAME,"quote")]
        L.append(tquotes)
        oc+=2
    except:
        print(L)
        driver.close()

# btn.click()
# tmp=[x.text for x  in driver.find_elements(By.CLASS_NAME,"quote")]

# print(tmp)

# driver.close()

from selenium.webdriver.common.by import By
from selenium import webdriver

#I can now use the selenium manager beta :
driver = webdriver.Firefox()
driver.get("http://quotes.toscrape.com/")
L=[]
while 1:
    try:
        
        tquotes=[x.text for x  in driver.find_elements(By.CLASS_NAME,"quote")]
        L.append(tquotes)
        btn=driver.find_element(By.CLASS_NAME,'next').find_element(By.TAG_NAME,'a')
        btn.click()
        
    except:
        print(L)
        driver.quit()
        break


from selenium.webdriver.common.by import By
from selenium import webdriver

#I can now use the selenium manager beta :
driver = webdriver.Firefox()
driver.get("http://quotes.toscrape.com/")
L=[]
if __name__=='__main__':
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
# cleaning data: to a Json format  {"quotes":[ {"text":"","author":"","tag":[,]}, {"text":"","author":"","tag":[,]}] }
    quotes=[]
    for i in L:
        for j in i:
            tempL=j.split("\n")
            if len(tempL)!=3:
                tempL.append("Tags: None")
        # print(tempL)
        # print({'quote':tempL[0],'author':' '.join(tempL[1].split()[1:-1]),'tags':tuple(tempL[2].split()[1:])})
        
            quotes.append({"text":tempL[0],"author":" ".join(tempL[1].split()[1:-1]),"tags":tuple(tempL[2].split()[1:])})

#save output in JSON:
import json
with open('data.json', 'w') as js:
    json.dump({'quotes':quotes},js,indent=3)



# #save the output in output.txt file:
# import sys
 
# # Save the original stdout
# original_stdout = sys.stdout
 
# # Redirect stdout to a file
# with open('output.txt', 'w') as f:
#     sys.stdout = f
#     print(quotes)
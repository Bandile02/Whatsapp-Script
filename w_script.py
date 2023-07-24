from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options();
options.add_argument(r'user-data-dir=C:\Users\YourBusinessName\AppData\Local\Google\Chrome\User Data\whatsapp')
#driver = webdriver.Chrome(r"C:\Users\Bandile\.wdm\drivers\chromedriver\win32\89.0.4389.23\chromedriver.exe",options=options)
driver = webdriver.Chrome(ChromeDriverManager().install())#,options=options)
driver.get("http://web.whatsapp.com/")
#time.sleep(10)
new_line=ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER)

while True:
    try:
        msg=driver.find_elements_by_xpath('*//div[@class="_1pJ9J"]')
        msg[-1].click()
        chat=driver.find_elements_by_xpath('*//div[@class="_1Gy50"]')
        msg_box=driver.find_element_by_xpath('//div[@class="p3_M1"]')
    except:
        pass   
    try:
        if "Shop" in chat[-1].text:
            msg_box.send_keys("/o",Keys.ENTER,Keys.ENTER)
            chat=driver.find_elements_by_xpath('*//div[@class="_1Gy50"]')
    except:
        pass
    try:
        chat=driver.find_elements_by_xpath('*//div[@class="_1Gy50"]')
    except:
        pass
    try:
        if "2" in chat[-1].text:
            if "Select" in chat[-2].text:
                msg_box.send_keys("/i",Keys.ENTER,Keys.ENTER)
                chat=driver.find_elements_by_xpath('*//div[@class="_1Gy50"]')
    except: 
        pass
    try:
        if "Do" in chat[-1].text:
            for x in range (0,len(chat),1):
                if "Write" in chat[x].text:
                    st=x
    except: 
        pass
    try:
        if "Done" in chat[-1].text:
            msg_box.send_keys("/h",Keys.ENTER,Keys.ENTER)
            for d in range(st,len(chat),1):
                for a in range(0,len(df),1):
                    if chat[d].text in df['Items'][a]:
                        msg_box.send_keys(df['Items'][a]+"  R"+str(df['Price'][a]))
                        new_line.perform() 
            msg_box.send_keys(Keys.ENTER,Keys.ENTER) 
            chat=driver.find_elements_by_xpath('*//div[@class="_1Gy50"]')  
    except: 
        pass                    
                        
    try:
        if "1" in chat[-1].text:
            if "Thank" in chat[-2].text:
                msg_box.send_keys("/o",Keys.ENTER,Keys.ENTER)
                chat=driver.find_elements_by_xpath('*//div[@class="_1Gy50"]')
    except:
        pass
    try:        
        if "Done" in chat[-3].text:
            msg_box.send_keys("/m",Keys.ENTER,Keys.ENTER)
            chat=driver.find_elements_by_xpath('*//div[@class="_1Gy50"]')   
    except: 
        pass

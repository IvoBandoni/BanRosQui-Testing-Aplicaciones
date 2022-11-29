from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

def login_succesful():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://magento.softwaretestingboard.com/")
    

    elementSign = driver.find_element(By.XPATH,"/html/body/div[2]/header/div[1]/div/ul/li[2]/a")
    elementSign.click()
    time.sleep(3)

    email      = driver.find_element(By.ID,'email')
    contraseña = driver.find_element(By.ID,'pass')
    boton      = driver.find_element(By.ID,'send2')

    email.send_keys('roni_cost@example.com')
    time.sleep(3)

    contraseña.send_keys('roni_cost3@example.com')
    time.sleep(3)

    boton.send_keys(Keys.ENTER)
    time.sleep(10)
    
    driver.close()

def __main__():
    login_succesful()

if __name__=='__main__':
    __main__()
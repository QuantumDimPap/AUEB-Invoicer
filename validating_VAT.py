import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time



#connects to firefox and based on the inputs finds the wanted elements
def giveAFM(afm,url,country):
    #options = webdriver.FirefoxProfile()
    options = Options()

    #if True then the browser does not open
    options.headless = True

    #here we define the driver that we will use in order to scrap the page
    driver = webdriver.Firefox(executable_path ="path_to_AUEB_Invoicer\\browser_drivers\\geckodriver.exe", options = options)

    #find elements by XPATH
    driver.get(url)
    driver.find_element(By.XPATH,country).click()
    #with the help of the xpath, we can locate very easy each element in a webpage.
    driver.find_element(By.XPATH,"//input[@id='number']").send_keys(afm)
    driver.find_element(By.XPATH,"//input[@id='submit']").click()
    time.sleep(5)

    try:
        element = driver.find_element(By.XPATH,"//span[@class='validStyle']")
    except Exception as e:
        element = driver.find_element(By.XPATH,"//tbody//tr[1]//td[1]")

    #from the element we located we get the text
    result = element.text
    result = result[0:3]
    driver.quit()
    return result







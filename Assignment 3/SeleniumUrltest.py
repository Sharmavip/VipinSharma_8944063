# Importing required libraries

# pip install selenium

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://it.conestogac.on.ca/")
time.sleep(5)

driver.maximize_window()
driver.execute_script("window.scrollTo(0, 500)")

#tab_link = driver.find_element(By.XPATH, "//div[@id='quick-actions']/div/div/a/span")
tab_link = driver.find_element(By.XPATH, "//span[normalize-space()='Connect to VPN']")

time.sleep(5)
tab_link.click()
time.sleep(5)


driver.find_element(By.XPATH, "//a[@aria-label='Search']//*[name()='svg']").click()
time.sleep(5)
search_site = driver.find_element(By.XPATH, "//div[@id='cludo-search-form']/div/input")

search_site.send_keys("Ivanti")


search_site.send_keys(Keys.RETURN)
time.sleep(5)
Expected: None = print(driver.find_element(By.XPATH, "/html/body").text)
Actual = "Your search for 'Ivanti' returned 2 results"


driver.find_element(By.XPATH, "//div[@id='cludo-search-results']/div/div[2]/div").click()

driver.find_element(By.XPATH, "//div[@id='navbarNav']/div/div/a").click()

driver.find_element(By.XPATH, "//div[@id='apps-tools']/div[2]/a/span/span[2]").click()

driver.find_element(By.XPATH, "//a[contains(text(),'eConestoga')]").click()

time.sleep(5)
driver.close()

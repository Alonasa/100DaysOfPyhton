from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

LINK = "https://secure-retreat-92358.herokuapp.com/"
EMAIL = "all.junk.mails.my@gmail.com"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(LINK)

name = driver.find_element(By.NAME, "fName")
name.send_keys("Alona", Keys.TAB)
surename = driver.find_element(By.NAME, "lName")
surename.send_keys("Sk", Keys.TAB)
mail = driver.find_element(By.NAME, "email")
mail.send_keys(EMAIL)
submit = driver.find_element(By.XPATH, "/html/body/form/button")
submit.click()

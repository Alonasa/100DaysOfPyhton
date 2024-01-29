from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(LINK)
data = driver.find_elements(By.ID, "articlecount")
text = data[0].text.split(" ")
print(text[0])

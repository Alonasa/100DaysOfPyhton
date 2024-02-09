import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

FORM_LINK = "https://forms.gle/Y26bJARvu7m65krC6"
WEBSITE_LINK = "https://appbrewery.github.io/Zillow-Clone/"

data = requests.get(url=WEBSITE_LINK).text
elements = BeautifulSoup(data, "html.parser")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(FORM_LINK)

ADVERTISINGS = elements.find_all(attrs={"class": "ListItem-c11n-8-84-3-StyledListCardWrapper"})
LINKS = [item.a["href"] for item in ADVERTISINGS]
PRICES = [el.text.replace("+", "/").split("/")[0] for el in
          elements.find_all("span", {"data-test": "property-card-price"})]

ADDRESSES = [el.text.replace("|", ",").split(",", 1)[1].strip() for el in elements.find_all("address")]

for item in range(len(ADDRESSES)):
    INPUTS = driver.find_elements(By.CSS_SELECTOR, ".Xb9hP > input")
    SUBMIT = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    INPUTS[0].send_keys(ADDRESSES[item])
    INPUTS[1].send_keys(PRICES[item])
    INPUTS[2].send_keys(LINKS[item])
    SUBMIT.click()
    driver.get(FORM_LINK)

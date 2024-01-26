from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

PRODUCT_LINK = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
PASSWORD = "jjbw dcrj tzun uydj"
EMAIL = "all.junk.mails.my@gmail.com"
ALERT_PRICE = 100

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(PRODUCT_LINK)
price_full = driver.find_element(By.CLASS_NAME, "a-price-whole")
product_title = driver.find_element(By.CLASS_NAME, "product-title-word-break").text
price = price_full.text.strip()
print(price)

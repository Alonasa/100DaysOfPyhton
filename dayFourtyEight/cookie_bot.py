from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://orteil.dashnet.org/experiments/cookie/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")
store = driver.find_element(By.CSS_SELECTOR, value="#store")

timeout = time.time() + 2
stop = time.time() + 2 * 60
while time.time() < stop:
    cookie.click()
    if time.time() > timeout:
        money = driver.find_element(By.CSS_SELECTOR, value="#money")
        money = int(money.text.replace(",", ""))
        store = driver.find_element(By.CSS_SELECTOR, value="#store")
        max_price = 0
        prev_element = driver.find_element(By.CSS_SELECTOR, value="#store div b")
        bought_something = False
        for element in driver.find_elements(By.CSS_SELECTOR, value="#store div b"):
            print(element.text)
            price = element.text.split(" - ")[1]
            price_num = int(price.replace(",", ""))
            print(price_num)
            print(f"I have {money} cookies")
            if int(money) > price_num:
                max_price = price_num
                prev_element = element
            else:
                prev_element.click()
                bought_something = True
                break
        if not bought_something:
            prev_element.click()
        timeout = time.time() + 5

result = driver.find_element(By.CSS_SELECTOR, value="#saveMenu #cps")
print(result.text)
driver.quit()

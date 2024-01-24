import smtplib

import requests
from bs4 import BeautifulSoup

PRODUCT_LINK = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
PASSWORD = "jjbw dcrj tzun uydj"
EMAIL = "all.junk.mails.my@gmail.com"
ALERT_PRICE = 100

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-GB, en-US; q=0.9,en; q=0.8"
}

data = requests.get(url=PRODUCT_LINK, headers=headers)
page = data.text
elements = BeautifulSoup(page, "html.parser")

price_full = elements.find("span", attrs={"class": "a-price"})
product_title = elements.find("span", attrs={"class": "product-title-word-break"}).text
price = price_full.text.strip().split('$')[1]

if float(price) < ALERT_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                            msg=f"Subject:Price Alert for {product_title} price is less\nthan {ALERT_PRICE}".encode(
                                'utf-8'))

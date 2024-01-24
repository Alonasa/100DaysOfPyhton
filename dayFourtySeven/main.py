import requests
from bs4 import BeautifulSoup

PRODUCT_LINK = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-GB, en-US; q=0.9,en; q=0.8"
}

data = requests.get(url=PRODUCT_LINK, headers=headers)
page = data.text
elements = BeautifulSoup(page, "html.parser")

price = elements.find("span", attrs={"class": "a-price"})
print(price.text.strip().split('$')[1])

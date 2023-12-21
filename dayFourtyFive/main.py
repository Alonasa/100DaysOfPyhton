from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "lxml")

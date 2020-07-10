import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup
import urllib.request

root_url = "https://baike.baidu.com/item/Python/407313"
response = urllib.request.urlopen(root_url)
html_content = response.read()

soup =  BeautifulSoup(html_content,"html.parser",from_encoding="utf-8")
links =  soup.find_all("a",href=re.compile(r"/item.+"))
for link in links:
    print(urljoin(root_url,link['href']))

# %%
from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as urReq
import requests

# %%
flipkart_url = "https://www.flipkart.com/search?q="+"tv"
# %%
flipkart_url
# %%
urReq(flipkart_url)
# %%
a = urReq(flipkart_url).read()
# %%
bs(a,'html.parser')
# %%
b = bs(a,'html.parser')
# %%
c = b.find_all("div",{"class":"_1AtVbE col-12-12"})
# %%
result = c[6]
# %%
d = result.div.div.div.a['href']
# %%
url = "https://www.flipkart.com/search?q=" + d
# %%
url
# %%
e = requests.get(url)
# %%
e.encoding = 'utf-8'
# %%
f = bs(e.text,"html.parser")
# %%
f
# %%
reviews = f.find_all("div",{"class":"_16PBlm"})
# %%
len(reviews)
# %%
rating = reviews[5].div.div.div.div.text
# %%
rating
# %%

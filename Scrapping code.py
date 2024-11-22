import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen 
import logging

base_url = 'https://www.amazon.in/s?k='
product = 'headphones'
product_url = base_url+product
urlclient = urlopen(product_url)
print(urlclient)
page_data = urlclient.read()
beautified_data_html = bs(page_data,'html.parser')
items = beautified_data_html.findAll("div", {"class":"sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16"})
print(len(items))
data = []
for item in items:
    url = 'https://www.amazon.in'+(item.find("div", {"class":"a-section a-spacing-small a-spacing-top-small"}).div.h2.a['href'])
    name = item.find("div", {"class":"a-section a-spacing-small a-spacing-top-small"}).div.h2.a.span.text
    try:
        product_client = urlopen(url)
    except Exception as e:
        print(e)
        
    product_data = product_client.read()
    beautified_product_data = bs(product_data, 'html.parser')
    comment_box = beautified_product_data.findAll("div", {"class": "a-section review aok-relative"})
    for rev in comment_box:
        review = rev.find("div", {"class":"a-expander-content reviewText review-text-content a-expander-partial-collapse-content"}).span.text
        product_data = {'name': name, 'url': url, 'review': review}
        data.append(product_data)

scrapped_data = pd.DataFrame(data)
scrapped_data.to_csv('Scrapped Data.csv')

import json

import pandas as pd
import glob  # this module helps in selecting files
import xml.etree.ElementTree as ET  # this module helps in processing xml files
from datetime import datetime

from bs4 import BeautifulSoup
import html5lib
import requests
import pandas as pd

import os
from PIL import Image
from IPython.display import IFrame

# url = "https://www.ibm.com/"
# r = requests.get(url)

# print(r.status_code)
# print(r.request.headers)
#
# print(r.request.body)
#
# header = r.headers
# print(r.headers)
#
# print(r.text[0:100])

# html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
#
# soup = BeautifulSoup(html, 'html5lib')
# print(soup.prettify())
#
# tag_object=soup.title
# print("tag object:",tag_object)
# print("tag object type:",type(tag_object))
#
# tag_object=soup.h3
# print(tag_object)
#
# tag_child = tag_object.b
# print(tag_child)
#
# parent_tag=tag_child.parent
# print(parent_tag)
#
# sibling_1=tag_object.next_sibling
# print(sibling_1)
#
# sibling_2=sibling_1.next_sibling
# print(sibling_2)
#
# print(tag_child['id'])
#
# print(tag_child.attrs)
# print(tag_child.get('id'))
#
#
# tag_string=tag_child.string
# print(tag_string)
#
# print(type(tag_string))
# unicode_string = str(tag_string)
# print(type(unicode_string))

# table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
# table_bs = BeautifulSoup(table, 'html5lib')
#
# table_rows=table_bs.find_all('tr')
# print(table_rows)
#
# first_row =table_rows[0]
# print(first_row)
#
# print(first_row.td)
#
# for i,row in enumerate(table_rows):
#     print("row",i,"is",row)
#
# for i,row in enumerate(table_rows):
#     print("row",i)
#     cells=row.find_all('td')
#     for j,cell in enumerate(cells):
#         print('colunm',j,"cell",cell)
#
# print(table_bs.find_all(id="flight"))
#
# print(table_bs.find_all(href=False))

# url = "http://www.ibm.com"
# data  = requests.get(url).text
# soup = BeautifulSoup(data,"html5lib")  # create a soup object using the variable 'data'
# for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>
#
#     print(link.get('href'))
#
# for link in soup.find_all('img'):# in html image is represented by the tag <img>
#     print(link)
#     print(link.get('src'))

# html_data = requests.get(
#     "https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks").text
# # print(html_data)
#
# print(html_data[760:783])
#
# soup = BeautifulSoup(html_data, 'html5lib')
# data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])
#
# for row in soup.find_all('tbody')[2].find_all('tr'):
#     col = row.find_all('td')
#     if col:
#         name = str(col[1].find_all('a')[1].string)
#         cap = str(col[2].string)
#         data.loc[len(data)] = [name, cap]
#
#
# print(data.head())

# url = "http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key=91acbb681c0315fc8c58cdf99bfc9a5d";
#
# data = requests.get(url).text
# soup = BeautifulSoup(data,'html5lib')
#
# json_data = soup.body.get_text();
# data_dict = json.loads(json_data)
# data_dict = (data_dict['rates'])
#
# # Create a DataFrame from the data dictionary
# df = pd.DataFrame.from_dict(data_dict, orient='index', columns=['Rate'])
#
# # Set the index name to 'Currency'
# df.index.name = 'Currency'
#
# print(df)
# df.to_csv('exchange_rates_1.csv')


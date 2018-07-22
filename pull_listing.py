from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import requests
import shutil
import sys
import time
import os
import csv

# If there are no arguments
if len(sys.argv) == 1:
    print('Please provide a target carousell listing url!')
    sys.exit()

print('Retrieving information from: '+sys.argv[1])
targetUrl = sys.argv[1]

# open chrome and load targeted page
browser = webdriver.Chrome()
browser.get(targetUrl)
print('loading')

# find the first image
img = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[2]/div[3]/div[1]/div/section/div[1]/section[1]/div/div/div[2]/div[1]/figure[2]/img')
src = img.get_attribute('src')
print('Carousell first image download url = '+src)

# Item title
title = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[2]/div[3]/div[1]/div/section/div[2]/section[1]/div[1]/div/div[1]/div/p')
print('Title: '+title.text)

# Item price
price = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[2]/div[3]/div[1]/div/section/div[2]/section[1]/div[3]/div/div/div/p')
print('Price: '+price.text)

# Item Category (Weak method)
category = ''
new = True
try:
    category = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[2]/div[3]/div[1]/div/section/div[2]/section[1]/div[6]/div/div/div/p/a')
    print('Category: '+category.text)
except NoSuchElementException:
    new = False
    print('This listing is missing the new or old display')
    category = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[2]/div[3]/div[1]/div/section/div[2]/section[1]/div[5]/div/div/div/p/a')
    print('Special Case Category: '+category.text)
# Item decription
desc = ''
try:
    desc = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[2]/div[3]/div[1]/div/section/div[2]/section[1]/div[7]/div/div/div/div/div/p')
    print('Description: '+desc.text)
except NoSuchElementException:
    #print("Unexpected error:", sys.exc_info()[0])
    print('This listing has no description')

writer = csv.writer(open('listingData.csv', 'w'))
writer.writerow(['title','price','category','desc'])
writer.writerow([title.text,price.text,category.text,desc.text])

window_before = browser.window_handles[0]
# download the image
r = requests.get(src,stream=True, headers={'User-agent': 'Mozilla/5.0'})
if r.status_code == 200:
    with open("c1.jpg", 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
        browser.quit()

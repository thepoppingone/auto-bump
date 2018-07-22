from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import requests
import shutil
import sys
import time
import os
import csv

title,price,category,desc = ['','','','']
# Get data from csv
with open('listingData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    firstRow = next(readCSV)
    secondRow = next(readCSV)
    title,price,category,desc = secondRow

# open chrome and load targeted page
browser = webdriver.Chrome()
browser.get('https://sg.carousell.com')
print('loading')
window_before = browser.window_handles[0]

sellButton = browser.find_element_by_id('navbarSellLink')
sellButton.click()

fbButton = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/button[1]')
fbButton.click()

window_after = browser.window_handles[1]
browser.switch_to_window(window_after)
time.sleep(2)

fuser = os.environ['FUSER']
fpass =os.environ['FPASS']

loginField = browser.find_element_by_name('email')
loginField.send_keys(fuser)

pwField = browser.find_element_by_name('pass')
pwField.send_keys(fpass) # switch to env var

loginBtn = browser.find_element_by_id('loginbutton')
loginBtn.click()
browser.switch_to_window(window_before)
time.sleep(4.5)

# testPanel = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/div/div/div/div[1]/div[2]/div[1]/div')
# testPanel.click()
uploadPanel = browser.find_element_by_id('photo0')
browser.execute_script("arguments[0].setAttribute('class','')", uploadPanel)
browser.execute_script("arguments[0].style.display = 'block';", uploadPanel)
imagePath = os.getcwd()+'/c1.jpg'
print('Image path: '+imagePath)
uploadPanel.send_keys(os.path.abspath(imagePath))

time.sleep(1.5)
saveButton = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/div/div/div/div[1]/div[1]/div[2]/button[5]')
saveButton.click()

time.sleep(1)
nextCatBtn = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/div/div/div/div[2]/button')
nextCatBtn.click()

time.sleep(1)
searchCatField = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/div/div/div/div/div/div[1]/div/form/span/input')
searchCatField.send_keys(category)

time.sleep(1)
catButton = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/div/div/div/div/div/div[1]/ul/li/button')
catButton.click()

time.sleep(1)
listNameField = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/div/div/div[1]/div/section/fieldset[1]/div/div[1]/div[1]/form/span/input')
listNameField.send_keys(title)

time.sleep(1)
priceNameField = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/div/div/div[1]/div/section/fieldset[1]/div/div[2]/div[1]/form/span[2]/input')
priceNameField.send_keys(price)

time.sleep(1)
new = True
radioBtn = ''
if new:
	radioBtn = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/div/div/div[1]/div/section/fieldset[2]/div[2]/ul/li[1]/label')
else:
	radioBtn = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/div/div/div[1]/div/section/fieldset[2]/div[2]/ul/li[2]/label')

radioBtn.click()
time.sleep(1)

descTextArea = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/div/div/div[1]/div/section/fieldset[3]/div[2]/div/div[1]/form/span/textarea')
descTextArea.send_keys(desc)

time.sleep(1)
listBtn = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/div/div/div[2]/button')
listBtn.click()



# webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()


#browser.quit()

from selenium import webdriver
from time import sleep
import base64

f = open('index.txt','rb')
user = f.readline()
pwd = f.readline()
user = base64.b64decode(base64.b64decode(user)).decode('utf8')
pwd = base64.b64decode(base64.b64decode(pwd)).decode('utf8')
f.close()

chrome = webdriver.Chrome(executable_path=r'C:\Users\12517\Desktop\IP地址查询\build\chromedriver.exe')
chrome.get('http://202.115.133.173:805/Login.html')
user_login = chrome.find_element_by_xpath('//*[@id="txtUser"]')
user_login.send_keys(user)
pwd_login = chrome.find_element_by_xpath('//*[@id="txtPWD"]')
pwd_login.send_keys(pwd)
login_click = chrome.find_element_by_xpath('//*[@id="ibtnLogin"]')
login_click.click()
sleep(1)
score = chrome.find_element_by_xpath('//*[@id="form1"]/div[4]/div[1]/ul/li[7]/a/span')
score.click()
score_click = chrome.find_element_by_xpath('//*[@id="form1"]/div[4]/div[1]/ul/li[7]/ul/li[1]/a/span')
score_click.click()
print_score = chrome.find_element_by_xpath('//*[@id="BtPrint"]')
print_score.click()
# yixuan_click = chrome.find_element_by_xpath('//*[@id="form1"]/div[4]/div[2]/div/ul/li[2]/a')
# yixuan_click.click()
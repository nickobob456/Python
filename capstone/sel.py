import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


browser = webdriver.Chrome()
browser.get("http://www.google.com/finance") #website for stockdata



elemA = browser.find_element_by_name("q")
elemA.send_keys('IBM') #Will come from Competitors
elemA.send_keys(Keys.RETURN)



time.sleep(3)
browser.find_element_by_link_text("Historical prices").click()
time.sleep(3)



elemDS = browser.find_element_by_name("startdate")
elemDS.send_keys("Nov 1, 2010") #Will come from main patent date -120

elemDE = browser.find_element_by_name("enddate")
elemDE.send_keys("Dec 1, 2010") #Will come from main patent date +120

time.sleep(1)
elemDE.send_keys(Keys.RETURN)



time.sleep(3)
browser.find_element_by_xpath('//*[@id="gf-viewc"]/div/div/div[2]/div[1]/div/div[3]/div/a').click()
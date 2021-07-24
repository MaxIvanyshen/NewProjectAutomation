from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import subprocess
import pyperclip

#needed variables
chromedriver_directory = "<WHERE YOU HAVE YOUR CHROMEDRIVER FILE>"
username = "<YOUR GITHUB USERNAME>"
passw = "<YOUR GITHUB PASSWORD>"
repo_directory = "<WHERE NEW REPOSITORY WILL BE COPIED>"

#getting porject name from user
print("Enter project name: ")
projectName = input()

#opening login page
driver = webdriver.Chrome(chromedriver_directory)
driver.get("https://www.github.com/login")

#sending login to page
login = driver.find_element_by_name("login")
login.send_keys(username)

#sending password to page
password = driver.find_element_by_name("password")
password.send_keys(passw)

#clicking 'log in' button
loginBtn = driver.find_element_by_name("commit")
loginBtn.click()

#opening page for creating new repository
driver.get("https://www.github.com/new")

#sending repositiry name to page
repoName = driver.find_element_by_name("repository[name]")
repoName.send_keys(projectName)

#adding README file and other changes + clicking 'create repository' button

addReadMe = driver.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/div[4]/div[1]/label/input[2]")
addReadMe.click()

submitBtn = driver.find_element_by_css_selector("#new_repository > div.js-with-permission-fields > button")
time.sleep(2)
submitBtn.click()

#copying repository link
codeBtn = driver.find_element_by_css_selector("#repo-content-pjax-container > div > div.gutter-condensed.gutter-lg.flex-column.flex-md-row.d-flex > div.flex-shrink-0.col-12.col-md-9.mb-4.mb-md-0 > div.file-navigation.mb-3.d-flex.flex-items-start > span > get-repo > details > summary")
codeBtn.click()

copyBtn = driver.find_element_by_css_selector("#repo-content-pjax-container > div > div.gutter-condensed.gutter-lg.flex-column.flex-md-row.d-flex > div.flex-shrink-0.col-12.col-md-9.mb-4.mb-md-0 > div.file-navigation.mb-3.d-flex.flex-items-start > span > get-repo > details > div > div > div:nth-child(1) > div > tab-container > div:nth-child(2) > div > div > clipboard-copy")
copyBtn.click()

driver.close()

#cloning repository to the PC
text = pyperclip.paste()
command = "git clone " + text

#going to cloned repository
os.chdir(repo_directory)
os.system(command)

driver.close()

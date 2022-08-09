from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import sys

#change these variables
username = "<YOUR GITHUB USERNAME>"
passw = "<YOUR GITHUB PASSWORD"

#needed variables
chromedriver_directory = sys.argv[1]
repo_directory = sys.argv[2]
projectName = sys.argv[3]


#creating webdriver instance
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(chromedriver_directory, options=option)

#opening login page
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

addReadMe = driver.find_element_by_xpath('//*[@id="repository_auto_init"]')
addReadMe.click()

submitBtn = driver.find_element_by_xpath('//*[@id="new_repository"]/div[5]/button')
time.sleep(2)
submitBtn.click()

#cloning repository to the PC
text = driver.current_url
command = "git clone " + text

#going to cloned repository
os.chdir(repo_directory)
os.system(command)

driver.close()

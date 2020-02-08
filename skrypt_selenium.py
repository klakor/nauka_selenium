from selenium import webdriver

from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.google.com/')
driver.maximize_window()

ele = driver.find_element_by_class('gLFyf gsfi')

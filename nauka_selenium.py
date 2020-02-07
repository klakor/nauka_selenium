from selenium import webdriver
import time
driver = webdriver.Chrome("/home/klaudia/Documents/chromedriver")
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

driver.maximize_window()

driver.get("https://python.org/")

driver.find_element_by_xpath("//a[@href='/doc/']").click()
driver.find_element_by_link_text("Library Reference").click()
ele = driver.find_element_by_name("q")
ele.clear()
ele.send_keys("unittest")
ele.send_keys(Keys.RETURN)

#time.sleep(1)
#driver.quit()




#driver.implicitly_wait(10)
#driver.get("https://www.pluralsight.com/")

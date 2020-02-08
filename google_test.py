import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitForGoogle(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.google.pl/")

    def tearDown(self):
        self.driver.quit()

    def testWait(self):
        driver=self.driver
        input_field = driver.find_element_by_name("q")
        input_field.send_keys("tester oprogramowania")
        input_field.submit()
        # Pobieram rezultaty wyszukiwania
        # results = driver.find_elements_by_class_name("g")
        # Czekam na rezultaty wyszukiwania
        results = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "g")))

        for r in results:
            print(r.text)
        sleep(3)

if __name__=='__main__':
    unittest.main()

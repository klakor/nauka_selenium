import unittest
from selenium import webdriver
from time import sleep

class WsbPlCheck(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.wsb.pl/')


    def testTitle(self):
        #sprawdzam, czy otworzylem wlasciwa strone
        self.assertIn("Bankowe", self.driver.title)
        #czekam 5 sek
        sleep(5)

    #def TestDrugi(self):
        #pass

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=3)

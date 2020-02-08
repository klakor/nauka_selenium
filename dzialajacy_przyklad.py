import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
# Sceanriusz:
# Rejestracja nowego uytkownika na stronie automationpractice.com
#
email_address = "datadata@data.com"
imie = "imie"
nazwisko = "nazwisko"
company = "company"

class APregistration(unittest.TestCase):
# Przypadki testowe:
# I. Niewybrane miasto
#
# Warunki wstepne:
    def setUp(self):
    # 1. otwarta przegladarka
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    # 2. otwarta strona http://automationpractice.com/index.php
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.maximize_window()


    def testNoCity(self):
        driver = self.driver
            # 1. Klknij "sign in"
        sign_in = driver.find_element_by_class_name('login')
        sign_in.click()

        # 2. Wpisz e-mail (data@data.com)
        email_input = driver.find_element_by_id("email_create")
        email_input.send_keys(email_address)

        # 3. Kliknij "create account"
        driver.find_element_by_id("SubmitCreate").click()

        # 4. Wybierz tytul
        driver.find_element_by_id("id_gender2").click()

        # 5. Wpisz imie
        driver.find_element_by_id("customer_firstname").send_keys(imie)

        # 6. Wpisz nazwisko
        driver.find_element_by_id("customer_lastname").send_keys(nazwisko)

        #7. Sprawdz poprawnosc e-maila
        email_value = driver.find_element_by_id("email").get_attribute("value")
        self.assertEqual(email_value, email_address)

        # 8. Wpisz haslo
        driver.find_element_by_id("passwd").send_keys("password")

        # 9. Wybierz date urodzenia
        day = Select(driver.find_element_by_id("days"))
        day.select_by_value("21")
        month = Select(driver.find_element_by_id("months"))
        month.select_by_value("7")
        year = Select(driver.find_element_by_id("years"))
        year.select_by_value("1980")

        #10. Sprawdz imie
        name = driver.find_element_by_id("firstname").get_attribute("value")
        self.assertEqual(name, imie)

        # 11. Sprawdz nazwisko
        lastname = driver.find_element_by_id("lastname").get_attribute("value")
        self.assertEqual(lastname, nazwisko)
        assert lastname == nazwisko

        #12. Wpisz firme
        driver.find_element_by_id("company").send_keys(company)

        #13. Wpisz adres
        driver.find_element_by_id("address1").send_keys("adres jakistam")

         #14. Wybierz stan
        country = Select(driver.find_element_by_id("id_state"))
        country.select_by_visible_text("California")

        # 15. Wpisz kod pocztowy
        driver.find_element_by_id("postcode").send_keys("00000")

        # 16. Wpisz nr telefonu
        driver.find_element_by_id("phone_mobile").send_keys("12345678")

        # 17. Wpisz alias adresu
        alias = driver.find_element_by_id("alias")
        alias.clear()
        alias.send_keys("Adres domyslny")

        # 18. Kliknij register
        driver.find_element_by_id("submitAccount").click()

        # Oczekiwany rezulat
        # (0. konto nie zostaje zalozone)
        # 1. Wyswietla sie blad - "City is required"
        errors = driver.find_elements_by_xpath('//div[@class="alert alert-danger"]/ol/li')
        assert len(errors) == 1
        error_text = errors[0].get_attribute("innerText")
        assert errors[0].is_displayed()
        assert "city is required" in error_text

        sleep(4)



    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)





#
# Oczekiwany rezulat
# (0. konto nie zostaje zalozone)
# 1. Wyswietla sie blad - "City is required"
pass

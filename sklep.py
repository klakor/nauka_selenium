import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

user_email = "data@data.com"
name = "Anna"
surname = "Kowalska"
password = "500+1000-"
birth_day = "6"
birth_month = "February "
birth_year = "1991"
company = "Kamsoft"
city = "Florida"
postal_code = "40400"
address = city, postal_code

# Scenariusz testowy:
# Rejestracja nowego uzytkownika na stronie http://automationpractice.com/index.php
class APregistration(unittest.TestCase):
    # Warunki wstepne
    def setUp(self):
        # 1. Otwarta przegladarka
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 2. Otwarta strona http://automationpractice.com/index.php
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.implicitly_wait(10)

    # Przypadki testowe:

    # I Niewybrane miasto
    def testNoCity(self):
        driver = self.driver
        # Kroki:
        # 1. Odszukaj sign in
        sign_in = driver.find_element_by_class_name("login")
        # Klknij "sign in"
        sign_in.click()
        #spij 4 sek


        # 2. Wpisz e-mail (data@data.com)
        driver.find_element_by_id("email_create").send_keys(user_email)

        # 3. Kliknij "create account"
        driver.find_element_by_name("SubmitCreate").click()

        # 4. Wybierz tytul
        driver.find_element_by_id("id_gender2").click()

        # 5. Wpisz imie
        driver.find_element_by_id("customer_firstname").send_keys(name)

        # 6. Wpisz nazwisko
        driver.find_element_by_id("customer_lastname").send_keys(surname)

        # 7. Sprawdz poprawnosc e-maila
        email_fact = driver.find_element_by_id("email").get_attribute("value")
        assert email_fact == user_email

        # 8. Wpisz haslo
        driver.find_element_by_id("passwd").send_keys(password)

        # 9. Wybierz date urodzenia
        day = Select(driver.find_element_by_id("days"))
        day.select_by_value(birth_day)
        month = Select(driver.find_element_by_id("months"))
        month.select_by_visible_text(birth_month)
        year = Select(driver.find_element_by_id("years"))
        year.select_by_value(birth_year)

        # 10. Sprawdz imie
        name_fact = driver.find_element_by_id("firstname").get_attribute("value")
        assert name_fact == name

        # 11. Sprawdz nazwisko
        surname_fact = driver.find_element_by_id("lastname").get_attribute("value")
        assert surname_fact == surname

        # 12. Wpisz firme
        driver.find_element_by_xpath("//*[@id='company']").send_keys(company)

        # 13. Wpisz adres
        #driver.find_element_by_css_selector("#address1").send_keys(adress)
        # 14. Wybierz stan
        # 15. Wpisz kod pocztowy
        # 16. Wpisz nr telefonu
        # 17. Wpisz alias adresu
        # 18. Kliknij register
        sleep(5)

    def tearDown(self):
        # Sprzatanie po kazdym tescie
        # Wylacz przegladarke
        self.driver.quit()

# Oczekiwany rezulat
# (0. konto nie zostaje zalozone)
# 1. Wyswietla sie blad - "City is required"

if __name__ == "__main__":
    unittest.main(verbosity=2)

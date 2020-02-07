# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def create_new_contact(self, wd):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(u"Петр")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(u"Петрович")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(u"Петров")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(u"петрич")
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(u"ПЕТООР")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(u"Петровкакомпания")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(u"ул. Петров")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("84956521474")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("+75641257896")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("89541236545")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("78444111")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("petrmail@emilo.com")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("petr2@emilo.com")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("petrmilo@emilo.ru")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("www.petrpetr.ru")
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("January")
        wd.find_element_by_name("byear").send_keys("1990")
        Select(wd.find_element_by_name("aday")).select_by_visible_text("2")
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("February")
        wd.find_element_by_name("ayear").send_keys("2015")
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(u"Адрес 2")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("2")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(u"что то")
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.create_new_contact(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()

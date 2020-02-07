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

    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def create_new_contact(self, wd, firstname, middlename, lastname, nickname, title, company, address, home, mobile,
                           work, fax, email1, email2, email3, homepage, bday, bmoth, byear, aday, amonth, ayear,
                           address2, phone2, notes):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nickname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email1)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(homepage)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(bday)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(bmoth)
        wd.find_element_by_name("byear").send_keys(byear)
        Select(wd.find_element_by_name("aday")).select_by_visible_text(aday)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(amonth)
        wd.find_element_by_name("ayear").send_keys(ayear)
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(address2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(phone2)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(notes)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.create_new_contact(wd, firstname = "Петр", middlename = "Петрович", lastname = "Петров", nickname = "петрич", title = "ПЕТООР", company = "Петровкакомпания", address = "ул. Петров", home = "84956521474", mobile = "+75641257896", work = "89541236545", fax = "78444111", email1 = "petrmail@emilo.com", email2 = "petr2@emilo.com", email3 = "petrmilo@emilo.ru", homepage = "www.petrpetr.ru", bday = "1", bmoth = "January", byear = "1990", aday = "2", amonth = "February", ayear = "2015", address2 = "Адрес 2", phone2 = "2", notes = "что то")
        self.return_to_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()

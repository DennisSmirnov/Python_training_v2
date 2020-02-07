# -*- coding: utf-8 -*-
from contact import Contact
from application2 import Application2
import pytest

@pytest.fixture
def app(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact (firstname = "Петр", middlename = "Петрович", lastname = "Петров", nickname = "петрич",
                                             title = "ПЕТООР", company = "Петровкакомпания", address = "ул. Петров", home = "84956521474",
                                             mobile = "+75641257896", work = "89541236545", fax = "78444111", email1 = "petrmail@emilo.com",
                                             email2 = "petr2@emilo.com", email3 = "petrmilo@emilo.ru", homepage = "www.petrpetr.ru", bday = "1",
                                             bmonth = "January", byear = "1990", aday = "2", amonth = "February", ayear = "2015", address2 = "Адрес 2",
                                             phone2 = "2", notes = "что то"))
    app.logout()



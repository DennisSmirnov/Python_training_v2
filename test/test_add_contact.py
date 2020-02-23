from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(firstname=firstname, middlename=middlename, lastname =lastname, address=address, email1=email1, company=company)
    for firstname in ["", random_string ("firstname", 10)]
    for middlename in ["", random_string("middlename", 20)]
    for lastname in ["", random_string ("lastname", 20)]
    for address in ["", random_string ("address", 20)]
    for email1 in ["", random_string ("email1", 20)]
    for company in ["", random_string ("cpmpany", 20)]
]
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_test_add_contact(app, contact):
    old_contact = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == app.contact.count()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

    #contact = Contact(firstname ="Петр", middlename ="Петрович", lastname ="Петров", nickname ="петрич",
     #                           title = "ПЕТООР", company = "Петровкакомпания", address = "улица_Петрова", home = "84956521474",
      #                          mobile = "+75641257896", work = "89541236545", fax = "78444111", email1 = "petrmail@emilo.com",
       #                         email2 = "petr2@emilo.com", email3 = "petrmilo@emilo.ru", homepage = "www.petrpetr.ru", bday = "1",
        #                        bmonth = "January", byear = "1990", aday = "2", amonth = "February", ayear = "2015", address2 = "Адрес 2",
         #                       phone2 = "2", notes = "что то")
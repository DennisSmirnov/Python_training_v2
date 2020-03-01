from model.contact import Contact
from random import randrange

def test_test_modify_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname ="Петр", middlename ="Петрович", lastname ="Петров", nickname ="петрич",
                                title = "ПЕТООР", company = "Петровкакомпания", address = "ул.Петров", home = "84956521474",
                                mobile = "+75641257896", work = "89541236545", fax = "78444111", email1 = "petrmail@emilo.com",
                                email2 = "petr2@emilo.com", email3 = "petrmilo@emilo.ru", homepage = "www.petrpetr.ru", bday = "1",
                                bmonth = "January", byear = "1990", aday = "2", amonth = "February", ayear = "2015", address2 = "Адрес 2",
                                phone2 = "2", notes = "что то"))
    old_contact = db.get_contact_list()
    index = randrange(len(old_contact))
    contact = Contact (firstname ="Иван", middlename ="Иванов", lastname ="Иванович", nickname ="иванич",
                                title = "ИВААН", company = "Петровкакомпания", address = "ул.Петров", home = "84956521474",
                                mobile = "+75641257896", work = "89541236545", fax = "78444111", email1 = "petrmail@emilo.com",
                                email2 = "petr2@emilo.com", email3 = "petrmilo@emilo.ru", homepage = "www.petrpetr.ru", bday = "1",
                                bmonth = "January", byear = "1991", aday = "3", amonth = "February", ayear = "2014", address2 = "Адрес 2",
                                phone2 = "1", notes = "это")
    #contact.id = old_contact[index].id
    app.contact.modify_contact_by_id(contact.id)
    new_contact = db.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact.remove(contact)
    assert old_contact == new_contact
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.group.get_contact_list(), key=Contact.id_or_max)
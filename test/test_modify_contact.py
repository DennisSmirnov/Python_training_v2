from model.contact import Contact
#
def test_test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname ="Петр", middlename ="Петрович", lastname ="Петров", nickname ="петрич",
                                title = "ПЕТООР", company = "Петровкакомпания", address = "ул. Петров", home = "84956521474",
                                mobile = "+75641257896", work = "89541236545", fax = "78444111", email1 = "petrmail@emilo.com",
                                email2 = "petr2@emilo.com", email3 = "petrmilo@emilo.ru", homepage = "www.petrpetr.ru", bday = "1",
                                bmonth = "January", byear = "1990", aday = "2", amonth = "February", ayear = "2015", address2 = "Адрес 2",
                                phone2 = "2", notes = "что то"))
    old_contact = app.contact.get_contact_list()
    contact = Contact (firstname ="Иван", middlename ="Иванов", lastname ="Иванович", nickname ="иванич",
                                title = "ИВААН", company = "Петровкакомпания", address = "ул. Петров", home = "84956521474",
                                mobile = "+75641257896", work = "89541236545", fax = "78444111", email1 = "petrmail@emilo.com",
                                email2 = "petr2@emilo.com", email3 = "petrmilo@emilo.ru", homepage = "www.petrpetr.ru", bday = "1",
                                bmonth = "January", byear = "1991", aday = "3", amonth = "February", ayear = "2014", address2 = "Адрес 2",
                                phone2 = "1", notes = "это")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
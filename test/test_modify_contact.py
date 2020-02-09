from model.contact import Contact
#
def test_test_modify_first_contact(app):
    old_contact = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname ="Петр", middlename ="Петрович", lastname ="Петров", nickname ="петрич",
                                title = "ПЕТООР", company = "Петровкакомпания", address = "ул. Петров", home = "84956521474",
                                mobile = "+75641257896", work = "89541236545", fax = "78444111", email1 = "petrmail@emilo.com",
                                email2 = "petr2@emilo.com", email3 = "petrmilo@emilo.ru", homepage = "www.petrpetr.ru", bday = "1",
                                bmonth = "January", byear = "1990", aday = "2", amonth = "February", ayear = "2015", address2 = "Адрес 2",
                                phone2 = "2", notes = "что то"))
    app.contact.modify_first_contact(Contact (firstname ="Иван", middlename ="Иванов", lastname ="Иванович", nickname ="иванич",
                                title = "ИВААН", company = "Петровкакомпания", address = "ул. Петров", home = "84956521474",
                                mobile = "+75641257896", work = "89541236545", fax = "78444111", email1 = "petrmail@emilo.com",
                                email2 = "petr2@emilo.com", email3 = "petrmilo@emilo.ru", homepage = "www.petrpetr.ru", bday = "1",
                                bmonth = "January", byear = "1991", aday = "3", amonth = "February", ayear = "2014", address2 = "Адрес 2",
                                phone2 = "1", notes = "это"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
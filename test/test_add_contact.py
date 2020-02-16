from model.contact import Contact
#

def test_test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname ="Петр", middlename ="Петрович", lastname ="Петров", nickname ="петрич",
                                title = "ПЕТООР", company = "Петровкакомпания", address = "улица_Петрова", home = "84956521474",
                                mobile = "+75641257896", work = "89541236545", fax = "78444111", email1 = "petrmail@emilo.com",
                                email2 = "petr2@emilo.com", email3 = "petrmilo@emilo.ru", homepage = "www.petrpetr.ru", bday = "1",
                                bmonth = "January", byear = "1990", aday = "2", amonth = "February", ayear = "2015", address2 = "Адрес 2",
                                phone2 = "2", notes = "что то")
    app.contact.create(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == app.contact.count()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


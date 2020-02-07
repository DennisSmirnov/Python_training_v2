from model.contact import Contact
#
def test_test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact (firstname ="Иван", middlename ="Иванов", lastname ="Иванович", nickname ="иванич",
                                title = "ИВААН", company = "Петровкакомпания", address = "ул. Петров", home = "84956521474",
                                mobile = "+75641257896", work = "89541236545", fax = "78444111", email1 = "petrmail@emilo.com",
                                email2 = "petr2@emilo.com", email3 = "petrmilo@emilo.ru", homepage = "www.petrpetr.ru", bday = "1",
                                bmonth = "January", byear = "1991", aday = "3", amonth = "February", ayear = "2014", address2 = "Адрес 2",
                                phone2 = "1", notes = "это"))
    app.session.logout()
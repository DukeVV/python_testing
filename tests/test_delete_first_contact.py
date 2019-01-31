
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov"))
    app.contact.delete_first_contact()


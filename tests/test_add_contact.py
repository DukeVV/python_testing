
from model.contact import Contact


def test_add_new_contact(app):
    app.contact.create_new(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov"))



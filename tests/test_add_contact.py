
from model.contact import Contact


def test_untitled_test_case(app):
    app.contact.create_new(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov"))



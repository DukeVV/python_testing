from model.contact import Contact


def test_modify_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="Sergei", middlename="Ivanovich", lastname="Sergeev"))


def test_modify_middlename(app):
    app.contact.modify_first_contact(Contact(firstname="Sergei", middlename="Ivanovich", lastname="Sergeev"))


def test_modify_lastname(app):
    app.contact.modify_first_contact(Contact(firstname="Sergei", middlename="Ivanovich", lastname="Sergeev"))


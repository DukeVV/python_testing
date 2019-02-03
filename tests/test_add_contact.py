
from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov")
    app.contact.create_new(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)








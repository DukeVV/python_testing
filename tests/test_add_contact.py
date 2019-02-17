
from model.contact import Contact
import pytest
import random
import string


def random_string_for_name_and_address(prefix, maxlen):
    symbols = string.ascii_letters + string.punctuation + " "*4
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_for_phones(maxlen):
    symbols = string.digits + " " + "-"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_for_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@rr.com"


testdata = [Contact(firstname="", middlename="", lastname="", address="", homephone="",
                    mobilephone="", workphone="", secondaryphone="", email="",
                    email2="", email3="")] + [Contact(firstname=random_string_for_name_and_address("firstname", 10),
                                                      middlename=random_string_for_name_and_address("middlename", 10),
                                                      lastname=random_string_for_name_and_address("lastname", 10),
                                                      address=random_string_for_name_and_address("address", 20),
                                                      homephone=random_string_for_phones(12),
                                                      mobilephone=random_string_for_phones(12),
                                                      workphone=random_string_for_phones(12),
                                                      secondaryphone=random_string_for_phones(12),
                                                      email=random_string_for_email("email", 20),
                                                      email2=random_string_for_email("email2", 20),
                                                      email3=random_string_for_email("email3", 20))
                                              for i in range(5)
                                              ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)










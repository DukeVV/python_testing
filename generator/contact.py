
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage(0)
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
                                              for i in range(n)
                                              ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))


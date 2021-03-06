from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, id=None, homephone=None, mobilephone=None,
                 workphone=None, secondaryphone=None, all_phones_from_home_page=None,
                 address=None, email=None, email2=None, email3=None, all_emails=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.address = address
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails = all_emails
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.middlename,
                                                     self.homephone, self.mobilephone, self.workphone, self.secondaryphone,
                                                     self.address, self.email, self.email2, self.email3)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

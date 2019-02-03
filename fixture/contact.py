from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_new(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_name(contact)
        # input data base
        wd.find_element_by_xpath("//input[21]").click()

    def fill_name(self, contact):
        wd = self.app.wd
        self.change_contact_field_value("firstname", contact.firstname)
        self.change_contact_field_value("middlename", contact.middlename)
        self.change_contact_field_value("lastname", contact.lastname)

    def change_contact_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_xpath("//div[@id='content']/div").click()

    def modify_first_contact(self, new_contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_name(new_contact)
        # input data base
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def check_contact(self):
        wd = self.app.wd
        if self.count() == 0:
            self.create_new(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            cells = element.find_elements_by_tag_name("td")
            text = cells[2].text
            id = element.find_element_by_name("selected[]"). get_attribute("value")
            contacts.append(Contact(lastname=text, id=id))
        return contacts



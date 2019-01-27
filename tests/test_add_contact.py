# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from model.contact import Contact


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_untitled_test_case(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_new_contact(wd, Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov"))
        self.logout(wd)

    def create_new_contact(self, wd, contact):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
        # fill name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # input data base
        wd.find_element_by_xpath("//input[21]").click()

    def logout(self, wd):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def login(self, wd, username, password):
        wd = self.wd
        self.open_home_page(wd)
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
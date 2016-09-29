# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.open_contacts_page(wd)
        self.create_contact(
            wd,
            first_name="Name",
            middle_name="Initials",
            last_name="Last name",
            nickname="nick34958",
            title="Boss",
            company="Google",
            address="Google str.12",
            home_phone_number="+100395845732",
            mobile_phone_number="+195684738592",
            work_phone_number="+1783958438948",
            fax_number="+1945842489348",
            email="address@email.com",
            email2="address2@email.com",
            email3="address3@email.com",
            homepage_url="https://myhomepage.org",
            bday=14,
            bmonth="October",
            byear=1923,
            aday=16,
            amonth="March",
            ayear=1975,
            address2="some secondary address",
            phone_number2="+100193857011",
            notes="first test contact"
        )
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def create_contact(self, wd, first_name, middle_name, last_name, nickname, title, company, address,
                       home_phone_number, mobile_phone_number, work_phone_number, fax_number, email, email2, email3,
                       homepage_url, bday, bmonth, byear, aday, amonth, ayear, address2, phone_number2, notes):
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(home_phone_number)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(mobile_phone_number)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(work_phone_number)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(fax_number)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(homepage_url)
        # fill birthday
        if not wd.find_element_by_xpath(
                        "//div[@id='content']/form/select[@name='bday']//option[@value='%s']" % bday).is_selected():
            wd.find_element_by_xpath(
                "//div[@id='content']/form/select[@name='bday']//option[@value='%s']" % bday).click()
        if not wd.find_element_by_xpath(
                        "//div[@id='content']/form/select[@name='bmonth']//option[@value='%s']" % bmonth).is_selected():
            wd.find_element_by_xpath(
                "//div[@id='content']/form/select[@name='bmonth']//option[@value='%s']" % bmonth).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(byear)
        # fill anniversary
        if not wd.find_element_by_xpath(
                        "//div[@id='content']/form/select[@name='aday']//option[@value='%s']" % aday).is_selected():
            wd.find_element_by_xpath(
                "//div[@id='content']/form/select[@name='aday']//option[@value='%s']" % aday).click()
        wd.find_element_by_name("theform").click()
        if not wd.find_element_by_xpath(
                        "//div[@id='content']/form/select[@name='amonth']//option[@value='%s']" % amonth).is_selected():
            wd.find_element_by_xpath(
                "//div[@id='content']/form/select[@name='amonth']//option[@value='%s']" % amonth).click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(phone_number2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(notes)
        # submit contact form
        wd.find_element_by_xpath("//div[@id='content']/form/input[@type='submit']").click()

    def open_contacts_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

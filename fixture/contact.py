from model.contact import Contact

import re

class ContactHelper(object):

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_select_value(self, select_name, value):
        wd = self.app.wd
        if value is not None:
            xpath_str = "//div[@id='content']/form/select[@name='{select_name}']//option[@value='{value}']".format(
                select_name=select_name, value=value
            )
            if not wd.find_element_by_xpath(xpath_str).is_selected():
                wd.find_element_by_xpath(xpath_str).click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.fill_contact_form(contact)
        # submit contact form
        wd.find_element_by_xpath("//div[@id='content']/form/input[@type='submit']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_contact_edit_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # click first group edit link
        wd.find_element_by_xpath("//table//tr[{0}]//td[8]//a".format(index + 2)).click()

    def open_contact_edit_page_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//input[@value='{0}']//..//..//td[8]//a".format(id)).click()

    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # click first group edit link
        wd.find_element_by_xpath("//table//tr[{0}]//td[7]//a".format(index + 2)).click()

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_edit_page_by_index(index)
        self.fill_contact_form(new_contact_data)
        # submit contact form
        wd.find_element_by_xpath("//div[@id='content']/form/input[@type='submit']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contact_edit_page_by_id(id)
        self.fill_contact_form(new_contact_data)
        # submit contact form
        wd.find_element_by_xpath("//div[@id='content']/form/input[@type='submit']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill contact form
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone_number)
        self.change_field_value("mobile", contact.mobile_phone_number)
        self.change_field_value("work", contact.work_phone_number)
        self.change_field_value("fax", contact.fax_number)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage_url)
        # fill birthday
        self.change_select_value("bday", contact.bday)
        self.change_select_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        # fill anniversary
        self.change_select_value("aday", contact.aday)
        self.change_select_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone_number2)
        self.change_field_value("notes", contact.notes)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # select contact with given index
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def open_contacts_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/edit.php"):
            wd.find_element_by_link_text("add new").click()

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") or wd.current_url.endswith("/index.php")):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        """
        Получение списка контактов с домашней страницы
        :return:
        """
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_css_selector('tr[name="entry"]'):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                last_name = cells[1].text
                first_name = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, first_name=first_name, last_name=last_name, address=address,
                                                  all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_page_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        home_phone_number = wd.find_element_by_name("home").get_attribute("value")
        work_phone_number = wd.find_element_by_name("work").get_attribute("value")
        mobile_phone_number = wd.find_element_by_name("mobile").get_attribute("value")
        phone_number2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(id=id, first_name=first_name, last_name=last_name, address=address,
                       email=email, email2=email2, email3=email3,
                       home_phone_number=home_phone_number, mobile_phone_number=mobile_phone_number,
                       work_phone_number=work_phone_number, phone_number2=phone_number2)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone_number = re.search("H: (.*)", text).group(1)
        work_phone_number = re.search("W: (.*)", text).group(1)
        mobile_phone_number = re.search("M: (.*)", text).group(1)
        phone_number2 = re.search("P: (.*)", text).group(1)
        return Contact(home_phone_number=home_phone_number, mobile_phone_number=mobile_phone_number,
                       work_phone_number=work_phone_number, phone_number2=phone_number2)

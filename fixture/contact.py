
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

    def open_first_contact_edit_page(self):
        wd = self.app.wd
        # click first group edit link
        wd.find_element_by_xpath("//table//tr[2]//td[8]//a").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_first_contact_edit_page()
        self.fill_contact_form(new_contact_data)
        # submit contact form
        wd.find_element_by_xpath("//div[@id='content']/form/input[@type='submit']").click()
        self.return_to_home_page()

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
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()

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
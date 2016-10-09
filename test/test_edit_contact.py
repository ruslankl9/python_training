# -*- coding: utf-8 -*-

from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(
        Contact(
            first_name="Name_edited",
            middle_name="Initials_edited",
            last_name="Last name_edited",
            nickname="nick34958_edited",
            title="Boss_edited",
            company="Google_edited",
            address="Google str.12_edited",
            home_phone_number="+100395845732_edited",
            mobile_phone_number="+195684738592_edited",
            work_phone_number="+1783958438948_edited",
            fax_number="+1945842489348_edited",
            email="address@email.com_edited",
            email2="address2@email.com_edited",
            email3="address3@email.com_edited",
            homepage_url="https://myhomepage.org/edited/",
            bday=1,
            bmonth="January",
            byear=1970,
            aday=11,
            amonth="june",
            ayear=1955,
            address2="some secondary address_edit",
            phone_number2="+100193857011 edited",
            notes="first test edited contact"
        )
    )
    app.session.logout()
# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(
        first_name="Name",
        middle_name="Initials",
        last_name="Last name",
        nickname="nick34958",
        title="Boss",
        company="Google",
        address="Google str.12",
        home_phone_number="+1-202-555-0113",
        mobile_phone_number="+1-202-555-0181",
        work_phone_number="+44 1632 960369",
        fax_number="+44 1632 960817",
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
        phone_number2="+44(1683)945893",
        notes="first test contact"
    )
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)
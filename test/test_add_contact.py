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
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)

"""
def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(
        first_name="",
        middle_name="",
        last_name="",
        nickname="",
        title="",
        company="",
        address="",
        home_phone_number="",
        mobile_phone_number="",
        work_phone_number="",
        fax_number="",
        email="",
        email2="",
        email3="",
        homepage_url="",
        bday="",
        bmonth="-",
        byear="",
        aday="",
        amonth="-",
        ayear="",
        address2="",
        phone_number2="",
        notes=""
    )
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)
"""
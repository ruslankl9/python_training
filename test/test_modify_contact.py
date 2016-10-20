# -*- coding: utf-8 -*-

from model.contact import Contact

def test_modify_first_contact_first_name(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="New First Name")
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name='Test'))
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)

"""
def test_modify_first_contact_last_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name='Test'))
    app.contact.modify_first_contact(Contact(last_name="New Last Name"))

def test_modify_first_contact_birthday(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name='Test'))
    app.contact.modify_first_contact(Contact(bday=1, bmonth="January", byear=1985))
"""
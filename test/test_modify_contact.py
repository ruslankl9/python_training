# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_modify_first_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name='Test'))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name="New First Name")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
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
# -*- coding: utf-8 -*-

from model.contact import Contact

def test_modify_first_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name='Test'))
    app.contact.modify_first_contact(Contact(first_name="New First Name"))

def test_modify_first_contact_last_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name='Test'))
    app.contact.modify_first_contact(Contact(last_name="New Last Name"))

def test_modify_first_contact_birthday(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name='Test'))
    app.contact.modify_first_contact(Contact(bday=1, bmonth="January", byear=1985))
# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest


def test_add_contact_data(app, db, data_contacts, check_ui):
    contact = data_contacts
    with pytest.allure.step('Given a contact list'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('When I add the contact to the list'):
        app.contact.create(contact)
    with pytest.allure.step('Then the new contact list is equal to the old list with the added contact'):
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)
        if check_ui:
            assert \
                sorted(
                    map(lambda x: Contact(
                            id=x.id,
                            first_name=x.first_name.strip(),
                            last_name=x.last_name.strip(),
                            address=x.address.strip(),
                            all_emails_from_home_page=x.all_emails_from_home_page.strip(),
                            all_phones_from_home_page=x.all_phones_from_home_page.strip()
                        ), new_contacts), key=contact.id_or_max
                ) == sorted(app.contact.get_contact_list(), key=contact.id_or_max)


def test_add_contact_json(app, db, json_contacts, check_ui):
    contact = json_contacts
    with pytest.allure.step('Given a contact list'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('When I add the contact to the list'):
        app.contact.create(contact)
    with pytest.allure.step('Then the new contact list is equal to the old list with the added contact'):
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)
        if check_ui:
            assert \
                sorted(
                    map(lambda x: Contact(
                            id=x.id,
                            first_name=x.first_name.strip(),
                            last_name=x.last_name.strip(),
                            address=x.address.strip(),
                            all_emails_from_home_page=x.all_emails_from_home_page.strip(),
                            all_phones_from_home_page=x.all_phones_from_home_page.strip()
                        ), new_contacts), key=contact.id_or_max
                ) == sorted(app.contact.get_contact_list(), key=contact.id_or_max)
# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import pytest


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name='Test'))
    with pytest.allure.step('Given a non-empty contact list'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('Given a random contact from the list'):
        contact = random.choice(old_contacts)
    with pytest.allure.step('When I delete the contact from the list'):
        app.contact.delete_contact_by_id(contact.id)
    with pytest.allure.step('Then the new contact list is equal to the old list without deleted contact'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) - 1 == len(new_contacts)
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
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
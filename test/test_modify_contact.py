# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import pytest


def test_modify_some_contact_first_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name='Test'))
    with pytest.allure.step('Given a non-empty contact list'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('Given a random contact from the list'):
        contact = random.choice(old_contacts)
    with pytest.allure.step('Given a contact with first_name'):
        new_contact = Contact(first_name="New First Name")
        new_contact.id = contact.id
    with pytest.allure.step('When I modify the contact from the list'):
        app.contact.modify_contact_by_id(contact.id, new_contact)
    with pytest.allure.step('Then the new contact list is equal to the old list with modified contact'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) == len(new_contacts)
        [x for x in old_contacts if x.id == new_contact.id][0].first_name = new_contact.first_name
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
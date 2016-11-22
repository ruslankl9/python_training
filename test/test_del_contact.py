# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name='Test'))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
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
import re
from random import randrange


def test_contact_info_on_home_page(app):
    contacts_from_home_page = app.contact.get_contact_list()
    index = randrange(len(contacts_from_home_page))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
        map(
            lambda x: clear(x),
                filter(lambda x: x is not None,
                   [contact.home_phone_number,
                    contact.mobile_phone_number,
                    contact.work_phone_number,
                    contact.phone_number2]
                )
            )
        )
    )

def merge_emails_like_on_home_page(contact):
    return '\n'.join([contact.email, contact.email2, contact.email3])

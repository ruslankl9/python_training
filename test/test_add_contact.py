# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string
import datetime


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' '*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

month_names = [datetime.date(2000, m, 1).strftime('%B') for m in range(1, 13)]

testdata = [Contact(first_name='', last_name='')] + \
[
    Contact(
        first_name=random_string("First Name", 10),
        middle_name=random_string("Middle Name", 20),
        last_name=random_string("Last Name", 20),
        nickname=random_string("nickname", 20),
        title=random_string("title", 20),
        company=random_string("Company", 20),
        address=random_string("Address", 20),
        home_phone_number=random_string("homephone", 10),
        mobile_phone_number=random_string("mobilephone", 10),
        work_phone_number=random_string("workphone", 10),
        fax_number=random_string("faxnumber", 10),
        email=random_string("email", 20),
        email2=random_string("email2", 20),
        email3=random_string("email3", 20),
        homepage_url=random_string("home_url", 20),
        bday=random.randrange(1, 28),
        bmonth=random.choice(month_names),
        byear=random.randrange(1900, 2016),
        aday=random.randrange(1, 28),
        amonth=random.choice(month_names),
        ayear=random.randrange(1900, 2016),
        address2=random_string("Address2", 20),
        phone_number2=random_string("phone2", 10),
        notes=random_string("notes", 100)
    )
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)
# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest
from contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(
        Contact(
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
    )
    app.session.logout()

def test_test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(
        Contact(
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
    )
    app.session.logout()

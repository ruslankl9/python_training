# -*- coding: utf-8 -*-
from model.contact import Contact

testdata = [
    Contact(
        first_name="FirstName1",
        middle_name="MiddleName1",
        last_name="LastName1",
        nickname="nickname1",
        title="title1",
        company="Company 1",
        address="Some str. 1",
        home_phone_number="+70010010101",
        mobile_phone_number="+70110010101",
        work_phone_number="+70210010101",
        fax_number="+70310010101",
        email="email1@email1.com",
        email2="email2@email1.com",
        email3="email3@email1.com",
        homepage_url="http://www.homeurl1.com/",
        bday=1,
        bmonth="January",
        byear=1951,
        aday=1,
        amonth="February",
        ayear=1961,
        address2="Addr2 str. 1",
        phone_number2="+70010410101",
        notes="Notes1"
    ),
    Contact(
        first_name="FirstName2",
        middle_name="MiddleName2",
        last_name="LastName2",
        nickname="nickname2",
        title="title2",
        company="Company 2",
        address="Some str. 2",
        home_phone_number="+70020020202",
        mobile_phone_number="+70120020202",
        work_phone_number="+70220020102",
        fax_number="+70320020202",
        email="email1@email2.com",
        email2="email2@email2.com",
        email3="email3@email2.com",
        homepage_url="http://www.homeurl2.com/",
        bday=2,
        bmonth="January",
        byear=1952,
        aday=2,
        amonth="February",
        ayear=1962,
        address2="Addr2 str. 2",
        phone_number2="+70020420202",
        notes="Notes2"
    )
]
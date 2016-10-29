# -*- coding: utf-8 -*-
from sys import maxsize

class Contact(object):

    def __init__(self, id=None, first_name=None, middle_name=None, last_name=None, nickname=None, title=None,
                 company=None, address=None, home_phone_number=None, mobile_phone_number=None, work_phone_number=None,
                 fax_number=None, email=None, email2=None, email3=None, homepage_url=None, bday=None, bmonth=None,
                 byear=None, aday=None, amonth=None, ayear=None, address2=None, phone_number2=None, notes=None,
                 all_emails_from_home_page=None, all_phones_from_home_page=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone_number = home_phone_number
        self.mobile_phone_number = mobile_phone_number
        self.work_phone_number = work_phone_number
        self.fax_number = fax_number
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage_url = homepage_url
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone_number2 = phone_number2
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.first_name == other.first_name \
               or self.last_name == other.last_name)

    def id_or_max(self, cn):
        if cn.id:
            return int(cn.id)
        else:
            return maxsize
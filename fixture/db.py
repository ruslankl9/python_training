import mysql.connector
from model.group import Group
from model.contact import Contact

class DbFixture(object):

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.coonection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.coonection.autocommit = True

    def get_group_list(self):
        _list = []
        cursor = self.coonection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id, name, header, footer) = row
                _list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return _list

    def get_contact_list(self):
        _list = []
        cursor = self.coonection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2"
                           " FROM addressbook WHERE deprecated = 0")
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2) = row
                _list.append(Contact(id=str(id), first_name=firstname, last_name=lastname, address=address,
                                     all_emails_from_home_page='\n'.join([email, email2, email3]),
                                     all_phones_from_home_page='\n'.join([home, mobile, work, phone2])
                                    ))
        finally:
            cursor.close()
        return _list

    def destroy(self):
        self.coonection.close()
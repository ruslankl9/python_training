# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, orm):
    # создаем группу если список групп пуст
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    all_groups = orm.get_group_list()
    group = random.choice(all_groups)
    # создаем контакт если список контактов пуст или нет контакта, который не находится в заданной группе
    contacts = orm.get_contacts_not_in_group(group)
    if len(contacts) == 0:
        app.contact.create(Contact(first_name='Test'))
        contacts = orm.get_contacts_not_in_group(group)
    contact = random.choice(contacts)
    old_contacts = orm.get_contacts_in_group(group)
    app.contact.add_to_group(contact, group)
    new_contacts = orm.get_contacts_in_group(group)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)
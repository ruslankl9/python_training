# -*- coding: utf-8 -*-
from model.group import Group
import pytest


def test_add_group_data(app, db, data_groups, check_ui):
    group = data_groups
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with pytest.allure.step('When I add a group %s to the list' % group):
        app.group.create(group)
    with pytest.allure.step('Then the new group list is equal to the old list with the added group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=group.id_or_max) == sorted(new_groups, key=group.id_or_max)
        if check_ui:
            assert sorted(map(lambda x: Group(id=x.id, name=x.name.strip()), new_groups), key=group.id_or_max) == \
                   sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_add_group_json(app, db, json_groups, check_ui):
    group = json_groups
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with pytest.allure.step('When I add a group %s to the list' % group):
        app.group.create(group)
    with pytest.allure.step('Then the new group list is equal to the old list with the added group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=group.id_or_max) == sorted(new_groups, key=group.id_or_max)
        if check_ui:
            assert sorted(map(lambda x: Group(id=x.id, name=x.name.strip()), new_groups), key=group.id_or_max) == \
                   sorted(app.group.get_group_list(), key=Group.id_or_max)
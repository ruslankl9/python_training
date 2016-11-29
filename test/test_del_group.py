# -*- coding: utf-8 -*-
from model.group import Group
import random
import pytest


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    with pytest.allure.step('Given a non-empty group list'):
        old_groups = db.get_group_list()
    with pytest.allure.step('Given a random group from the list'):
        group = random.choice(old_groups)
    with pytest.allure.step('When I delete the group (id=%s) from the list' % group.id):
        app.group.delete_group_by_id(group.id)
    with pytest.allure.step('Then the new group list is equal to the old group without deleted group'):
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(map(lambda x: Group(id=x.id, name=x.name.strip()), new_groups), key=group.id_or_max) == \
                   sorted(app.group.get_group_list(), key=Group.id_or_max)
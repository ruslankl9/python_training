# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_some_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group = Group(name="New group")
    new_group.id = group.id
    app.group.modify_group_by_id(group.id, new_group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    [x for x in old_groups if x.id == new_group.id][0].name = new_group.name
    assert sorted(old_groups, key=group.id_or_max) == sorted(new_groups, key=group.id_or_max)
    if check_ui:
        assert sorted(map(lambda x: Group(id=x.id, name=x.name.strip()), new_groups), key=group.id_or_max) == \
               sorted(app.group.get_group_list(), key=Group.id_or_max)
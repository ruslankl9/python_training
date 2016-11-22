# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group_data(app, db, data_groups, check_ui):
    group = data_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=group.id_or_max) == sorted(new_groups, key=group.id_or_max)
    if check_ui:
        assert sorted(map(lambda x: Group(id=x.id, name=x.name.strip()), new_groups), key=group.id_or_max) == \
               sorted(app.group.get_group_list(), key=Group.id_or_max)

def test_add_group_json(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=group.id_or_max) == sorted(new_groups, key=group.id_or_max)
    if check_ui:
        assert sorted(map(lambda x: Group(id=x.id, name=x.name.strip()), new_groups), key=group.id_or_max) == \
               sorted(app.group.get_group_list(), key=Group.id_or_max)
# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="group1", header="4234324", footer="6ergdgdfgg"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
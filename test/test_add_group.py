from model.group import Group
import pytest
from data.groups import testdata
#
#@pytest.mark.parametrize("group", tessdata, ids=[repr(x) for x in tessdata])

def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with pytest.allure.step('When i add a group %s to the list' % group):
        app.group.create(group)
    with pytest.allure.step('the new group list is equal to the old list with the added group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# добавление групп через интерфейс
#def test_add_group(app, json_groups):
#    group = json_groups
#    old_groups = app.group.get_group_list()
#    app.group.create(group)
#    assert len(old_groups) + 1 == app.group.count()
#    new_groups = app.group.get_group_list()
#    old_groups.append(group)
#   assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        def clean(group):
            name = "".join(group.name.split())
            return Group(id=group.id, name=name)
        new_groups_db = map(clean, new_groups)
        new_groups_app = map(clean, app.group.get_group_list())
        assert sorted(new_groups_db, key=Group.id_or_max) == sorted(new_groups_app, key=Group.id_or_max)

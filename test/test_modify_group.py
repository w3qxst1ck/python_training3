from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    old_groups = db.get_group_list()
    modifing_group = random.choice(old_groups)
    index = old_groups.index(modifing_group)
    group = Group(name="New group")
    group.id = modifing_group.id
    app.group.modify_group_by_id(modifing_group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        def clean(group):
            name = "".join(group.name.split())
            return Group(id=group.id, name=name)
        new_groups_db = map(clean, new_groups)
        new_groups_app = map(clean, app.group.get_group_list())
        assert sorted(new_groups_db, key=Group.id_or_max) == sorted(new_groups_app, key=Group.id_or_max)


# def test_modify_group_header(app, db, check_ui):
#     if len(db.get_group_list()) == 0:
#         app.group.create(Group(name='test'))
#     old_groups = db.get_group_list()
#     modifing_group = random.choice(old_groups)
#     index = old_groups.index(modifing_group)
#     group = Group(header="New header")
#     group.id = old_groups[index].id
#     app.group.modify_group_by_id(modifing_group.id, group)
#     new_groups = db.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[index] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#     if check_ui:
#         def clean(group):
#             name = "".join(group.name.split())
#             return Group(id=group.id, name=name)
#         new_groups_db = map(clean, new_groups)
#         new_groups_app = map(clean, app.group.get_group_list())
#         assert sorted(new_groups_db, key=Group.id_or_max) == sorted(new_groups_app, key=Group.id_or_max)

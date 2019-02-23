from model.group import Group


def test_group_list(app, db):
    # ui_list = app.group.get_group_list()

    def clean(group):
        name = "".join(group.name.split())
        return Group(id=group.id, name=name)
    db_list = map(clean, db.get_group_list())
    ui_list = map(clean, app.group.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

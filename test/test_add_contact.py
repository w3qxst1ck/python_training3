# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="asdasd", middlename="asd", lastname="fddfdf", nickname="fdfddffd",
                               title="adfadf", company="asdfafd"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login( username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",
                               title="", company=""))
    app.session.logout()


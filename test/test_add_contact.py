# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="asdasd", middlename="asd", lastname="fddfdf", nickname="fdfddffd",
                               title="adfadf", company="asdfafd"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",
                               title="", company=""))


# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest


testdata = [
    Contact(firstname="asdasd", middlename="asd", lastname="fddfdf", nickname="fdfddffd",
                               title="adfadf", company="asdfafd", homephone="634850", workphone="89679185042"),
    Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", homephone="", workphone="")
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = (Contact(firstname="", middlename="", lastname="", nickname="",
                               title="", company="", homephone="", workphone=""))
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


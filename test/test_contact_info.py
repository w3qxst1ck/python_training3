import re
from random import randrange


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                                  filter(lambda x: x is not None, [contact.homephone,
                                                                                   contact.workphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                                filter(lambda x: x is not None, [contact.email,
                                                                                 contact.email2, contact.email3]))))


def test_personal_info_home_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_personal_info_on_contact_view_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_view_page = app.contact.get_contact_info_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.firstname == contact_from_edit_page.firstname
    assert contact_from_view_page.middlename == contact_from_edit_page.middlename
    assert contact_from_view_page.lastname == contact_from_edit_page.lastname
    assert contact_from_view_page.nickname == contact_from_edit_page.nickname
    assert contact_from_view_page.title == contact_from_edit_page.title
    assert contact_from_view_page.company == contact_from_edit_page.company
    assert contact_from_view_page.address == contact_from_edit_page.address

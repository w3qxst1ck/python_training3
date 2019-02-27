from model.contact import Contact
import random


def test_modify_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='test'))
    old_contacts = db.get_contact_list()
    modifing_contact = random.choice(old_contacts)
    index = old_contacts.index(modifing_contact)
    contact = Contact(firstname="New_firstname")
    contact.id = modifing_contact.id
    app.contact.modify_contact_by_id(modifing_contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        def clean(contact):
            firstname = "".join(contact.firstname.split())
            lastname = "".join(contact.lastname.split())
            return Contact(id=contact.id, firstname=firstname, lastname=lastname)
        new_contacts_db = map(clean, new_contacts)
        new_contacts_app = map(clean, app.contact.get_contact_list())
        assert sorted(new_contacts_db, key=Contact.id_or_max) == sorted(new_contacts_app, key=Contact.id_or_max)


# def test_modify_contact_middlename(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(middlename='test'))
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(middlename="New middlename")
#     contact.id = old_contacts[0].id
#     app.contact.modify_first_contact(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#     old_contacts[0] = contact
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


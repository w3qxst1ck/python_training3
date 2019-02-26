from model.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='test'))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        def clean(contact):
            firstname = "".join(contact.firstname.split())
            lastname = "".join(contact.lastname.split())
            return Contact(id=contact.id, firstname=firstname, lastname=lastname)
        new_contacts_db = map(clean, new_contacts)
        new_contacts_app = map(clean, app.contact.get_contact_list())
        assert sorted(new_contacts_db, key=Contact.id_or_max) == sorted(new_contacts_app, key=Contact.id_or_max)



class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @staticmethod
    def validate_phone_number(phone_number):
        return phone_number.isdigit() and len(phone_number) == 10
       
class ContactList:
    all_contacts = []
     
    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            new_contact = Contact(name, phone_number)
            cls.all_contacts.append(new_contact)
        else:
            raise ValueError("Ошибка при вводе номера")

ContactList.add_contact("John Doe", "1234567890")
ContactList.add_contact("Alice", "1234567890")
ContactList.add_contact("Bob", "0987654321")                
for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number)

ContactList.add_contact("Alice", "123456780")
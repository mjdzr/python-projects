from collections import defaultdict

class ContactBook:

    # Initialize empty book
    def __init__(self):
        self.contacts = defaultdict(dict)

    # Add contact
    def add_contact(self, name, phone, email=None):
        if name in self.contacts:
            print("Name already registered")
            return

        self.contacts.update({
            name:{
                'phone': phone,
                'email': email
            }
        })

        print("Contact added successfully.")

    # View contacts
    def view_contacts(self):
        print("Contact List:")
        for name, info in self.contacts.items():
            print(f"name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print("*" * 50)

    # Delete contact
    def remove_contact(self, name):

        # Don't do anything if the name isn't in contact
        if name not in self.contacts:
            print("Contact not found! Skipping...")
            return

        del self.contacts[name]
        print("Contact deleted successfully.")

    # Update contact
    def update_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email

            print("Contact updated successfully.")
            return

        print('Contact not found!')


if __name__ == "__main__":
    book = ContactBook()

while True:
    print('Welcome to contact book! Choose an option:')
    print('-------------------------------------')
    # Get input from user from 1 to 5 to perform actions:
    print('1. Add contact')
    print('2. View contacts')
    print('3. Remove contact')
    print('4. Update contact')
    print('5. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        name = input('Enter name: ')
        phone = input('Enter phone number: ')
        email = input('Enter email address (optional): ')
        book.add_contact(name, phone, email)
    elif choice == '2':
        book.view_contacts()
    elif choice == '3':
        name = input('Enter name to remove: ')
        book.remove_contact(name)
    elif choice == '4':
        name = input('Enter name to update: ')
        phone = input('Enter new phone number (optional): ')
        email = input('Enter new email address (optional): ')
        book.update_contact(name, phone, email)
    elif choice == '5':
        print('Exiting contact book.')
        break
    else:
        print('Invalid choice. Please try again.')

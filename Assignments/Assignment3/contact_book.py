#Create a contact book application where users can add, view, update, and delete contacts.

# Define the contact book as a dictionary
contact_book = {}

def add_contact(name, phone, email):
    """
    Add a new contact to the contact book.

    Parameters:
    name (str): The name of the contact
    phone (str): The phone number of the contact
    email (str): The email address of the contact
    """
    contact_book[name] = {'phone': phone, 'email': email}
    print(f"Contact {name} added successfully.")

def view_contacts():
    """
    View all contacts in the contact book.
    """
    if not contact_book:
        print("No contacts available.")
    else:
        for name, details in contact_book.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

def update_contact(name, phone=None, email=None):
    """
    Update an existing contact in the contact book.

    Parameters:
    name (str): The name of the contact
    phone (str): The new phone number of the contact (optional)
    email (str): The new email address of the contact (optional)
    """
    if name in contact_book:
        if phone:
            contact_book[name]['phone'] = phone
        if email:
            contact_book[name]['email'] = email
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} not found.")

def delete_contact(name):
    """
    Delete a contact from the contact book.

    Parameters:
    name (str): The name of the contact to delete
    """
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

def contact_book_app():
    """
    function to run the contact book application.
    """
    while True:
        print("Contact Book Application")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(name, phone, email)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone number (leave blank to keep unchanged): ")
            email = input("Enter new email address (leave blank to keep unchanged): ")
            update_contact(name, phone or None, email or None)
        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

contact_book_app()
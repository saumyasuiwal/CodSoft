# Contact Manager Application

contacts = []

def show_menu():
    print("\n===== Contact Manager =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- Contact List ---")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} - {c['phone']}")

def search_contact():
    keyword = input("Enter name or phone number to search: ").lower()
    found = False
    for c in contacts:
        if keyword in c["name"].lower() or keyword in c["phone"]:
            print("\n--- Contact Found ---")
            print(f"Name: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    view_contacts()
    try:
        idx = int(input("Enter contact number to update: ")) - 1
        if 0 <= idx < len(contacts):
            print("Leave blank to keep existing value.")
            name = input(f"New name ({contacts[idx]['name']}): ") or contacts[idx]['name']
            phone = input(f"New phone ({contacts[idx]['phone']}): ") or contacts[idx]['phone']
            email = input(f"New email ({contacts[idx]['email']}): ") or contacts[idx]['email']
            address = input(f"New address ({contacts[idx]['address']}): ") or contacts[idx]['address']
            
            contacts[idx] = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_contact():
    view_contacts()
    try:
        idx = int(input("Enter contact number to delete: ")) - 1
        if 0 <= idx < len(contacts):
            deleted = contacts.pop(idx)
            print(f"Deleted contact: {deleted['name']}")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option (1-6): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please enter a number between 1 and 6.")
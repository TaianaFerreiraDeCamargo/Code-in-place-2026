# Database of users and passwords
user_database = {
    "TAIANA": "adminCIP2026",
    "Student": "passwordCIP2026"
}

"""This function, system_login,user authentication. it prompts the user for their credentials and checks if they exist in the database"""
def system_login():
    username = input("Username: ")
    password = input("Password: ")

    if username in user_database and user_database[username] == password:
        print("[SUCCESS] Login successful!")
    else:
        print("[ERROR] Invalid username or password.")

"""This function, named add_user(), is used to register a new user in a simple system (likely using a dictionary called user_database)."""
def add_user():
    print("\n=== ADD NEW USER ===")

    username = input("Enter new username: ").strip()

    if username in user_database:
        print("[ERROR] User already exists.")
        return

    password = input("Enter password: ")

    user_database[username] = password

    print(f"[SUCCESS] User '{username}' has been added.")

""" This function, Prompts the user for a username and removess their account."""
def remove_user():
    print("\n=== DELETE USER ACCOUNT ===")

    username = input("Enter username to delete: ").strip()

    if username in user_database:
        user_database.pop(username)
        print(f"[SUCCESS] User '{username}' has been deleted.")
    else:
        print("[ERROR] User not found.")

""" This function, change_password(), efficiently handles user password updates. it prompts for a username, verifies if it exists in the database, and safely updates the password dictionary while providing clear error and success messages."""
def change_password():
    print("\n=== CHANGE PASSWORD ===")

    username = input("Username: ").strip()

    if username not in user_database:
        print("[ERROR] User not found.")
        return

    new_password = input("New password: ")

    user_database[username] = new_password

    print("[SUCCESS] Password updated.")


def list_users():
    print("\n=== USER LIST ===")

    for user in user_database:
        print("-", user)

"""This is a clean and well-structured main menu loop for a user management system. it provides a clear interface and handles user navigation effectively."""
def main():
    while True:

        print("\n========================")
        print(" Registration system ")
        print("========================")
        print("1 - Login")
        print("2 - Add User")
        print("3 - Remove User")
        print("4 - list of names user")
        print("5 - Change Password")
        print("6 - Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            system_login()

        elif choice == "2":
            add_user()

        elif choice == "3":
            remove_user()

        elif choice == "4":
            list_users()

        elif choice == "5":
            change_password()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("[ERROR] Invalid option.")


if __name__ == "__main__":
    main()
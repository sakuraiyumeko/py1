def login():
    wrong = 0
    try:
        with open("info.txt", "r") as file:
            users = [line.strip().split(',') for line in file if line.strip()]
    except FileNotFoundError:
        print("No users registered yet.")
        return False

    if not users:
        print("No users registered yet.")
        return False

    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for stored_username, stored_password in users:
            if username == stored_username and password == stored_password:
                print(f"Welcome {username}!")
                return True
        wrong += 1
        print("Invalid username or password.\n")
        if wrong >= 3:
            print("System locked.")
            return False


def register():
    existing_users = set()

    try:
        with open("info.txt", "r") as file:
            for line in file:
                if line.strip():
                    stored_username, _ = line.strip().split(',')
                    existing_users.add(stored_username)
    except FileNotFoundError:
        pass

    while True:
        newusername = input("Enter a username: ")
        if newusername == ' ':
            print("You entered an empty username.")
            continue
        if newusername in existing_users:
            print("Username already exists. Please choose another one.")
            continue

        newpassword = input("Enter a password: ")
        if newpassword == ' ':
            print("You entered an empty password.")
        if len(newpassword)<8:
            print("Password must be at least 8 characters long.")
        confirm = input("Confirm? It cannot be modified after confirmation. (y/n): ").lower()

        if confirm == 'y':
            with open("info.txt", "a") as file:
                file.write(newusername + ',' + newpassword + '\n')
            print("Registration successful.")
            break
        elif confirm == 'n':
            continue
        else:
            print("Invalid confirmation input.")


def main_menu():
    while True:
        print("""
What would you like to do?
    1. Register
    2. Login
    3. Quit
""")
        choice = input("Enter your choice: ")
        if choice == '1':
            register()
        elif choice == '2':
            logged_in = login()
            if logged_in:
                logged_in_menu()
        elif choice == '3':
            print("See you later!")
            quit()
        else:
            print("Invalid option.")


def logged_in_menu():
    while True:
        print("""
What would you like to do?
    1. Quit
""")
        choice = input("Enter your choice: ")
        if choice == '1':
            print("See you later!")
            quit()
        else:
            print("Invalid option.")

main_menu()

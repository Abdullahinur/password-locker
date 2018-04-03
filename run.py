#!/usr/bin/env python3.6
import pyperclip
from user import User


def create_user(fname, lname, phone, email):
    '''
    Function to create a new contact
    '''
    new_user = User(fname, lname, phone, email)
    return new_user


def save_users(user):
    '''
    Function to save contact
    '''
    user.save_user()


def delete_user(user):
    '''
    Function to delete a contact
    '''
    user.delete_user()


def find_user(number):
    '''
    Function that finds a user by their first name
    '''
    return User.find_by_number(number)


def check_existing_users(fname):
    '''
    Function that checks if a contact exists with that first name and returns a boolean
    '''
    return User.user_exist(fname)


def display_users():
    '''
    Function that returns all the saved user_list
    '''
    return User.display_users()


def copy_existing_email(phone_number):
    '''
    Function that copys the Firstname of a user to the machine #### This will be changed
    '''

    return User.copy_email(phone_number)


def main():
    print("\n")
    print("Welcome to Ab's PassWord Locker")
    print("This will store your credentails and generate a password for you")
    print("My name is Ab,")
    print("What's yours")

    user_name = input()

    print(f"Hello {user_name}. What would you like to do?")

    print("\n")

    while True:
        print(f"Hello {user_name}.")
        print("You can use this program by typing some simple phrases")
        print("Here are some phrases to get you started: # new - create new user, # display - displays the users, # find - find a user, # del - del a user, # copy - copy user info, # exit - exit the password locker")

        phrases = input().lower()

        if phrases == 'new':
            print("New User")
            print("-" * 10)

            print("First name .....")
            first_name = input()

            print("Last name .....")
            last_name = input()

            print("User name .....")
            user_name = input()

            print("Phone number .....")
            phone_number = input()

            print("Email address .......")
            email = input()

            # Create and save new contact
            save_users(create_user(first_name, last_name, phone_number, email))

            print("\n")

            print(f"Welcome NEW USER: {first_name} {last_name}")

            print("\n")

        elif phrases == 'display':

            if display_users():

                print("Here is a list of current users")

                print("\n")

                for user in display_users():

                    print(f"{user.first_name} {user.last_name} .............{user.phone_number}")

                print("\n")

            else:
                print("\n")

                print("There aren't any users yet")

                print("\n")

        elif phrases == 'find':

            print("Enter the number you want to search for")

            search_number = input()

            if check_existing_users(search_number):

                print('-' * 20)

                search_user = find_user(search_number)

                print("Here is the account associated with that number")

                print(f"{search_user.first_name} {search_user.last_name}")

                print('-' * 20)

                print(f"Phone number .....{search_user.phone_number}")

                print(f"Email ......{search_user.email}")

            else:
                print("That User does not exist")

        elif phrases == 'del':

            print("Enter the number you want to delete")

            delete_number = input()

            if check_existing_users(delete_number):

                search_delete_user = find_user(delete_number)

                print(f"The following user: {search_delete_user.first_name} {search_delete_user.last_name} has been deleted")

                delete_user(search_delete_user)

            else:
                print("That contact does not exist")

        elif phrases == 'copy':

            print("Enter the number for the email you want to copy")

            search_number_for_email = input()

            if check_existing_users(search_number_for_email):

                user_found = find_user(search_number_for_email)

                user_email = copy_existing_email(search_number_for_email)

                paste_user_email = pyperclip.paste()

                print(f"{ pyperclip.paste()} which belongs to {user_found.first_name} {user_found.last_name} has been pasted to your clipboard")

            else:

                print("The contact does not exist")

        elif phrases == 'exit':

            print("Bye .........")

        else:

            print("I really didn't get that. Please use the short phrases")


if __name__ == '__main__':
    main()
